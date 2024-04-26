// node标准库
let crypto = require('crypto');
const CryptoJS = require('crypto-js');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

var t = ['bbOy'];

function $_DJB(e) {
    this['$_BAEt'] = e || [];
}

$_DJB.prototype = {
    '$_EHp': function(e) {

        var t = this['$_BAEt'];
        if (t['indexOf'])
            return t['indexOf'](e);
        for (var n = 0, r = t['length']; n < r; n += 1)
            if (t[n] === e)
                return n;
        return -1;
    },

    '$_EBl': function(e) {
        var t = this['$_BAEt'];
        if (t['map'])
            return new $_DJB(t['map'](e));
        for (var n = [], r = 0, o = t['length']; r < o; r += 1)
            n[r] = e(t[r], r, this);
        return new $_DJB(n);
    },
};

function $_BHJM(e) {

    var t = ''
        , n = 0;
    (e || [])['length'];
    while (!t && e[n])
        t = e[n] && e[n][4],
            n++;
    if (!t)
        return e;
    for (var r = '', o = ['mouse', 'touch', 'pointer', 'MSPointer'], i = 0, s = o['length']; i < s; i++)
        0 === t['indexOf'](o[i]) && (r = o[i]);
    for (var a = e['slice'](), _ = a['length'] - 1; 0 <= _; _--) {
        var c = a[_]
            , l = c[0];
        if (-1 < new $_DJB(['move', 'down', 'up'])['$_EHp'](l))
            0 !== (c[4] || '')['indexOf'](r) && a['splice'](_, 1);
    }
    return a;
}

function $_BHHa(e) {

    var t = 32767;
    return 'number' != typeof e ? e : (t < e ? e = t : e < -t && (e = -t),
        Math['round'](e));
}

function $_BHIj(e) {
    var t = 0
        , n = 0
        , r = []
        , o = this
        , i = 0;
    if (e['length'] <= 0)
        return [];
    for (var s = null, a = null, _ = $_BHJM(e), c = _['length'], l = c < 300 ? 0 : c - 300; l < c; l += 1) {
        var u = _[l]
            , p = u[0];
        -1 < new $_DJB(['down', 'move', 'up', 'scroll'])['$_EHp'](p) ? (s || (s = u),
            a = u,
            r['push']([p, [u[1] - t, u[2] - n], $_BHHa(i ? u[3] - i : i)]),
            t = u[1],
            n = u[2],
            i = u[3]) : -1 < new $_DJB(['blur', 'focus', 'unload'])['$_EHp'](p) && (r['push']([p, $_BHHa(i ? u[1] - i : i)]),
            i = u[1]);
    }
    return o['$_BGBt'] = s,
        o['$_BGCZ'] = a,
        r;
}


