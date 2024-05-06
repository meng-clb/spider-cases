// node标准库
let crypto = require('crypto');
const CryptoJS = require('crypto-js');

function H(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

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

var $_GHr = function(e) {
    for (var t = [], n = 0, r = e['length']; n < r; n += 1)
        t['push'](e['charCodeAt'](n));
    return t;
};
var $_HDB = function(e) {
    var t = $_HCR($_GHr(e));
    return t['res'] + t['end'];
};

var $_HEv = function(e) {
    var t = $_HCR(e);
    return t['res'] + t['end'];
};
var $_CEDu = function() {
    return {
        'v': '9.1.9-glhvqm',
        'te': false,
        '$_BCQ': true,
        'ven': 'Google Inc. (Intel)',
        'ren': 'ANGLE (Intel, Intel(R) UHD Graphics 620 (0x00005917) Direct3D11 vs_5_0 ps_5_0, D3D11)',
        'fp': [
            'down',
            758,
            308,
            1713970205097,
            'pointerdown',
        ],
        'lp': [
            'up',
            758,
            308,
            1713970205160,
            'pointerup',
        ],
        'em': {
            'ph': 0,
            'cp': 0,
            'ek': '11',
            'wd': 1,
            'nt': 0,
            'si': 0,
            'sc': 0,
        },
        'tm': {
            'a': 1713970195054,
            'b': 1713970197145,
            'c': 1713970197146,
            'd': 0,
            'e': 0,
            'f': 1713970195082,
            'g': 1713970195082,
            'h': 1713970195082,
            'i': 1713970195094,
            'j': 1713970195405,
            'k': 1713970195095,
            'l': 1713970195406,
            'm': 1713970197102,
            'n': 1713970197139,
            'o': 1713970197152,
            'p': 1713970198885,
            'q': 1713970198885,
            'r': 1713970198888,
            's': 1713970198964,
            't': 1713970198964,
            'u': 1713970198970,
        },
        'dnf': 'dnf',
        'by': 0,
    };
};


// ====== 加密 =========
var config = {
    'aeskey': '',
};
var te = function() {
    function e() {
        return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
    }

    return function() {
        return e() + e() + e() + e();
    };
}();

var $_CCHI = function(e) {
    return config['aeskey'] && !e || (config['aeskey'] = te()),
        config['aeskey'];
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
// ==================


var second_w = function(gt, challenge, cc, ss, aeskey) {
    var i = {
            '$_EIi': {
                '$_CAAj': 1713968330549,
                'protocol': 'https://',
                'gt': gt,
                'challenge': challenge,
                'offline': false,
                'new_captcha': true,
                'product': 'popup',
                'width': '300px',
                'https': true,
                'api_server': 'api.geetest.com',
                'type': 'fullpage',
                'static_servers': [
                    'static.geetest.com',
                    'static.geevisit.com',
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
                'cc': 8,
                'supportWorker': true,
                '$_FFG': {
                    'pt': 0,
                },
                'aeskey': aeskey,
                'theme': 'wind',
                'theme_version': '1.5.8',
                'logo': true,
                'feedback': 'https://www.geetest.com/contact#report',
                'c': cc,
                's': ss,
                'i18n_labels': {
                    'copyright': '由极验提供技术支持',
                    'error': '网络不给力',
                    'error_content': '请点击此处重试',
                    'error_title': '网络超时',
                    'fullpage': '智能检测中',
                    'goto_cancel': '取消',
                    'goto_confirm': '前往',
                    'goto_homepage': '是否前往验证服务Geetest官网',
                    'loading_content': '智能验证检测中',
                    'next': '正在加载验证',
                    'next_ready': '请完成验证',
                    'read_reversed': false,
                    'ready': '点击按钮进行验证',
                    'refresh_page': '页面出现错误啦！要继续操作，请刷新此页面',
                    'reset': '请点击重试',
                    'success': '验证成功',
                    'success_title': '通过验证',
                },
            },
            '$_CCFN': '-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1',
        }
        , e = 'M(*((1((M(('
        , t = 'M(*((1((M(('
        ,
        n = '-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1'
        , r = ''
        , o = i['$_EIi']
        , s = 365598;
    i['$_CECj'] = '';

    for (var a = [['lang', 'zh-cn' || 'zh-cn'], ['type', 'fullpage'], ['tt', function(e, t, n) {
        if (!t || !n)
            return e;
        var r, o = 0, i = e, s = t[0], a = t[2], _ = t[4];
        while (r = n['substr'](o, 2)) {
            o += 2;
            var c = parseInt(r, 16)
                , l = String['fromCharCode'](c)
                , u = (s * c * c + a * c + _) % e['length'];
            i = i['substr'](0, u) + l + i['substr'](u);
        }
        return i;
    }(e, o['c'], o['s']) || -1], ['light', r || -1], ['s', H($_HDB(t))], ['h', H($_HDB(n))], ['hh', H(n)], ['hi', H(i['$_CCFN'])], ['vip_order', undefined || -1], ['ct', undefined || -1], ['ep', $_CEDu() || -1], ['passtime', s || -1], ['rp', H(o['gt'] + o['challenge'] + s)]], _ = 0; _ < a['length']; _++)
        i['$_CECj'] += '"' + a[_][0] + '":' + JSON['stringify'](a[_][1]) + ',';

    i['$_CEEc'] = function l() {
        var t = ['bbOy'];
        return function(e) {
            t['push']('');
            var r = '';
            !function o(e, t) {
                function n(e) {
                    var t = 5381
                        , n = e['length']
                        , r = 0;
                    while (n--)
                        t = (t << 5) + t + e['charCodeAt'](r++);
                    return t &= ~(1 << 31);
                }

                var o_str = 'function o(e,t){var $_CFGDq=__GCt.$_CI,$_CFGCO=[\'$_CFGGz\'].concat($_CFGDq),$_CFGEY=$_CFGCO[1];$_CFGCO.shift();var $_CFGFh=$_CFGCO[0];function n(e){var $_DDHGQ=__GCt.$_DH()[8][12];for(;$_DDHGQ!==__GCt.$_DH()[10][10];){switch($_DDHGQ){case __GCt.$_DH()[10][12]:var t=5381,n=e[$_CFGDq(1)],r=0;while(n--)t=(t<<5)+t+e[$_CFGDq(85)](r++);$_DDHGQ=__GCt.$_DH()[8][11];break;case __GCt.$_DH()[8][11]:return t&=~(1<<31);break;}}}100<new Date()[$_CFGEY(273)]()-t[$_CFGDq(273)]()&&(e=$_CFGEY(1158)),r=$_CFGDq(765)+i[$_CFGDq(1185)]+$_CFGEY(1129)+n(o[$_CFGEY(16)]()+n(n[$_CFGEY(16)]())+n(e[$_CFGEY(16)]()))+$_CFGEY(1126);}';
                var n_str = 'function n(e){var $_DDHGQ=__GCt.$_DH()[8][12];for(;$_DDHGQ!==__GCt.$_DH()[10][10];){switch($_DDHGQ){case __GCt.$_DH()[10][12]:var t=5381,n=e[$_CFGDq(1)],r=0;while(n--)t=(t<<5)+t+e[$_CFGDq(85)](r++);$_DDHGQ=__GCt.$_DH()[8][11];break;case __GCt.$_DH()[8][11]:return t&=~(1<<31);break;}}}';
                var e_str = 'bbOy';
                var $_CECj = '"lang":"zh-cn","type":"fullpage","tt":"M(9A(U(-(92rEd((sX5)@M9)((BOFlb1(","light":"SPAN_0","s":"c7c3e21112fe4f741921cb3e4ff9f7cb","h":"321f9af1e098233dbd03f250fd2b5e21","hh":"39bd9cad9e425c3a8f51610fd506e3b3","hi":"09eb21b3ae9542a9bc1e8b63b3d9a467","vip_order":-1,"ct":-1,"ep":{"v":"9.1.9-glhvqm","te":false,"$_BCQ":true,"ven":"Google Inc. (Intel)","ren":"ANGLE (Intel, Intel(R) UHD Graphics 620 (0x00005917) Direct3D11 vs_5_0 ps_5_0, D3D11)","fp":["down",787,307,1713965776086,"pointerdown"],"lp":["up",787,307,1713965776233,"pointerup"],"em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0},"tm":{"a":1713965750386,"b":1713965753135,"c":1713965753135,"d":0,"e":0,"f":1713965750423,"g":1713965750423,"h":1713965750423,"i":1713965750445,"j":1713965751270,"k":1713965750445,"l":1713965751270,"m":1713965753101,"n":1713965753118,"o":1713965753141,"p":1713965770948,"q":1713965770948,"r":1713965770953,"s":1713965771037,"t":1713965771037,"u":1713965771048},"dnf":"dnf","by":0},"passtime":1552,"rp":"29b02fc9c8d05b28ff91565dc86c1cb0",';
                100 < new Date()['getTime']() - t['getTime']() && (e = 'qwe'),
                    r = '{' + $_CECj + '"captcha_token":"' + n(o_str + n(n_str) + n(e_str)) + '","n8md":"gfdpqvbj"}';
            }(t['shift'](), new Date());
            i['$_CEAR'] = $_HEv(encrypt1(r, aeskey));
        };
    }();
    i['$_CEEc']('');
    return i;
};

// var gt = '019924a82c70bb123aae90d483087f94';
// var challenge = 'c9cff9b64298fafb762d57df2d56126c';
// var c = [
//     12,
//     58,
//     98,
//     36,
//     43,
//     95,
//     62,
//     15,
//     12,
// ];
// var s = '3a58662d';
// var aeskey = '1a0f4801f8b33b74';
// console.log(second_w(gt, challenge, c, s, aeskey));