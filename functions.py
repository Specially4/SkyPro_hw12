import json
from json import JSONDecodeError
from path_file import POST_PATH, UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def load_json():
    """
    Данная функция проверяет получиться ли прочитать и открыть файл JSON
    """
    with open(POST_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def search(arg: str):
    """
    Данная функция выполняет поиск по файлу полученному JSON
    """
    dict_content = []
    post = load_json()
    for item in post:
        if arg.lower() in item["content"].lower():
            dict_content.append(item)
        else:
            continue
    return dict_content


def upload_post(path, text):
    """
    Данная функция загружает в JSON пост пользователя
    """
    data = load_json()
    with open("posts.json", "w", encoding="utf-8") as file:
        dict_post ={}
        dict_post["pic"] = path
        dict_post["content"] = text
        data.append(dict_post)
        json.dump(data, file, indent=2, ensure_ascii=False)

