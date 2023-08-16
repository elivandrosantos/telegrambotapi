import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class CriandoEmail():
    def __init__(self):
        pass

    def enviando_email(self):
        # Configurações do servidor de email
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'SEUEMAIL@gmail.com'
        smtp_password = 'SUACHAVE'

        # Informações do email
        from_email = 'SEUEMAIL@gmail.com'
        to_email = 'EMAILQUESERAENVIADO@gmail.com'
        subject = 'Atualização Clientes Bot Telegram'

        # Caminho para o arquivo XLSX gerado
        file_path = 'clientes.xlsx'

        # Crie a mensagem do email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Adicione o corpo do email (opcional)
        body = "Segue planilha atualizada de clientes."
        msg.attach(MIMEText(body, 'plain'))

        # Anexe o arquivo XLSX
        with open(file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype="xlsx")
            attachment.add_header('Content-Disposition', f'attachment; filename={file_path}')
            msg.attach(attachment)

        # Envie o email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
