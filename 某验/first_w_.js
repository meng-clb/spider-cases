const {RSAKey} = require('node-jsencrypt');
const CryptoJS = require('crypto-js');

// ========== 浏览器指纹 ============
function $_DJw(e) {
    this['$_BAEp'] = e || [];
}

$_DJw.prototype.$_EBL = function(e) {
    var t = this['$_BAEp'];
    if (t['map'])
        return new $_DJw(t['map'](e));
    for (var n = [], r = 0, o = t['length']; r < o; r += 1)
        n[r] = e(t[r], r, this);
    return new $_DJw(n);
};

var $_BJAc = function() {
    return [
        'textLength',
        'HTMLLength',
        'documentMode',
        'A',
        'ARTICLE',
        'ASIDE',
        'AUDIO',
        'BASE',
        'BUTTON',
        'CANVAS',
        'CODE',
        'IFRAME',
        'IMG',
        'INPUT',
        'LABEL',
        'LINK',
        'NAV',
        'OBJECT',
        'OL',
        'PICTURE',
        'PRE',
        'SECTION',
        'SELECT',
        'SOURCE',
        'SPAN',
        'STYLE',
        'TABLE',
        'TEXTAREA',
        'VIDEO',
        'screenLeft',
        'screenTop',
        'screenAvailLeft',
        'screenAvailTop',
        'innerWidth',
        'innerHeight',
        'outerWidth',
        'outerHeight',
        'browserLanguage',
        'browserLanguages',
        'systemLanguage',
        'devicePixelRatio',
        'colorDepth',
        'userAgent',
        'cookieEnabled',
        'netEnabled',
        'screenWidth',
        'screenHeight',
        'screenAvailWidth',
        'screenAvailHeight',
        'localStorageEnabled',
        'sessionStorageEnabled',
        'indexedDBEnabled',
        'CPUClass',
        'platform',
        'doNotTrack',
        'timezone',
        'canvas2DFP',
        'canvas3DFP',
        'plugins',
        'maxTouchPoints',
        'flashEnabled',
        'javaEnabled',
        'hardwareConcurrency',
        'jsFonts',
        'timestamp',
        'performanceTiming',
        'internalip',
        'mediaDevices',
        'DIV',
        'P',
        'UL',
        'LI',
        'SCRIPT',
        'touchEvent',
    ];
};

var $_BIHK = function(e) {
    return void 0 === e;
};

var $_BIBF = function() {
    var n = this
        , r = {}
        , o = [];
    return new $_DJw($_BJAc())['$_EBL'](function(e) {
        var t = r[e];
        o['push']($_BIHK(t) ? -1 : t);
    }),
        o['join']('!!');
};
// =========== 指纹结束 =====================

// ================ 计算r的值 ===============
function X() {
    var rsa = new RSAKey();
    rsa['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    return rsa;
}


te = function() {
    function e() {
        return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
    }

    return function() {
        return e() + e() + e() + e();
    };
}();

var config = {
    'aeskey': undefined,
};
var $_CCHI = function(e) {
    return config['aeskey'] && !e || (config['aeskey'] = te()),
        config['aeskey'];
};

var $_CCGH = function(e) {
    var t = new X()['encrypt']($_CCHI(e));
    while (!t || 256 !== t['length'])
        t = new X()['encrypt']($_CCHI(!0));
    return t;
};
// ================ r结束 ===============

// ================ o开始 ===============
var parse = function(e) {
    for (var t = e['length'], n = [], r = 0; r < t; r++)
        n[r >>> 2] |= (255 & e['charCodeAt'](r)) << 24 - r % 4 * 8;
    return new l[('init')](n, t);
};

var encrypt1 = function(e, t, n) {
    t = CryptoJS.enc.Utf8.parse(t),
    n && n['iv'] || ((n = n || {})['iv'] = CryptoJS.enc.Utf8.parse('0000000000000000'));
    var r = CryptoJS.AES.encrypt(e, t, n);
    var o = r['ciphertext']['words'];
    var i = r['ciphertext']['sigBytes'];
    var s = [];
    for (var a = 0; a < i; a++) {
        var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s['push'](_);
    }
    return s;
};

// ================ o结束 ===============

// ================ i开始 ===============
var $_HBX = function(e, t) {
    return e >> t & 1;
};

var $_GJr = function(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
};
var $_HCR = function(e, o) {
    for (var t = function(e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            1 === $_HBX(t, r) && (n = (n << 1) + $_HBX(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var _;
        if (a + 2 < s)
            _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2],
                n += $_GJr(t(_, 7274496)) + $_GJr(t(_, 9483264)) + $_GJr(t(_, 19220)) + $_GJr(t(_, 235));
        else {
            var c = s % 3;
            2 == c ? (_ = (e[a] << 16) + (e[a + 1] << 8),
                n += $_GJr(t(_, 7274496)) + $_GJr(t(_, 9483264)) + $_GJr(t(_, 19220)),
                r = '.') : 1 == c && (_ = e[a] << 16,
                n += $_GJr(t(_, 7274496)) + $_GJr(t(_, 9483264)),
                r = '.' + '.');
        }
    }
    return {
        'res': n,
        'end': r,
    };
};

var $_HEv = function(e) {
    var t = $_HCR(e);
    return t['res'] + t['end'];
};
// ================ i结束 ===============


// ==================== 主程序 ===========
var first_w = function(gt, challenge) {

    var t = {
        $_EJY: {
            'gt': gt,
            'challenge': challenge,
            'offline': false,
            'new_captcha': true,
            'product': 'popup',
            'width': '300px',
            'https': true,
            'api_server': 'apiv6.geetest.com',
            'protocol': 'https://',
            'type': 'fullpage',
            'static_servers': [
                'static.geetest.com/',
                'static.geevisit.com/',
            ],
            'beeline': '/static/js/beeline.1.0.1.js',
            'voice': '/static/js/voice.1.2.4.js',
            'click': '/static/js/click.3.1.0.js',
            'fullpage': '/static/js/fullpage.9.1.9-glhvqm.js',
            'slide': '/static/js/slide.7.9.2.js',
            'geetest': '/static/js/geetest.6.0.9.js',
            'aspect_radio': {
                'slide': 103,
                'click': 128,
                'voice': 128,
                'beeline': 50,
            },
        },
    };

    var e = $_BIBF();  // 浏览器指纹验证

    t['$_CCFN'] = e,
        t['$_EJY']['cc'] = 8,
        t['$_EJY']['ww'] = true,
        t['$_EJY']['i'] = e;

    var r = $_CCGH();
    var o = encrypt1(JSON['stringify'](t['$_EJY']), $_CCHI());
    var i = $_HEv(o);
    var s = {
        'gt': t['$_EJY']['gt'],
        'challenge': t['$_EJY']['challenge'],
        'lang': 'zh-cn',
        'pt': 0,
        'client_type': 'web',
        'w': i + r,
    };
    return {
        'w': s['w'],
        'aeskey': config.aeskey,
    };
};
// first_w()
console.log(first_w());
