# [Where to go](http://forluc.pythonanywhere.com/)

["Where to go"](http://forluc.pythonanywhere.com/) - приложение, созданное для отметок на карте(кофеен, экскурсии и т.д.)
![where_to_go](https://github.com/Forluc/yandex-afisha_1/assets/75582238/6d4beaf8-1c03-42f8-8c47-333001771089)

## Окружение

### Требования к установке

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки
зависимостей:

```bash
$ pip install -r requirements.txt
``` 

Создайте `.env` файл рядом с `manage.py` и добавьте:

```
SECRET_KEY=[django secret key]
DEBUG=[True or False]
ALLOWED_HOSTS='127.0.0.1'
```

## Сценарий использования web-приложения

- Сделайте миграцию, создайте суперюзера и запустите сервер Django

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

- Перейдите в [django-admin](https://127.0.0.1:8000/admin)
- Введите логин и пароль от ранее созданной учетной записи
- Выберите поле `Places` и нажмите после `ADD PLACE`
- Заполните поля данными, добавьте по желанию фотографии и нажмите `SAVE`

#### load_place

Для удобного добавления локаций есть команда `load_place`. Для добавления выполните команду(где после команды нужно написать `url-адрес json-файла`):

```bash
$ python manage.py load_place https://example/example.json
$ python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9A%D0%BE%D0%B2%D0%BE%D1%80%D0%BA%D0%B8%D0%BD%D0%B3%20Gravity.json
```
Оформление json-файла:
![1](https://github.com/Forluc/yandex-afisha_1/assets/75582238/2bad3b45-3f72-4b19-8e68-80adbeb6434a)

### Цель проекта

Скрипт написан в образовательных целях на онлайн-курсе [Devman](https://dvmn.org)
