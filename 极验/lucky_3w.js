var {RSAKey} = require('node-jsencrypt');
var CryptoJS = require('crypto-js');
let crypto = require('crypto');

function md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

// 关于轨迹加密的处理
function ct(t) {
    this['$_BCAO'] = t || [];
}

ct.prototype.$_CAE = function(t) {
    var e = this['$_BCAO'];
    if (e['map'])
        return new ct(e['map'](t));
    for (var n = [], r = 0, i = e['length']; r < i; r += 1)
        n[r] = t(e[r], r, this);
    return new ct(n);
};
var $_FD_ = function() {
    function n(t) {
        var e = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
            , n = e['length']
            , r = ''
            , i = Math['abs'](t)
            , o = parseInt(i / n);
        n <= o && (o = n - 1),
        o && (r = e['charAt'](o));
        var s = '';
        return t < 0 && (s += '!'),
        r && (s += '$'),
        s + r + e['charAt'](i %= n);
    }

    var t = function(t) {
        for (var e, n, r, i = [], o = 0, s = 0, a = t['length'] - 1; s < a; s++)
            e = Math['round'](t[s + 1][0] - t[s][0]),
                n = Math['round'](t[s + 1][1] - t[s][1]),
                r = Math['round'](t[s + 1][2] - t[s][2]),
            0 == e && 0 == n && 0 == r || (0 == e && 0 == n ? o += r : (i['push']([e, n, r + o]),
                o = 0));
        return 0 !== o && i['push']([e, n, o]),
            i;
    }(guiji)
        , r = []
        , i = []
        , o = [];
    return new ct(t)['$_CAE'](function(t) {
        var e = function(t) {
            for (var e = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]], n = 0, r = e['length']; n < r; n++)
                if (t[0] == e[n][0] && t[1] == e[n][1])
                    return 'stuvwxyz~'[n];
            return 0;
        }(t);
        e ? i['push'](e) : (r['push'](n(t[0])),
            i['push'](n(t[1]))),
            o['push'](n(t[2]));
    }),
    r['join']('') + '!!' + i['join']('') + '!!' + o['join']('');
};
var $_BBED = function(t, e, n) {
    if (!e || !n)
        return t;
    var r, i = 0, o = t, s = e[0], a = e[2], _ = e[4];
    while (r = n['substr'](i, 2)) {
        i += 2;
        var c = parseInt(r, 16)
            , u = String['fromCharCode'](c)
            , l = (s * c * c + a * c + _) % t['length'];
        o = o['substr'](0, l) + u + o['substr'](l);
    }
    return o;
};


//rsa
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
    'aeskey': undefined,
};
var $_CCIm = function(e) {
    return config['aeskey'] && !e || (config['aeskey'] = ee()),
        config['aeskey'];
};
var G = function() {
    var rsa = new RSAKey();
    rsa.setPublic('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    return rsa;
};
var $_CCDm = function(e) {
    var t = new G()['encrypt']($_CCIm(e));
    while (!t || 256 !== t['length'])
        t = new G()['encrypt']($_CCIm(!0));
    return t;
};

function H(t, e) {
    for (var n = e['slice'](-2), r = [], i = 0; i < n['length']; i++) {
        var o = n['charCodeAt'](i);
        r[i] = 57 < o ? o - 87 : o - 48;
    }
    n = 36 * r[0] + r[1];
    var s, a = Math['round'](t) + n, _ = [[], [], [], [], []], c = {}, u = 0;
    i = 0;

    for (var l = (e = e['slice'](0, -2))['length']; i < l; i++)
        c[s = e['charAt'](i)] || (c[s] = 1,
            _[u]['push'](s),
            u = 5 == ++u ? 0 : u);
    var h, f = a, d = 4, p = '', g = [1, 2, 5, 10, 50];
    while (0 < f)
        0 <= f - g[d] ? (h = parseInt(Math['random']() * _[d]['length'], 10),
            p += _[d][h],
            f -= g[d]) : (_['splice'](d, 1),
            g['splice'](d, 1),
            d -= 1);
    return p;
}

var $_CCCY = function() {
    return {
        'v': '7.9.2',
        '$_BIE': false,
        'me': true,
        'tm': {
            'a': 1706017034364,
            'b': 1706017034923,
            'c': 1706017034924,
            'd': 0,
            'e': 0,
            'f': 1706017034376,
            'g': 1706017034376,
            'h': 1706017034376,
            'i': 1706017034376,
            'j': 1706017034376,
            'k': 0,
            'l': 1706017034521,
            'm': 1706017034902,
            'n': 1706017034906,
            'o': 1706017034929,
            'p': 1706017035275,
            'q': 1706017035275,
            'r': 1706017035286,
            's': 1706017035300,
            't': 1706017035300,
            'u': 1706017035300,
        },
        'td': -1,
    };
};

// AES加密
var encrypt1 = function(e, t, n) {
    // AES加密
    l = {
        key: CryptoJS.enc.Utf8.parse(t),
        iv: CryptoJS.enc.Utf8.parse('0000000000000000'),
    };
    var r = CryptoJS.AES.encrypt(e, l.key, {
        iv: l.iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7,
    });
    var o = r['ciphertext']['words'];
    var i = r['ciphertext']['sigBytes'];
    var s = [];
    for (a = 0; a < i; a++) {
        var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s['push'](_);
    }
    return s;
};
var $_HAn = function(e, t) {
    return e >> t & 1;
};
var $_GIQ = function(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
};
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
        'end': r,
    };
};
// 对AES加密后返回的数组进行处理为字符串
var $_HDZ = function(e) {
    var t = $_HBR(e);
    return t['res'] + t['end'];
};

