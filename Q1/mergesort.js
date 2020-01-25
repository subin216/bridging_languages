
var fs = require('fs');
var path = require('path');

// Merge the two arrays: left and right
function merge(left, right) {
	let resultArray = [], leftIndex = 0, rightIndex = 0;

	while (leftIndex < left.length && rightIndex < right.length) {
		if (left[leftIndex] < right[rightIndex]) {
			resultArray.push(left[leftIndex]);
			leftIndex++;
		} else {
			resultArray.push(right[rightIndex]);
			rightIndex++;
		}
	}

	return resultArray
		.concat(left.slice(leftIndex))
		.concat(right.slice(rightIndex));
}

function mergeSort(arr) {
	if (arr.length <= 1) {
		return arr;
	}
	const halfPoint = Math.floor(arr.length / 2);
	const left = arr.slice(0, halfPoint);
	const right = arr.slice(halfPoint);
	// console.log("left ", left)
	// console.log("right ", right)
	return merge(mergeSort(left), mergeSort(right));
}


var filePath = path.join(__dirname, process.argv[2]);
var stuff = fs.readFileSync(filePath, 'utf8');
// const arr = process.argv[2];
// console.log(stuff);

// console.log(stuff.split("\n"));

let arr = stuff.split("\n")[1];
// console.log(arr.split(" ").map(n => Number(n)));
arr = arr.split(" ").map(n => Number(n));

console.log(mergeSort(arr).join(" "));
// console.log(mergeSort([4, 6, 2, 68, 2, 1, 66, 22]));