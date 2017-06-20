from flask import render_template
from app import app
import poempicker

@app.route('/')
def index():
    poems = poempicker.generate_poems(poempicker.get_text_url(poempicker.urls[0]))
    return render_template('index.html',
                            urls = poempicker.urls,
                            content = poems)
