from cryptography.fernet import Fernet 
import os

def Carregar_Chave():
    return open("chave.key", "rb").read()

def Descriptografar_Arquivo(Arquivo, Chave):
    f = Fernet(Chave)
    with open(Arquivo, "rb") as File: 
        Dados = File.read()
        Dados_Descriptografados = f.decrypt(Dados)
    with open(Arquivo, "wb") as File: 
        File.write(Dados_Descriptografados)

def Encontrar_Arquivos(Diretorio):
    Lista = []
    for Raiz, _, Arquivos in os.walk(Diretorio):
        for Nome in Arquivos: 
            Caminho = os.path.join(Raiz, Nome)
            if Nome != "ransoware.py" and not Nome.endswith(".key"):
                Lista.append(Caminho)
    return Lista

def main(): 
    Chave = Carregar_Chave()
    Arquivos = Encontrar_Arquivos("test_files")
    for Arquivo in Arquivos: 
        Descriptografar_Arquivo(Arquivo, Chave)
    print("Arquivos restaurados com sucesso!")

if __name__ == "__main__":
    main()