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

**[看准网](https://www.kanzhun.com/search?cityCode=34&industryCodes=52&pageNum=1&query=%E6%93%8D%E4%BD%9C%E5%91%98&type=4)**

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



 



**声明: 此项目由本人学习存储代码使用, 所有代码均用于学习, 如果你获取了源码, 请在24小时内从你的计算机删除, 请勿用于非法用途.**