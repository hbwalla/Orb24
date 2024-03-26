// import {addClassToContainer} from "menu-functions";
const my_import = require("./menu-functions.js")
// import {addFunction} from "./menu-functions.js";
const sample = require("./output.json");


function range(start, end) {
    return Array(end - start + 1).fill().map((_, idx) => start + idx)
};

// $(document).ready(function() {
//     my_import.addClassToContainer();
// });

var size = Object.keys(sample).length;

let index = 0;
let result = range(0, size - 1);

while (index < result.length) {
    var obj = JSON.stringify(sample[result[index]]["type"]);

    if (obj.includes("class")) {
        console.log("class!");
    };
        
    if (obj.includes("function")) {
            console.log("function!");
            // addFunction();
    };

    index++;
};