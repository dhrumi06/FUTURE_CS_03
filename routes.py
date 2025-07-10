import os
from flask import render_template, request, redirect, send_file, url_for
from app import app
from app.config import UPLOAD_FOLDER, SECRET_KEY
from app.encryption import encrypt_file, decrypt_file
from io import BytesIO

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    data = uploaded_file.read()
    encrypted = encrypt_file(data, SECRET_KEY)
    enc_filename = uploaded_file.filename + '.enc'
    with open(os.path.join(UPLOAD_FOLDER, enc_filename), 'wb') as f:
        f.write(encrypted)
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, 'rb') as f:
        enc_data = f.read()
    decrypted = decrypt_file(enc_data, SECRET_KEY)
    original_name = filename.replace('.enc', '')
    return send_file(BytesIO(decrypted), as_attachment=True, download_name=original_name)

