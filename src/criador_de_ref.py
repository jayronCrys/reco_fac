import cv2

# Dicionário para mapear os ids para nomes baseado nos ids passados no nomeio daz imgs usadas para treino
Nome = "nome"
nomes = {
    1: Nome
} #pode ter mais ids dependendo de quantos ids foram repassados no treino, caso houver um id que não corresponda a nenhum tipo ds imagem
#o reconhecimento simplesmente nunca terá match

reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read('classificadorLBPH.yml')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)

#abre a câmera para vídeo e captura todos os frames como foto para fazer reconhecimento 
while True:
    sucesso, frame = video.read()
    if not sucesso:
        break

    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = face_cascade.detectMultiScale(frame_cinza, 1.3, 5)

    for (x, y, largura, altura) in rostos:
        rosto_recortado = frame_cinza[y:y + altura, x:x + largura]
        rosto_redimensionado = cv2.resize(rosto_recortado, (220, 220))

        # O modelo tenta prever de quem é o rosto
        id_previsto, confianca = reconhecedor.predict(rosto_redimensionado)

        # Retorna um acerto para confianca menor que 65
        if confianca < 65:
            nome_usuario = nomes.get(id_previsto, "Desconhecido")
            cor_caixa = (0, 255, 0) # Verde para conhecido
        else:
            nome_usuario = "Desconhecido"
            cor_caixa = (0, 0, 255) # Vermelho para desconhecido

        texto_tela = f"{nome_usuario} ({round(100 - confianca)}%)"

        cv2.rectangle(frame, (x, y), (x + largura, y + altura), cor_caixa, 2)
        cv2.putText(frame, texto_tela, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor_caixa, 2)

    cv2.imshow("Sistema de Reconhecimento Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()