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
        # escala de cinza
        imagem_completa = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
        
        id_usuario = int(os.path.split(caminho)[-1].split(".")[1])

        # busca os rostos na imagem
        faces_detectadas = face_cascade.detectMultiScale(imagem_completa, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, largura, altura) in faces_detectadas:
            # Recorta a imagem para pegar APENAS a região do rosto
            rosto_recortado = imagem_completa[y:y+altura, x:x+largura]
            
            # Adiciona o recorte nas listas
            faces.append(rosto_recortado)
            ids.append(id_usuario)

    return faces, np.array(ids)

print("Treinando sistema...")
rostos, lista_ids = buscar_imagens_e_ids()

# Treinar o modelo com as fotos e seus ids
reconhecedor.train(rostos, lista_ids)

# Salvar o arquivon treinado
reconhecedor.write('classificadorLBPH.yml')
print("Treinamento finalizado 'classificadorLBPH.yml' gerado.")