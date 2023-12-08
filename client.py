import socket
import sys
import os

def send_file_to_server():
    # 获取用户输入的服务器 IP、端口号和文件路径
    server_ip = input("请输入服务器IP地址:")
    server_port = int(input("请输入服务器端口号："))
    file_path = input("请输入文件路径：")

    # 创建UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # 获取文件名
        file_name = os.path.basename(file_path)

        # 发送文件名
        sock.sendto(file_name.encode("utf-8"), (server_ip, server_port))

        # 读取文件内容并发送
        with open(file_path, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                sock.sendto(data, (server_ip, server_port))

        print("文件发送完成")

    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在")

    finally:
        # 关闭套接字
        sock.close()

if __name__ == "__main__":
    send_file_to_server()

"""
运行环境:
Python 3.x
Windows、Linux 或 macOS 

配置选项：
虚拟机 IP 地址：将 server_ip 变量设置为服务器的虚拟机 IP 地址。
 服务器端口号：将 server_port 变量设置为服务器监听的端口号。

运行程序：
在终端或命令行界面中执行以下命令以启动客户端：
python3 client.py  目标ip 目标端口号 文件路径

在程序运行期间，可以通过 Ctrl+C 中断程序。
"""