from flask import Flask, render_template, request
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verifica si se ha enviado un archivo
        if 'file' in request.files:
            file = request.files['file']

            # Lee la imagen y la convierte a base64
            if file and allowed_file(file.filename):
                base64_image = convert_to_base64(file)
                return render_template('index.html', base64_image=base64_image)

    return render_template('index.html')

def allowed_file(filename):
    # Verifica si la extensión del archivo es válida (puedes personalizar las extensiones)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def convert_to_base64(file):
    # Lee la imagen en formato binario
    image_binary = file.read()

    # Codifica la imagen en base64
    base64_encoded = base64.b64encode(image_binary)

    # Decodifica bytes a cadena de texto (UTF-8)
    base64_string = base64_encoded.decode('utf-8')
    
    print(base64_string)

    return base64_string

if __name__ == '__main__':
    app.run(debug=True)
