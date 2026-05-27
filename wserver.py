import sys
import os
from pathlib import Path
from flask import Flask, send_from_directory


def _get_html_dir():
    if os.environ.get('UNIFIED_TPL'):
        return os.environ['UNIFIED_TPL']
    if getattr(sys, 'frozen', False):
        return str(Path(sys._MEIPASS) / 'html')
    return str(Path(__file__).parent / 'html')


app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory(_get_html_dir(), 'index.html')


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(_get_html_dir(), filename)
