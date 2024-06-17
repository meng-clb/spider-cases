## 逆向案例

**[网易云音乐](https://music.163.com/)**
> 实现功能：
> 1. 逆向请求参数   **(AES|RSA)**
> 2. 实现下载歌曲链接的获取
> 3. 获取歌曲的评论

**[喜马拉雅](https://www.ximalaya.com/category/a3_b10880/p2/)**
> 实现功能:
> 1. 逆向请求参数  **md5**
> 2. 获取页面数据

**[建设库](https://www.jiansheku.com/search/expired/?page=5)**
> 实现功能:
> 1. 请求头参数逆向  **md5**
> 2. 获取页面数据集

**[海南免税店](https://m.hltmsp.com/passport/login?backURL=%2F%2Fm.hltmsp.com%2Fuser)**
> 实现功能:
> 1. 模拟登陆  **md5**
> 2. 总共4次请求
> ```
> (1) 第一次, 验证失败
> (2) 第二次, 请求验证码接口
> (3) 第三次, 携带验证码正确坐标进行请求
> (4) 第四次, 正式登陆

**[莫莫铺子](http://mmpz.ttzhuijuba.com/?r=/l&cids=9&site=classify&sort=0)**
> 实现功能:
> 1. 获取页面商品数据
> 2. 逆向请求参数sign值  **md5加密**

**[中大网校](https://ke.wangxiao.cn/)**
> 实现功能:
> 1. 模拟登陆
> 2. 逆向密码加密方式  **rsa**

**[土巴兔](https://www.to8to.com/new_login.php)**
> 实现功能:
> 1. 模拟登陆
> 2. 逆向账号密码加密  **rsa加密, 使用同一个key**

**[币数据](https://www.mytokencap.com/)**
> 实现功能:
> 1. 逆向请求参数, 获取到页面数据 **md5**


**[一品威客](https://www.epwk.com/login.html)**
> 实现功能:
> 1. 模拟登陆
> 2. 逆向请求头Signature参数 **AES,MD5**

*

*[看准网](https://www.kanzhun.com/search?cityCode=34&industryCodes=52&pageNum=1&query=%E6%93%8D%E4%BD%9C%E5%91%98&type=4)
**

> 实现功能:
> 1. 请求参数的加密逆向 AES加密
> 2. 返回的加密值进行解密 AES

**[有道翻译](https://fanyi.youdao.com/#/)**

> 实现功能:
> 1. 请求参数sign逆向 **md5**
> 2. 返回的加密参数进行解密

**[易车](https://car.yiche.com/siyucivic/peizhi/)**

> 实现功能:
> 1. 请求头参数X-Sign,X-User-Guid逆向
> 2. sign参数使用md5加密
> 3. user-guid参数隐藏在cookie中

**[艺恩](https://www.endata.com.cn/BoxOffice/BO/year/index.html)**

> 实现功能:
> 1. 混淆代码进行还原
> 2. 数据进行解密  **DES**



**[问财](https://www.iwencai.com/unifiedwap/result?w=%E6%B6%A8%E8%B7%8C%E5%B9%85%E5%A4%A7%E4%BA%8E%E7%AD%89%E4%BA%8E0%E5%B0%8F%E4%BA%8E%E7%AD%89%E4%BA%8E5%25%EF%BC%8C&querytype=fund&addSign=1712064372700)**

> 实现功能:
> 1. 逆向请求头参数Hexin-V
> 2. 参数是cookie中获取到
> 3. hook cookie拿到参数的生成

**[微博](https://m.weibo.cn/)**
> 实现功能:
> 1. 热搜榜单获取所有的链接(部分完成)
> 2. 通过链接拿到所有评论(完成, 未测试极限能拿多少)
> 3. 通过主页ID获取所有的文章(以媒体类为主体写的, 更适用于媒体类, 测试赵今麦, 只能拿部分)

**[大众点评](https://www.dianping.com/)**
> 实现功能:
> 1. 获取商家的各种信息
> 2. 对商家的评论进行获取


**[去哪儿](https://www.qunar.com/)**
> 实现功能:
> 1. 自动登录
> 2. 获取酒店信息


**[空气质量在心啊检测分析平台](https://www.aqistudy.cn/)**
> 实现功能:
> 1. 对请求参数的加密
> 2. 对返回的加密数据做解密


**[99安全中心](https://aq.99.com/V3/NDUser_Login.htm)**
> 实现功能:
> 1. 登录密码加密逆向


**[七麦数据](https://www.qimai.cn/)**
> 实现功能:
> 1. 对请求参数进行逆向
> 2. 获取到返回的数据


**[CBA](https://data-server.cbaleague.com/api/team-match-datas/team-entirety-list)**
> 实现功能:
> 1. 对返回的数据做解密处理


**[长佩文学](https://m.gongzicp.com/)**
> 实现功能:
> 对返回的数据进行解密处理  **AES**


**[猿人学](https://match.yuanrenxue.cn/list)**

**[第二题](https://match.yuanrenxue.cn/match/2)**

```markdown
思路:
hook页面的cookie, cookie过期很快, hook之后通过调用栈找到入口, 进行逆向.
网站是ob混淆, 按照顺序扣就可以了.
有一个参数需要单独处理, 时间戳.
```

**[第十三题](https://match.yuanrenxue.cn/match/13)**

````markdown
思路:
第一次请求页面, 会返回一个script标签, 里边的内容就是cookie, 使用re拿到cookie.

使用这个cookie进行数据的获取.
````

**[第一题](https://match.yuanrenxue.cn/match/1)**

````markdown
思路:
先过debugger, 直接让setInterval置空, 会检测setInterval函数, 对toString做伪装.

然后发现请求参数加密, 使用xhr断点, 断api接口, 发现是简单的混淆.
直接扣代码, 解除混淆, 拿到加密参数m的值.
````

**[懂车帝](https://www.dongchedi.com/)**
> 实现功能:
> 1. 字体反爬处理
> 2. 获取二手车数据



**声明: 此项目由本人学习存储代码使用, 所有代码均用于学习, 如果你获取了源码, 请在24小时内从你的计算机删除, 请勿用于非法用途.
**