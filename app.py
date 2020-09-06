from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/get_music', methods=['GET', 'POST'])
def send_music():
    if request.method == 'POST':
        music_name = request.form.get('music_name')
        print(request.form)
        music_file = open("music/" + music_name + ".mp3", "rb")
        data = music_file.read()
        music_file.close()
        return data
    else:
        return "kikk! Game Music API"


if __name__ == '__main__':
    app.run()
