# free_translate
<h1>最简单、永远免费、不限流量的翻译解决方案</h1>
<h1>一、在VPS中部署服务器端，后台执行</h1>

google_translate_server.py


```
sudo -i
nohup python  /root/google_translate_server.py  2>&1 &
disown -h
```

<h1>二、本地执行客户端发送翻译请求(需修改服务器端IP地址）</h1>

```
url = 'http://127.0.0.1:9041/translate'     ##填入google_translate_server.py的服务器地址
```

google_tralslate_client_example.py
本地执行客户端发送翻译请求


google_tralslate_client_file.py
本地执行客户端，发送翻译本地某个TXT文件请求，翻译后保存在同一目录

