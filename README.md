# StudyPilot Web

基于 Flask 的大学生学管理 Web 平台，支持 AI 刷题与 CS 八股文背诵卡片。

## 功能

- **AI 刷题**：输入课程名生成选择题、判断题、填空题
- **背诵卡片**：35张 CS 八股文卡片，6大领域，点击翻转查看解释

## 背诵卡片模块

| 分类 | 卡片数 | 内容 |
|------|--------|------|
| 数据结构 | 6 | 数组、链表、栈、队列、哈希表、二叉树 |
| 算法 | 6 | O(n)/O(1)/O(n^2)、二分查找、DP、递归 |
| 操作系统 | 5 | 进程、线程、死锁、虚拟内存、上下文切换 |
| 计算机网络 | 6 | TCP握手/挥手、HTTP/HTTPS、DNS、OSI、GET/POST |
| 数据库 | 5 | ACID、索引、JOIN、SQL vs NoSQL、Redis |
| 编程基础 | 7 | OOP、单例/工厂、栈/堆、编译/解释、Git、REST |

## 安装与运行

```bash
pip install -r requirements.txt
python app.py
```

访问 http://localhost:5000

## 技术栈

- Python 3 / Flask
- Bootstrap 5