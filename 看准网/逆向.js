const cryptoJs = require('crypto-js');
var MA = function(e) {
    void 0 === e && (e = 16);
    for (var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'.split(''), n = '', r = 0; r < e; r++) {
        n += t[Math.ceil(61 * Math.random())];
    }
    return n;
};


var l = function(e, t) {
    // e: 要加密的数据
    // t: iv
    var key = {
        'words': [
            1193550929,
            1635214187,
            1197891916,
            1111046002,
        ],
        'sigBytes': 16,
    };
    var r = cryptoJs.AES.encrypt(e, key, {
        iv: cryptoJs.enc.Utf8.parse(t),
        mode: cryptoJs.mode.CBC,
        padding: cryptoJs.pad.Pkcs7,
    });
    return r = r.toString();
};


function encrypt(data) {
    var s = MA();
    var n = JSON.stringify(data);
    var b = l(n, s).replace(/\//g, '_').replace(/\+/g, '-').replace(/=/g, '~');
    return {'b': b, 'kiv': s};
}

var c = function(e, t) {
    // e: 要解密的数据
    // t: iv
    var key = {
        'words': [
            1193550929,
            1635214187,
            1197891916,
            1111046002,
        ],
        'sigBytes': 16,
    };
    var r = cryptoJs.AES.decrypt(e.toString(), key, {
        iv: cryptoJs.enc.Utf8.parse(t),
        mode: cryptoJs.mode.CBC,
        padding: cryptoJs.pad.Pkcs7,
    });
    return r = r.toString(cryptoJs.enc.Utf8);
};

function decrypt(data, iv) {
    return c(data, iv);
}
