const axios = require('axios');

const exec = require('child_process').exec;
const execSync = require('child_process').execSync;

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}


let count = 0; // Shared among calls
async function start_docker(n) {
    count += 1 // Only throw error if it's current (next call to start_docker resets)

    console.log("Docker: stopping...")
    execSync("docker compose -f docker-compose-dev.yml down --volumes", {stdio: "ignore"})
    console.log("Docker: stopped.")


    console.log("Docker: starting...")
    const curr_count = count;
    exec(`docker compose -f docker-compose-dev.yml -f override-${n}.yml up --build`, {maxBuffer: 1024 * 1024 * 100}, (err, stdout, stderr) => {
        if (curr_count == count) {
            console.error(err)
            console.error(stderr)
            throw err
        } else {
            console.log("DOcker: Caught err:", err)
        }
    });

    while (true) {
        try {
            const res = await axios.get('http://localhost/api/clips/')
            if (res.data.length > 3) {
                console.log("Docker: waiting for all containers")
                await sleep(10000)
                return true;
            }
        } catch (e) {
            // console.log("Axios err")
            await sleep(1000)
        }
        
    }
}

async function stop_docker() {
    console.log("Docker: stopping...")
    execSync("docker compose -f docker-compose-dev.yml down --volumes", {stdio: "ignore"})
    console.log("Docker: stopped.")
}

async function main() {
    await start_docker(10);
    res = await axios.get('http://localhost/api/clips/');

    console.log(res.data);
    await stop_docker();
}



module.exports = {
    start_docker,
    stop_docker
}