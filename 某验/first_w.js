let CryptoJS = require('crypto-js');
const {RSAKey} = require('node-jsencrypt');


var get_first_w = function(gt, challenge) {
    var config = {
        'aeskey': undefined,
    };
    var $_EJY = {
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
        'static_servers': ['static.geetest.com/', 'static.geevisit.com/'],
        'beeline': '/static/js/beeline.1.0.1.js',
        'voice': '/static/js/voice.1.2.4.js',
        'click': '/static/js/click.3.1.0.js',
        'fullpage': '/static/js/fullpage.9.1.9-glhvqm.js',
        'slide': '/static/js/slide.7.9.2.js',
        'geetest': '/static/js/geetest.6.0.9.js',
        'aspect_radio': {'slide': 103, 'click': 128, 'voice': 128, 'beeline': 50},
        'cc': 8,
        'ww': true,
        'i': '-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1',
    };

    //  获取第一个w的r值
    function X() {
        var rsa = new RSAKey();
        rsa['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
        return rsa;
    }

    var e = function() {
        return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
    };
    var te = function() {
        return e() + e() + e() + e();
    };

    var $_CCHI = function(e) {
        return config['aeskey'] && !e || (config['aeskey'] = te()),
            config['aeskey'];
    };
    $_CCGH = function(e) {
        var t = new X()['encrypt']($_CCHI(e));
        while (!t || 256 !== t['length'])
            t = new X()['encrypt'](this['$_CCHI'](!0));
        return t;
    };
    // var random_ = function() {
    //     var r = '';
    //     for (var i = 0; i < 4; i++) {
    //         r = r + ((65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1));
    //     }
    //     return r;
    // };

// 获取o的值
    var encrypt1 = function(e, t, n) {
        t = CryptoJS.enc.Utf8.parse(t),
        n && n['iv'] || ((n = n || {})['iv'] = CryptoJS.enc.Utf8.parse('0000000000000000'));
        var r = CryptoJS.AES['encrypt'](e, t, n);
        var o = r['ciphertext']['words'];
        var i = r['ciphertext']['sigBytes'];
        var s = [];
        for (var a = 0; a < i; a++) {
            var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
            s['push'](_);
        }
        return s;
    };
    var o = encrypt1(JSON['stringify']($_EJY), config.aeskey);

// 获取i的值
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

    var r = $_CCGH();
    var i = $_HEv(o);
    var w = i + r;

    return {
        w: w,
        aeskey: config.aeskey,
    };
};
get_first_w();
// console.log(get_first_w());