var os = require('os')

console.log('Ten cua he thong: ', os.hostname());
console.log('Dung luong dang dung: %d / %d',os.freemem(),os.totalmem());
console.log('Thong tin cua Cpu:');
console.dir(os.cpus());
console.log('Thong tin cua giao dien mang:');
console.dir(os.networkInterfaces());
