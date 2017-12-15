import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders

_user = "734887251@qq.com"
_pwd  = "szkrbtvolfaabehb"
_to   = "8613296489829@kindle.cn"

def send_email():
	path = r'G:\python\zhihu\ribao\content'
	for file in os.listdir(path):
		file_path = os.path.join(path,file)
		msg = MIMEMultipart()
		msg['Subject'] = 'convert' #邮件标题
		msg['From'] = _user	#显示发件人
		msg['To'] = _to	#接收邮箱
		attfile = file_path
		basename = os.path.basename(file_path) 
		print(basename)
	# fp = open(attfile,'rb')
	# att = MIMEText(fp.read(),'base64','gbk')
	# att['Content-Type'] = 'application/octer-stream'
	# att.add_header('Content-Disposition', 'attachment',filename=('gbk', '', basename))
	# encoders.encode_base64(att)
	# msg.attach(att)
	# s = smtplib.SMTP_SSL("smtp.qq.com", 465,timeout = 30)#连接smtp邮件服务器,端口默认是25
	# s.login(_user, _pwd)#登陆服务器
	# s.sendmail(_user, _to, msg.as_string())#发送邮件
	# s.close()

# if __name__ == '__main__':
# 	send_email()