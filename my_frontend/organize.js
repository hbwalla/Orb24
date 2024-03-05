var file = "/Users/haileywallace/Desktop/orb_dev/Orb24/my_frontend/text.txt"

const fs = require('fs')

fs.readFile(file, (err, data) => {
    if (err) throw err;
    console.log(data.toString());
});

// want to use JSON.parse() for this! Have to put text file in JSON format