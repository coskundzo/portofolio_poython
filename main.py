# Import
from flask import Flask, render_template, request, redirect
from datetime import datetime
import os

app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')

# Form verilerini kaydetme
@app.route('/', methods=['POST'])
def process_form():
    if 'email' in request.form and 'text' in request.form:
        email = request.form['email']
        text = request.form['text']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Verileri form.txt dosyasına kaydet
        with open('form.txt', 'a', encoding='utf-8') as file:
            file.write(f"\n--- Yeni Form Kaydı ---\n")
            file.write(f"Tarih: {timestamp}\n")
            file.write(f"E-posta: {email}\n")
            file.write(f"Mesaj: {text}\n")
            file.write("-" * 50 + "\n")
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
