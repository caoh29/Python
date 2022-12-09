let n;
var result = 1;

function factorial(n){
    let i = 1;
    while(i <= n){
        result = result * i;
        i++;
    }
    return result
}


factorial(10);
console.log(result)