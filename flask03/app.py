from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save('test.txt')
    return 'アップロードされました'


@app.route('/upload-files', methods=['POST'])
def upload_files():
    files = request.files.getlist('files')
    for i, f in enumerate(files):
        f.save('test{}.txt'.format(i))
    return 'アップロードされました'


if __name__ == '__main__':
    app.run()
