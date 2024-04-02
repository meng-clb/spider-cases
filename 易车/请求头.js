// node标准库
let crypto = require('crypto');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

var timestamp = +new Date;


function sign() {
    var n = '';
    var i = '{"cityId":"1004","serialId":"1661"}'
        , o = '19DDD1FBDFF065D3A4DA777D2D7A81EC';
    n = 'cid=' + '508' + '&param=' + i + o + timestamp;

    return do_md5(n);
}


function user_guid(cookie) {
    e = 'UserGuid';
    var t, r = new RegExp('(^| )' + e + '=([^;]*)(;|$)'), n = '';
    return (t = cookie.match(r)) && (n = t[2]),
        decodeURIComponent(n);
}


function main(cookie) {
    x_sign = sign();
    x_user_guid = user_guid(cookie);
    return {
        'X-Timestamp': timestamp,
        'X-Sign': x_sign,
        'X-User-Guid': x_user_guid,
    };
}