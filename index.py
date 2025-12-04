import os
import pyautogui
import threading
from pynput import mouse
import time
import sys
from cryptography.fernet import Fernet


CHAVE_CRIPTO = 'sua_chave_de_criptografia_aqui' 

def gerar_chave():
    return os.urandom(32).hex()  

def criptografar_arquivo(nome_arquivo, chave):
    f = Fernet(chave)
    with open(nome_arquivo, 'wb') as f_out:
        f.encrypt(open(nome_arquivo, 'rb').read())
        f_out.write(f.encrypt(open(nome_arquivo, 'rb').read()))

def descriptografar_arquivo(chave, nome_arquivo):
    f = Fernet(chave)
    with open(nome_arquivo, 'wb') as f_in:
        data = f.decrypt(open(nome_arquivo, 'rb').read())
        f_in.write(data)

def criar_pasta_temp():
    os.makedirs('temp', exist_ok=True)  # Cria a pasta temporária se ela não existir

def inicializar_spoofer():
    global CHAVE_CRIPTO, KEY_FILE

    if not os.path.isfile('KEY'):
        CHAVE_CRIPTO = gerar_chave()
        cria_arquivo_criptografado()
        print(f'Chave de criptografia gerada: {CHAVE_CRIPTO}')

   
    try:
        with open('KEY', 'r') as f_key:
            CHAVE_CRIPTO = f_key.read()
    except FileNotFoundError:
        print('Erro ao carregar chave de criptografia. Gerando uma nova...')
        CHAVE_CRIPTO = gerar_chave()
        cria_arquivo_criptografado()

    KEY_FILE = 'KEY'  

def criar_arquivo_criptografado():
    nome_arquivo = CHAVE_CRIPTO + '.key'
    cryptografar_arquivo(nome_arquivo, CHAVE_CRIPTO)
    print(f'Arquivo de chave criptografado salvo como {nome_arquivo}')

def monitorar_mouse():
    while True:
        x, y = pyautogui.position()
        with open('mouse_pos.txt', 'a') as f:
            f.write(f'{x}, {y}\n')
        time.sleep(0.1)

def executar_spoofer():
    
    print('Spoofer iniciado!')

if __name__ == '__main__':
    inicializar_spoofer()
    criar_pasta_temp()
    threading.Thread(target=monitorar_mouse).start()
    executar_spoofer()
