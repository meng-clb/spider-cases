const CryptoJS = require('crypto-js');
window = {
    _$pr: [],
};
_0x4e96b4 = window;

_$Wa = Date.parse(new Date());
// console.log(_$Wa);
_0x4e96b4['_$pr']['push'](_0x474032(_$Wa));

var _$Ww = CryptoJS['enc']['Utf8']['parse'](_0x4e96b4['_$pr']['toString']());
_0x29dd83 = CryptoJS['AES']['encrypt'](_$Ww, _0x4e96b4['_$qF'], {
    'mode': CryptoJS['mode']['ECB'],
    'padding': CryptoJS['pad']['Pkcs7'],
});
var cookie = _0x29dd83['toString']();