В репозитории на Gitlab/BitBucket/Github actions сделать автоматический прогон тестов на каждый коммит // ДЗ
-------------
### Цель:
Настроить процесс CI/CD.

### Задания:
* Для репозитория, созданного во втором домашнем задании, (или любого форкнутого проекта с гитхаба) необходимо настроить процесс CI/CD.
Используя инструменты CI/CD, например:
  * 1). https://github.com/marketplace/circleci
  * 2). https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/
  * 3). Локальный GitlabCI в Docker, https://docs.gitlab.com/ee/install/docker.html

В пайплан должны входить:
  * сборка проекта (желательно собирать приложение в Docker-контейнер, пригодится в следующем дз. Имеет смысл в качестве базового образа брать [Linux alpine](https://hub.docker.com/_/alpine/), тк это минимизированный образ, в котором нет ничего лишнего. За счет выбора базового имаджа можно существенно сократить время сборки).
  * запуск тестов (достаточно наличия одного, самого простого теста. Самое главное - чтобы для запуска тестов была сделана отдельная джоба, которую можно запустить без сборки проекта)

Критерии оценки:
* CI/CD пайплайн включает в себя только сборку проекта - 6 баллов
* CI/CD пайплайн включает сборку и запуск тестов проекта - 10 баллов
### Результаты:
Для проэкта [flask-sqlite3-todo-crud](https://gitlab.com/kyourselfer/otus_sre202207/) (из 2-го ДЗ)

На внешнем сервисе Gtlab настроен CI [.gitlab-ci.yml](https://gitlab.com/kyourselfer/otus_sre202207/-/blob/main/.gitlab-ci.yml), использовались след. stages:
- build: сборка выполняется на docker для front-nginx, back-flask
- test: выполняется без сборки, используя python lib pytest-testinfra [test-url.py](https://gitlab.com/kyourselfer/otus_sre202207/-/blob/main/test-url.py) для проверки резолва, отклика порта и статуса ответа 200
- deploy: выполняется запуск по средством docker-compose контейнезированого приложения по сценарию [docker-compose.yml](https://gitlab.com/kyourselfer/otus_sre202207/-/blob/main/docker-compose.yml)

Описание
------------
ДЗ реализовано на основании готового кода, благодаря разработчику [Zenahr](https://github.com/Zenahr/flask-sqlite3-todo-crud) 

Требования
------------
Packages version min.: python 3.6, pip 3.9

Запуск (как продеплоить приложение)
------------
`git remote add origin https://gitlab.com/kyourselfer/otus_sre202207.git`

`git branch -M main`

`git push -uf origin main`

`docker-compose up -d`

`python3 test-url.py`

Лицензия
-------------
BSD 2-Clause LicenseZZ

Автор
-------------
Eliseev V.A.