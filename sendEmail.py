import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = ''
pw = ''

to_addr1 = ''
to_addr2 = ''


#msg = MIMEText('hello, Meng Yang', 'plain', 'utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr('bin chen <%s>' % from_addr)
msg['To'] = _format_addr('admin <%s>' % to_addr2)
msg['Subject'] = Header('Data From Ju Mei', 'utf-8').encode()

msg.attach(MIMEText('send with file', 'plain', 'utf-8'))

#with open('/Users/binchen/dev/jumei/data/JuMei.xls', 'rb') as f:

with open('/home/eric/dev/jumei/JuMei.xls', 'rb') as f:
    mime = MIMEBase('xls', 'xls', filename='JuMei.xls')

    mime.add_header('Content-Disposition', 'attachment', filename='JuMeil.xls')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    mime.set_payload(f.read())

    encoders.encode_base64(mime)

    msg.attach(mime)

stmp_server = 'smtp.163.com'

server = smtplib.SMTP(stmp_server,25)
server.set_debuglevel(1)
server.login(from_addr,pw)
server.sendmail(from_addr,[to_addr1,to_addr2], msg.as_string())
server.quit()

