from app import app
from poempicker import *
import markovify

@app.route('/')
def index():
    text = get_text_url('http://mek.oszk.hu/01000/01006/html/vs184602.htm')
    text.replace('\n', '<br>')
    model = markovify.Text(text)
    content = ''
    for i in range(10):
        sentence = str(model.make_sentence())
        if (sentence != 'None'):
            content += sentence
    return content
