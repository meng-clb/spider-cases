var {RSAKey} = require('node-jsencrypt')
var CryptoJS = require('crypto-js')
// node标准库
let crypto = require('crypto');
function V(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}
var $_GGc = function(e) {
    for (var t = [], n = 0, r = e['length']; n < r; n += 1)
        t['push'](e['charCodeAt'](n));
    return t;
}
var $_HAn = function(e, t) {
    return e >> t & 1;
}
var $_GIQ = function(e) {
    var t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()';
    return e < 0 || e >= t['length'] ? '.' : t['charAt'](e);
}
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
        'end': r
    };
}
var $_HCm = function(e) {
    var t = $_HBR($_GGc(e));
    return t['res'] + t['end'];
}


var $_CEHi = function() {
    var e = {
        'v': '9.1.8-bfget5'
    };
    this['$_EHw'];
    e['$_E_'] = false,
    e['me'] = true;
    var t =  {
            "puppet": false,
            "phantom": false,
            "nightmare": false,
            "selenium": false,
            "vendor": "Google Inc. (0x05404C42)",
            "renderer": "ANGLE (0x05404C42, Parallels Display Adapter (WDDM) (0x00000000) Direct3D11 vs_5_0 ps_5_0, D3D11)"
        }
    return e['ven'] = t['vendor'] || -1,
    e['ren'] = t['renderer'] || -1,
    e['fp'] = [
    "move",
    390,
    908,
    1705671036944,
    "pointermove"
],
    e['lp'] = [
        "up",
        826,
        303,
        1705671037779,
        "pointerup"
    ],
    e['em'] = {
    "ph": 0,
    "cp": 0,
    "ek": "11",
    "wd": 1,
    "nt": 0,
    "si": 0,
    "sc": 0
},
    e['tm'] = {
    "a": 1705671028826,
    "b": 1705671029186,
    "c": 1705671029187,
    "d": 0,
    "e": 0,
    "f": 1705671028834,
    "g": 1705671028834,
    "h": 1705671028834,
    "i": 1705671028834,
    "j": 1705671028834,
    "k": 0,
    "l": 1705671029089,
    "m": 1705671029179,
    "n": 1705671029181,
    "o": 1705671029190,
    "p": 1705671029457,
    "q": 1705671029458,
    "r": 1705671029462,
    "s": 1705671029464,
    "t": 1705671029464,
    "u": 1705671029464
},  // 当前这里的时间没有处理 不确定是否有问题
    e['dnf'] = 'dnf',
    e['by'] = 0,
    e;
}


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
    'aeskey': undefined
}
var $_CCIm = function(e) {
    return config['aeskey'] && !e || (config['aeskey'] = ee()),
    config['aeskey'];
}
var G = function() {
        var rsa = new RSAKey();
        rsa.setPublic('00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81', '10001');
        return rsa
}
var $_CCHk = function(e) {
    var t = new G()['encrypt']($_CCIm(e));
    while (!t || 256 !== t['length'])
        t = new G()['encrypt']($_CCIm(!0));
    return t;
}

var encrypt1 = function(e, t, n) {
    // AES加密
      l = {
        key: CryptoJS.enc.Utf8.parse(t),
        iv: CryptoJS.enc.Utf8.parse('0000000000000000'),
      }
      var r = CryptoJS.AES.encrypt(e, l.key, {
          iv: l.iv,
          mode: CryptoJS.mode.CBC,
          padding: CryptoJS.pad.Pkcs7
        })
    var o = r['ciphertext']['words']
    var i = r['ciphertext']['sigBytes']
    var s = []
    for (a = 0; a < i; a++) {
        var _ = o[a >>> 2] >>> 24 - a % 4 * 8 & 255;
        s['push'](_);
    }
    return s;
}


