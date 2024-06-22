# import asyncio
# from ollama import AsyncClient
from translate import Translator
import ollama
from gtts import gTTS
#from io import BytesIO


response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'who fastest animal on the earth? tell me in one sentence',
  },
])
#print(response['message']['content'])

translator = Translator(from_lang="en", to_lang="si")
translation = translator.translate(response['message']['content'])
# print(translation)



#mp3_fp = BytesIO()
tts = gTTS(translation, lang='si')
#tts.write_to_fp(mp3_fp)
tts.save('hello.mp3')


