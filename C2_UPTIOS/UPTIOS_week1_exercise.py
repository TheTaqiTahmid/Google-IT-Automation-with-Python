import socket
import requests

def check_localhost():
    localhost = socket.gethostbyname("localhost")
    return localhost == '127.0.0.1'

def check_connectivity():
    ref = requests.get('http://www.google.com')
    return ref.status_code == 200 # this is http status code. 200 is ok, 403 is forbidden, 404 is not found 


