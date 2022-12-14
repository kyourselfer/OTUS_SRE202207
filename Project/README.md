В соответствии с практиками SRE реализовать проэкт за 21 день(до 26 декабря 2023 г.) по внедрению инфраструктуры 
-------------
Переделка плана с нацеливанием на суть опыта с ориентированием до 12.01.2023

Последовательность среза на главном, с соблюдением сроков:
- Запустить главное:
  + minikube `запущено`
  + prom-stack `запущено`
  + grafana oncall
    + Настроено эскалирование (slack/telegram) + тех. записи
- `до 12.01` Описаны все пункты согласно примерному плану защиты проектной работы 

### Ориентировочный план реализации:
Внедряем:
- Первый этап
  - Запустить k3s/minikube
  - Настроить prometheus operator
  - Настроить grafana oncall
    - Настроить escalation chain добавление узла в кластер на тригер перегрузки кластера
  - Запустить DevOps CI/CD для вашего кода
  - Automate infrastructure scaling `не реализуемо исходя из возможностей инфраструктуры`
  - Как вы будете соблюдать правило 50/50 ( стратегия ) `нужно ознакомиться/вспомнить`
  - Проведите SRE тренинг для других команд (pdf презентация)
- Второй этап 
  - Определите SLA,SLO,SLI. Чем вы руководствовались, с кем вы общались в компании?
  - Измерьте поведение Вашей системы на соответствие SL*. Как вы этого добьетесь?
  - Определите Error-Budgeet (velocity vs quality)
  - Определите OKR для SRE `нужно ознакомиться/вспомнить`
- Третий этап
  - Внедрите мониторинг
  - Golden signals: latency, saturation, traffic, errors 
  - В процессе релиза упал memcached. Выпустите Blameles postmortem `со стороны app не имею кэширующего функционала для redis/memcached` 
  - Исправьте архитектуру чтобы этого больше не происходило
- Четвертый этап 
  - Проверьте что падение memcached больше не ломает систему. проведите эксперимент `со стороны app не имею кэширующего функционала для redis/memcached` 
  - Handle improvement discussion `нужно ознакомиться/вспомнить` 
  - Response scenarios based on proactive monitoring `нужно ознакомиться/вспомнить`

### Результаты:

Описание
------------
Проект реализован:
- На основании готового кода, благодаря разработчику [Zenahr](https://github.com/Zenahr/flask-sqlite3-todo-crud)
- Руководителю Сергею Караткевичу
- Дмитрию Жиляеву
- Антону Бурнашеву
- Анастасии Порхун

Требования
------------
Minikube version recom.: v1.26.0
Packages version min.: python 3.6, pip 3.9

Лицензия
-------------
BSD 2-Clause LicenseZZ

Автор
-------------
Eliseev V.A.