var $_CCBN = function(gt, challenge, cc, ss, t, e, n) {
    var r = this
        , i = {
        '$_GIF': 1706013617487,
        'protocol': 'https://',
        'is_next': true,
        'type': 'multilink',
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'https': true,
        'offline': false,
        'product': 'embed',
        'api_server': 'https://api.geetest.com',
        'static_servers': [
            'static.geetest.com/',
            'static.geevisit.com/',
        ],
        'isPC': true,
        'autoReset': true,
        'width': '100%',
        '$_DHX': {
            '$_BCN': 0,
        },
        'id': 'a72e3d4a1ed2b8c44fe50d2e9feffa598',
        'bg': 'pictures/gt/d401d55fc/bg/8690f32fa.jpg',
        'fullbg': 'pictures/gt/d401d55fc/d401d55fc.jpg',
        'link': '',
        'ypos': 66,
        'xpos': 0,
        'height': 160,
        'slice': 'pictures/gt/d401d55fc/slice/8690f32fa.png',
        'mobile': true,
        'theme': 'ant',
        'theme_version': '1.2.6',
        'template': '',
        'logo': true,
        'clean': false,
        'fullpage': false,
        'feedback': 'https://www.geetest.com/contact#report',
        'show_delay': 250,
        'hide_delay': 800,
        'benchmark': false,
        'version': '6.0.9',
        'show_voice': true,
        'c': cc,
        's': ss,
        'so': 0,
        'i18n_labels': {
            'cancel': '取消',
            'close': '关闭验证',
            'error': '请重试',
            'fail': '请正确拼合图像',
            'feedback': '帮助反馈',
            'forbidden': '怪物吃了拼图，请重试',
            'loading': '加载中...',
            'logo': '由极验提供技术支持',
            'read_reversed': false,
            'refresh': '刷新验证',
            'slide': '拖动滑块完成拼图',
            'success': 'sec 秒的速度超过 score% 的用户',
            'tip': '请完成下方验证',
            'voice': '视觉障碍',
        },
        'gct_path': '/static/js/gct.b71a9027509bc6bcfef9fc6a196424f5.js',
    }
        , o = {
        'lang': 'zh-cn',
        'userresponse': H(t, i['challenge']),
        'passtime': n,
        'imgload': 33,
        'aa': e,
        'ep': $_CCCY(),
    };
    o['rp'] = md5(i['gt'] + i['challenge']['slice'](0, 32) + o['passtime']);
    var u = $_CCDm()
        , l = encrypt1(JSON['stringify'](o), $_CCIm())
        , h = $_HDZ(l)
        , f = {
        'gt': i['gt'],
        'challenge': i['challenge'],
        'lang': 'zh-cn',
        '$_BCN': 0,
        'client_type': 'web',
        'w': h + u,
    };
    return f;
};


function three_w(gui_ji, gt, challenge, juli, shijian, c, s) {
    guiji = gui_ji;
    var l = $_BBED($_FD_(), c, s);
    return $_CCBN(gt, challenge, c, s, juli, l, shijian);
}

var guiji = [
    [
        -43,
        -28,
        0,
    ],
    [
        0,
        0,
        0,
    ],
    [
        0,
        0,
        43,
    ],
    [
        4,
        0,
        53,
    ],
    [
        18,
        0,
        61,
    ],
    [
        35,
        0,
        69,
    ],
    [
        61,
        0,
        77,
    ],
    [
        92,
        3,
        85,
    ],
    [
        135,
        4,
        89,
    ],
    [
        183,
        4,
        97,
    ],
    [
        229,
        4,
        105,
    ],
    [
        229,
        4,
        106,
    ],
];
// console.log()
var c = [12, 58, 98, 36, 43, 95, 62, 15, 12];
var s = '37662a43';
// var l = $_BBED($_FD_(), c, s);
var juli = 228;  // 横向拖拽的距离
var shijian = 106;  // 拖拽时间
var gt = '019924a82c70bb123aae90d483087f94';
var challenge = '72e3d4a1ed2b8c44fe50d2e9feffa598h6';
// console.log($_CCBN(gt, challenge, c, s, juli, l, shijian))
// console.log($_CCDm())
console.log(three_w(guiji, gt, challenge, juli, shijian, c, s));