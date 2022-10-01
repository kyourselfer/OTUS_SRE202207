Автоматизация: CLI, Data transformation // ДЗ
-------------
#### Цель:
Распарсить вывод API и отдать его в формате Prometheus

Результаты:

* Приложение [flask-sqlite3-todo-crud](https://github.com/Zenahr/flask-sqlite3-todo-crud/blob/master/app.py) отвечает на три запроса:
/ GET
/add POST
/update POST
Проверьте код ответа приложения, время ответа либо иные важдые для ваших SLI на данные запросы и отдайте эту информацию в формате Prometheus
* Получите ответ от API http://open-notify.org/Open-Notify-API/ISS-Location-Now/ и сконвертируйте его в формат Prometheus

* Экспортер возвращает данные в нужном формате 6/10
* Экспортер возвращает данные для flask приложения 8/10
* Экспортер возвращает данные для flask и внешнего api 10/10

Описание
------------
Проэкт реализован на основании готового кода, благодаря разработчику [Zenahr](https://github.com/Zenahr/flask-sqlite3-todo-crud)

И реализуется испольуя инфраструктурные инструмены Vagrant, Ansible, Docker

После выполнения процесса build'а, для проверки перейдите в браузере по [URI](http://127.0.0.1:5000/)

Требования
------------
Packages version min.: python 3.6, pip 3.9

Как добавить новый код
------------
Посредством git и добавления ваших изменений через PR в файлы:
- ansible роли [flask-sqlite3-todo-crud](https://raw.githubusercontent.com/kyourselfer/OTUS_SRE202207/main/03_basic-of-SRE/flask-sqlite3-todo-crud/)
- файла инфраструктурной конфигурации [vagrantfile](https://raw.githubusercontent.com/kyourselfer/OTUS_SRE202207/main/03_basic-of-SRE/Vagrantfile)

Запуск (как продеплоить приложение)
------------
`python3 json-to-prom.py`

Лицензия
-------------

BSD 2-Clause LicenseZZ

Автор
-------------
Eliseev V.A.