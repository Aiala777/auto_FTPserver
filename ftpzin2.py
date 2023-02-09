from ftplib import FTP
from datetime import date, timedelta, datetime
import os, gzip, shutil
import schedule
import time
# import TkInter, tkFileDialog



today = datetime.now().strftime("%Y%m%d")
hora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

#nome do dominio e login:
ftp = FTP('ftp.slisystem.com.br')
ftp.login(user='Eficaz', passwd = 'EfiC@zVinte21')


# movendo os arquivos tentando 4x
# def movendo():
#         tentativas = 0 
#         while tentativas < 4:
#             try:
#                 mover()
#                 tentativas += 1
#             except OSError as error:
#                 time.sleep(10)
#                 print('Tentando mover novamente')
#                 mover()
#         hora2 = datetime.now().strftime("%H:%M:%S")
#         print('Arquivos Movidos', hora2)
#         print('------------------------------------------------')  


# # variavel com nome modificado com a data do dia atual):
# jovem = (today+'All.txt')

#funções com suas respectivas carteiras, (cwd) = mudar o diretorio/ 
def ativos_sa ():
    print('Conectando...')
    print('Conectado.')
    print('Iniciando', hora)
    ftp.cwd('/Ativos_SA/Outbound')  
    # os.chdir
    with open('Telefones_Alteracao_Ativos SA_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Ativos SA_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Ativos SA_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Ativos SA_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Ativos SA_'+today+'_All.txt',fp.write)
        ftp.close()
        shutil.move('Telefones_Alteracao_Ativos SA_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def Digio ():
    ftp.cwd('/Digio/Outbound')  
    with open('Telefones_Alteracao_Digio_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Digio_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Digio_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Digio_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Digio_'+today+'_All.txt',fp.write)     
        shutil.move('Telefones_Alteracao_Digio_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
   
            
def HoepersAgibank ():
    ftp.cwd('/Hoepers_-_Agibank/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Agibank_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Agibank_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Agibank_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Hoepers - Agibank_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Agibank_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Agibank_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def Hoeperscybelar ():
    ftp.cwd('/Hoepers_-_Cybelar/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Cybelar_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Cybelar_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Cybelar_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Hoepers - Cybelar_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Cybelar_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Cybelar_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def Hoepersestacio ():
    ftp.cwd('/Hoepers_-_Faculdade_Estacio_de_Sa/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Faculdade Estacio de Sa_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Faculdade Estacio de Sa_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Faculdade Estacio de Sa_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Hoepers - Faculdade Estacio de Sa_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Faculdade Estacio de Sa_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Faculdade Estacio de Sa_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def HoepersSalfer ():
    ftp.cwd('/Hoepers_-_Salfer/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Salfer_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Salfer_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Salfer_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Hoepers - Salfer_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Salfer_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Salfer_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def HoepersSemear():
    ftp.cwd('/Hoepers_-_Semear/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Semear_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Semear_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Semear_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Hoepers - Semear_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Semear_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Semear_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def HoepersSemear3 ():
    ftp.cwd('/Hoepers_-_Semear_III/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Semear III_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Semear III_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Semear III_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Hoepers - Semear III_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Semear III_'+today+'_All.txt',fp.write)  
        shutil.move('Telefones_Alteracao_Hoepers - Semear III_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')     


def HoepersSemear4 (): 
    ftp.cwd('/Hoepers_-_Semear_IV/Outbound')  
    with open('Telefones_Alteracao_Hoepers - Semear IV_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Semear IV_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Semear IV_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos') 
    with open('Telefones_Alteracao_Hoepers - Semear IV_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Hoepers - Semear IV_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Hoepers - Semear IV_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')         


def Pefisa():
    ftp.cwd('/Pernambucanas/Outbound')  
    with open('Telefones_Alteracao_Pernambucanas_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Pernambucanas_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Pernambucanas_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Pernambucanas_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Pernambucanas_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Pernambucanas_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def Return():
    ftp.cwd('/Return/Outbound')  
    with open('Telefones_Alteracao_Return_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Return_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Return_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Return_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Return_'+today+'_All.txt',fp.write)
        shutil.move('Telefones_Alteracao_Return_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')



def TimConsumer (): 
    ftp.cwd('/Tim_-_Consumer/Outbound')  
    with open('Telefones_Alteracao_Tim - Consumer_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Tim - Consumer_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Tim - Consumer_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')
    with open('Telefones_Alteracao_Tim - Consumer_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Tim - Consumer_'+today+'_All.txt',fp.write) 
        shutil.move('Telefones_Alteracao_Tim - Consumer_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')


def TimCorporate():      
    ftp.cwd('/Tim_-_Corporate/Outbound')  
    with open('Telefones_Alteracao_Tim - Corporate_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Tim - Corporate_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Tim - Corporate_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')  
    with open('Telefones_Alteracao_Tim - Corporate_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Tim - Corporate_'+today+'_All.txt',fp.write)   
        shutil.move('Telefones_Alteracao_Tim - Corporate_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')   


def TimLive ():    
    ftp.cwd('/Tim_-_Live/Outbound')  
    with open('Telefones_Alteracao_Tim - Live_'+today+'_11.txt', 'wb') as fp:
        ftp.retrbinary('RETR Telefones_Alteracao_Tim - Live_'+today+'_11.txt',fp.write)
        shutil.move('Telefones_Alteracao_Tim - Live_'+today+'_11.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')   
    with open('Telefones_Alteracao_Tim - Live_'+today+'_All.txt', 'wb') as fp: 
        ftp.retrbinary('RETR Telefones_Alteracao_Tim - Live_'+today+'_All.txt',fp.write)   
        shutil.move('Telefones_Alteracao_Tim - Live_'+today+'_All.txt', 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos')   
    ftp.close()
    print('ftp sucesso') 
  

# def mover():
#     root_old = 'C:/Users/arthuraiala/Desktop/ftp/poggerzin'
#     root_new = 'Z:/_PLANEJAMENTO/MIS/WKS/WksRecebidos'
#     file_names = os.listdir(root_old)
#     for file_name in file_names:
#       shutil.move(os.path.join(root_old, file_name), root_new)
#     # files = ftp.dir('C:/Users/arthuraiala/Desktop/ftp')
#     # for i, file in enumerate(files):
#     #     if file and file.startswith(jovem):
#     #         ftp.get(f'C:/Users/arthuraiala/Desktop/ftp/ftpzada/{file}', f'Q:/_PLANEJAMENTO/MIS/WKS/WksRecebidos/{file}')

 
# Testar caso o mover não de certo
# shutil.copytree('path_to/start/folder', 'path_to/destination/folder', dirs_exist_ok=True) 


#'chamando' as funções
def biruleibe():
    ativos_sa()
    Digio()
    HoepersAgibank()
    Hoeperscybelar()
    Hoepersestacio()
    HoepersSalfer()
    HoepersSemear()
    HoepersSemear3()
    HoepersSemear4()
    Pefisa()
    Return()
    TimConsumer()
    TimCorporate()
    TimLive()
    

schedule.every().day.at("07:30").do(biruleibe)

while True:
  schedule.run_pending()

# biruleibe()

