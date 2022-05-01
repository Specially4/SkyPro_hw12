from flask import render_template, Blueprint, request
import logging

from main import utils
from loader.utils import *


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="info.log", level=logging.INFO, encoding='utf-8')


@loader_blueprint.route("/post/", methods=["GET"])
def create_new_post():
    """
    Страничка для загрузки поста пользователя
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post/", methods=["POST"])
def create_new_post_by_user():
    """
    Страничка с загруженным постом пользователя. Есть проверка на формат загруженного файла, либо на отсутствие контента
    """
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутствует часть данных")
        return "Отсутствует часть данных"
    posts = utils.load_json(POST_PATH)
    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        return "Неверный тип изображения"

    add_post(posts, new_post)

    return render_template("post_uploaded.html", new_post=new_post)
