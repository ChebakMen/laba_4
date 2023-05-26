import sqlite3
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance
import requests
import os
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024  # 1 MB limit for uploaded files
IMG = './ing'  # папка для загруженных файлов
app.config['IMG'] = IMG 

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/img/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['IMG'], filename)

if __name__ == '__main__':
    app.config['IMG'] = 'img'
    os.makedirs(app.config['IMG'], exist_ok=True)
    app.run(debug=True)

'''
data_base = sqlite3.connect('itproger.db')

#Курсор
c = data_base.cursor()

c.execute("""CREATE TABLE asas (
    title text,
    full_text text,
    views integer,
    avtor text

)""" )
#Добавление
c.execute("INSERT INTO asas VALUES ('GOOGLEEE', 'Gogle is very gooood',100, 'Admin')")

c.execute("SELECT rowid, title FROM asas")
print(c.fetchall())
data_base.commit()

data_base.close()
'''