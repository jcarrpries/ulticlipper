console.log("hi")

const fs = require("fs");
const FILENAME = "results.json"
function mergeReplicas(n, data) {
    const f = fs.readFileSync(FILENAME)
    const j = JSON.parse(f)
    j[n] = data;
    fs.writeFileSync(FILENAME, JSON.stringify(j, null, 2))
    console.log(`Merged [replicas=${n}] results into "results.json".`)
}

mergeReplicas(2, undefined)