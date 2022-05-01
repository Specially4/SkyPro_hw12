import json
from exceptions import *


def load_json(path):
    """
    Проверяем загрузиться ли JSON файл
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(posts, substring):
    """
    Выполняем поиск по слову в списке постов
    """
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
