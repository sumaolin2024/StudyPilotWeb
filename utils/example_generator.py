# -*- coding: utf-8 -*-
"""Smart Example Generator - generates memory-enhancing examples from card content"""

import re

def generate_example(term: str, explanation: str, category: str = "") -> dict:
    """Generate a memory-enhancing example based on card content."""
    
    # Extract key concepts
    keywords = extract_keywords(term, explanation)
    
    # Generate components
    scenario = generate_scenario(term, category, keywords)
    analogy = generate_analogy(term, category, keywords)
    mnemonic = generate_mnemonic(term, keywords)
    
    return {
        "scenario": scenario,
        "analogy": analogy,
        "mnemonic": mnemonic,
        "formatted": f"{scenario}\n\n{analogy}\n\n{mnemonic}"
    }


def extract_keywords(term: str, explanation: str) -> list:
    """Extract key technical terms."""
    tech_terms = re.findall(r'[A-Z]{2,}[a-z]*|[a-z]+[A-Z]+[a-z]*|[\u4e00-\u9fff]{2,4}', 
                            term + " " + (explanation or ""))
    # Deduplicate and filter
    seen = set()
    result = []
    for t in tech_terms:
        if t not in seen and len(t) >= 2:
            seen.add(t)
            result.append(t)
    return result[:6]


def generate_scenario(term: str, category: str, keywords: list) -> str:
    """Generate a practical scenario example."""
    kw = keywords[:3] if keywords else [term[:8]]
    
    templates = {
        "计算机网络": [
            f"场景：你在调试网络时，用 Wireshark 抓包发现 {kw[0] if kw else term} 字段异常。通过分析 {kw[1] if len(kw)>1 else '数据包'}，你定位到问题出在传输层，成功修复了丢包问题。",
        ],
        "操作系统": [
            f"场景：你的程序运行时发现内存占用持续增长，通过分析 {kw[0] if kw else term}，你意识到是 {kw[1] if len(kw)>1 else '资源'} 没有正确释放，最终用 Valgrind 定位了内存泄漏。",
        ],
        "MySQL": [
            f"场景：线上数据库查询突然变慢，你查看慢查询日志后发现 {kw[0] if kw else term} 相关操作耗时过长。通过优化 {kw[1] if len(kw)>1 else '索引'}，查询时间从 2 秒降到 50ms。",
        ],
        "Redis": [
            f"场景：缓存服务在高并发下出现雪崩，你检查发现是 {kw[0] if kw else term} 策略不当。调整为 {kw[1] if len(kw)>1 else '随机过期'} 后，系统恢复稳定。",
        ],
        "Java": [
            f"场景：代码 review 时同事指出你的 {kw[0] if kw else term} 实现有问题。你查阅了 {kw[1] if len(kw)>1 else '官方文档'}，重构成更优雅的方式，性能提升了 30%。",
        ],
        "C++": [
            f"场景：程序 crash 在 {kw[0] if kw else term} 相关代码。你用 GDB 调试后发现是 {kw[1] if len(kw)>1 else '内存管理'} 问题，修复后程序稳定运行。",
        ],
        "算法与数据结构": [
            f"场景：LeetCode 刷题时遇到 {term[:15]} 问题。你想到了 {kw[0] if kw else '关键'} 技巧，用 {kw[1] if len(kw)>1 else '最优解'} 一次 AC，击败了 95% 的提交。",
        ],
    }
    
    tmpl_list = templates.get(category, [
        f"场景：在实际项目中，你遇到了与 {term[:15]} 相关的问题。通过理解 {kw[0] if kw else '核心概念'}，你快速找到了解决方案，避免了踩坑。",
    ])
    
    import random
    return random.choice(tmpl_list)


