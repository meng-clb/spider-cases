var JSEncrypt = require('node-jsencrypt');
var publickeystr = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDhNhuAr4UjFv+cj99PbAQWWx9H \
	X+3jSRThJqJdXkWUMFMTRay8EYRtPFIiwiOUU4gCh4ePMxiuZJWUBHe1waOkXEFc \
	Kg17luhVqECsO+EOLhxa3yHoXA5HcSKlG85hNV3G4uQCr+C8SOE0vCGTnMdnEGmU \
	nG1AGGe44YKy6XR4VwIDAQAB';

function rsa_encrypt(e) {
    var o = new JSEncrypt();
    return o.setPublicKey(publickeystr), o.encrypt(e);
}

function main(name, pwd) {
    let user = {};
    user.name = encodeURIComponent(rsa_encrypt(name));
    user.pwd = encodeURIComponent(rsa_encrypt(pwd));
    // console.log(user);
    return user;
}

// main('123456', '123456');

