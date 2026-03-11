import whisper

model = whisper.load_model("small")

result = model.transcribe(record_file, fp16=False, language=language)
transcription = result["text"]
print(transcription)
