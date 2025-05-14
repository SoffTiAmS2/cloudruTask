from flask import Flask
import socket
import os

echo_server = Flask(__name__)

@echo_server.route('/')
def index():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "N/A"
    author = os.getenv('AUTHOR', 'Unknown')
    return f"""
    <h1>Echo Server</h1>
    <p>Hostname: {hostname}</p>
    <p>IP Address: {ip}</p>
    <p>Author: {author}</p>
    """

if __name__ == '__main__':
    echo_server.run(host='0.0.0.0', port=8000)