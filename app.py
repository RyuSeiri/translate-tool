import translators
# target text
text = "Hello, world!"
# language 
target_language = "ja"

translated_text = translators.translate_text_google(text, target_language)
print(translated_text)

translated_text = translators.translate_text_microsoft(text, target_language)
print(translated_text)

translated_text = translators.translate_text_ibm(text, target_language)
print(translated_text)

translated_text = translators.translate_text_baidu(text, target_language)
print(translated_text)
