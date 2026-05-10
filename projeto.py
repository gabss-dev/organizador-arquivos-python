import os
import shutil

pasta = r"C:\Users\gabri\Downloads"

tipos = {
    ".pdf": "PDFs",
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".mp3": "Musicas",
    ".mp4": "Videos",
    ".zip": "Compactados",
    ".txt": "Documentos"
}

arquivos = os.listdir(pasta)

for arquivo in arquivos:

    nome, extensao = os.path.splitext(arquivo)

    extensao = extensao.lower()

    if extensao in tipos:
        pasta_destino = tipos[extensao]
        caminho_pasta = os.path.join(pasta, pasta_destino)
        os.makedirs(caminho_pasta, exist_ok=True)
        origem = os.path.join(pasta, arquivo)
        destino = os.path.join(caminho_pasta, arquivo)
        shutil.move(origem, destino)
        print(f"{arquivo} movido para {pasta_destino}")
