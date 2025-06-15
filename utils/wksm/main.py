import os
import subprocess
from google import genai
import smtplib
from email.mime.text import MIMEText

key = os.environ['KEY_SUMMARY']
sha = os.environ['GIT_SHA']
password = os.environ['PASSWORD_REMINDER']
party = os.environ['SENDER_REMINDER']


client = genai.Client(api_key=key)



response = client.models.generate_content(
    model='gemini-2.5-flash-preview-05-20'
    content=''
)


def process_sha(hash):
    return subprocess.check_output(["git", "diff", hash]).decode()
    
def sendEmail()



