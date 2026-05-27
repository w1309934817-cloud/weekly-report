import sys
import os
import time
import socket
import threading
import atexit

os.environ['FLASK_ENV'] = 'production'

PORT = 8300


def _port_in_use():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    in_use = s.connect_ex(('127.0.0.1', PORT)) == 0
    s.close()
    return in_use


def _wait_for_server(timeout=10):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if _port_in_use():
            return True
        time.sleep(0.3)
    return False


def _start_flask():
    from wserver import app as flask_app
    from waitress import serve
    serve(flask_app, host='127.0.0.1', port=PORT, threads=2)


def main():
    started_by_us = False
    if not _port_in_use():
        server_thread = threading.Thread(target=_start_flask, daemon=True)
        server_thread.start()
        started_by_us = True
        atexit.register(lambda: os._exit(0))

    if not _wait_for_server():
        print('服务启动超时')
        sys.exit(1)

    try:
        import webview
        webview.create_window(
            '周报生成器',
            f'http://localhost:{PORT}',
            width=1100,
            height=780,
            resizable=True,
            min_size=(800, 600),
        )
        webview.start(gui='cocoa' if sys.platform == 'darwin' else None)
    except Exception as e:
        print(f'窗口启动失败: {e}')
    finally:
        if started_by_us:
            os._exit(0)


if __name__ == '__main__':
    main()
