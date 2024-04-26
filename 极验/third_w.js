// node标准库
let crypto = require('crypto');
const CryptoJS = require('crypto-js');
const {RSAKey} = require('node-jsencrypt');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}


function $_BBED(t, e, n) {

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
}

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

function $_FD_(guiji) {
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
}

function cul_l(guiji, c, s) {
    var r = $_FD_(guiji);
    l = $_BBED(r, c, s);
    return l;
}

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

function $_CCCY() {
    var now = +new Date();
    var ep = {
        'v': '7.9.2',
        '$_BIE': false,
        'me': true,
        'tm': {
            'a': now - 1363,
            'b': now - 1363 + 351,
            'c': now - 1363 + 351,
            'd': 0,
            'e': 0,
            'f': now - 1363 + 351 - 343,
            'g': now - 1363 + 351 - 343 + 50,
            'h': now - 1363 + 351 - 343 + 50,
            'i': now - 1363 + 351 - 343 + 50,
            'j': now - 1363 + 351 - 343 + 50 + 90,
            'k': now - 1363 + 351 - 343 + 50 + 90 - 40,
            'l': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30,
            'm': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200,
            'n': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15,
            'o': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10,
            'p': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10 + 350,
            'q': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10 + 350,
            'r': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10 + 350 + 5,
            's': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10 + 350 + 5 + 100,
            't': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10 + 350 + 5 + 100,
            'u': now - 1363 + 351 - 343 + 50 + 90 - 40 + 30 + 200 + 15 + 10 + 350 + 5 + 100 + 20,
        },
        'td': -1,
    };
    return ep;
}


function e() {
    return (65536 * (1 + Math['random']()) | 0)['toString'](16)['substring'](1);
}

function te() {
    return e() + e() + e() + e();
}

var quanju = {
    '$_EID': {
        'aeskey': undefined,
    },
};

function $_CCHU(e) {
    return quanju['$_EID']['aeskey'] && !e || (quanju['$_EID']['aeskey'] = te()),
        quanju['$_EID']['aeskey'];
}

function $_CCDm(e) {
    var rsa = new RSAKey();
    rsa['setPublic']('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
    var t = rsa['encrypt']($_CCHU(e));
    while (!t || 256 !== t['length'])
        t = rsa['encrypt']($_CCHU(!0));
    return t;
}

function encrypt1(e, t, n) {
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

function $_FEX(e) {
    var t = $_HCK(e);
    return t['res'] + t['end'];
}

// t > x_jvli: x轴滑动的距离
// e > guiji: 加密之后的轨迹
// n > shijian: 滑块所用的时间
function third_w(gt, challenge, c, ss, x_jvli, guiji, shijian) {

    var i = {
        'gt': gt,
        'challenge': challenge,
    };
    var o = {
        'lang': 'zh-cn',
        'userresponse': H(x_jvli, i['challenge']),
        'passtime': shijian,
        'imgload': 1649,
        'aa': cul_l(guiji, c, ss),
        'ep': $_CCCY(),
    };

    o['h9s9'] = '1816378497';


    o['rp'] = do_md5(i['gt'] + i['challenge']['slice'](0, 32) + o['passtime']);

    var u = $_CCDm()
        , l = encrypt1(JSON['stringify'](o), $_CCHU())
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
}

