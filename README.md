# Cryptography
A personal project built for me to learn more about Qt (using PySide 6), cipher algorithms and how to write maintainable code using OOP principles.
- A cross-platform app for encrypting files and text.
- Uses a user-provided password combined with a randomly generated salt to create encryption keys. The password is required for both encryption and decryption.
- Accepts pre-encrypted files only if the format is supported* by the app.
- Encrypted output can be saved in any format supported* by the app.

*Supported formats a can be found in: **'src/utils/file_strategy'**

## Getting Started
### Prerequisites

- Python 3.13+

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sab-992/cryptography.git
cd cryptography
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the **"main.py"** file with:
```bash
python main.py
```

### View Logs
If any error happened during, they can be logged by enabling the setting in the utils/settings.py file. The logs will be saved in detail the utils/logs/details folder or simply in the utils/logs/logs.txt file.