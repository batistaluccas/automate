import os
import fitz  # PyMuPDF
from PIL import Image


#pip install Pillow PyMuPDF

# ---------------------------------------------------------------------
# 🟩 CAMINHO BASE: Onde estão as pastas dos itens (cada uma com o PDF e os TIFFs).
# Por padrão, usamos o caminho onde o script está. Se quiser, substitua pelo caminho fixo:
# Exemplo: BASE_DIR = r"C:\Users\SeuUsuario\Desktop\PastaDosArquivos"
# ---------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def is_tiff(file):
    # Verifica se o arquivo é TIFF
    return file.lower().endswith(('.tif', '.tiff'))

def encontrar_tiffs(pasta_item):
    # Procura todos os arquivos TIFF em subpastas (recursivo)
    tiff_paths = []
    for root, dirs, files in os.walk(pasta_item):
        for file in files:
            if is_tiff(file):
                tiff_paths.append(os.path.join(root, file))
    return sorted(tiff_paths)  # Retorna em ordem alfabética

def criar_pdf_final(caminho_pdf, tiff_paths, output_path):
    # Cria o PDF final com o PDF principal + TIFFs rotacionados
    doc = fitz.open(caminho_pdf)  # Começa com o PDF original

    for tiff_file in tiff_paths:
        img = Image.open(tiff_file).convert("RGB")
        
        # 🔁 ROTACIONA A IMAGEM EM 180 GRAUS (posição correta)
        img = img.rotate(180, expand=True)

        img_pdf = fitz.open()
        rect = fitz.Rect(0, 0, *img.size)
        page = img_pdf.new_page(width=rect.width, height=rect.height)

        # Insere a imagem como página no PDF
        img_bytes = img.tobytes("jpeg", "RGB")
        page.insert_image(rect, stream=img_bytes)

        # Adiciona a imagem ao PDF final
        doc.insert_pdf(img_pdf)

    doc.save(output_path)
    doc.close()

def processar_itens():
    # Percorre todas as pastas dentro da pasta base
    for nome_pasta in os.listdir(BASE_DIR):
        pasta_item = os.path.join(BASE_DIR, nome_pasta)

        if not os.path.isdir(pasta_item):
            continue  # Ignora se não for pasta

        # 🟥 AJUSTE IMPORTANTE:
        # O nome do PDF principal deve seguir o padrão: _12345.pdf (com underline e mesmo nome da pasta)
        nome_pdf = f"_{nome_pasta}.pdf"
        caminho_pdf = os.path.join(pasta_item, nome_pdf)

        if not os.path.isfile(caminho_pdf):
            print(f"[!] PDF principal não encontrado: {caminho_pdf}")
            continue

        # Busca os arquivos TIFF dentro da pasta (e subpastas)
        tiff_paths = encontrar_tiffs(pasta_item)

        if not tiff_paths:
            print(f"[!] Nenhum TIFF encontrado em: {nome_pasta}")
            continue

        # 🟦 PDF FINAL: será salvo na pasta onde está o script, com sufixo "_final.pdf"
        nome_pdf_final = f"{nome_pasta}_final.pdf"
        destino_pdf_final = os.path.join(BASE_DIR, nome_pdf_final)

        criar_pdf_final(caminho_pdf, tiff_paths, destino_pdf_final)

        print(f"[✔] PDF final criado: {nome_pdf_final}")

# 🔁 Executa o script
if __name__ == "__main__":
    processar_itens()