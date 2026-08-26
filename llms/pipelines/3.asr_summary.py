from transformers import pipeline
from transformers import logging

logging.set_verbosity_error()

# Load the pipeline with the Whisper model
asr = pipeline("automatic-speech-recognition",
               model="openai/whisper-base.en", 
               device_map='auto')

# Path to your audio file (.wav or .mp3)
audio_path = "./pipelines/mlk_speech.mp3"   

# Transcribe the audio
result = asr(audio_path, return_timestamps = True)

# Print the transcription
#print("Transcription:", result["text"] )

prompt  = f"Summarize the following in 3 sentenses: \n {result['text']}"

# Summarise that speech 
summarize = pipeline("text-generation", 
                     model="Qwen/Qwen2.5-3B-Instruct", 
                     device_map = 'auto')
summary = summarize(prompt, return_full_text = False)  
print(summary[0]["generated_text"])

