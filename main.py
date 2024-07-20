import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microphone() as source:
    # Ajuste para o ruído ambiente
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source)  # Define o microfone como fonte de áudio

    try:
        # Reconhece o áudio usando o Google
        texto_reconhecido = r.recognize_google(audio, language='pt-BR')
        print("Texto reconhecido:", texto_reconhecido)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro na solicitação ao Google: {e}")
