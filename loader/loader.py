from flask import render_template, Blueprint, request, send_from_directory
import logging
from functions import search
from path_file import POST_PATH, UPLOAD_FOLDER
from functions import is_filename_allowed, load_json, upload_post, search

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/create_post/", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/my_post", methods=["GET", "POST"])
def page_post_upload():
    try:
        picture = request.files.get("picture")
        text = request.form["content"]
        filename = picture.filename
        if is_filename_allowed(filename):
            picture.save(filename)
            upload_post(filename, text)
            return render_template("post_uploaded.html", filename=filename, content=text)
        else:
            logging.info(f'Попытка загрузки файла неверного формата')
            return "Тип файла не поддерживается"
    except:
        return "Ошибка загрузки"


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)
