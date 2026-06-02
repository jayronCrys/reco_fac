
import cv2
import os

def capturar_da_webcam():
    # Criar pasta para salvar as fotos se ela não existir
    if not os.path.exists('banco_faces'):
        os.makedirs('banco_faces')

    video = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    id_usuario = 1
    amostra = 1
    numero_max_amostras = 30

    print("Olhe para a câmera. Capturando fotos...")
    
    while True:
        sucesso, frame = video.read()
        if not sucesso:
            break

        frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostos = face_cascade.detectMultiScale(frame_cinza, 1.3, 5)

        for (x, y, largura, altura) in rostos:
            rosto_recortado = frame_cinza[y:y + altura, x:x + largura]
            rosto_redimensionado = cv2.resize(rosto_recortado, (220, 220))

            caminho_foto = f"banco_faces/usuario.{id_usuario}.{amostra}.jpg"
            cv2.imwrite(caminho_foto, rosto_redimensionado)
            print(f" Foto {amostra} salva com sucesso!")

            cv2.rectangle(frame, (x, y), (x + largura, y + altura), (0, 255, 0), 2)
            amostra += 1

        cv2.imshow("Cadastrando Rosto", frame)
        cv2.waitKey(100)

        if amostra > numero_max_amostras or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Cadastro concluído!")
    video.release()
    cv2.destroyAllWindows()

# Isso garante que se você rodar esse arquivo sozinho ele ainda funciona
if __name__ == "__main__":
    capturar_da_webcam()
