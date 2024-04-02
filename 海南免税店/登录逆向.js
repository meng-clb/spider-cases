// node标准库
let crypto = require('crypto');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

// 第一次登录请求
function randomStr(e) {
    for (var t = 'abcdfsdferwrjhtjfdgofdgfdgrew1234569798ere', n = '', o = t.length, i = 0; i < e; i++)
        n += t.charAt(Math.floor(Math.random() * o));
    return n;
}


var data = {};
var e = 'hltmsp5615466';
var o = '';

var ident;
;
var nonce_str = randomStr(Math.floor(26 * Math.random()) + 6);

var t = 2022051288 + Math.floor(Date.now() / 1e3) + ''
    , n = Math.floor(9 * Math.random()) + 1;
t = '' + n + t.substring(t.length - n, t.length) + t.substring(0, t.length - n);
var time_stamp = t;

// 加密处理函数
function manage(data) {
    Object.keys(data).sort().map((function(e) {
            null === data[e] || void 0 === data[e] || '' === data[e] || Array.isArray(data[e]) || (o += ''.concat(e, '=').concat(data[e], '&'));
        }
    )),
        o += 'app_key='.concat(e);
    data.sign = do_md5(o).toUpperCase();
}

function one() {
    ident = (new Date).getTime();
    data = {
        'mobile': '账号',
        'password': '密码',
        'platformId': '1',
        'shop_id': 6,
        'token': null,
        'ident': ident,
        'appid': 'duty_h5',
        'nonce_str': nonce_str,
        'time_stamp': time_stamp,
    };
    manage(data);
    return data;
}

function two() {
    ident = (new Date).getTime();
    data = {
        'platformId': '1',
        'shop_id': 6,
        't': ident,
        'ident': ident,
        'appid': 'duty_h5',
        'nonce_str': nonce_str,
        'time_stamp': time_stamp,
    };
    manage(data);
    return data;
}

function three(ident, position) {
    data = {
        'position': position,
        'ident': ident,
        'platformId': 1,
        'shop_id': 6,
        't': (new Date().getTime()),
        'appid': 'duty_h5',
        'nonce_str': nonce_str,
        'time_stamp': time_stamp,
    };
    manage(data);
    return data;
}

function four(ident) {
    data = {
        'mobile': '账号',
        'password': '密码',
        'platformId': '1',
        'shop_id': 6,
        'token': null,
        'ident': ident,
        'appid': 'duty_h5',
        'nonce_str': nonce_str,
        'time_stamp': time_stamp,
    };
    manage(data);
    return data;
}


