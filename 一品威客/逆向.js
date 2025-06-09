// node标准库
let crypto = require('crypto');
let CryptoJS = require('crypto-js');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}


var h_e = function() {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 5;
    return Math.random().toString(36).substring(3, 3 + e);
};



function r(e) {
    return r = 'function' == typeof Symbol && 'symbol' == typeof Symbol.iterator ? function(e) {
            return typeof e;
        }
        : function(e) {
            return e && 'function' == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? 'symbol' : typeof e;
        }
        ,
        r(e);
}

var f = function(t) {
    var e = '';
    return Object.keys(t).sort().forEach((function(n) {
            e += n + ('object' === Object(r)(t[n]) ? JSON.stringify(t[n], (function(t, e) {
                    return 'number' == typeof e && (e = String(e)),
                        e;
                }
            )).replace(/\//g, '\\/') : t[n]);
        }
    )),
        e;
};


var l = {
    key: CryptoJS.enc.Utf8.parse('fX@VyCQVvpdj8RCa'),
    iv: CryptoJS.enc.Utf8.parse(function(t) {
        for (var e = '', i = 0; i < t.length - 1; i += 2) {
            var n = parseInt(t[i] + '' + t[i + 1], 16);
            e += String.fromCharCode(n);
        }
        return e;
    }('00000000000000000000000000000000')),
};

var v = function(data) {
    return function(data) {
        return CryptoJS.AES.encrypt(data, l.key, {
            iv: l.iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        }).toString();
    }(data);
};

var h = function(t) {
    var data = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , e = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : 'a75846eb4ac490420ac63db46d2a03bf'
        , n = e + f(data) + f(t) + e;
    return n = do_md5(n),
        n = v(n);
};

// var Signature = h(U, M, 'a75846eb4ac490420ac63db46d2a03bf');
// console.log(Signature);

function main(data) {
    var D = parseInt((new Date).getTime() / 1e3);
    var U = {
        'App-Ver': '',
        'Os-Ver': '',
        'Device-Ver': '',
        Imei: '',
        'Access-Token': '',
        Timestemp: D,
        NonceStr: ''.concat(D).concat(h_e()),
        'App-Id': '4ac490420ac63db4',
        'Device-Os': 'web',
    };
    U.Signature = h(U, data, 'a75846eb4ac490420ac63db46d2a03bf');
    return U
}

console.log(main());