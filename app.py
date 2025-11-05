from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    dest_lang = request.form['dest_lang']
    translated = translator.translate(text, dest=dest_lang)
    return render_template('index.html', 
                           original=text, 
                           translated=translated.text, 
                           dest_lang=dest_lang)

if __name__ == '__main__':
    app.run(debug=True)