import os
import subprocess

def gerar_chave():
    return 'sua_nova_chave_aqui'  

def criar_arquivo_criptografado(nome):
    with open(nome, 'w') as f:
        f.write(gerar_chave())

def salvar_chave_em_arquivo():
    criar_arquivo_criptografado('KEY')
    print('Chave de criptografia salva em KEY.key!')

def ler_chave_do_arquivo():
    try:
        with open('KEY', 'r') as f:
            return f.read()
    except FileNotFoundError:
        print('Erro ao carregar chave de criptografia. Gerando uma nova...')
        return gerar_chave()

if __name__ == '__main__':
    salvar_chave_em_arquivo() 
