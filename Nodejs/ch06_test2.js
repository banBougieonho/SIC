var result = 0;

console.time('tinh_cai_gi');
for (var i = 1; i<=1000; i++)
{
    result+=i;
}
console.timeEnd('tinh_cai_gi');
console.log("Cong tu 1 den 1000 :  ",result);

console.log("Day la duong dan file a: ",__filename);
console.log("Day la duong dan thu muc chua file a: ",__dirname);

var Person = {name: 'Bou', age: 20};
console.dir(Person)

console.log('Cha dich dc: '+process.argv.length);
console.dir(process.argv);

process.argv.forEach(function(item,index)
{
    console.log(index + ':' + item);
});