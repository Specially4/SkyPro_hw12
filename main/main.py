from flask import render_template, Blueprint, request
import logging
from functions import search
from path_file import POST_PATH, UPLOAD_FOLDER
from functions import is_filename_allowed, load_json, upload_post, search

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def main_page():
    if type(load_json(POST_PATH)) == list:
        return render_template("index.html")
    else:
        return f'Обнаружена ошибка:{load_json(POST_PATH)}'


@main_blueprint.route("/search")
def page_tag():
    s = request.args.get("s").lower()
    logging.info(f'Выполнен поиск по запросу: {s}')
    if s:
        dict_search = search(s, path=POST_PATH)
        return render_template("post_list.html", data=dict_search, req=s)
    return 'Вы ничего не ввели'
