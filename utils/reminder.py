import smtplib
import os
from email.mime.text import MIMEText


password = os.environ['PASSWORD_REMINDER']
sender = os.environ['SENDER_REMINDER']
recipients = os.environ['RECIPIENTS_REMINDER'].split(',')


msg = MIMEText(
    """
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f9f9ff; color: #1a1a1a; padding: 20px;">
        <p style="font-size: 20px; color: #6a0dad;"><b>Yo Gang 👑🔥</b></p>
        
        <p style="font-size: 18px;">
            <b><u style="color: #ff4500;">Just your daily hype check-in:</u></b> it's 
            <b style="color: #007acc;">LeetCode time</b> 💻⚔️
        </p>
        
        <p style="font-size: 16px; line-height: 1.6;">
            Lock in for <b style="color: #228b22;">15 minutes</b>. Give it your best shot — 
            don`t overthink, just vibe with the code. 🧘‍♂️💭<br>
            If it`s giving <span style="color: #d00000;"><b>final boss energy</b></span>, 
            <u style="color: #ff6347;">no shame in peeking at the solution</u>. <br>
            <b style="color: #ff1493;">Learn, level up, and move on</b> 🧠📈
        </p>
        
        <p style="font-size: 18px;">
            <b style="color: #8a2be2;">You`re built different.</b> <br>
            <b style="color: #1e90ff;">Always have been.</b> <br>
            <span style="text-decoration: underline; color: #ff8c00;"><b>Don`t forget that.</b></span><br>
            Let`s get it 🐐💪
        </p>

        <p style="font-size: 16px;">
            <i style="color: #808080;">Stay legendary,</i><br>
            — Your inner <b><u style="color: #ff1493;">goat</u></b> 🚀
        </p>
    </body>
    </html>
    """,
    "html"
)

msg['Subject'] = '💪🔥 LOCK IN ON THAT LEETCODE GRIND 💪🔥'
msg['From'] = sender
msg['To'] = ', '.join(recipients)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())


