# Mahojin AI Auto Check-in Bot

A Python-based automation tool for daily check-ins on [Mahojin AI](https://app.mahojin.ai/maho-point) to earn points. Supports multiple accounts and independent proxies.

## Features
- **Multi-account Support**: Manage multiple sessions in one go.
- **Proxy Support**: Assign a unique HTTP/SOCKS proxy to each account.
- **Security Focused**: Sensitive credentials are stored in an ignored `config.json`.
- **Timezone Aware**: Automatically handles timezone offsets to match browser behavior.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/crhywun/Mahojin-bot.git
   cd Mahojin-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `config.json` file in the root directory (you can copy `config.json.example`):
   ```bash
   cp config.json.example config.json
   ```

2. **How to get your Cookie**:
   - Open [Mahojin Points Page](https://app.mahojin.ai/maho-point) in your browser.
   - Login to your account.
   - Press `F12` to open Developer Tools.
   - Go to the **Network** tab and refresh the page.
   - Find a request named `point` or `check-in`.
   - In the **Request Headers**, copy the full string value of the `cookie` header.

3. Edit `config.json` and paste your cookie and proxy (optional):
   ```json
   [
       {
           "name": "MyAccount",
           "cookie": "your_full_cookie_string_here",
           "proxy": "http://127.0.0.1:7890"
       }
   ]
   ```

## Usage

Run the script manually:
```bash
python mahojin_checkin.py
```

## Disclaimer
This tool is for educational purposes only. Use it at your own risk. The author is not responsible for any account bans or issues caused by using this script.