var $_HDZ = function(e) {
    var t = $_HBR(e);
    return t['res'] + t['end'];
}
var second_w = function(gt, challenge, c, ss, aeskey) {
    config.aeskey = aeskey
    var i = {'$_CCGk':'-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1', '$_EHw':{
            "$_CAAC": 1705668463332,
            "protocol": "https://",
            "gt": gt,
            "challenge": challenge,
            "offline": false,
            "new_captcha": true,
            "product": "float",
            "width": "300px",
            "https": true,
            "api_server": "api.geetest.com",
            "type": "fullpage",
            "static_servers": [
                "static.geetest.com",
                "static.geevisit.com"
            ],
            "voice": "/static/js/voice.1.2.4.js",
            "click": "/static/js/click.3.1.0.js",
            "beeline": "/static/js/beeline.1.0.1.js",
            "fullpage": "/static/js/fullpage.9.1.8-bfget5.js",
            "slide": "/static/js/slide.7.9.2.js",
            "geetest": "/static/js/geetest.6.0.9.js",
            "aspect_radio": {
                "slide": 103,
                "click": 128,
                "voice": 128,
                "beeline": 50
            },
            "cc": 6,
            "supportWorker": true,
            "$_FEl": {
                "pt": 0
            },
            "aeskey": config.aeskey,
            "theme": "wind",
            "theme_version": "1.5.8",
            "logo": true,
            "feedback": "https://www.geetest.com/contact#report",
            "c": c,
            "s": ss,
            "i18n_labels": {
                "copyright": "由极验提供技术支持",
                "error": "网络不给力",
                "error_content": "请点击此处重试",
                "error_title": "网络超时",
                "fullpage": "智能检测中",
                "goto_cancel": "取消",
                "goto_confirm": "前往",
                "goto_homepage": "是否前往验证服务Geetest官网",
                "loading_content": "智能验证检测中",
                "next": "正在加载验证",
                "next_ready": "请完成验证",
                "read_reversed": false,
                "ready": "点击按钮进行验证",
                "refresh_page": "页面出现错误啦！要继续操作，请刷新此页面",
                "reset": "请点击重试",
                "success": "验证成功",
                "success_title": "通过验证"
            }
        }}
      , e = 'M(*((1((M(('
      , t = 'M(*((1((M(('
      , n = '-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1magic data-1'
      , r = 'DIV_0'
      , o = i['$_EHw']
      , s = 509019;
    i["$_CEGM"] = '';
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
    }(e, o['c'], o['s']) || -1], ['light', r || -1], ['s', V($_HCm(t))], ['h', V($_HCm(n))], ['hh', V(n)], ['hi', V(i['$_CCGk'])], ['vip_order', i['vip_order'] || -1], ['ct', i['ct'] || -1], ['ep', $_CEHi() || -1], ['passtime', s || -1], ['rp', V(o['gt'] + o['challenge'] + s)]], _ = 0; _ < a['length']; _++)
        i['$_CEGM'] += '"' + a[_][0] + '":' + JSON['stringify'](a[_][1]) + ',';
    // process.exit()

    // var c = $_BEH();
    i['$_CEIV'] = function l() {
        var t = ['bbOy'];
        return function(e) {
            t['push'](e['toString']());
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
                100 < new Date()['getTime']() - t['getTime']() && (e = 'qwe'),
                r = '{' + i['$_CEGM'] + '"captcha_token":"' + n("function o(e,t){var $_CFICg=tLnKP.$_Ci,$_CFIBQ=['$_CFIFx'].concat($_CFICg),$_CFIDE=$_CFIBQ[1];$_CFIBQ.shift();var $_CFIEy=$_CFIBQ[0];function n(e){var $_DECAh=tLnKP.$_DC()[12][34];for(;$_DECAh!==tLnKP.$_DC()[20][31];){switch($_DECAh){case tLnKP.$_DC()[20][34]:var t=5381,n=e[$_CFICg(59)],r=0;$_DECAh=tLnKP.$_DC()[28][33];break;case tLnKP.$_DC()[20][33]:while(n--)t=(t<<5)+t+e[$_CFICg(80)](r++);$_DECAh=tLnKP.$_DC()[28][32];break;case tLnKP.$_DC()[8][32]:return t&=~(1<<31);break;}}}100<new Date()[$_CFIDE(223)]()-t[$_CFIDE(223)]()&&(e=$_CFICg(1173)),r=$_CFICg(722)+i[$_CFIDE(1136)]+$_CFIDE(1151)+n(o[$_CFICg(71)]()+n(n[$_CFICg(71)]())+n(e[$_CFICg(71)]()))+$_CFICg(1109);}" + n('function n(e){var $_DECAh=tLnKP.$_DC()[12][34];for(;$_DECAh!==tLnKP.$_DC()[20][31];){switch($_DECAh){case tLnKP.$_DC()[20][34]:var t=5381,n=e[$_CFICg(59)],r=0;$_DECAh=tLnKP.$_DC()[28][33];break;case tLnKP.$_DC()[20][33]:while(n--)t=(t<<5)+t+e[$_CFICg(80)](r++);$_DECAh=tLnKP.$_DC()[28][32];break;case tLnKP.$_DC()[8][32]:return t&=~(1<<31);break;}}}') + n('bbOy')) + '","gdyf":"kqy8o0w7"}';
            }(t['shift'](), new Date()),
            i['$_CEEg'] = $_HDZ(encrypt1(r, $_CCIm()));
        }
        ;
    }(),
    i['$_CEIV']('');
    return i
}

/*
var gt = "019924a82c70bb123aae90d483087f94"
var challenge = "981fe17f9095f9d5cc1aa2a9b1e53fe6"
var c = [
                12,
                58,
                98,
                36,
                43,
                95,
                62,
                15,
                12]
var s = "7a535473"
console.log($_CCIm())
console.log(second_w(gt, challenge, c, s)['$_CEEg'])*/
