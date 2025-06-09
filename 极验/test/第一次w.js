var {RSAKey} = require('node-jsencrypt')
var CryptoJS = require('crypto-js')

// 生成指纹处理
var $_BJA_ = [
    "textLength",
    "HTMLLength",
    "documentMode",
    "A",
    "ARTICLE",
    "ASIDE",
    "AUDIO",
    "BASE",
    "BUTTON",
    "CANVAS",
    "CODE",
    "IFRAME",
    "IMG",
    "INPUT",
    "LABEL",
    "LINK",
    "NAV",
    "OBJECT",
    "OL",
    "PICTURE",
    "PRE",
    "SECTION",
    "SELECT",
    "SOURCE",
    "SPAN",
    "STYLE",
    "TABLE",
    "TEXTAREA",
    "VIDEO",
    "screenLeft",
    "screenTop",
    "screenAvailLeft",
    "screenAvailTop",
    "innerWidth",
    "innerHeight",
    "outerWidth",
    "outerHeight",
    "browserLanguage",
    "browserLanguages",
    "systemLanguage",
    "devicePixelRatio",
    "colorDepth",
    "userAgent",
    "cookieEnabled",
    "netEnabled",
    "screenWidth",
    "screenHeight",
    "screenAvailWidth",
    "screenAvailHeight",
    "localStorageEnabled",
    "sessionStorageEnabled",
    "indexedDBEnabled",
    "CPUClass",
    "platform",
    "doNotTrack",
    "timezone",
    "canvas2DFP",
    "canvas3DFP",
    "plugins",
    "maxTouchPoints",
    "flashEnabled",
    "javaEnabled",
    "hardwareConcurrency",
    "jsFonts",
    "timestamp",
    "performanceTiming",
    "internalip",
    "mediaDevices",
    "DIV",
    "P",
    "UL",
    "LI",
    "SCRIPT",
    "touchEvent"
]
function ae(e) {
    this['$_BADk'] = e || [];
}
ae.prototype.$_DJp = function(e) {
    var t = this['$_BADk'];
    return new ae(t['map'](e));
}
var $_BIHS = function(e) {
    return void 0 === e;
}
var $_BIBi = function() {
    var n = this
      , r = {}
      , o = [];
    return new ae($_BJA_)['$_DJp'](function(e) {
        var t = r[e];
        o['push']($_BIHS(t) ? -1 : t);
    }),
    o['join']('!!');
}

// 生成公钥
var ee = function() {
    function e() {
        return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
    }
    return function() {
        return e() + e() + e() + e();
    }
    ;
}();
config = {
    'aeskey': undefined
}
var $_CCIm = function(e) {
    return config['aeskey'] && !e || (config['aeskey'] = ee()),
    config['aeskey'];
}
var G = function() {
        var rsa = new RSAKey();
        rsa.setPublic('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
        return rsa
}
var $_CCHk = function(e) {
    var t = new G()['encrypt']($_CCIm(e));
    while (!t || 256 !== t['length'])
        t = new G()['encrypt']($_CCIm(!0));
    return t;
}

// 数据加密
var encrypt1 = function(e, t, n) {
    // AES加密
      l = {
        key: CryptoJS.enc.Utf8.parse(t),
        iv: CryptoJS.enc.Utf8.parse('0000000000000000'),
      }
      var r = CryptoJS.AES.encrypt(e, l.key, {
          iv: l.iv,
          mode: CryptoJS.mode.CBC,
          padding: CryptoJS.pad.Pkcs7
        })
    var o = r['ciphertext']['words']
    var i = r['ciphertext']['sigBytes']
    var s = []
    for (a = 0; a < i; a++) {
        var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s['push'](_);
    }
    return s;
}
var $_HAn = function(e, t) {
    return e >> t & 1;
}
var $_GIQ = function(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}
var $_HBR = function(e, o) {
    var i = this;
    o || (o = i);
    for (var t = function(e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            1 === $_HAn(t, r) && (n = (n << 1) + $_HAn(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var _;
        if (a + 2 < s)
            _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2],
            n += $_GIQ(t(_, 7274496)) + $_GIQ(t(_, 9483264)) + $_GIQ(t(_, 19220)) + $_GIQ(t(_, 235));

        else {
            var c = s % 3;
            2 == c ? (_ = (e[a] << 16) + (e[a + 1] << 8),
            n += $_GIQ(t(_, 7274496)) + $_GIQ(t(_, 9483264)) + $_GIQ(t(_, 19220)),
            r = '.') : 1 == c && (_ = e[a] << 16,
            n += $_GIQ(t(_, 7274496)) + $_GIQ(t(_, 9483264)),
            r = '.' + '.');
        }
    }
    return {
        'res': n,
        'end': r
    };
}
// 对AES加密后返回的数组进行处理为字符串
var $_HDZ = function(e) {
    var t = $_HBR(e);
    return t['res'] + t['end'];
}

function first_w(gt, challenge) {
    var t = {'$_EIY':{
    "gt": gt,
    "challenge": challenge,
    "offline": false,
    "new_captcha": true,
    "product": "float",
    "width": "300px",
    "https": true,
    "api_server": "apiv6.geetest.com",
    "protocol": "https://",
    "type": "fullpage",
    "static_servers": [
        "static.geetest.com/",
        "static.geevisit.com/"
    ],
    "beeline": "/static/js/beeline.1.0.1.js",
    "voice": "/static/js/voice.1.2.4.js",
    "click": "/static/js/click.3.1.0.js",
    "fullpage": "/static/js/fullpage.9.1.8-bfget5.js",
    "slide": "/static/js/slide.7.9.2.js",
    "geetest": "/static/js/geetest.6.0.9.js",
    "aspect_radio": {
        "slide": 103,
        "click": 128,
        "voice": 128,
        "beeline": 50
    },
    "cc": 6,
    "ww": true,
    "i": "-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1"
}}
        // , n = {'cc': 6,};
    // 生成一个指纹
    var e = $_BIBi();
    // t['$_CCGk'] = e,
        t['$_EIY']['cc'] = 6,
        t['$_EIY']['ww'] = true,
        t['$_EIY']['i'] = e;
    // 生成公钥
    var r = $_CCHk()
        , o = encrypt1(JSON['stringify'](t['$_EIY']), $_CCIm())
        , i = $_HDZ(o)
        , s = {
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'pt': 0,
        'client_type': 'web',
        'w': i + r,
        'aeskey': config.aeskey
    };
    console.log(i)
    return s
}
// first_w('019924a82c70bb123aae90d483087f94', '4c68715eabbe49c779d14248956c6fba')