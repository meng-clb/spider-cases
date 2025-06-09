// node标准库
let crypto = require('crypto');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

function main(t, e) {
    e = '5dd20b08158402032845b45f5b67a349';
    var n = ''
        , r = 0
        , a = [];
    for (var i in t)
        (t[i] || 0 == t[i]) && a.push(''.concat(i, '=').concat(t[i]));
    for (var o in a.sort(),
        a)
        n = ''.concat(n).concat(0 === r ? '' : '&').concat(a[o]),
            r++;
    var c = do_md5(''.concat(n, '&key=').concat(e));
    return c;
}

e = '5dd20b08158402032845b45f5b67a349';
// data.sign = fun(data, e)
// console.log(data);