import smtplib
import json
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # porta de SMTP (587 é comum para TLS)

# Informações de login
email_login = 'EMAIL_INFO'
senha = 'PASSWORD_INFO'

# Destinatário e remetente
remetente = email_login

with open('amigos.json', 'r', encoding='utf-8') as arquivo:
    # Carregando os dados do arquivo JSON
    dados = json.load(arquivo)

emails = []

for i in dados:
    emails.append(i['email'])


random.shuffle(emails)

for i in range(len(emails)):
    destinatario = emails[i]
    for j in dados:
        if j['email'] == emails[(i + 1) % len(emails)]:
            nome = j['nome']
            gostos = j['gostos']
            break
    
    for k in dados:
        if k['email'] == emails[i]:
            nome2 = k['nome']
            gostos2 = k['gostos']
            break

    # Criando o objeto do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Amigo Secreto da Vila'
  

    # Corpo do e-mail
    corpo = f" Ola, {nome2}, voce foi convocado(a) para o amigo barra da Vila da folha. \n \n Leve a barra que {nome} gosta. Para te ajudar, ele(a) gosta de: {gostos}. \n \n Lembre de n comentar na call viu carai?! 'AI Q N SEI ONDE É, N VOU'. \n Condominio Mar Mediterraneo, mais conhecido como Casa da Tia Polly. \n Seja feliz e coma chocolate. \n Essa mensagem foi gerada automaticamente e foi enviada para todos os 9 participantes com seus devidos amigos secretos \n"



    msg.attach(MIMEText(corpo, 'plain'))

    # Conectando-se ao servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_login, senha)

    # Enviando o e-mail
    server.sendmail(remetente, destinatario, msg.as_string())

    # Encerrando a conexão com o servidor
    server.quit()

    print(emails[i] + ' - E-mail enviado com sucesso!')