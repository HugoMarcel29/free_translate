import os
import requests
import time
from tqdm import tqdm

def translate_paragraph(paragraph, url):
    data = {'text': paragraph}
    response = requests.post(url, json=data)
    translated_text = None

    if response.status_code == 200:
        translated_text = response.json()['translated_text']

    return translated_text

def translate_long_text(input_file):
    url = 'http://79.133.126.241:9041/translate'    #填入google_translate_server.py的服务器地址
    max_length = 1500  # 段落最大长度
    max_attempts = 3   # 最大重试次数

    output_file = f"{os.path.splitext(input_file)[0]}_tran.txt"  # 输出文件名为输入文件名后面增加 "_tran"

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    paragraphs = split_text_into_paragraphs(text, max_length)
    translated_text = ""

    sum_start_time = time.time()
    start_time = time.time()
    with tqdm(total=len(paragraphs), desc='翻译进度') as pbar:
        for i, paragraph in enumerate(paragraphs):
            attempts = 0
            success = False

            while attempts < max_attempts and not success:
                translated_paragraph = translate_paragraph(paragraph, url)

                if translated_paragraph is not None:
                    translated_text += f"{paragraph}\n\n{translated_paragraph}\n\n"
                    success = True
                else:
                    print(f'Translation failed for paragraph {i + 1}')
                    attempts += 1
                    time.sleep(1)  # 等待一段时间再重试

            pbar.update(1)  # 更新进度条
            pbar.set_postfix({'耗时': f"{time.time() - start_time:.2f} 秒"})  # 显示耗时
            start_time = time.time()  # 更新开始时间

    end_time = time.time()
    elapsed_time = end_time - sum_start_time
    print(f"总耗时：{elapsed_time:.2f} 秒")  # 显示整个文件翻译耗时

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

def split_text_into_paragraphs(text, max_length):
    paragraphs = text.split('\n')
    split_paragraphs = []
    current_paragraph = ''

    for paragraph in paragraphs:
        if len(current_paragraph) + len(paragraph) <= max_length:
            current_paragraph += paragraph + '\n'
        else:
            split_paragraphs.append(current_paragraph.strip())
            current_paragraph = paragraph + '\n'

    if current_paragraph:
        split_paragraphs.append(current_paragraph.strip())

    return split_paragraphs

# 调用示例
translate_long_text('D:\\Download\\to_translate.txt')
