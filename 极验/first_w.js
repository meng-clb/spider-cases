const {RSAKey} = require('node-jsencrypt');
const CryptoJS = require('crypto-js');

function $_DJB(e) {
    this['$_BAEt'] = e || [];
    // console.log(this['$_BAEt']);
}

$_DJB['prototype'] = {
    '\u0024\u005f\u0045\u0042\u006c': function(e) {
        var t = this['$_BAEt'];
        if (t['map'])
            return new $_DJB(t['map'](e));
        for (var n = [], r = 0, o = t['length']; r < o; r += 1)
            n[r] = e(t[r], r, this);
        return new $_DJB(n);
    },
};


function $_BIBg() {

    var n = this
        , r = {}
        , o = [];
    var arr = [
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
    // new $_DJB(arr)
    return new $_DJB(arr)['$_EBl'](function(e) {

        var t = r[e];
        o['push']((void 0 === t) ? -1 : t);
    }),
        o['join']('!!');
}

var quanju = {
    '$_EJV': {
        'gt': '',  // TODO 这里需要传递进来值
        'challenge': '',
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
        'fullpage': '/static/js/fullpage.9.1.9-r8k4eq.js',
        'slide': '/static/js/slide.7.9.2.js',
        'geetest': '/static/js/geetest.6.0.9.js',
        'aspect_radio': {
            'slide': 103,
            'click': 128,
            'voice': 128,
            'beeline': 50,
        },
    },
    '$_EID': {
        'aeskey': undefined,
    },
};


function e() {
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
}

function te() {
    return e() + e() + e() + e();
}

function $_CCHU(e) {
    return quanju['$_EID']['aeskey'] && !e || (quanju['$_EID']['aeskey'] = te()),
        quanju['$_EID']['aeskey'];
}


function $_CCGw(e) {
    var rsa = new RSAKey();
    rsa['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    var t = rsa['encrypt']($_CCHU(e));
    while (!t || 256 !== t['length'])
        t = rsa['encrypt']($_CCHU(!0));
    return t;
}

function parse(e) {

    for (var t = e['length'], n = [], r = 0; r < t; r++)
        n[r >>> 2] |= (255 & e['charCodeAt'](r)) << 24 - r % 4 * 8;
    return new l['init'](n, t);
}

function encrypt1(e, t, n) {

    // t = u['parse'](t),
    // n && n['iv'] || ((n = n || {})['iv'] = u['parse']('0000000000000000'));
    // var r = m['encrypt'](c, e, t, n);
    var key = t;
    var iv = '0000000000000000';
    key = CryptoJS.enc.Utf8.parse(t);
    iv = CryptoJS.enc.Utf8.parse(iv);
    var r = CryptoJS.AES.encrypt(e, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
    });

    var o = r['ciphertext']['words'];
    var i = r['ciphertext']['sigBytes'];
    var s = [];

    for (var a = 0; a < i; a++) {
        var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s['push'](_);
    }
    return s;
}

function $_HBT(e, t) {
    return e >> t & 1;
}

function $_GJI(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}

function $_HCK(e, o) {
    var i = this;
    o || (o = i);
    for (var t = function(e, t) {
        for (var n = 0, r = 24 - 1; 0 <= r; r -= 1)
            1 === $_HBT(t, r) && (n = (n << 1) + $_HBT(e, r));
        return n;
    }, n = '', r = '', s = e['length'], a = 0; a < s; a += 3) {
        var _;
        if (a + 2 < s)
            _ = (e[a] << 16) + (e[a + 1] << 8) + e[a + 2],
                n += $_GJI(t(_, 7274496)) + $_GJI(t(_, 9483264)) + $_GJI(t(_, 19220)) + $_GJI(t(_, 235));
        else {
            var c = s % 3;
            2 == c ? (_ = (e[a] << 16) + (e[a + 1] << 8),
                n += $_GJI(t(_, 7274496)) + $_GJI(t(_, 9483264)) + $_GJI(t(_, 19220)),
                r = '.') : 1 == c && (_ = e[a] << 16,
                n += $_GJI(t(_, 7274496)) + $_GJI(t(_, 9483264)),
                r = '.' + '.');
        }
    }
    return {
        '\u0072\u0065\u0073': n,
        '\u0065\u006e\u0064': r,
    };
}

function $_HEt(e) {
    var t = $_HCK(e);
    return t['res'] + t['end'];
}


function get_first_w(gt, challenge) {
    quanju.$_EJV.gt = gt;
    quanju.$_EJV.challenge = challenge;
    var t = quanju;
    var n = t['$_EID'];

    var e = $_BIBg();  // 浏览器指纹验证
    t['$_CCFY'] = e,
        t['$_EJV']['cc'] = 8,
        t['$_EJV']['ww'] = true,
        t['$_EJV']['i'] = e;
    var r = $_CCGw()
        , o = encrypt1(JSON['stringify'](t['$_EJV']), $_CCHU())
        , i = $_HEt(o);
    var s = {
        '\u0067\u0074': t['$_EJV']['gt'],
        '\u0063\u0068\u0061\u006c\u006c\u0065\u006e\u0067\u0065': t['$_EJV']['challenge'],
        '\u006c\u0061\u006e\u0067': 'zh-cn',
        '\u0070\u0074': 0,
        '\u0063\u006c\u0069\u0065\u006e\u0074\u005f\u0074\u0079\u0070\u0065': 'web',
        '\u0077': i + r,
    };
    return {
        'params': s,
        'aeskey': quanju['$_EID']['aeskey'],
        'finger_print': e
    };
}

// get_first_w();

// console.log($_CCHU());
// console.log(quanju['$_EID']['aeskey']);