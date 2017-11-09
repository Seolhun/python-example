function extractOddNumbers(n) {
    let result = n.match(/\d*[13579]+/g);
    result.forEach(function (value, index) {
        if (value % 2 !== 0) {
            result[index] = Math.pow(value, 2)
        }
    })


    let sum = result.reduce(function (a, b) {
        return a + b;
    }, 0);
    return console.log(sum)
}

extractOddNumbers("ab2v9bc13j5jf4jv21")