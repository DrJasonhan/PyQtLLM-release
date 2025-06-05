[中文版本](README_CN.md) | [English Version](README.md)

# JARVIS - PyQt LLM Desktop Application

<img src="resources/icons/yinhexi.png" width="200" alt="application_icon">

JARVIS is a PySide6-based desktop chat application that supports interaction with various large language models, featuring a clean modern UI design and rich functionality.

## Features

- 💬 Multi-turn conversation support
- 🖼️ Image upload and parsing (supports QWen-VL-Plus vision model)
- 📁 File upload and content extraction
- 🔄 Conversation history management
- 🤖 Multi-model support (currently supports QWen and Deepseek)
- 🎨 Borderless draggable window design
- ⚙️ Model parameter configuration

## Installation Guide

### System Requirements
- Python 3.9+
- macOS / Windows / Linux

### Installation Steps

1. Clone repository:
```bash
git clone https://github.com/yourusername/pyqtllm.git
cd pyqtllm
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run application:
```bash
python main.py
```

## Usage Instructions

1. **Start Conversation**:
   - Enter questions in the input box at bottom, press Enter or click Send button
   - Click "+" button to create new conversation

2. **File Upload**:
   - Drag files to upload area or click upload button
   - Currently supports images (.jpg, .png etc.) and text files

3. **Model Selection**:
   - Click model button to select different providers
   - Set API key to enable model access

4. **Conversation History**:
   - View and manage history in "History Chats" tab
   - Supports batch deletion of conversations

## Project Structure

```
pyqtllm/
├── data/                  # Data storage
│   └── conversations.db   # SQLite database
├── resources/             # Resource files
│   ├── icons/             # App icons
│   └── UI.ui              # Qt Designer UI file
├── src/                   # Source code
│   ├── controllers/       # Controllers
│   │   └── chat_controller.py
│   ├── models/            # Data models
│   │   └── db_manager.py
│   ├── services/          # Service layer
│   │   └── llm_service.py
│   └── ui/                # UI components
│       ├── UI.py          # Generated UI code
│       └── main_window.py # Main window implementation
├── main.py                # Application entry
├── README.md              
└── LICENSE                
```

## Dependencies

Core dependencies:
- PySide6 >= 6.7.0
- SQLite3
- requests

## Contribution Guide

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -am 'Add some feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Create Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Developer

- Shuai Han (https://www.polyu.edu.hk/bre/people/academic-staff/dr-shuai-han/)
