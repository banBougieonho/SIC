http = require('http')
http.createServer(function(rq,res){
    res.writeHead(200,{'Content - Type': 'text/html'});
    res.write('<h1>Hi Bou</h1>')
    res.end('\r\nKet thuc trang web')
}).listen(8089)