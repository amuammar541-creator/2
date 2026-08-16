import subprocess
import sys
import os
import time
import signal

def run_process(command, name):
    """تشغيل عملية منفصلة تمامًا ومراقبتها"""
    print(f"🔄 Starting {name}...")
    # start_new_session=True يجعل العملية مستقلة تمامًا عن العملية الأم
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
        text=True
    )
    print(f"✅ {name} started with PID: {process.pid}")
    return process

if __name__ == "__main__":
    print("🚀 Starting System...")
    
    # 1. تشغيل البوت الرئيسي (Telegram/WhatsApp Extractor)
    bot_process = run_process("python -m app.main", "Main Bot")
    
    # 2. تشغيل الوكيل الذكي (AI Agent)
    agent_process = run_process("python ai_engineer_agent/main.py", "AI Agent")
    
    # 3. حلقة لانهائية للحفاظ على تشغيل السكربت ومراقبة العمليات
    try:
        while True:
            time.sleep(10)
            
            # التحقق من أن البوت ما زال يعمل
            if bot_process.poll() is not None:
                print("⚠️ Main Bot stopped! Restarting...")
                bot_process = run_process("python -m app.main", "Main Bot")
            
            # التحقق من أن الوكيل ما زال يعمل
            if agent_process.poll() is not None:
                print("⚠️ AI Agent stopped! Restarting...")
                agent_process = run_process("python ai_engineer_agent/main.py", "AI Agent")
                
    except KeyboardInterrupt:
        print("🛑 Shutting down...")
        if bot_process.poll() is None:
            bot_process.terminate()
        if agent_process.poll() is None:
            agent_process.terminate()
        sys.exit(0)
