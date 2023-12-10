# free_translate
最简单、永远免费、不限流量的翻译解决方案

google_translate_server.py  在VPS中部署服务器端，后台执行。
sudo -i
nohup python  /root/google_translate_server.py  2>&1 &
disown -h

本地执行客户端发送翻译请求(需修改服务器端IP地址）
google_tralslate_client_example.py    本地执行客户端发送翻译请求
google_tralslate_client_file.py        本地执行客户端，发送翻译本地某个TXT文件请求，翻译后保存在同一目录

