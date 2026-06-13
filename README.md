# StudyPilot Web

基于 Flask 的大学生学管理 Web 平台，整合 CSView 八股文知识库。

## 功能

- **AI 刷题**：输入"八股文"获取 34 道算法/网络/数据库面试真题
- **背诵卡片**：381 张 CS 八股文卡片，覆盖 7 大领域，点击翻转查看解释

## 背诵卡片模块（来源：csview.cn）

| 分类 | 卡片数 | 内容 |
|------|--------|------|
| 计算机网络 | ~40 | TCP/UDP、HTTP、IP协议、三次握手/四次挥手 |
| 操作系统 | ~60 | 进程/线程、内存管理、并发、文件系统 |
| MySQL | ~50 | 存储引擎、索引、锁、事务、日志 |
| Redis | ~30 | 数据结构、持久化、应用场景、集群 |
| Java | ~40 | 集合、并发、JVM、Spring |
| C++ | ~50 | 内存管理、指针引用、继承多态、编译链接、STL |
| 系统设计 | ~110 | 设计模式、海量数据处理、分布式 |

## 安装与运行

```bash
pip install -r requirements.txt
python app.py
```

访问 http://localhost:5000
刷题时输入课程名"八股文"即可使用 CSView 题库。

## 技术栈

- Python 3 / Flask
- Bootstrap 5
- 数据来源：csview.cn