from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'zhaozexinhuli@163.com'
    receivers = ['yuxuan.zhang@thoughtworks.com', 'zexin.zhao@thoughtworks.com']
    message = MIMEText('用Python发送邮件.', 'plain', 'utf-8')
    message['From'] = Header('shuaige', 'utf-8')
    message['To'] = Header('dog', 'utf-8')
    message['Subject'] = Header('just a kidding', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'zzx534218')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()