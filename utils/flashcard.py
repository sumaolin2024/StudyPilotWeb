#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""背诵卡片数据模块 - CS八股文"""

FLASHCARD_DATA = [
    # ---- 数据结构 ----
    {"id":1,  "category":"数据结构", "term":"数组 (Array)",
     "explanation":"一块连续的内存空间，存放相同类型的数据。就像一排编号的储物柜，每个柜子只能放同一种东西。",
     "example":"Python: arr = [10, 20, 30]; arr[1] → 20。知道编号（下标），直接就能拿到。"},
    {"id":2,  "category":"数据结构", "term":"链表 (Linked List)",
     "explanation":"每个数据节点里存着「自己的值」和「下一个节点的地址」。就像寻宝游戏，每张纸条上写着下一个纸条的位置。",
     "example":"单向链表：A→B→C→None。要找到C，必须从A开始一个个找。插入/删除很快，但查找慢。"},
    {"id":3,  "category":"数据结构", "term":"栈 (Stack)",
     "explanation":"后进先出 (LIFO)。就像一摞盘子，每次只能拿最上面那个。最后放上去的，最先被拿走。",
     "example":"浏览器「后退」按钮：访问 A→B→C，点击后退→回到B，再后退→回到A。Python: list.append() + list.pop() 就是栈。"},
    {"id":4,  "category":"数据结构", "term":"队列 (Queue)",
     "explanation":"先进先出 (FIFO)。就像排队买奶茶，先来的人先买到。",
     "example":"打印机任务队列：先提交的文档先打印。Python: from collections import deque; q=deque(); q.append('A'); q.popleft()→'A'。"},
    {"id":5,  "category":"数据结构", "term":"哈希表 (Hash Table)",
     "explanation":"通过「哈希函数」把键(key)算成一个数字，直接定位到存储位置。就像图书馆给每本书一个索书号，按号码找书架。",
     "example":"Python 的 dict: student = {'name':'小明','age':18}; student['name']→'小明'。不管字典多大，查找速度都接近 O(1)。"},
    {"id":6,  "category":"数据结构", "term":"二叉树 (Binary Tree)",
     "explanation":"每个节点最多有两个子节点（左孩子和右孩子）。就像族谱，一个人最多有两个直接后代。",
     "example":"二叉搜索树：左 < 根 < 右。找数字5: 根是8→去左边→根是3→去右边→找到5。每次排除一半。"},

    # ---- 算法 ----
    {"id":7,  "category":"算法", "term":"时间复杂度 O(n)",
     "explanation":"衡量算法运行时间随数据量增长的速度。O(n) 表示「数据多10倍，时间也多10倍」。",
     "example":"遍历一个列表：for x in lst: print(x)。100个元素打印100次，1000个打印1000次——线性增长。"},
    {"id":8,  "category":"算法", "term":"时间复杂度 O(1)",
     "explanation":"常数时间——无论数据多大，操作时间不变。就像不管冰箱里有多少鸡蛋，拿最外面那一个都是一下子。",
     "example":"lst[0] 取列表第一个元素，100个元素和100万个元素耗时一样。"},
    {"id":9,  "category":"算法", "term":"时间复杂度 O(n^2)",
     "explanation":"嵌套循环——数据多10倍，时间多100倍。就像每个人都要和其他所有人握手。",
     "example":"冒泡排序：for i in range(n): for j in range(n-i-1): ...。n=100时约5000次比较，n=1000时约50万次。"},
    {"id":10, "category":"算法", "term":"二分查找 (Binary Search)",
     "explanation":"在「已排序」的数组中，每次和中间值比，淘汰一半。就像猜数字1-100，每次猜中间数。",
     "example":"lst=[2,5,8,12,16,23,38,56,72,91]; 找23: 中间是16→小了→去右半→中间是56→大了→去左半→中间是23→找到！O(log n)。"},
    {"id":11, "category":"算法", "term":"动态规划 (DP)",
     "explanation":"把大问题拆成小问题，每个小问题只算一次并记下来。就像算斐波那契：F(5)=F(4)+F(3)，F(4)和F(3)各自只需算一次，存着复用。",
     "example":"爬楼梯：一次爬1或2级，爬到第10级有几种方法？dp[i]=dp[i-1]+dp[i-2]。dp[1]=1, dp[2]=2, dp[3]=3, ..."},
    {"id":12, "category":"算法", "term":"递归 (Recursion)",
     "explanation":"函数自己调用自己，每次把问题缩小，直到最简单的情况。就像俄罗斯套娃，打开一个里面还有一个。",
     "example":"阶乘：fact(5)=5xfact(4)=5x4xfact(3)=...=5x4x3x2x1=120。必须有一个「终止条件」(fact(0)=1)，否则无限循环。"},

    # ---- 操作系统 ----
    {"id":13, "category":"操作系统", "term":"进程 (Process)",
     "explanation":"正在运行的程序实例，拥有独立的内存空间。就像一个独立的厨房，有自己的灶台、食材，别人不能随便进来。",
     "example":"打开两个记事本窗口 = 两个进程。它们各自有独立的内存，互不干扰。一个崩溃不影响另一个。"},
    {"id":14, "category":"操作系统", "term":"线程 (Thread)",
     "explanation":"进程内部的「轻量级执行单元」，多个线程共享同一块内存。就像厨房里的多个厨师，共用同一个灶台和食材。",
     "example":"浏览器的一个标签页卡住了，其他标签还能用——因为现代浏览器每个标签是独立进程。但同一个标签页里的JS代码，多个任务跑在多个线程上，共享页面数据。"},
    {"id":15, "category":"操作系统", "term":"死锁 (Deadlock)",
     "explanation":"两个（或多个）线程互相等待对方手里的资源，谁都不肯放手，结果都卡住了。就像两个人过独木桥，各走一边谁也不让，都过不去。",
     "example":"线程A拿着锁1等锁2，线程B拿着锁2等锁1。破解方法：让所有人都按相同顺序拿锁（先拿1再拿2）。"},
    {"id":16, "category":"操作系统", "term":"虚拟内存 (Virtual Memory)",
     "explanation":"操作系统给每个进程「画饼」——让进程以为自己拥有全部内存，实际上物理内存不够时就借用硬盘空间。就像办公桌不够大，把不常用的文件先放抽屉里。",
     "example":"8GB 物理内存，却可以同时跑 10GB 程序。OS 把不活跃的内存页换到硬盘（pagefile.sys），需要时再换回来。"},
    {"id":17, "category":"操作系统", "term":"上下文切换 (Context Switch)",
     "explanation":"CPU 从运行一个进程/线程切换到另一个。就像你同时写作业和回微信，切换时要把当前进度「存档」再加载另一个。",
     "example":"单核CPU 同时运行浏览器和音乐播放器——实际上是以极快速度来回切换（毫秒级），让你感觉是「同时」的。切换太频繁会降低效率。"},

    # ---- 计算机网络 ----
    {"id":18, "category":"计算机网络", "term":"TCP 三次握手",
     "explanation":"建立 TCP 连接前的「打招呼」流程，确保双方都能收发数据。就像打电话：「喂，听得到吗？」「听得到，你呢？」「我也听得到，开始聊吧。」",
     "example":"1. 客户端→服务器: SYN  2. 服务器→客户端: SYN+ACK  3. 客户端→服务器: ACK"},
    {"id":19, "category":"计算机网络", "term":"TCP 四次挥手",
     "explanation":"断开 TCP 连接的流程。因为 TCP 是全双工（双方都能发数据），需要各自说「我不发了」。就像挂电话：「我说完了」「好的」「我也说完了」「好的拜拜」。",
     "example":"1. A→B: FIN  2. B→A: ACK  3. B→A: FIN  4. A→B: ACK"},
    {"id":20, "category":"计算机网络", "term":"HTTP vs HTTPS",
     "explanation":"HTTP 是明文传输，就像寄明信片，谁都能看。HTTPS = HTTP + SSL/TLS 加密，就像把信放信封里再寄。",
     "example":"HTTP: http://example.com → 数据明文传输。HTTPS: https://example.com → 数据加密，只有你和目标服务器能解密。"},
    {"id":21, "category":"计算机网络", "term":"DNS (域名解析)",
     "explanation":"把人类好记的域名（如 baidu.com）翻译成机器用的 IP 地址。就像电话本：联系人姓名→电话号码。",
     "example":"输入 baidu.com → 问 DNS 服务器 IP是啥 → DNS 回答 → 浏览器连到这个 IP。"},
    {"id":22, "category":"计算机网络", "term":"OSI 七层模型",
     "explanation":"把网络通信分成7层，每层干自己的活。就像寄快递：打包(应用层)→翻译(表示层)→建立会话(会话层)→选快递(传输层)→规划路线(网络层)→装箱(数据链路层)→发车(物理层)。",
     "example":"口诀「应表会传网链物」。最常用 TCP/IP 四层：应用层+传输层+网络层+网络接口层。"},
    {"id":23, "category":"计算机网络", "term":"GET vs POST",
     "explanation":"HTTP 请求的两种方法。GET 像图书馆检索卡查书名——参数放在URL里可见。POST 像把申请表塞进信封——参数放在请求体里，不显示在URL上。",
     "example":"GET: /search?q=python → 查询参数暴露在网址栏。POST: 提交登录表单 → 用户名密码在请求体里。"},

    # ---- 数据库 ----
    {"id":24, "category":"数据库", "term":"ACID 事务",
     "explanation":"数据库事务的四个特性：原子性(要么全做要么不做)、一致性(数据前后都合法)、隔离性(并发互不干扰)、持久性(做完永久保存)。就像银行转账：扣钱和加钱必须一起成功或一起失败。",
     "example":"A 转 100 给 B: A扣100 + B加100。如果第二步失败，第一步必须回滚。不能出现扣了钱但没收到的情况。"},
    {"id":25, "category":"数据库", "term":"索引 (Index)",
     "explanation":"数据库的「目录」，给某个字段建索引后，查找速度从「全书翻一遍」变成「查目录翻到对应页」。B+树是最常用的索引结构。",
     "example":"SELECT * FROM users WHERE email='test@xx.com'。无索引: 逐行扫100万条。有索引: 走B+树 O(log n)，几十次磁盘读。"},
    {"id":26, "category":"数据库", "term":"SQL JOIN",
     "explanation":"把两张表按某个条件「拼接」起来。INNER JOIN 只保留两边都匹配的行（交集），LEFT JOIN 保留左表全部。",
     "example":"SELECT u.name, o.amount FROM users u INNER JOIN orders o ON u.id=o.user_id → 用户名+订单金额。"},
    {"id":27, "category":"数据库", "term":"SQL vs NoSQL",
     "explanation":"SQL（如MySQL）是「先规定格式再填数据」，结构固定。NoSQL（如MongoDB）是「随便什么格式都能存」，灵活但缺少强约束。就像 Excel表格 vs 便签纸。",
     "example":"存用户信息：SQL 需要先建表。NoSQL 直接存 JSON，下次可以加新字段不加限制。"},
    {"id":28, "category":"数据库", "term":"Redis 缓存",
     "explanation":"把热点数据放在内存里，访问速度极快（微秒级），但内存贵所以只放最常用的。就像把最常用的工具放桌面上，不常用的收柜子里。",
     "example":"网站首页「热门文章」每天被访问100万次。放 Redis 里直接从内存返回，速度提升100倍。"},

    # ---- 编程基础 ----
    {"id":29, "category":"编程基础", "term":"面向对象 (OOP)",
     "explanation":"把数据和操作数据的方法打包在一起。三大特性：封装（隐藏细节）、继承（子类复用父类）、多态（同一接口不同实现）。就像遥控器：按「开机」，不需要知道电路怎么工作的。",
     "example":"class Dog(Animal): def speak(self): return '汪汪'。继承 Animal，只需重写 speak()。"},
    {"id":30, "category":"编程基础", "term":"设计模式 - 单例",
     "explanation":"确保一个类只有一个实例，全局都能访问。就像一个国家只有一个总统，不管谁问「总统是谁」答案都一样。",
     "example":"数据库连接池——全局只有一个连接池实例，谁用谁来拿连接用完再还。"},
    {"id":31, "category":"编程基础", "term":"设计模式 - 工厂模式",
     "explanation":"不直接 new 对象，而是通过「工厂方法」创建。就像去餐厅点餐，只需要告诉服务员你要什么。",
     "example":"ShapeFactory.create('circle')→Circle; create('square')→Square。调用者不需要知道具体构造。"},
    {"id":32, "category":"编程基础", "term":"栈内存 vs 堆内存",
     "explanation":"栈：存放局部变量，自动分配自动释放，速度快但空间小。堆：存放对象（new出来的），手动/GC释放，速度慢但空间大。就像口袋 vs 仓库。",
     "example":"int x = 5 → x 在栈上。List lst = new ArrayList() → 引用在栈上，实际数据在堆上。"},
    {"id":33, "category":"编程基础", "term":"编译型 vs 解释型",
     "explanation":"编译型：写好代码→一次性翻译成机器码→运行（C/C++）。解释型：边读边执行（Python/JS）。前者快但移植麻烦，后者慢但灵活跨平台。",
     "example":"C语言：写完→gcc编译→.exe→发给别人运行。Python：写完→python xxx.py→逐行解释执行，得连源码一起给。"},
    {"id":34, "category":"编程基础", "term":"Git 版本控制",
     "explanation":"记录文件的每次修改，可以随时回到任何历史版本。就像打游戏时的存档，死了可以读档重来。",
     "example":"git add→暂存修改; git commit→存档; git push→同步到远程; git reset→回到某个存档。"},
    {"id":35, "category":"编程基础", "term":"RESTful API",
     "explanation":"一种设计 Web API 的风格。用 HTTP 方法表示动作：GET（查）、POST（增）、PUT（改）、DELETE（删）。每个 URL 代表一种资源。就像图书馆的标准借阅流程。",
     "example":"GET /users/1 → 查用户1; POST /users → 创建用户; PUT /users/1 → 更新; DELETE /users/1 → 删除。"},
]

def get_cards_by_category(category=None):
    if category:
        return [c for c in FLASHCARD_DATA if c["category"] == category]
    return FLASHCARD_DATA

def get_categories():
    cats = {}
    for c in FLASHCARD_DATA:
        cat = c["category"]
        if cat not in cats:
            cats[cat] = 0
        cats[cat] += 1
    return cats