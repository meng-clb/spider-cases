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
// console.log($_FD_(guiji));
var c = [12, 58, 98, 36, 43, 95, 62, 15, 12];
var s = '37356a73';
console.log(cul_l())
