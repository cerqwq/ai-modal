# 💬 AI Modal

AI弹窗组件工具，支持弹窗设计、动画、交互。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 💬 弹窗设计
- 🚪 抽屉组件生成
- 🔔 通知组件生成
- 🍞 Toast组件生成
- 💡 Tooltip组件生成
- 🗨️ 对话框系统设计

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_modal import create_tools

tools = create_tools()

# 弹窗设计
modal = tools.design_modal("确认删除", "modern")

# 弹窗代码
code = tools.generate_modal_code("确认弹窗", "react")

# 抽屉组件
drawer = tools.generate_drawer("右侧", "react")

# 通知组件
notification = tools.generate_notification(["成功", "错误", "警告"], "react")

# Toast组件
toast = tools.generate_toast(["右上", "底部"], "react")

# Tooltip组件
tooltip = tools.generate_tooltip(["悬停", "点击"], "react")
```

## 📁 项目结构

```
ai-modal/
├── tools.py       # 弹窗工具核心
└── README.md
```

## 📄 许可证

MIT License
