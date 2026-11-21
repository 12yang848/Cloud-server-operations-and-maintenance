import psutil
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# ================= 配置区 =================
SENDER_EMAIL = "3431612260@qq.com"      # 你的发件 QQ 邮箱
AUTH_CODE = "cmkvjpyanxjrcifb"                 # 刚才拿到的授权码（注意不要带空格）
RECEIVER_EMAIL = "3431612260@qq.com"    # 接收告警的邮箱（可以填同一个）

CPU_THRESHOLD = 80.0
MEM_THRESHOLD = 80.0
DISK_THRESHOLD = 90.0
# ==========================================

def send_email_alert(message):
    """发送邮件告警"""
    # 邮件内容设置
    mail_msg = MIMEText(message, 'plain', 'utf-8')
    mail_msg['Subject'] = Header('⚠️ 服务器监控告警', 'utf-8')
    mail_msg['From'] = SENDER_EMAIL
    mail_msg['To'] = RECEIVER_EMAIL

    try:
        # 使用 SSL 加密连接 QQ 邮箱的 SMTP 服务器
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(SENDER_EMAIL, AUTH_CODE)
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], mail_msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败: {e}")

def check_system():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alerts = []

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"CPU 使用率过高: {cpu_usage}%")

    mem = psutil.virtual_memory()
    if mem.percent > MEM_THRESHOLD:
        alerts.append(f"内存使用率过高: {mem.percent}%")

    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"磁盘使用率过高: {disk.percent}%")

    if alerts:
        alert_message = f"时间: {current_time}\n\n" + "\n".join(alerts)
        
        # 1. 写入本地日志
        with open("/root/server_alerts.log", "a", encoding="utf-8") as f:
            f.write(f"[{current_time}]\n" + "\n".join(alerts) + f"\n{'-'*30}\n")
            
        # 2. 发送邮件告警
        send_email_alert(alert_message)
        print(f"[{current_time}] 发现异常，已尝试发送邮件！")
    else:
        print(f"[{current_time}] 系统运行正常。CPU: {cpu_usage}% | 内存: {mem.percent}% | 磁盘: {disk.percent}%")

if __name__ == "__main__":
    check_system()