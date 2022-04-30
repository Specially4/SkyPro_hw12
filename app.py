import logging
from path_file import POST_PATH, UPLOAD_FOLDER
from flask import Flask, request, render_template, send_from_directory
from functions import is_filename_allowed, load_json, upload_post, search

from main.main import main_blueprint
from loader.loader import loader_blueprint

logging.basicConfig(filename="info.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s', encoding="utf-8")

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errorhandler(413)
def page_not_found(e):
    logging.error("Загрузка файла больше установленного размера!")
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413


if __name__ == '__main__':
    app.run(Debug=True)

