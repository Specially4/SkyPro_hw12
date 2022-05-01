import logging
from flask import Flask, send_from_directory

from main.views import main_blueprint
from loader.views import loader_blueprint


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errorhandler(413)
def page_not_found():
    """
    Обработка ошибки 413
    """
    logging.error("Загрузка файла больше установленного размера!")
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(Debug=True)
