import socket

from requests import get

print('Hostname: ', socket.gethostname())
print('Local IP: ', socket.gethostbyname(socket.gethostname()))
print('Public IP: ', get('https://api.ipify.org').text)
