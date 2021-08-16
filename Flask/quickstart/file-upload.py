from flask import request, Flask
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f'/var/www/uploads/{secure_filename(file.filename)}')
