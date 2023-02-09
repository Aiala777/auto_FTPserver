from ftplib import FTP
import ftplib
import time
import schedule
from datetime import date, timedelta, datetime
import os

def main():
    esterday = (date.today() - timedelta(days=0)).strftime('%d.%m')
    today = datetime.now().strftime("%Y%m%d")
    hora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    print('iniciando', hora)

    HOSTNAME = "ftp.slisystem.com.br"
    USERNAME = "Eficaz"
    PASSWORD = "EfiC@zVinte21"
    PORT = 990

    print('connecting..')
    
    #conectar com ftp server
    ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD, PORT)
    
    # força a codificação UTF-8
    ftp_server.encoding = "utf-8"

    print('Conectado...')

    

    


    caminho = "C://Users/Python/Downloads"
lista_arquivos = os.listdir(caminho)

lista_datas = []
for arquivo in lista_arquivos:
    # descobrir a data desse arquivo
    if ".xlsx" in arquivo:
        data = os.path.getmtime(f"{caminho}/{arquivo}")
        lista_datas.append((data, arquivo))
    


main()




