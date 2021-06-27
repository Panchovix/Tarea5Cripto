import imaplib
import re
from contextlib import redirect_stdout

#datos
host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)
imap.login('correo', 'contraseña')
imap.select('Inbox')
_, x = imap.search(None,'FROM', 'paratodos@tenpo.cl')

#get msg id
def getMsgID(x):
    a = 0
    for num in x[0].split():
        if a == 40:
            break
        _, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        datito= data[0][1].decode()
        datito=datito.replace("Message-ID:", "")
        datito=datito.replace(">", "")
        datito=datito.replace("<", "")
        datito=datito.replace("Message-Id:", "")
        datito=datito.strip()
        print(datito)
        a += 1
        with open('MsgIDsTenpo.txt', 'a') as f: #se crea el archivo de texto con el data set
            with redirect_stdout(f):
                print(datito)
#first and second last received
def getSecondLastReceived(x):
    a = 0
    for num in x[0].split():
        if a == 40:
            break
        _, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') 
        datito2= data[0][1].decode()                                       
        datito2=datito2.replace("Message-ID:", "")
        datito2=datito2.replace(">", "")
        datito2=datito2.replace("<", "")
        datito2=datito2.replace("Message-Id:", "")
        datito2 = datito2.split("Received")
        print("Received" + datito2[2]) #penultimo received
        a += 1
        with open('SecondLastReceivedTenpo.txt', 'a') as f: #se crea el archivo de texto con el data set
            with redirect_stdout(f):
                print("Received" + datito2[2])
        
def getFirstReceived(x):
    a = 0
    for num in x[0].split():
        if a == 40:
            break
        _, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') 
        datito2= data[0][1].decode()                                       
        datito2=datito2.replace("Message-ID:", "")
        datito2=datito2.replace(">", "")
        datito2=datito2.replace("<", "")
        datito2=datito2.replace("Message-Id:", "")
        datito2 = datito2.split("Received")
        print("Received" + datito2[len(datito2) - 1]) #primer received
        a += 1
        with open('FirstReceivedTenpo.txt', 'a') as f: #se crea el archivo de texto con el data set
            with redirect_stdout(f):
                print("Received" + datito2[len(datito2) - 1])       
# get utc
def getUTC(x):
    a = 0
    for num in x[0].split():
        if a == 40:
            break
        _, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])') 
        datito3= data[0][1].decode()
        datito3=datito3.replace("Message-ID:", "")
        datito3=datito3.replace(">", "")
        datito3=datito3.replace("<", "")
        datito3=datito3.replace("Message-Id:", "")
        datito3=datito3.split("Received")
        d3=datito3[len(datito3) - 1] #1st recibido
        d33 = str(d3[-15:])
        a += 1
        with open('UTCsTenpo.txt', 'a') as f: #se crea el archivo de texto con el data set
            with redirect_stdout(f):
                print (d33)
# get from
def getFrom(x):
    a = 0
    for num in x[0].split():
        if a == 40:
            break
        _, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])') #From
        datito4= data[0][1].decode()
        datito4=datito4.replace("Message-ID:", "")
        datito4=datito4.replace(">", "")
        datito4=datito4.replace("<", "")
        datito4=datito4.replace("Message-Id:", "")
        datito4=datito4.strip()
        print(datito4)
        a += 1
        with open('MailsTenpo.txt', 'a') as f: #se crea el archivo de texto con el data set
            with redirect_stdout(f):
                print(datito4)           

getMsgID(x)
getFirstReceived(x)
getSecondLastReceived(x)
getUTC(x)
getFrom(x)
imap.close()