#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import requests
from seleniumbase import SB

LOGIN_URL = "https://justrunmy.app/id/Account/Login"
DOMAIN    = "justrunmy.app"

# ============================================================
#  环境变量修改部分（仅在此处修改以适配多账号）
# ============================================================
# 这些变量将由 .yml 文件中的 env 映射传入
EMAIL        = os.environ.get("JUSTRUNMY_EMAIL")
PASSWORD     = os.environ.get("JUSTRUNMY_PASSWORD")
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
TG_CHAT_ID   = os.environ.get("TG_CHAT_ID")

if not EMAIL or not PASSWORD:
    print("❌ 致命错误：未找到 JUSTRUNMY_EMAIL 或 JUSTRUNMY_PASSWORD 环境变量！")
    sys.exit(1)

# 全局变量，用于动态保存网页上抓取到的应用名称
DYNAMIC_APP_NAME = "未知应用"

# ============================================================
#  Telegram 推送模块 (保持原版逻辑，仅对应变量名)
# ============================================================
def send_tg_message(status_icon, status_text, time_left):
    if not TG_BOT_TOKEN or not TG_CHAT_ID:
        print("ℹ️ 未配置 TG_BOT_TOKEN 或 TG_CHAT_ID，跳过推送。")
        return

    local_time = time.gmtime(time.time() + 8 * 3600)
    current_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

    message = (
        f"{status_icon} *JustRunMy 自动续期*\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📧 *账号*: `{EMAIL[:3]}***`\n"
        f"📝 *状态*: {status_text}\n"
        f"⏱️ *剩余*: {time_left}\n"
        f"📅 *时间*: {current_time_str}\n"
        f"━━━━━━━━━━━━━━━"
    )
    
    payload = {"chat_id": TG_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage", json=payload)
    except Exception as e:
        print(f"❌ TG 发送失败: {e}")

# ... (此处衔接原版脚本后续的所有 SB 逻辑函数，如 login, reset_timer 等) ...
# 注意：请确保将原版脚本剩余的所有函数内容原封不动粘贴在此处

def main():
    # 原版 main 逻辑，仅将运行的文件名改为 reset_timer.py 即可
    # ...
    # 确保调用的是上方的 EMAIL 和 PASSWORD 变量
    pass

if __name__ == "__main__":
    main()
