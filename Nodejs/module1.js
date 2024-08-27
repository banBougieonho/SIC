var calc ={};
calc.add = function(a,b)
{
    return a+b;
}
module.exports = calc;
console.log('Before lam gi do trong module -'+'Ket qua cua phep tinh cong la: %d', calc.add(10,20));
console.log("Cach goi ham");

var calcc = require('./calc.js')
console.log('Sau khi cat module thi ket qua cua phep cong la :',calcc.add(10,20))