import smtplib
import email.message
import time
import random
#importação das bibliotecas necessárias para funcionamento do script

def e_mail():
    arquivo= open('mails.txt', 'r') #faz a leitura do arquivo TXT com as informações separadas por :
    email_empresa= []
    nome = []
    #arrays para armanezamento das informações

    for pedacos in arquivo:
        teste=pedacos.split(':') #separação do e-mail e nome do contato
        email_empresa.append(teste[0]) #inserção das informações no array 
        nome.append(teste[1]) #inserção das informações no array 
        print(teste[0],teste[1]) #Print das informações coletadas


    for n in range(len(nome)):
        print(email_empresa[n]) #Printar e-mail que está sendo enviado
        to_email = str(email_empresa[n]) #Variável responsável para o envio do e-mail


        pausa_envio = random.randrange(2, 7, 1) #Randomização para envio do e-mail nos tempos espaçados para evitar SPAM.
        
        time.sleep(pausa_envio) #Pausa dos Segundos Randomizados


        texto = """
<p>Acesse: guiaanonima.com</p>
<p>Aqui vai o HTML do que você quer enviar no corpo do texto</p>
    """

        subject= "Oi "+str(nome[n])+"..." #Assunto do e-mail, nesse caso, dá pra personalizar com Nome ou até E-mail.


        msg = email.message.Message() #Configuração da biblioteca na variável msg
        msg['Disposition-Notification-To'] = 'penegui@guiaanonima.com' #configuração do recebimento de notificação caso o destinatário abra a mensagem
        msg['Disposition-Notification-To'] = '"From" <penegui@guiaanonima.com>' #configuração do recebimento de notificação caso o destinatário abra a mensagem
        msg['Subject'] = subject

        msg['From'] = 'seuemail@email.com' #configuração do SEU e-mail, e-mail que irá ENVIAR
        msg['To'] = to_email #Para quem vai
        password = "sua_senha" #Senha do seu e-mail para AUTENTICAR no servidor
        msg.add_header('Content-Type', 'text/html') #configuração para envio de HTML
        msg.set_payload(texto) #Configuração do Texto - corpo do e-mail - na requisição

        s = smtplib.SMTP('smtp.seuServidor.com:587') #Seu Servidor SMTP : Porta SMTP do seu Server
        s.starttls() #inicialização do SSL/TLS para criptografia do e-mail

        s.login(msg['From'], password) #Login no servidor

        s.sendmail(msg['From'], [msg['To']], msg.as_string()) #Envio do e-mail
        


e_mail()
