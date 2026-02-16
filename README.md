# Mahojin AI 自动签到脚本

一个基于 Python 的自动化工具，用于在 [Mahojin AI](https://app.mahojin.ai/maho-point) 平台上进行每日签到以获取积分。支持多账号管理及独立代理配置。

## 功能特性
- **多账号支持**：一次性管理多个账号的签到。
- **独立代理**：可以为每个账号分配唯一的 HTTP/SOCKS 代理，有效防止账号关联。
- **安全性**：敏感的 Cookie 信息存储在被 Git 忽略的 `config.json` 中，防止泄露。
- **时区模拟**：自动计算时区偏移量，完美模拟真实浏览器行为。

## 安装步骤

1. 克隆仓库：
   ```bash
   git clone https://github.com/crhywun/Mahojin-bot.git
   cd Mahojin-bot
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 配置说明

1. 在根目录下创建一个 `config.json` 文件（可以直接复制示例文件）：
   ```bash
   cp config.json.example config.json
   ```

2. **如何获取 Cookie**:
   - 在浏览器中打开 [Mahojin 积分页面](https://app.mahojin.ai/maho-point)。
   - 登录你的账号。
   - 按下 `F12` 打开开发者工具。
   - 切换到 **Network (网络)** 标签页并刷新页面。
   - 找到一个名为 `point` 或 `check-in` 的请求。
   - 在 **Request Headers (请求标头)** 中，完整复制 `cookie` 字段的值。

3. 编辑 `config.json`，粘贴你的 Cookie 和代理信息（可选）：
   ```json
   [
       {
           "name": "我的账号",
           "cookie": "这里填入你复制的完整字符串",
           "proxy": "http://127.0.0.1:7890"
       }
   ]
   ```

## 使用方法

手动运行脚本：
```bash
python mahojin_checkin.py
```

## 免责声明
本工具仅供学习和研究使用。使用本脚本产生的任何后果（如账号封禁等）由使用者自行承担，作者概不负责。
