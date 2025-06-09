let crypto = require('crypto');
const {RSAKey} = require('node-jsencrypt');
const CryptoJS = require('crypto-js');
var H = function(t, e) {
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
};


var $_CCCY = function() {
    return {
        'v': '7.9.2',
        '$_BIE': false,
        'me': true,
        'tm': {
            'a': 1714045553784,
            'b': 1714045554055,
            'c': 1714045554055,
            'd': 0,
            'e': 0,
            'f': 1714045553797,
            'g': 1714045553797,
            'h': 1714045553797,
            'i': 1714045553797,
            'j': 1714045553797,
            'k': 0,
            'l': 1714045553862,
            'm': 1714045554046,
            'n': 1714045554049,
            'o': 1714045554061,
            'p': 1714045554368,
            'q': 1714045554368,
            'r': 1714045554374,
            's': 1714045554468,
            't': 1714045554468,
            'u': 1714045554474,
        },
        'td': -1,
    };
};

function X(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

function U() {
    var rsa = new RSAKey();
    rsa['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    return rsa;
}

var rt = function() {
    function e() {
        return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
    }

    return function() {
        return e() + e() + e() + e();
    };
}();

var $_CCEc = (Ot = rt(),
        function(t) {
            return !0 === t && (Ot = rt()),
                Ot;
        }
);

var $_CCDm = function(t) {
    var e = new U()['encrypt']($_CCEc(t));
    while (!e || 256 !== e['length'])
        e = new U()['encrypt']($_CCEc(!0));
    return e;
};

var parse = function(t) {
    for (var e = t['length'], n = [], r = 0; r < e; r++)
        n[r >>> 2] |= (255 & t['charCodeAt'](r)) << 24 - r % 4 * 8;
    return new u[('init')](n, e);
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

var $_FEX = function(e) {
    var t = $_HCR(e);
    return t['res'] + t['end'];
};


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


var cul_l = function(guiji, cc, ss) {
    var l = $_BBED($_FD_(guiji), cc, ss);
    return l;
};


// t: 距离
// e: 轨迹加密后的数据
// n: 时间
var $_CCBN = function(gt, challenge, t, e, n, c, s) {
    var i = {
        'gt': gt,
        'challenge': challenge,
        'c': c,
        's': s,
    }
        , o = {
        'lang': 'zh-cn',
        'userresponse': H(t, i['challenge']),
        'passtime': n,
        'imgload': 72,
        'aa': e,
        'ep': $_CCCY(),
    };

    o['h9s9'] = '1816378497';

    o['rp'] = X(i['gt'] + i['challenge']['slice'](0, 32) + o['passtime']);

    var u = $_CCDm()
        , l = encrypt1(JSON['stringify'](o), $_CCEc())
        , h = $_FEX(l)
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

var third_w = function(gt, challenge, juli, guiji, shijian, c, s) {
    var l = cul_l(guiji, c, s);  // 轨迹加密后的数据
    return $_CCBN(gt, challenge, juli, l, shijian);
};

var guiji = [
    [
        -45,
        -39,
        0,
    ],
    [
        0,
        0,
        0,
    ],
    [
        1,
        0,
        118,
    ],
    [
        2,
        0,
        123,
    ],
    [
        3,
        0,
        130,
    ],
    [
        4,
        0,
        135,
    ],
    [
        5,
        0,
        138,
    ],
    [
        6,
        0,
        140,
    ],
    [
        6,
        0,
        142,
    ],
    [
        7,
        0,
        145,
    ],
    [
        8,
        0,
        147,
    ],
    [
        9,
        0,
        151,
    ],
    [
        10,
        0,
        153,
    ],
    [
        10,
        0,
        154,
    ],
    [
        11,
        0,
        157,
    ],
    [
        12,
        0,
        159,
    ],
    [
        13,
        0,
        161,
    ],
    [
        14,
        0,
        163,
    ],
    [
        15,
        0,
        165,
    ],
    [
        16,
        0,
        168,
    ],
    [
        17,
        0,
        170,
    ],
    [
        18,
        0,
        171,
    ],
    [
        18,
        0,
        173,
    ],
    [
        19,
        0,
        176,
    ],
    [
        20,
        0,
        178,
    ],
    [
        21,
        0,
        181,
    ],
    [
        22,
        0,
        183,
    ],
    [
        22,
        0,
        187,
    ],
    [
        23,
        0,
        190,
    ],
    [
        24,
        0,
        191,
    ],
    [
        25,
        0,
        195,
    ],
    [
        26,
        0,
        197,
    ],
    [
        26,
        0,
        199,
    ],
    [
        28,
        0,
        202,
    ],
    [
        29,
        0,
        205,
    ],
    [
        30,
        0,
        209,
    ],
    [
        30,
        0,
        216,
    ],
    [
        30,
        1,
        220,
    ],
    [
        31,
        1,
        221,
    ],
    [
        31,
        1,
        372,
    ],
];
var juli = 31;
var shijian = 372;
var gt = '019924a82c70bb123aae90d483087f94';
var challenge = '6636e2faac8f2e61a4d586f627f195577u';
var c = [
    12,
    58,
    98,
    36,
    43,
    95,
    62,
    15,
    12,
];
var s = '6b732c71';
console.log(third_w(gt, challenge, juli, guiji, shijian, c, s));