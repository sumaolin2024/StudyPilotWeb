# StudyPilot Web

StudyPilot Web 是一个面向大学生的学习管理平台，基于 Flask 构建，支持登录注册、任务管理、AI 刷题和学习统计。

## 功能介绍

- 登录 / 注册系统
- 学习任务管理：添加、删除、标记完成
- AI 刷题系统：自动生成选择题、判断题、填空题，并自动评分
- 数据统计系统：使用 matplotlib 可视化完成率与刷题成绩
- Bootstrap5 响应式前端界面

## 技术栈

- Python 3.14
- Flask
- SQLite
- Bootstrap5
- Jinja2
- matplotlib

## 安装方法

1. 进入项目目录：

```bash
cd StudyPilotWeb
```

2. 创建虚拟环境并激活：

```bash
python -m venv venv
venv\Scripts\activate
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

## 运行方法

```bash
py app.py
```

打开浏览器访问：

```text
http://127.0.0.1:5000
```

## 项目结构

- `app.py`：应用入口
- `routes/`：路由视图模块
- `utils/`：数据库、题库与统计工具
- `templates/`：页面模板
- `static/`：静态资源

## 注意事项

- 初次运行后，SQLite 数据库文件会自动创建在 `instance/study_pilot.db`
- 生成的统计图保存在 `static/plots/`
