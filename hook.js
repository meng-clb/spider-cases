// hook cookie
Object.defineProperty(document, 'cookie', {
    set: function(val) {
        debugger;
    },
});

// hook windows对象下某个参数
Object.defineProperty(window, '_$ss', {
    set(val) {
        debugger;
    },
});

// 使用Function constructor 实现的无限debugger
(function() {
    Function.prototype.constructor_ = Function.prototype.constructor;
    Function.prototype.constructor = function(val) {
        if (val === 'debugger') {
            return {};
        }
        return Function.prototype.constructor_(val);
    };
})();