function $_HD_(e) {
    var p = {
        '\u006d\u006f\u0076\u0065': 0,
        '\u0064\u006f\u0077\u006e': 1,
        '\u0075\u0070': 2,
        '\u0073\u0063\u0072\u006f\u006c\u006c': 3,
        '\u0066\u006f\u0063\u0075\u0073': 4,
        '\u0062\u006c\u0075\u0072': 5,
        '\u0075\u006e\u006c\u006f\u0061\u0064': 6,
        '\u0075\u006e\u006b\u006e\u006f\u0077\u006e': 7,
    };

    function h(e, t) {
        for (var n = e['toString'](2), r = '', o = n['length'] + 1; o <= t; o += 1)
            r += '0';
        return n = r + n;

    }

    function f(e) {
        var t = []
            , n = e['length']
            , r = 0;
        while (r < n) {
            var o = e[r]
                , i = 0;
            while (1) {
                if (16 <= i)
                    break;
                var s = r + i + 1;
                if (n <= s)
                    break;
                if (e[s] !== o)
                    break;
                i += 1;
            }
            r = r + 1 + i;
            var a = p[o];
            0 != i ? (t['push'](8 | a),
                t['push'](i - 1)) : t['push'](a);
        }
        for (var _ = h(32768 | n, 16), c = '', l = 0, u = t['length']; l < u; l += 1)
            c += h(t[l], 4);
        return _ + c;

    }

    function c(e, t) {
        for (var n = [], r = 0, o = e['length']; r < o; r += 1)
            n['push'](t(e[r]));
        return n;

    }

    function d(e, t) {

        e = function _(e) {

            var t = 32767
                , n = (e = c(e, function(e) {
                return t < e ? t : e < -t ? -t : e;
            }))['length']
                , r = 0
                , o = [];
            while (r < n) {
                var i = 1
                    , s = e[r]
                    , a = Math['abs'](s);
                while (1) {
                    if (n <= r + i)
                        break;
                    if (e[r + i] !== s)
                        break;
                    if (127 <= a || 127 <= i)
                        break;
                    i += 1;
                }
                1 < i ? o['push']((s < 0 ? 49152 : 32768) | i << 7 | a) : o['push'](s),
                    r += i;
            }
            return o;
        }(e);
        var n, r = [], o = [];
        c(e, function(e) {

            var t = Math['ceil'](function n(e, t) {

                return 0 === e ? 0 : Math['log'](e) / Math['log'](t);
            }(Math['abs'](e) + 1, 16));
            0 === t && (t = 1),
                r['push'](h(t - 1, 2)),
                o['push'](h(Math['abs'](e), 4 * t));
        });
        var i = r['join']('')
            , s = o['join']('');
        return n = t ? c(function a(e, t) {

            var n = [];
            return c(e, function(e) {

                t(e) && n['push'](e);
            }),
                n;
        }(e, function(e) {

            return 0 != e && e >> 15 != 1;
        }), function(e) {

            return e < 0 ? '1' : '0';
        })['join']('') : '',
        h(32768 | e['length'], 16) + i + s + n;

    }

    return function(e) {

        for (var t = [], n = [], r = [], o = [], i = 0, s = e['length']; i < s; i += 1) {
            var a = e[i]
                , _ = a['length'];
            t['push'](a[0]),
                n['push'](2 === _ ? a[1] : a[2]),
            3 === _ && (r['push'](a[1][0]),
                o['push'](a[1][1]));
        }
        var c = f(t) + d(n, !1) + d(r, !0) + d(o, !0)
            , l = c['length'];
        return l % 6 != 0 && (c += h(0, 6 - l % 6)),
            function u(e) {

                for (var t = '', n = e['length'] / 6, r = 0; r < n; r += 1)
                    t += '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz~'['charAt'](parseInt(e['slice'](6 * r, 6 * (r + 1)), 2));
                return t;
            }(c);
    }(e);
}

