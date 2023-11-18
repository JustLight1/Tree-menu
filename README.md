<a id="anchor"></a>
<div align=center>

  # Приложение Древовидное меню

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

</div>

## Описание тестового задания

```
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
```

### Технологии

Python 3.9.10

Django 4.2

## Получение древовидного меню

* Необходимо сделать GET запрос на эндпоинт `menu/`.

<details>
<summary>
<h4>Запуск проекта</h4>
</summary>

<br>

~~~
склонировать проект git clone git@github.com:JustLight1/Tree-menu.git
~~~
- При первом запуске для функционирования проекта обязательно установить виртуальное окружение, установить зависимости,  выполнить миграции:

```
python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt

```
pip install -r requirements.txt
```
- Выполните миграции БД. Из папки backend с файлом manage.py выполните команду:
```
python manage.py makemigrations
python manage.py migrate
```
- Для создания суперюзера из папки backend с файлом manage.py выполните команду:
```
python manage.py createsuperuser
```

- Для запуска сервера из папки backend с файлом manage.py выполните команду:

```
python manage.py runserver
```
</details>


<details>
<summary>
<h4>Шаблон наполнения env-файла</h4>
</summary>

<br>

```env
  DEBUG=False
  SECRET_KEY=
```

</details>

## Контакты:

**Форов Александр** 

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
