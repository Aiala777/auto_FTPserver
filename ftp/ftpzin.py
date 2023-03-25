from ftplib import FTP
import ftplib
import time
import schedule
from datetime import date, timedelta, datetime

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


main()




