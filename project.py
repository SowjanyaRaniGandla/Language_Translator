from googletrans import Translator

file_name=input("enter input file...")
trans_lang=input("enter translation language")
dest=trans_lang.capitalize()
#print(dest)
file_name=open(file_name,'r')
data=file_name.read()

languages={
    'Telugu' : 'te',
    'Japanese' : 'ja',
    'Russian' : 'ru',
    'Italian' : 'it',
    'Latin' : 'la',
    'Hindi' : 'hi',
    'Arabic' : 'ar',
    'Greek' : 'el',
    'Korean' : 'ko',
    'Urdu' : 'ur',
    'Gujarati' : 'gu',
    'French':'fr',
    'Bulgarian' : 'bg',
    'Chinese' : 'zh-CN',
    'Irish' : 'ga',
    'German' : 'de',
    'Indonesian' : 'id',
    'Lao' : 'lo',
    'Marathi' : 'mr',
    'Persian' : 'fa',
    'Sindhi': 'sd',
    'Spanish' : 'es',
    'Zulu':'zu'

}
output_lang=languages[dest]
translator=Translator()


#for key,value in languages.items() :
print(translator.translate(data,dest=output_lang).text)
print("Input data is in ",translator.detect(data),"...")



