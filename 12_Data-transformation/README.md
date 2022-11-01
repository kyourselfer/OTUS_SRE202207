Автоматизация: CLI, Data transformation // ДЗ
-------------
### Цель:
Распарсить вывод API и отдать его в формате Prometheus

### Задания:
* Варианты решения задания для приложений:
  * 1). Локальное приложение на Flask [flask-sqlite3-todo-crud](https://github.com/Zenahr/flask-sqlite3-todo-crud/blob/master/app.py), проверьте код ответа, время ответа либо иные важдые для ваших SLI на данные запросы и отдайте эту информацию в формате Prometheus
  * 2). Удалённое приложение [ISS-Location-Now](http://open-notify.org/Open-Notify-API/ISS-Location-Now/), получите ответ от API и сконвертируйте его в формат Prometheus
* Экспортер возвращает данные в нужном формате 6/10
* Экспортер возвращает данные для flask приложения 8/10
* Экспортер возвращает данные для flask и внешнего api 10/10
### Результаты:

Сервисы [ISS-Location-Now](http://api.open-notify.org/iss-now.json), [flask-sqlite3-todo-crud](https://github.com/Zenahr/flask-sqlite3-todo-crud/blob/master/app.py) проверены на корректность([скриптом test-url.py](https://github.com/kyourselfer/OTUS_SRE202207/blob/main/12_Data-transformation/test-url.py) с pytest):
- Существование доменного имени приложенмя/сервиса на ДНС серверах;
- Откликом порта назначения приложения/сервиса;
- Получены 200 кода ответа приложения/сервиса.

Удалённое приложение [ISS-Location-Now](http://open-notify.org/Open-Notify-API/ISS-Location-Now/):
- Получен ответ от [API](http://api.open-notify.org/iss-now.json) и сконвертирован в формат Prometheus, используя [скрипт json-to-prom.py](https://github.com/kyourselfer/OTUS_SRE202207/blob/main/12_Data-transformation/json-to-prom.py) доступный по адресу [http://localhost:9090](http://localhost:9090) 

Локальное приложение на Flask [flask-sqlite3-todo-crud](https://github.com/kyourselfer/OTUS_SRE202207/blob/main/12_Data-transformation/flask-sqlite3-todo-crud/app.py) отдаёт SLI по пути [/metrics](http://localhost/metrics):
- `service_uptime` # HELP service_uptime Hold the time elasted since service startup
- `response_time_last` # HELP response_time_last Hold the last request response time
- `flask_http_request_total` # HELP flask_http_request_total Total number of HTTP requests
- `flask_http_request_duration_seconds_bucket{le="$VALUE",method="$VALUE",path="$VALUE",status="$VALUE"}` # HELP flask_http_request_duration_seconds Flask HTTP request duration in seconds

В итоге удалось достичь цели `Экспортер возвращает данные для flask приложения 8/10`

И не удалось достичь цели `Экспортер возвращает данные для flask и внешнего api 10/10`

Описание
------------
Проэкт реализован на основании готового кода, благодаря разработчику [Zenahr](https://github.com/Zenahr/flask-sqlite3-todo-crud) и сервису "International Space Station Current Location" 

И реализуется испольуя инфраструктурные инструмены python3 и библиотеки prometheus_flask_exporter, prometheus_client, requests

После выполнения скриптов описанных выше, для проверки перейдите в браузере по URL адресам localhost)

Требования
------------
Packages version min.: python 3.6, pip 3.9

Запуск (как продеплоить приложение)
------------
`python3 json-to-prom.py`

`python3 flask-sqlite3-todo-crud/app.py`

`python3 test-url.py`

Лицензия
-------------
BSD 2-Clause LicenseZZ

Автор
-------------
Eliseev V.A.