function first() {
    var e = [
        [
            'move',
            575,
            5,
            1713604921028,
            'pointermove',
        ],
        [
            'move',
            575,
            4,
            1713604921029,
            'mousemove',
        ],
        [
            'move',
            598,
            13,
            1713604921037,
            'pointermove',
        ],
        [
            'move',
            613,
            24,
            1713604921043,
            'pointermove',
        ],
        [
            'move',
            627,
            35,
            1713604921050,
            'pointermove',
        ],
        [
            'move',
            638,
            45,
            1713604921058,
            'pointermove',
        ],
        [
            'move',
            648,
            54,
            1713604921066,
            'pointermove',
        ],
        [
            'move',
            661,
            67,
            1713604921074,
            'pointermove',
        ],
        [
            'move',
            670,
            77,
            1713604921084,
            'pointermove',
        ],
        [
            'move',
            680,
            88,
            1713604921092,
            'pointermove',
        ],
        [
            'move',
            688,
            99,
            1713604921098,
            'pointermove',
        ],
        [
            'move',
            696,
            110,
            1713604921106,
            'pointermove',
        ],
        [
            'move',
            702,
            121,
            1713604921114,
            'pointermove',
        ],
        [
            'move',
            706,
            129,
            1713604921122,
            'pointermove',
        ],
        [
            'move',
            711,
            141,
            1713604921130,
            'pointermove',
        ],
        [
            'move',
            714,
            151,
            1713604921138,
            'pointermove',
        ],
        [
            'move',
            717,
            160,
            1713604921146,
            'pointermove',
        ],
        [
            'move',
            720,
            168,
            1713604921154,
            'pointermove',
        ],
        [
            'move',
            721,
            177,
            1713604921162,
            'pointermove',
        ],
        [
            'move',
            724,
            183,
            1713604921171,
            'pointermove',
        ],
        [
            'move',
            726,
            190,
            1713604921178,
            'pointermove',
        ],
        [
            'move',
            729,
            193,
            1713604921186,
            'pointermove',
        ],
        [
            'move',
            728,
            193,
            1713604921187,
            'mousemove',
        ],
        [
            'move',
            729,
            195,
            1713604921194,
            'pointermove',
        ],
        [
            'move',
            730,
            200,
            1713604921202,
            'pointermove',
        ],
        [
            'move',
            729,
            199,
            1713604921203,
            'mousemove',
        ],
        [
            'move',
            731,
            202,
            1713604921210,
            'pointermove',
        ],
        [
            'move',
            731,
            204,
            1713604921218,
            'pointermove',
        ],
        [
            'move',
            732,
            205,
            1713604921226,
            'pointermove',
        ],
        [
            'move',
            732,
            205,
            1713604921234,
            'pointermove',
        ],
        [
            'move',
            732,
            206,
            1713604921242,
            'pointermove',
        ],
        [
            'move',
            732,
            209,
            1713604921250,
            'pointermove',
        ],
        [
            'move',
            732,
            211,
            1713604921258,
            'pointermove',
        ],
        [
            'move',
            732,
            213,
            1713604921266,
            'pointermove',
        ],
        [
            'move',
            732,
            217,
            1713604921276,
            'pointermove',
        ],
        [
            'move',
            732,
            220,
            1713604921282,
            'pointermove',
        ],
        [
            'move',
            732,
            225,
            1713604921293,
            'pointermove',
        ],
        [
            'move',
            732,
            229,
            1713604921299,
            'pointermove',
        ],
        [
            'move',
            732,
            233,
            1713604921310,
            'pointermove',
        ],
        [
            'move',
            732,
            239,
            1713604921314,
            'pointermove',
        ],
        [
            'move',
            732,
            244,
            1713604921323,
            'pointermove',
        ],
        [
            'move',
            732,
            243,
            1713604921324,
            'mousemove',
        ],
        [
            'move',
            730,
            250,
            1713604921331,
            'pointermove',
        ],
        [
            'move',
            730,
            257,
            1713604921340,
            'pointermove',
        ],
        [
            'move',
            727,
            265,
            1713604921347,
            'pointermove',
        ],
        [
            'move',
            727,
            273,
            1713604921355,
            'pointermove',
        ],
        [
            'move',
            726,
            283,
            1713604921363,
            'pointermove',
        ],
        [
            'move',
            726,
            288,
            1713604921373,
            'pointermove',
        ],
        [
            'move',
            726,
            294,
            1713604921379,
            'pointermove',
        ],
        [
            'move',
            726,
            297,
            1713604921387,
            'pointermove',
        ],
        [
            'move',
            726,
            301,
            1713604921394,
            'pointermove',
        ],
        [
            'move',
            726,
            304,
            1713604921403,
            'pointermove',
        ],
        [
            'move',
            726,
            307,
            1713604921410,
            'pointermove',
        ],
        [
            'move',
            726,
            309,
            1713604921450,
            'pointermove',
        ],
        [
            'down',
            726,
            309,
            1713604923932,
            'pointerdown',
        ],
        [
            'focus',
            1713604923939,
        ],
        [
            'up',
            726,
            309,
            1713604924010,
            'pointerup',
        ],
    ];  // 轨迹
    return $_HD_($_BHIj(e));
}


function second() {
    return $_HD_([]);
}

function $_BIHS(e) {
    return void 0 === e;
}

