#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""刷题生成模块 + 八股文题库"""
import json
import random
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path(__file__).parent.parent / "static" / "quiz_output.txt"

BAGUWEN_QUESTIONS = [
  {
    "course": "八股文",
    "type": "choice",
    "question": "快速排序平均时间复杂度？",
    "answer": "O(n log n)",
    "options": [
      "O(n)",
      "O(n log n)",
      "O(n^2)",
      "O(log n)"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "归并排序空间复杂度？",
    "answer": "O(n)",
    "options": [
      "O(1)",
      "O(log n)",
      "O(n)",
      "O(n log n)"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "堆排序空间复杂度？",
    "answer": "O(1)",
    "options": [
      "O(1)",
      "O(log n)",
      "O(n)",
      "O(n log n)"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "快速排序是稳定排序。",
    "answer": "错"
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "归并排序是稳定排序。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "冒泡排序最好情况O(n)。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "快速排序采用____法思想。",
    "answer": "分治"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "DFS全称深度____搜索。",
    "answer": "优先"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "BFS用____数据结构实现。",
    "answer": "队列"
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "二分查找前提？",
    "answer": "数组有序",
    "options": [
      "数组有序",
      "数组无序",
      "链表",
      "哈希"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "LRU缓存最佳结构？",
    "answer": "哈希表+双向链表",
    "options": [
      "数组",
      "哈希表+双向链表",
      "栈",
      "二叉树"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "二叉搜索树中序遍历有序。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "动态规划=分治法。",
    "answer": "错"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "全排列用____算法。",
    "answer": "回溯"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "LRU全称Least ____ Used。",
    "answer": "Recently"
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "Kadane算法解？",
    "answer": "最大子数组和",
    "options": [
      "最大子数组和",
      "LCS",
      "背包",
      "最短路径"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "判断链表环用？",
    "answer": "快慢指针",
    "options": [
      "快慢指针",
      "DP",
      "二分",
      "贪心"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "岛屿数量只能用DFS。",
    "answer": "错"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "反转链表可____或递归。",
    "answer": "迭代"
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "TCP三次握手先发？",
    "answer": "SYN",
    "options": [
      "ACK",
      "SYN",
      "FIN",
      "RST"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "TCP四次挥手主动方先发？",
    "answer": "FIN",
    "options": [
      "SYN",
      "ACK",
      "FIN",
      "RST"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "TCP靠序列号+ACK保可靠。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "TCP流量控制字段____。",
    "answer": "窗口"
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "HTTP 200=？",
    "answer": "成功",
    "options": [
      "成功",
      "重定向",
      "客户端错",
      "服务器错"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "HTTP 404=？",
    "answer": "未找到",
    "options": [
      "成功",
      "未找到",
      "服务器错",
      "重定向"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "HTTPS=HTTP+SSL/TLS。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "DNS解析____为IP。",
    "answer": "域名"
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "InnoDB默认索引？",
    "answer": "B+树",
    "options": [
      "哈希",
      "B+树",
      "红黑树",
      "跳表"
    ]
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "Redis分布式锁命令？",
    "answer": "SETNX",
    "options": [
      "SET",
      "SETNX",
      "GET",
      "INCR"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "Redis单线程模型。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "HashMap链表>____转红黑树(JDK8)。",
    "answer": "8"
  },
  {
    "course": "八股文",
    "type": "choice",
    "question": "进程间通信最快？",
    "answer": "共享内存",
    "options": [
      "管道",
      "共享内存",
      "消息队列",
      "Socket"
    ]
  },
  {
    "course": "八股文",
    "type": "judge",
    "question": "线程共享进程堆内存。",
    "answer": "对"
  },
  {
    "course": "八股文",
    "type": "fill",
    "question": "死锁四条件:互斥、____、不可剥夺、循环等待。",
    "answer": "请求保持"
  }
]


class QuizGenerator:
    def get_quiz_data(self, course_name):
        """Return structured quiz data as list of question dicts."""
        if course_name == "八股文":
            questions = BAGUWEN_QUESTIONS.copy()
            random.shuffle(questions)
            return questions[:15]
        return self._generate_demo_data(course_name)

    def generate_quiz(self, course_name):
        """Generate quiz for a course"""
        if course_name == "八股文":
            return self._generate_baguwen_quiz()
        return self._generate_demo_quiz(course_name)

    def _generate_baguwen_quiz(self):
        """Generate quiz from 八股文 question bank"""
        questions = BAGUWEN_QUESTIONS.copy()
        random.shuffle(questions)
        selected = questions[:15]  # Pick 15 questions
        
        lines = []
        lines.append(f"课程: 八股文  生成时间: {datetime.now().isoformat()}")
        lines.append("")
        
        q_num = {"choice": 0, "judge": 0, "fill": 0}
        
        for i, q in enumerate(selected, 1):
            q_type = q["type"]
            q_num[q_type] = q_num.get(q_type, 0) + 1
            
            if q_type == "choice":
                lines.append(f"选择题 {q_num['choice']}. {q['question']}")
                opts = q.get("options", [])
                labels = ["A", "B", "C", "D"]
                for j, opt in enumerate(opts):
                    lines.append(f" {labels[j]}. {opt}")
                lines.append(f"   答案: {q['answer']}")
            elif q_type == "judge":
                lines.append(f"判断题 {q_num['judge']}. {q['question']}")
                lines.append(f"   答案: {q['answer']}")
            elif q_type == "fill":
                lines.append(f"填空题 {q_num['fill']}. {q['question']}")
                lines.append(f"   答案: {q['answer']}")
            lines.append("")
        
        content = "\n".join(lines)
        OUTPUT_FILE.write_text(content, encoding="utf-8")
        return True

    def _generate_demo_data(self, course_name):
        """Generate structured demo data"""
        questions = []
        for i in range(1, 6):
            questions.append({
                "course": course_name,
                "type": "choice",
                "question": course_name + " 的示例选择题 " + str(i) + "？",
                "answer": random.choice(["A", "B", "C", "D"]),
                "options": ["选项1", "选项2", "选项3", "选项4"]
            })
        for i in range(1, 6):
            questions.append({
                "course": course_name,
                "type": "judge",
                "question": course_name + " 的示例判断题 " + str(i) + "。",
                "answer": random.choice(["对", "错"])
            })
        for i in range(1, 6):
            questions.append({
                "course": course_name,
                "type": "fill",
                "question": course_name + " 的示例填空题 " + str(i) + "：____。",
                "answer": "示例答案" + str(i)
            })
        random.shuffle(questions)
        return questions

    def _generate_demo_quiz(self, course_name):
        """Generate demo quiz (placeholder)"""
        lines = [f"课程: {course_name}  生成时间: {datetime.now().isoformat()}"]
        lines.append("")
        
        for i in range(1, 6):
            lines.append(f"选择题 {i}. {course_name} 的示例选择题？")
            lines.append(" A. 选项1  B. 选项2  C. 选项3  D. 选项4")
            lines.append(f"   答案: {random.choice(['A','B','C','D'])}")
            lines.append("")
        
        for i in range(1, 6):
            lines.append(f"判断题 {i}. {course_name} 的示例判断题。")
            lines.append(f"   答案: {random.choice(['对','错'])}")
            lines.append("")
        
        for i in range(1, 6):
            lines.append(f"填空题 {i}. {course_name} 的示例填空题：____。")
            lines.append(f"   答案: {f'示例答案{i}'}")
            lines.append("")
        
        content = "\n".join(lines)
        OUTPUT_FILE.write_text(content, encoding="utf-8")
        return True
