from flask import render_template, Blueprint, request
import logging
from main.utils import *
from config import *
from exceptions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="info.log", level=logging.INFO, encoding="utf-8")


@main_blueprint.route('/')
def main_page():
    """
    Главная страничка
    """
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def page_tag():
    """
    Страничка с найденными постами. Так же есть обработка проблемы с открытием файла
    """
    s = request.args.get("s", "").lower()
    logging.info(f'Выполнен поиск по запросу: {s}')
    try:
        posts = load_json(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"
    filtered_post = search_post_by_substring(posts, s)
    return render_template("post_list.html", data=filtered_post, req=s)