function third(e, t) {

    var n = this
        , r = {}  // 第一次请求的指纹
        , o = [];
    arr = [
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
    return new $_DJB(arr)['$_EBl'](function(e) {

        var t = r[e];
        o['push']($_BIHS(t) ? -1 : t);
    }),
        o['join']('magic data');
}

function fourth() {
    return 'SPAN_0';
}

function $_GHM(e) {
    for (var t = [], n = 0, r = e['length']; n < r; n += 1)
        t['push'](e['charCodeAt'](n));
    return t;
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


function p(e) {
    var t = $_HCK($_GHM(e));
    return t['res'] + t['end'];
}


function cul_i(gt, challenge, ss, finger_print) {
    var now = +new Date();
// console.log(now);
    var $_CEDy = {
        'v': '9.1.9-r8k4eq',
        'te': false,
        '$_BBp': true,
        'ven': 'Google Inc. (Intel)',
        'ren': 'ANGLE (Intel, Intel(R) UHD Graphics 620 (0x00005917) Direct3D11 vs_5_0 ps_5_0, D3D11)',
        'fp': [
            'move',
            678,
            319,
            now,
            'pointermove',
        ],
        'lp': [
            'up',
            794,
            302,
            now + 889,
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
        'dnf': 'dnf',
        'by': 0,
    };


    var i = this
        , e = first()
        , t = second()
        , n = third()
        , r = fourth()
        , o = {
        'gt': gt,
        'challenge': challenge,
        'c': [
            12,
            58,
            98,
            36,
            43,
            95,
            62,
            15,
            12,
        ],
        's': ss,
    }
        , s = 20764;
    var result = '';
    for (var a = [['lang', 'zh-cn'], ['type', 'fullpage'], ['tt', function(e, t, n) {

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
        // 这里是指纹, 第一次w的指纹
    }(e, o['c'], o['s']) || -1], ['light', r || -1], ['s', do_md5(p(t))], ['h', do_md5(p(n))], ['hh', do_md5(n)], ['hi', do_md5(finger_print)], ['vip_order', undefined || -1], ['ct', undefined || -1], ['ep', $_CEDy || -1], ['passtime', s || -1], ['rp', do_md5(o['gt'] + o['challenge'] + s)]], _ = 0; _ < a['length']; _++)
        result += '"' + a[_][0] + '":' + JSON['stringify'](a[_][1]) + ',';
    return result;
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


function $_HEt(e) {
    var t = $_HCK(e);
    return t['res'] + t['end'];
}

function cul_second_w(aeskey, gt, challenge, ss, finger_print) {
    var one_code = 'function o(e,t){var $_CFHIS=yCtOu.$_CT,$_CFHHv=[\'$_CFIBZ\'].concat($_CFHIS),$_CFHJL=$_CFHHv[1];$_CFHHv.shift();var $_CFIAt=$_CFHHv[0];function n(e){var $_DDHGx=yCtOu.$_Dm()[6][14];for(;$_DDHGx!==yCtOu.$_Dm()[12][11];){switch($_DDHGx){case yCtOu.$_Dm()[4][14]:var t=5381,n=e[$_CFHJL(41)],r=0;$_DDHGx=yCtOu.$_Dm()[0][13];break;case yCtOu.$_Dm()[6][13]:while(n--)t=(t<<5)+t+e[$_CFHJL(51)](r++);$_DDHGx=yCtOu.$_Dm()[8][12];break;case yCtOu.$_Dm()[0][12]:return t&=~(1<<31);break;}}}100<new Date()[$_CFHJL(228)]()-t[$_CFHIS(228)]()&&(e=$_CFHIS(1192)),r=$_CFHIS(781)+i[$_CFHIS(1121)]+$_CFHJL(1194)+n(o[$_CFHJL(45)]()+n(n[$_CFHJL(45)]())+n(e[$_CFHJL(45)]()))+$_CFHJL(1117);}';
    var second_code = 'function n(e){var $_DDHGx=yCtOu.$_Dm()[6][14];for(;$_DDHGx!==yCtOu.$_Dm()[12][11];){switch($_DDHGx){case yCtOu.$_Dm()[4][14]:var t=5381,n=e[$_CFHJL(41)],r=0;$_DDHGx=yCtOu.$_Dm()[0][13];break;case yCtOu.$_Dm()[6][13]:while(n--)t=(t<<5)+t+e[$_CFHJL(51)](r++);$_DDHGx=yCtOu.$_Dm()[8][12];break;case yCtOu.$_Dm()[0][12]:return t&=~(1<<31);break;}}}';
    var third_code = 'bbOy';
    // t = []
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

        // 100 < new Date()['getTime']() - t['getTime']() && (e = 'qwe');
        s = n(one_code + n(second_code) + n(third_code));

        r = '{' + cul_i(gt, challenge, ss, finger_print) + '"captcha_token":"' + n(one_code + n(second_code) + n(third_code)) + '","otpj":"jm4jwcx7"}';

    }(t['shift'](), new Date());

    return $_HEt(encrypt1(r, aeskey));
}

var aeskey = '2e8cc3d0418cb37a';
var gt = '019924a82c70bb123aae90d483087f94';
var challenge = 'e49e0ff763ade65c04f76a10ac8f564c';
var ss= '5472592a';
finger_print = '-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1'

console.log(cul_second_w(aeskey, gt, challenge, ss, finger_print));