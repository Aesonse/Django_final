import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Мой первый Django-сайт</title>
</head>
<body>

<h1>Мой первый Django-сайт</h1>

<p>Этот сайт был создан с использованием Django - известного фреймворка для веб-разработки на Python.</p>

<h2>Обо мне</h2>

<p>Меня зовут Алиса, и я полный профан и новичок в веб-разработке. Я начала изучать Django совсем недавно и решила создать этот сайт, чтобы проверить свои навыки.</p>

<p>Я надеюсь, что мой сайт будет приличным и его не стыдно будет показать новичкам, которые, как и я, только начинают свой путь в веб-разработке.</p>

</body>
</html>
    """
    logger.info("index page was requested")
    return HttpResponse(response)


def about(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Обо мне</title>
</head>
<body>

<h1>Обо мне</h1>

<p>Всем привет! Я Алиса, и я очень люблю программирование. Я с детства хотела научиться создавать программы, сайты. Да и вообще очень любила сидение за компом))). Однако оно мне казалось недоступным моему изучению (я из обычной гуманитарной школы без нормальной математики и информатики). В общем спустя много лет я всетаки решилась и вот полтора года как изучаю программирование.</p>

<p>Программирование отлично развивает мозг, заставляет находить разные интересные решение к задачам. Хочется познавать все больше и больше.</p>

<p>Я надеюсь, что мой сайт поможет другим людям, которые также интересуются программированием.</p>

</body>
</html>
    """
    logger.info("about page was requested")
    return HttpResponse(response)