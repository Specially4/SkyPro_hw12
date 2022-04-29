import json
from json import JSONDecodeError


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def load_json(arg):
    """
    Данная функция проверяет получиться ли прочитать и открыть файл JSON
    """
    try:
        with open(arg, "r", encoding="utf-8") as file:
            post = json.load(file)
        return post
    except FileNotFoundError:
        return "Файл JSON не найден"
    except JSONDecodeError:
        return "Не удалось прочитать файл JSON"


def search(arg, path):
    """
    Данная функция выполняет поиск по файлу полученному JSON
    """
    dict_content = []
    with open(path, "r", encoding="utf-8") as file:
        post = json.load(file)

    for item in post:
        if arg in item["content"]:
            dict_content.append(item)
        else:
            continue
    return dict_content


def upload_post(path_json, path, text):
    """
    Данная функция загружает в JSON пост пользователя
    """
    data = load_json(path_json)
    with open("posts.json", "w", encoding="utf-8") as file:
        dict_post ={}
        dict_post["pic"] = path
        dict_post["content"] = text
        data.append(dict_post)
        json.dump(data, file, indent=2, ensure_ascii=False)