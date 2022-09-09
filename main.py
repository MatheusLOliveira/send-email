from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'MEU_EMAIL'
minha_senha = 'MINHA_SENHA'

email_destinatario = 'EMAIL_DO_DESTINATARIO'

nome_remetente = 'MEU_NOME'
de_remetente = 'FROM'
assunto = 'SUBJECT'

nome_imagem = 'example.png'

#  ENVIO DO TEXTO POR HTML
with open('template.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome= nome_remetente, data=data_atual)

msg = MIMEMultipart()
msg['from'] = de_remetente  
msg['to'] = email_destinatario  # Cliente
msg['subject'] = assunto

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

#  ENVIO DE IMAGEM EM ANEXO
with open(nome_imagem, 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
