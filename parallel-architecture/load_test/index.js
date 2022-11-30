// CURRENT TODO (for replicas other than 4):
// - set replica vals (to more than just 4)
// - uncomment the part that skips the checkpoint continue.

const axios = require('axios');
const process = require('process');
const docker_ctl = require('./spin_up.js');

const fs = require("fs");

const NUM_TRIALS = 30
// const NUM_TRIALS = 15
// const N_VALS = [1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 75, 100, 125, 150, 175, 200]
const N_VALS = [1, 2, 3, 4, 5, 10, 25, 50, 100, 150, 200]
const ENDPOINTS = [
  'http://localhost/api/clips/',
  'http://localhost/api/clips/3/',
  'http://localhost/api/clips_by_video/3/',
  'http://localhost/api/tags/',
  'http://localhost/api/tags/3/',
  'http://localhost/api/tag_groups/',
  'http://localhost/api/tag_groups/3/',
]
// const REPLICA_VALS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 25]
const REPLICA_VALS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
// const REPLICA_VALS = [4]
const CUTOFF_MS = 10000
const FILENAME = "results.json"


// function mergeReplicas(n, data) {
//     const f = fs.readFileSync(FILENAME)
//     const j = JSON.parse(f)
//     j[n] = data;
//     fs.writeFileSync(FILENAME, JSON.stringify(j, null, 2))
//     console.log(`Merged [replicas=${n}] results into "results.json".`)
// }

function checkData(n, url, burstSize) {
  const f = fs.readFileSync(FILENAME)
  const j = JSON.parse(f)
  if (j[n] && j[n][url] && j[n][url][burstSize]) {
    return true
  } else {
    return false
  }
}

function getReplicaCheckpoint() {
  const f = fs.readFileSync(FILENAME)
  const j = JSON.parse(f)
  for (let i = 20; i > 0; i--) {
    if (j[i]) {
      return i
    }
  }
}

function logData(n, url, burstSize, time) {
  const f = fs.readFileSync(FILENAME)
  const j = JSON.parse(f)
  if (!j[n]) {
    j[n] = {};
  }
  if (!j[n][url]) {
    j[n][url] = {};
  }
  if (!j[n][url][burstSize]) {
    j[n][url][burstSize] = {};
  }

  j[n][url][burstSize] = time;
  fs.writeFileSync(FILENAME, JSON.stringify(j, null, 2))
  // console.log(`Merged [replicas=${n}, url=${url}] results into "results.json".`)
}


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

function average(list) {
  const sum = list.reduce((a, b) => a + b, 0);
  const avg = sum / list.length;
  return avg
}

async function get(url) {
  const start = process.hrtime();
  // const res = await axios.get('http://localhost/api/clips/3/')

  try {
    const res = await axios.get(url)
    const [secs, nanosecs] = process.hrtime(start)
    const ms = (secs*1000 + nanosecs/1000000)
    if (res.status == 200) {
      return ms
    }

    console.log("Status code: ", res.status)

  } catch (e) {
    console.log("get() error, ", e?.status)
    return null;
  }
}

async function burst(n_concurrent, url) {
  const promises = []
  const times = []
  // Send requests
  for(let i = 0; i < n_concurrent; i++){
    promises.push(get(url));
  }

  // Set response handlers
  promises.forEach(p => {
    p.then(ms => times.push(ms)) // append time
  })

  await Promise.all(promises)
  if (times.some(t => t === null)) {
    // console.log("some times were null")
    return null
  }


  return average(times)
}



async function multiBurst(n_concurrent, url) {
  const runs = []
  // const n_trials = 30
  for (let i=0; i<NUM_TRIALS; i++) {
    console.log("Burst", i+1, "/30")
    const avg = await burst(n_concurrent, url);
    if (avg == null) {
      // console.log("an avg was null")
      return null
    }
    runs.push(avg)
  }


  avg = average(runs)
  return avg
}

async function mainLoop() {
  console.log("Main loop start")

  // const times = {};
  const checkpt = getReplicaCheckpoint();
  console.log("Replia Checkpoint: ", checkpt)
  for (n_replicas of REPLICA_VALS) {





    if (n_replicas < checkpt) {
      console.log("Skipping ",n_replicas, "replicas. Less than checkpoint.")
      continue;
    }







    console.log(n_replicas, "replicas, from list:", REPLICA_VALS)
    console.timeLog("running time");
    await docker_ctl.start_docker(n_replicas)
    // times[n_replicas] = {};

    for (url of ENDPOINTS) {
      console.timeLog("running time");
      // times[n_replicas][url] = {}
      for (n of N_VALS) {
        if (checkData(n_replicas, url, n)) {
          console.log("cached: skipping iteration")
          continue; // skip 1 iteration of inner loop
        }
        
        const avg = await multiBurst(n, url);
        console.log(n, ":", avg);

        if (avg === null) {
          console.log("null in mainLoop(), breaking")
          break;
        }

        logData(n_replicas, url, n, avg)
    
        if (avg > CUTOFF_MS) {
          // Save time, stop once requests take longer than 1s
          break;
        }
      }
    }
    // Merge results into "results.json"
    // mergeReplicas(n_replicas, times[n_replicas])
    // console.log("Results merged into results.json")
  }
  
  // console.log("times:");
  // console.log(times);

  console.log("All Done.")
  console.timeLog("running time");
  console.timeEnd("running time")

  return true

}

async function main() {
  console.time("running time");
  while (true) {
    try {
      const exit_status = await mainLoop()
      if (exit_status == true) {
        console.log("Exiting.")
        return true;
      }
    } catch (e) {
      console.log("\n\n\n\n\nCaught e:", e)
      console.log("Retrying")
      await sleep(1000)
    }
  }
}

main()





