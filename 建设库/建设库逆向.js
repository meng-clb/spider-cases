let crypto = require('crypto');

function do_md5(e) {
    return crypto.createHash('md5').update(e.toString()).digest('hex');
}

var f = (new Date).getTime();
var timestamp = f;

var eu = function(e) {
    var t = nu(e)
        , n = '';
    for (var i in t) {
        var r = tu(e[t[i]]);
        null != r && '' != r.toString() && (n += t[i] + '=' + r + '&');
    }
    return n;
};
var nu = function(e) {
    var t = new Array
        , n = 0;
    for (var i in e)
        t[n] = i,
            n++;
    return t.sort();
};
var tu = function e(t) {
    var n;
    if (Array.isArray(t)) {
        for (var r in n = new Array,
            t) {
            var o = t[r];
            for (var i in o)
                null == o[i] ? delete t[r][i] : Array.isArray(t[r][i]) && e(t[r][i]);
        }
        return n = t,
            JSON.stringify(n).replace(/^(\s|")+|(\s|")+$/g, '');
    }
    return n = t && t.constructor === Object ? JSON.stringify(t) : t;
};
var Jc = function(e, t, time) {
    var n = t + e + time;
    return n = do_md5(n);
};

function main(page) {
    data = {
	'eid': '',
	'achievementQueryType': 'and',
	'achievementQueryDto': [],
	'personnelQueryDto': {
		'queryType': 'and',
	},
	'aptitudeQueryDto': {
		'hasAptitude': 1,
		'startAptitudeValidityDate': '2024-03-25',
		'endAptitudeValidityDate': '2024-04-25',
		'aptitudeDtoList': [
			{
				'codeStr': '',
				'queryType': 'and',
				'aptitudeType': 'qualification',
			},
		],
		'aptitudeSource': 'new',
	},
	'page': {
		'page': page,
		'limit': '20',
		'order': 'desc',
	},
}
    var sign = (param = data,
        time = f,
        t = eu(param),
        Jc('ghaepVf6IhcHmgnk4NCTXLApxQkBcvh1', Jc('mwMlWOdyM7OXbjzQPulT1ndRZIAjShDB', Jc('ZuSj0gwgsKXP4fTEz55oAG2q2p1SVGKK', t, time), time), time));
    return {'sign': sign, 'timestamp': timestamp}
}

