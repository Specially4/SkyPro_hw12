from flask import render_template, Blueprint, request
from functions import upload_post, is_filename_allowed

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')
def main_page():
    return render_template("post_form.html")

@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    picture = request.files.get("picture")
    text = request.form["content"]
    filename = picture.filename
    if is_filename_allowed(filename):
        path = "/uploads/images/" + filename
        picture.save(path)
        upload_post(path, text)
        return render_template("post_uploaded.html", filename=path, content=text)
    else:
        return f"Тип файла не поддерживается"
