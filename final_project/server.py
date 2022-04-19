from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # pass the user's english text to a method for translation.
    translated_text = translator.english_to_french(textToTranslate)
    return "Translated text to French: {}.".format(translated_text)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # pass user's french text to a method for translation.
    translated_text = translator.french_to_english(textToTranslate)
    return "Translated text to English: {}.".format(translated_text)

@app.route("/")
def renderIndexPage():
    # Render index page to serve translation requests.
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
