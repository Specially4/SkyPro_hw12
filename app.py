import logging

from flask import Flask, request, render_template, send_from_directory
from functions import is_filename_allowed, load_json, upload_post, search

# from main.main import main_blueprint
# from loader.loader import loader_blueprint

logging.basicConfig(filename="info.log", level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s', encoding="utf-8")


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# app.register_blueprint(main_blueprint)
# app.register_blueprint(loader_blueprint)


@app.route("/")
def page_index():
    if type(load_json(POST_PATH)) == list:
        return render_template("index.html")
    else:
        return render_template("index.html", info=f'Обнаружена ошибка:{load_json(POST_PATH)}')


@app.route("/search")
def page_tag():
    s = request.args.get("s").lower()
    logging.info(f'Выполнен поиск по запросу: {s}')
    if s:
        dict_search = search(s, path=POST_PATH)
        return render_template("post_list.html", data=dict_search, req=s)
    return 'Вы ничего не ввели'


@app.route("/create_post/", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@app.route("/my_post", methods=["GET", "POST"])
def page_post_upload():
    try:
        picture = request.files.get("picture")
        text = request.form["content"]
        filename = picture.filename
        if is_filename_allowed(filename):
            path = f"../uploads/images/{filename}"
            picture.save(f"./uploads/images/{filename}")
            upload_post(POST_PATH, path, text)
            return render_template("post_uploaded.html", filename=path, content=text)
        else:
            logging.info(f'Попытка загрузки файла неверного формата')
            return "Тип файла не поддерживается"
    except:
        return "Ошибка загрузки"

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

@app.errorhandler(413)
def page_not_found(e):
    logging.error("Загрузка файла больше установленного размера!")
    return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>", 413

if __name__ == "__main__":
    app.run(Debug=True)

