// node标准库
let crypto = require('crypto');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

function gen_sign() {
    var e = 'fsdsogkndfokasodnaso';
    const o = (new Date).getTime();
    var u = 'fanyideskweb';
    var d = 'webfanyi';
    var sign = do_md5(`client=${u}&mysticTime=${o}&product=${d}&key=${e}`);
    return {
        sign: sign,
        mysticTime: o,
    };
}

function b(e) {
    return crypto.createHash('md5').update(e).digest();
}

var decrypt = (data) => {
    var t = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl';
    var o = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4';
    const n = Buffer.alloc(16, b(t))
        , a = Buffer.alloc(16, b(o))
        , i = crypto.createDecipheriv('aes-128-cbc', n, a);
    let c = i.update(data, 'base64', 'utf-8');
    return c += i.final('utf-8'),
        c;
};



