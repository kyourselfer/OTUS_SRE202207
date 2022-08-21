Основные принципы в SRE // ДЗ
-------------
#### Цель:
+Составить краткое описание проекта

+Описать как добавить новый код

+Описать как продеплоить приложение

+Добавьте Readme в репозиторий

-Создайте диаграмму для будущего приложения используя [mingrammer](https://github.com/mingrammer/diagrams), добавьте диаграмму и ее код в репозиторий

+Создайте локальное окружение для разработки используя Vagrant

+Добавьте код локального окружения в репозиторий [Vagrantfile](https://raw.githubusercontent.com/kyourselfer/OTUS_SRE202207/main/03_basic-of-SRE/Vagrantfile)

+Напишите простой деплой для любого веб-приложения, [flask-sqlite3-todo-crud](https://github.com/Zenahr/flask-sqlite3-todo-crud) и продеплойте приложение на локальное окружение

+Добавьте код в репозиторий

+Используйте Mkdocs для оформления документации. Добавьте документацию в репозиторий.

Описание
------------
Проэкт реализован на основании готового кода, благодаря разработчику [Zenahr](https://github.com/Zenahr/flask-sqlite3-todo-crud)

И реализуется испольуя инфраструктурные инструмены Vagrant, Ansible, Docker

После выполнения процесса build'а, для проверки перейдите в браузере по [URI](http://127.0.0.1:5000/)

Требования
------------
Если запуск происходит на территории РФ необходимо наличие рабочего VPN [для загрузки локально Vagrant образа ОС](https://vagrantcloud.com/)

Ansible version min.: 2.7.0

Vagrant version min.: 2.0.0

Packages version min.: python 3.6, pip 3.9

Как добавить новый код
------------
Посредством git и добавления ваших изменений через PR в файлы:
- ansible роли [flask-sqlite3-todo-crud](https://raw.githubusercontent.com/kyourselfer/OTUS_SRE202207/main/03_basic-of-SRE/flask-sqlite3-todo-crud/)
- файла инфраструктурной конфигурации [vagrantfile](https://raw.githubusercontent.com/kyourselfer/OTUS_SRE202207/main/03_basic-of-SRE/Vagrantfile)

Запуск (как продеплоить приложение)
------------
`vagrant up`

Лицензия
-------------

BSD 2-Clause LicenseZZ

Автор
-------------
Eliseev V.A.