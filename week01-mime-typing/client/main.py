import socket
import mimetypes
import sys
import os

# Add project root to path (so shared/ can be imported)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from shared.protocol import prepare_packet

def send_files(file_list, host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        for file_path in file_list:
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'

            with open(file_path, 'rb') as f:
                data = f.read()

            packet = prepare_packet(mime_type, data)
            s.sendall(packet)

            print(f"Sent {file_path} as {mime_type}")

if __name__ == "__main__":
    # Correct absolute paths
    files = [
        os.path.join(PROJECT_ROOT, "assets", "sample.png"),
        os.path.join(PROJECT_ROOT, "assets", "notes.txt")
    ]

    send_files(files)