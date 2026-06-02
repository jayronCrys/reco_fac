import cv2
import os
import numpy as np

# Inicializar o reconhecedor
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def buscar_imagens_e_ids():
    caminhos_imagens = [os.path.join('banco_faces', f) for f in os.listdir('banco_faces')]
    faces = []
    ids = []

    for caminho in caminhos_imagens:
        # Carrega a imagem em modo escala de cinza pra economizar processamento
        imagem_face = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
        
        # Extrai o id e o nome do arquivo ss tiver
        id_usuario = int(os.path.split(caminho)[-1].split(".")[1])
        
        faces.append(imagem_face)
        ids.append(id_usuario)
        
    return faces, np.array(ids)

print("Treinando sistema...")
rostos, lista_ids = buscar_imagens_e_ids()

# Treinar o modelo com as fotos e seus ids
reconhecedor.train(rostos, lista_ids)

# Salvar o arquivon treinado
reconhecedor.write('classificadorLBPH.yml')
print("Treinamento finalizado 'classificadorLBPH.yml' gerado.")

