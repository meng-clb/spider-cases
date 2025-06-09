// node标准库
let crypto = require('crypto');
function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

function main() {
    var n = Date.now().toString();
    var r = do_md5(n + '9527' + n.substr(0, 6));
    return {'timestamp': n, 'code': r};
}


// console.log(main())