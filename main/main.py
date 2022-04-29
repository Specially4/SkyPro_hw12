from flask import render_template, Blueprint, request
from functions import search

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search/?s=<arg>')
def search_page(arg):
    s = request.args.get(arg).lower()
    dict_search = search(s)
    return render_template("post_list.html", data=dict_search, req=s)
