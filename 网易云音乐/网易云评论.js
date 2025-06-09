const CryptoJS = require('crypto-js');
const {setMaxDigits, RSAKeyPair, encryptedString} = require('./rsa.js');

function a(a) {
    var d, e, b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', c = '';
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
    return c;
}

function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
        , d = CryptoJS.enc.Utf8.parse('0102030405060708')
        , e = CryptoJS.enc.Utf8.parse(a)
        , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC,
    });
    return f.toString();
}

function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
        d = new RSAKeyPair(b, '', c),
        e = encryptedString(d, a);
}

function fun(d, e, f, g) {
    var h = {}
        , i = a(16);
    return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h;
}


// 获取歌曲链接
function main(song_id) {
    let d = `{"ids":"[${song_id}]","level":"standard","encodeType":"aac","csrf_token":"7f841d17d5a1cc2672e080979b2dc659"}`;
    let e = '010001';
    let f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7';
    let g = '0CoJUm6Qyw8W8jud';
    let data = fun(d, e, f, g);

    return data;
}

function comment() {
    // 替换歌曲id, pageNo 可以获取不同页数的评论, 修改pageSize可以获得不同的数据量
    let d ='{' +
        '"rid":"R_SO_4_2130933471",' +
        '"threadId":"R_SO_4_2130933471",' +
        '"pageNo":"2",' +
        '"pageSize":"100",' +
        '"cursor":"1711193956224",' +
        '"offset":"0",' +
        '"orderType":"1",' +
        '"csrf_token":"7f841d17d5a1cc2672e080979b2dc659"' +
        '}'

    let one = '{' +
        '"rid":"R_SO_4_2136351674",' +
        '"threadId":"R_SO_4_2136351674",' +
        '"pageNo":"1",' +
        '"pageSize":"20",' +
        '"cursor":"-1",' +
        '"offset":"0",' +
        '"orderType":"1",' +
        '"csrf_token":"7f841d17d5a1cc2672e080979b2dc659"' +
        '}'

    let e = '010001';
    let f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7';
    let g = '0CoJUm6Qyw8W8jud';
    let data = fun(d, e, f, g);
    // console.log(data);
    return data;
}

// comment()