import 'expect-puppeteer'

describe('App', () => {
  beforeEach(async () => {
    await page.setViewport({
      width: 1200,
      height: 800,
      deviceScaleFactor: 1,
    });

    // 'proxy' is substitute for 'localhost' when running containers over bridge network
    await page.goto('http://proxy')

    //////////////////////////////////////////
    // To turn on logging, uncomment this line
    //////////////////////////////////////////
    page.on('console', msg => console.log('FROM BROWSER:', msg.text()))

    // Clear database
    await page.evaluate(async () => {
      fetch('/api/cleardatabase/', {method: 'DELETE'})
    })
  })

  it('should display "Ultimate Clipper" text on title page', async () => {
    let element = await page.waitForSelector('.title')
    let value = await element.evaluate(el => el.textContent, element)
    await expect(value).toMatch(/Ultimate Clipper/)

    let [sync_link] = await page.$x("//a[contains(., 'Sync')]")
    await sync_link.click()
  
    let title = await page.waitForSelector('.card-header-title')
    value = await title.evaluate(el => el.textContent, title)
    await expect(value).toMatch(/Synchronize clips/)
  })

  jest.setTimeout(60000)
  it('should have searchable and viewable clips after uploading', async () => {
    // expect to be on the homepage
    await page.waitForSelector('#hero-title-text')
    await expect(page.content()).resolves.toMatch(/The Ultimate Clipper Tool/)
    // navigate to search page
    await page.waitForSelector('#search-nav-item')
    let [search_nav] = await page.$x('//a[contains(., "Search")]')
    await search_nav.click()
    await expect(page.content()).resolves.toMatch(/Search for clips/)

    // press search
    await page.waitForSelector('#search-button')
    await page.click('#search-button')
    // expect there to be no results
    let results_count_el = await page.waitForSelector('#results-count')
    let results_count = await results_count_el.evaluate(el => el.textContent)

    await expect(results_count).toMatch(/Results: 0/)
  
    // navigate to sync page
    let [sync_nav] = await page.$x('//a[contains(., "Sync")]')
    await sync_nav.click()
    // expect to be on sync page
    await expect(page.content()).resolves.toMatch(/Synchronize clips/)

    // ----- SYNC FLOW ----- //
    // fill out URL form
    await page.type('#url-input', 'https://www.youtube.com/watch?v=B_RPq7Gh_20')
    // upload analytics file
    await page.evaluate(async () => {
      await fetch('/static/test_data/RaleighFlyers2019-stats.csv').then((resp) => {
        return resp.text()
      }).then((text) => {
        let file = new File([text], 'testimport.csv')
        const dataTransfer = new DataTransfer()
        dataTransfer.items.add(file)
        document.getElementById('stats-file-input').files = dataTransfer.files
      })
    })
    // press upload
    await page.click('#upload-button')

    await page.waitForSelector('table')
    await expect(page.content()).resolves.toMatch('Synchronize clips: chooseGame')

    // Find game from who's date matches 2019-04-05
    let [td_with_date_el] = await page.$x('//td[contains(., "2019-04-05")]')
    // Press Select
    await page.evaluate(async (el) => {
      el.parentElement.childNodes[3].childNodes[0].click()
    }, td_with_date_el)
    await page.waitForSelector('iframe')
    await expect(page.content()).resolves.toMatch('Synchronize clips: halves')
    
    // Press continue on the 'select halves' screen
    await page.click('#continue-button')
    await page.waitForSelector('select')
    await expect(page.content()).resolves.toMatch('Synchronize clips: verify')


    // Press next clip to change next clip
    await page.click('#next-clip-button')
    // Press edit to edit second clip
    await page.click('#edit-button')
    await expect(page.content()).resolves.toMatch(/Edit.+of clip 2/)
    await page.click('#reset-button')

    // Press continue
    await page.click('#continue-button')
    await page.waitForSelector('select')
    await expect(page.content()).resolves.toMatch('Synchronize clips: verify')
    let start_el = await page.$('#start-button')
    await expect(start_el.evaluate(el => el.textContent)).resolves.toMatch(/4:01/)

    // Press Submit on the verify screen
    await page.click('#submit-button')
    // Expect to see "generated" in the content
    // await page.waitForSelector('#done-msg')
    await expect(page.content()).resolves.toMatch('generated')

    // ----- SEARCH FLOW ----- //
    // Navigate to the search screen
    let [search_nav2] = await page.$x('//a[contains(., "Search")]')
    await search_nav2.click()
    await expect(page.content()).resolves.toMatch(/Search for clips/)

    // press search
    // expect there to be more than 0 results
    await page.waitForSelector('#search-button')
    await page.click('#search-button')
    // expect there to be no results
    results_count_el = await page.waitForSelector('#results-count')
    let results_count_1 = await results_count_el.evaluate(el => el.textContent)

    await expect(results_count_1).toMatch(/Results: \d\d+/)

    // Select 'GOAL' event type
    let [goal_option] = await page.$x('//option[contains(., "GOAL")]')
    await goal_option.click()
    // Press search
    await page.click('#search-button')
    // Expect there to be less than the previous number of results
    try {
      await page.waitForSelector('#search-loading', {timeout: 2000})
    } catch (err) {} // it's ok if we miss this
    results_count_el = await page.waitForSelector('#results-count')
    let results_count_2 = await results_count_el.evaluate(el => el.textContent)

    expect(parseInt(results_count_2.split(' ')[1])).toBeLessThan(parseInt(results_count_1.split(' ')[1]))

    // Press the link <a> that has view in the text
    let [view_link] = await page.$x('//a[contains(., "view")]')
    await view_link.click()
    // Expect there to be an iframe
    await page.waitForSelector('iframe')
    await page.waitForSelector('button')
    // Expect that there is a button with the text "10" (for the score timestamps)
    let [button_10_el] = await page.$x('//button[contains(., "10")]')
    expect(button_10_el).toBeDefined()
    // Expect that there is a button with the text "GOAL" (for the events timestamps)
    let [button_GOAL_el] = await page.$x('//button[contains(., "GOAL")]')
    expect(button_GOAL_el).toBeDefined()
  })
})
