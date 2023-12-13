import requests


def translate_paragraph(paragraph, url):
    data = {'text': paragraph}
    response = requests.post(url, json=data)
    translated_text = None

    if response.status_code == 200:
        translated_text = response.json()['translated_text']

    return translated_text

# 调用示例
paragraph = 'hello world'
url = 'http://127.0.0.1:9041/translate'    #填入google_translate_server.py的服务器地址
print(translate_paragraph(paragraph, url))
