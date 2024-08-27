process.on('tre2s',function(dem)
          {
    console.log('Su kien tre xay ra: ',dem,'s');
});

setTimeout(function()
{
    console.log('Gi gi do su kien di dc 2s');
    process.emit('tre2s',5);
},2000);