def generate_analogy(term: str, category: str, keywords: list) -> str:
    """Generate an easy-to-remember analogy."""
    analogies = {
        "TCP": "类比：TCP 像快递挂号信——发送方寄出后必须等收件人签收确认，没收到确认就重发。",
        "UDP": "类比：UDP 像扔纸飞机——扔出去就完事了，不管对方有没有收到。",
        "HTTP": "类比：HTTP 像去餐厅点餐——你说要什么（Request），服务员给你端上来（Response），一次交互就结束。",
        "进程": "类比：进程像一个独立的小公司——有自己的办公室（内存空间）、员工（线程）和资源。",
        "线程": "类比：线程像公司里的员工——共享办公室和资源，但每个人做不同的事。",
        "死锁": "类比：死锁像两个人过独木桥——A 等 B 让路，B 等 A 让路，结果谁都过不去。",
        "索引": "类比：数据库索引像书的目录——不翻全书就能快速找到某章在哪一页。",
        "缓存": "类比：缓存像办公桌上的常用文件——不用每次都去档案室翻，伸手就能拿到。",
        "锁": "类比：数据库锁像厕所门——一次只能一个人用，外面的人得排队等。",
        "事务": "类比：事务像银行转账——要么钱从 A 到 B 全部完成，要么全部回滚，不能转一半。",
        "JVM": "类比：JVM 像一个万能翻译官——把你的 Java 代码翻译成不同操作系统都能听懂的语言。",
        "指针": "类比：指针像快递单号——不直接拿货，而是告诉你货在仓库哪个位置。",
        "递归": "类比：递归像俄罗斯套娃——打开一个发现里面还有一个，直到最小的那个。",
        "动态规划": "类比：DP 像记账本——把算过的结果记下来，下次用直接查，不用重算。",
        "排序": "类比：排序算法像整理扑克牌——不同方法（冒泡/快排/归并）就是不同的洗牌整理策略。",
    }
    
    # Try exact match
    for key, value in analogies.items():
        if key in term or key == term:
            return f"类比：{value}"
    
    # Generic fallback
    return f"类比：{term[:10]} 像一个工具箱里的专用工具——看起来不起眼，但在特定场景下是不可替代的。"


def generate_mnemonic(term: str, keywords: list) -> str:
    """Generate a one-line memory aid."""
    mnemonics = {
        "TCP": "一句话：TCP = 三次握手建立连接 + 四次挥手断开 + 可靠传输。",
        "UDP": "一句话：UDP = 无连接 + 不可靠 + 快，适合视频直播。",
        "HTTP": "一句话：HTTP = 请求-响应模型，状态码 2xx成功/3xx重定向/4xx客户端错/5xx服务端错。",
        "进程": "一句话：进程 = 资源分配的最小单位，独立内存空间。",
        "线程": "一句话：线程 = CPU 调度的最小单位，共享进程内存。",
        "死锁": "一句话：死锁四条件 = 互斥 + 请求保持 + 不可剥夺 + 循环等待，缺一不锁。",
        "索引": "一句话：索引 = 用空间换时间，B+树是最常用的数据库索引结构。",
        "缓存": "一句话：缓存 = 用空间换时间，把热点数据放在离 CPU 更近的地方。",
        "事务": "一句话：事务 ACID = 原子性 + 一致性 + 隔离性 + 持久性。",
        "JVM": "一句话：JVM = 堆存对象 + 栈存引用 + 方法区存类信息，GC 自动回收堆垃圾。",
        "指针": "一句话：指针 = 存地址的变量，*取值 &取地址，空指针是万恶之源。",
        "递归": "一句话：递归 = 基线条件 + 递归条件，栈溢出说明忘了设出口。",
        "动态规划": "一句话：DP = 记忆化搜索，状态 + 转移方程，自底向上填表。",
        "排序": "一句话：快排 = O(n log n) 平均，分治 + 分区；归并 = 稳定 O(n log n)，空间 O(n)。",
    }
    
    for key, value in mnemonics.items():
        if key in term or key == term:
            return f"一句话记忆：{value}"
    
    return f"一句话记忆：{term[:12]}——理解原理比死记硬背更重要，在项目中多实践自然就记住了。"


# Generate examples for all flashcard data
def enrich_flashcard_examples():
    """Read flashcard data, replace empty placeholders with generated examples."""
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
    from utils.flashcard import FLASHCARD_DATA
    
    count = 0
    for card in FLASHCARD_DATA:
        example = card.get("example", "")
        if not example or len(example) < 10:
            gen = generate_example(card["term"], card.get("explanation", ""), card.get("category", ""))
            card["example"] = gen["formatted"]
            card["_generated"] = True
            count += 1
    
    print(f"Generated examples for {count} cards")
    return count

print("example_generator module loaded")
