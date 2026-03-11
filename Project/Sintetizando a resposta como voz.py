from gtts import  gTTS

gtts_object = gTTS(text=chatgpt_response, lang=language, slow=False)

response_audio = "/content/response_audio.wav"
gtts_object.save(response_audio)

display(Audio(response_audio, autoplay=True))
