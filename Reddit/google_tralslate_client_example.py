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
url = 'http://79.133.126.241:9041/translate'
print(translate_paragraph(paragraph, url))
