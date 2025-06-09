// node标准库
let cryptoJS = require('crypto');
let CryptoJS = require('crypto-js');

function do_md5(e) {
    return cryptoJS.createHash('md5').update(e.toString()).digest('hex');
}

const askiZExYII01 = 'aPnyDR5Ca6FMIfdw';//AESkey，可自定义
const asideGdRY692 = 'bNpeyqJl34VlZ7ng';//密钥偏移量IV，可自定义

const ackK9cbiA0YB = 'dX1N15fjv5KdeCyi';//AESkey，可自定义
const acimrLO29gRI = 'f3v35CzxuYjqwizp';//密钥偏移量IV，可自定义

const dsk9EbiUpi5W = 'hIFclTxH0JalYZiu';//DESkey，可自定义
const dsi3gJ2aZe1f = 'xMFHANC8X1TunaGs';//密钥偏移量IV，可自定义

const dckE15Yk15AF = 'oHLKvpN54hwpLWjt';//DESkey，可自定义
const dcik4kPiOWjo = 'pdgLk9FGBd5kXbm0';//密钥偏移量IV，可自定义

const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

function Base64() {
    _keyStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
    this.encode = function(input) {
        var output = '';
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
        input = _utf8_encode(input);
        while (i < input.length) {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else {
                if (isNaN(chr3)) {
                    enc4 = 64;
                }
            }
            output = output + _keyStr.charAt(enc1) + _keyStr.charAt(enc2) + _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
        }
        return output;
    }
    ;
    this.decode = function(input) {
        var output = '';
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, '');
        while (i < input.length) {
            enc1 = _keyStr.indexOf(input.charAt(i++));
            enc2 = _keyStr.indexOf(input.charAt(i++));
            enc3 = _keyStr.indexOf(input.charAt(i++));
            enc4 = _keyStr.indexOf(input.charAt(i++));
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
            output = output + String.fromCharCode(chr1);
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }
        }
        output = _utf8_decode(output);
        return output;
    }
    ;
    _utf8_encode = function(string) {
        string = string.replace(/\r\n/g, '\n');
        var utftext = '';
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c);
            } else {
                if ((c > 127) && (c < 2048)) {
                    utftext += String.fromCharCode((c >> 6) | 192);
                    utftext += String.fromCharCode((c & 63) | 128);
                } else {
                    utftext += String.fromCharCode((c >> 12) | 224);
                    utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                    utftext += String.fromCharCode((c & 63) | 128);
                }
            }
        }
        return utftext;
    }
    ;
    _utf8_decode = function(utftext) {
        var string = '';
        var i = 0;
        var c = c1 = c2 = 0;
        while (i < utftext.length) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            } else {
                if ((c > 191) && (c < 224)) {
                    c2 = utftext.charCodeAt(i + 1);
                    string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                    i += 2;
                } else {
                    c2 = utftext.charCodeAt(i + 1);
                    c3 = utftext.charCodeAt(i + 2);
                    string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                    i += 3;
                }
            }
        }
        return string;
    };
}


function ObjectSort(obj) {
    var newObject = {};
    Object.keys(obj).sort().map(function(key) {
        newObject[key] = obj[key];
    });
    return newObject;
}


var BASE64 = {
    encrypt: function(text) {
        var b = new Base64();
        return b.encode(text);
    },
    decrypt: function(text) {
        var b = new Base64();
        return b.decode(text);
    },
};

var AES = {
    encrypt: function(text, key, iv) {
        var secretkey = do_md5(key).substr(16, 16);
        var secretiv = do_md5(iv).substr(0, 16);
        // console.log('real key:', secretkey);
        // console.log('real iv:', secretiv);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.AES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        });
        return result.toString();
    },
    decrypt: function(text, key, iv) {
        var secretkey = do_md5(key).substr(16, 16);
        var secretiv = do_md5(iv).substr(0, 16);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.AES.decrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        });
        return result.toString(CryptoJS.enc.Utf8);
    },
};

var DES = {
    encrypt: function(text, key, iv) {
        var secretkey = do_md5(key).substr(0, 16);
        var secretiv = do_md5(iv).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        });
        return result.toString();
    }, decrypt: function(text, key, iv) {
        var secretkey = do_md5(key).substr(0, 16);
        var secretiv = do_md5(iv).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.decrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7,
        });
        return result.toString(CryptoJS.enc.Utf8);
    },

};

var pov0M2gfR = function(method, obj) {
    var appId = '271c2aab7dd615dacbadcb41d3c77fa4';
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    const dckE15Yk15AF = 'oHLKvpN54hwpLWjt';//DESkey，可自定义
    const dcik4kPiOWjo = 'pdgLk9FGBd5kXbm0';//密钥偏移量IV，可自定义
    // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
    var param = {
        appId: appId,
        method: method,
        timestamp: timestamp,
        clienttype: clienttype,
        object: obj,
        secret: do_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj))),
    };
    param = BASE64.encrypt(JSON.stringify(param));
    param = DES.encrypt(param, dckE15Yk15AF, dcik4kPiOWjo);
    return param;
};


s = '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';

function deIZLF7oahc0DLiXbqt(data) {
    data = AES.decrypt(data, askiZExYII01, asideGdRY692);
    data = DES.decrypt(data, dsk9EbiUpi5W, dsi3gJ2aZe1f);
    data = BASE64.decrypt(data);
    return data;
}

// 对请求参数做加密处理
function params(city = '苏州') {
    var data = {
        'city': city,
    };
    return pov0M2gfR('GETDATA', data);
}

// 对返回的加密数据做解密处理
function decrypt(data) {
    return deIZLF7oahc0DLiXbqt(data);
}

