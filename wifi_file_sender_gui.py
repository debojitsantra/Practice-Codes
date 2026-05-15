import tkinter as tk
from tkinter import filedialog, messagebox
import socket
import threading
import os
import time

DEVICE_NAME = socket.gethostname()
PORT = 5001
BROADCAST_PORT = 5002
devices = {}


def get_broadcast_ip():
    ip = 192.168.0.102

    parts = ip.split('.')
    parts[-1] = '255'
    return '.'.join(parts)


def broadcast_presence():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_ip = '192.168.0.255'  # replace with your correct subnet broadcast
    print(f"🌐 Broadcasting to {broadcast_ip}")
    while True:
        try:
            s.sendto(DEVICE_NAME.encode(), (broadcast_ip, BROADCAST_PORT))
        except PermissionError:
            print("🚫 Broadcast permission denied")
        time.sleep(2)

def listen_for_devices():
    global devices
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', BROADCAST_PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if addr[0] != socket.gethostbyname(socket.gethostname()):
            devices[addr[0]] = data.decode()


def file_server():
    s = socket.socket()
    s.bind(('', PORT))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        filename = conn.recv(1024).decode()
        conn.send(b'READY')
        with open("received_" + os.path.basename(filename), 'wb') as f:
            while True:
                bytes_read = conn.recv(4096)
                if not bytes_read:
                    break
                f.write(bytes_read)
        conn.close()
        print(f"📥 Received file from {addr[0]}")


class FileSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📡 Wi-Fi File Sender")
        self.filepath = None

        self.file_label = tk.Label(root, text="No file selected.")
        self.file_label.pack(pady=10)

        tk.Button(root, text="📂 Select File", command=self.select_file).pack(pady=5)

        self.device_listbox = tk.Listbox(root, height=5)
        self.device_listbox.pack(pady=5)

        tk.Button(root, text="🔄 Refresh Devices", command=self.update_device_list).pack(pady=5)
        tk.Button(root, text="📤 Send File", command=self.send_file).pack(pady=10)

        self.status = tk.Label(root, text="", fg="blue")
        self.status.pack()

        self.update_device_list()

    def select_file(self):
        self.filepath = filedialog.askopenfilename()
        if self.filepath:
            self.file_label.config(text=os.path.basename(self.filepath))

    def update_device_list(self):
        self.device_listbox.delete(0, tk.END)
        for ip, name in devices.items():
            self.device_listbox.insert(tk.END, f"{name} ({ip})")

    def send_file(self):
        selection = self.device_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a device to send the file.")
            return
        if not self.filepath:
            messagebox.showerror("Error", "Please select a file first.")
            return

        selected = self.device_listbox.get(selection[0])
        ip = selected.split('(')[-1].replace(')', '')
        threading.Thread(target=self._send_file, args=(ip,), daemon=True).start()

    def _send_file(self, ip):
        try:
            s = socket.socket()
            s.connect((ip, PORT))
            s.send(os.path.basename(self.filepath).encode())
            ack = s.recv(1024)
            if ack != b'READY':
                raise Exception("Receiver not ready.")
            with open(self.filepath, 'rb') as f:
                while chunk := f.read(4096):
                    s.send(chunk)
            s.close()
            self.status.config(text=f"✅ File sent to {ip}")
        except Exception as e:
            self.status.config(text=f"❌ Error: {str(e)}")


if __name__ == '__main__':
    threading.Thread(target=broadcast_presence, daemon=True).start()
    threading.Thread(target=listen_for_devices, daemon=True).start()
    threading.Thread(target=file_server, daemon=True).start()

    root = tk.Tk()
    app = FileSenderApp(root)
    root.mainloop()