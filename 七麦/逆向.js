window = global;

function o(n) {
    return String['fromCharCode'](n);
}

function cv(t) {
    t = window['encodeURIComponent'](t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
        return o('0x' + t);
    });
    try {
        return btoa(t);
    } catch (n) {
        x = this;
        return x['Buffer']['from'](t)['toString']('base64');
    }
}

function oZ(n, t) {
    // t = t || u();
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n['join']('');
}

var fn = function(t) {
    t['baseURL'] = new URL(t.url).origin;

    var e, r = +new Date - (0) - 1661224081041, a = [];

    void 0 === t['params'] && (t['params'] = {}),
        Object['keys'](t['params'])['forEach'](function(n) {
            if (n == 'analysis')
                return false;
            t['params']['hasOwnProperty'](n) && a['push'](t['params'][n]);
        });
    a = a['sort']()['join']('');
    a = cv(a);
    a = (a += '@#' + t['url']['replace'](t['baseURL'], '')) + ('@#' + r) + ('@#' + 3);
    e = cv(oZ(a, 'xyz517cda96efgh'));
    -1 == t['url']['indexOf']('analysis') && (t['url'] += (-1 != t['url']['indexOf']('?') ? '&' : '?') + 'analysis' + '=' + window['encodeURIComponent'](e));
    return t.url;
};

console.log(fn({
    'url': 'https://api.qimai.cn/rank/index',
    'params': {
        'brand': 'free',
        'device': 'iphone',
        'country': 'cn',
        'genre': '36',
        'date': '2024-04-15',
        'page': 2,
        'is_rank_index': 1,
        'snapshot': '15:40:04',
    },
}));