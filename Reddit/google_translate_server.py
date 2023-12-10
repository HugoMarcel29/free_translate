from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

class GoogleFreeTranslate:
    def __init__(self):
        self.endpoint = 'https://translate.googleapis.com/translate_a/single'

    def translate(self, text, source_lang='en', target_lang='zh-CN'):
        params = {
            'client': 'gtx',
            'sl': source_lang,
            'tl': target_lang,
            'dt': 't',
            'dj': 1,
            'q': text,
        }

        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'DeepLBrowserExtension/1.3.0 Mozilla/5.0 (Macintosh;'
            ' Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/111.0.0.0 Safari/537.36',
        }

        response = requests.get(self.endpoint, params=params, headers=headers)
        if response.status_code == 200:
            translation = ''.join(i['trans'] for i in response.json()['sentences'])
            return translation
        else:
            return 'Translation failed'

@app.route('/translate', methods=['POST'])
def translate_text():
    content = request.json
    text = content.get('text')
    if text:
        translator = GoogleFreeTranslate()
        translated_text = translator.translate(text)
        return jsonify({'translated_text': translated_text})
    else:
        return jsonify({'error': 'Text not provided'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9041)
