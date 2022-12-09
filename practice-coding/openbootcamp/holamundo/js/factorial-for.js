let n;
var result = 1;

function factorial(n){
    for(let i = 1; i <= n; i++){
        result = result * i;
    };
    return result
}


factorial(10);
console.log(result)