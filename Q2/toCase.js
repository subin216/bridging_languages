const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const commandLineArgs = require('command-line-args')



const optionDefinitions = [
	{ name: 'case', alias: 'c', type: String },
	{ name: 'input', alias: 'i', type: String }
]

const options = commandLineArgs(optionDefinitions)
// console.log(options);


const filePath = path.join(__dirname, options.input);
const stuff = fs.readFileSync(filePath, 'utf8');
console.log(stuff);

const cp = spawn('python', ['cases.py', stuff, options.case]);

cp.stdout.on("data", data => {
	console.log(data.toString())
})
cp.stderr.on("data", err => console.log(err.toString()))