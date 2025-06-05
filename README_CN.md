[English Version](README.md) | [中文版本](README_CN.md)

# JARVIS - PyQt LLM 桌面应用

<img src="resources/icons/yinhexi.png" width="200" alt="应用图标">


JARVIS 是一个基于 PySide6 的桌面聊天应用，支持与多种大语言模型交互，具有简洁现代的UI设计和丰富的功能。

## 功能特性

- 💬 多轮对话支持
- 🖼️ 图片上传和解析
- 📁 文件上传和内容提取
- 🔄 对话历史管理
- 🤖 多模型支持 (目前支持 QWen 和 Deepseek)
- 🎨 无边框可拖动窗口设计
- ⚙️ 模型参数配置

## 安装指南

### 系统要求
- Python 3.9+
- macOS / Windows / Linux

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/pyqtllm.git
cd pyqtllm
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 运行应用：
```bash
python main.py
```

## 使用说明

1. **开始对话**：
   - 在底部输入框中输入问题，按Enter或点击发送按钮
   - 点击"+"按钮创建新对话

2. **文件上传**：
   - 拖拽文件到上传区域或点击上传按钮
   - 目前支持图片(.jpg, .png等)和文本文件

3. **模型选择**：
   - 点击模型按钮选择不同的模型提供商
   - 设置API密钥以启用模型访问

4. **对话历史**：
   - 在"History Chats"标签页查看和管理历史对话
   - 支持批量删除对话

## 项目结构

```
pyqtllm/
├── data/                  # 数据存储
│   └── conversations.db   # SQLite数据库
├── resources/             # 资源文件
│   ├── icons/             # 应用图标
│   └── UI.ui              # Qt Designer UI文件
├── src/                   # 源代码
│   ├── controllers/       # 控制器
│   │   └── chat_controller.py
│   ├── models/            # 数据模型
│   │   └── db_manager.py
│   ├── services/          # 服务层
│   │   └── llm_service.py
│   └── ui/                # UI组件
│       ├── UI.py          # 生成的UI代码
│       └── main_window.py # 主窗口实现
├── main.py                # 应用入口
├── README.md              # 说明文件
└── LICENSE                # 许可证
```

## 依赖项

核心依赖：
- PySide6 >= 6.7.0
- SQLite3
- requests

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 项目仓库
2. 创建特性分支 (`git checkout -b feature/your-feature`)
3. 提交更改 (`git commit -am 'Add some feature'`)
4. 推送到分支 (`git push origin feature/your-feature`)
5. 创建Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情见 LICENSE 文件。

## 开发者

- Shuai HAN (https://www.polyu.edu.hk/bre/people/academic-staff/dr-shuai-han/)
