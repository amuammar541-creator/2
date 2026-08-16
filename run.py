import subprocess
import sys
import os
import time

# تشغيل البوت الرئيسي
print("🔄 Starting Telegram Bot...")
bot_process = subprocess.Popen([sys.executable, "-m", "app.main"])
print(f"✅ Bot started (PID: {bot_process.pid})")

# تشغيل الوكيل الذكي
print("🔄 Starting AI Agent...")
agent_process = subprocess.Popen([sys.executable, "ai_engineer_agent/main.py"])
print(f"✅ Agent started (PID: {agent_process.pid})")

# انتظار انتهاء العمليات (حتى لا يتوقف السكربت)
try:
    bot_process.wait()
    agent_process.wait()
except KeyboardInterrupt:
    bot_process.terminate()
    agent_process.terminate()
