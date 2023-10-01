# Where to go

"Where to go" - приложение, созданное для отметок на карте(кофеен, экскурсии и т.д.)

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

### Цель проекта

Скрипт написан в образовательных целях на онлайн-курсе [Devman](https://dvmn.org)
