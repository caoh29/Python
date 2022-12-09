let n;
var result = 1;

function factorial(n){
    let i = 1;
    while(true){
        result = result * i;
        i++;

        if (i == n){
            break;
        }
    }
    return result
}


factorial(10);
console.log(result)