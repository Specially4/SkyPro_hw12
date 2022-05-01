import json
from config import POST_PATH, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from exceptions import WrongImgType

def save_picture(picture):
    """
    Функция для проверки формата изображения
    """
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in ALLOWED_EXTENSIONS:
        raise WrongImgType(f'Неверный формат файла! Допустимы только {", ".join(ALLOWED_EXTENSIONS)}')
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path

def add_post(post_list, post):
    """
    Добавление нового поста в файл JSON
    """
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)
