var f = require('fs')
f.writeFile('./exp.txt','Hello Bou',function(err){
    if (err){
        console.log("Loi gi file " + err);
    }
    else{
        console.log("ghi file thanh cong !")
    }
})