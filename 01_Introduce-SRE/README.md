Введение в SRE // ДЗ
-------------
#### Цель:
Настроено окружение: 
------------
Ubuntu 22.04

PyCharm + MARP

docker 20.10.17

minikube v1.26.0

virtualbox+vagrant

...

Запуск
------------
Возможные режимы OpenVPN:
##### TLS (server-client)
##### STATIC (p2p)
 
##### Чтобы настроить использование режима TLS:

Включить `openvpn_server`

Включить `openvpn_client`

На стороне клиента вы должны определить переменную `openvpn_remotehost` с ip адресом сервера

##### Чтобы настроить использование режима STATIC (один ключ на две точки):

Включить `openvpn_server`

Включить `openvpn_client`

Включить `openvpn_static`

На стороне клиента вы должны определить переменную `openvpn_remotehost` с ip адресом сервера

Переменные роли
------------
| Имя                         | Умолчание                                                   | Описание                                                                                                              |
|-----------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| openvpn_cacertificate       | ''                                                          | открытый ключ авторитетного цента сертификации(CA) (подписываем закрытым ключем CA)                                   |
| openvpn_cipherstatic        | AES-256-CBC                                                 | алгоритм шифрование который используется для STATIC режима                                                            |
| openvpn_ciphertls           | AES-256-CFB8                                                | алгоритм шифрование который используется для TLS режима                                                               |
| openvpn_client              | false                                                       | Вкл. в режим клиента                                                                                                  |
| openvpn_clientcertificate   | ''                                                          | открытый ключ клиента                                                                                                 |
| openvpn_clientendpoint      | 10.8.0.2                                                    | конечный адресс клиентской стороны                                                                                    |
| openvpn_clientifconfig      | "{{ openvpn_clientendpoint }} {{ openvpn_serverendpoint }}" | ifconfig задействовано в STATIC режиме (клиентская сторона)                                                           |
| openvpn_clientkey           | ''                                                          | закрытый ключ клиента                                                                                                 |
| openvpn_complzo             | true                                                        | метод компрессии                                                                                                      |
| openvpn_daemon              | true                                                        | демонизация процесса                                                                                                  |
| openvpn_dev                 | tun                                                         | драйвер (два режима tun(3-4 уровень OSI используется в основном для шлюзов)                                           |tap(2 уровень OSI - клиентская сетевая должна быть в той же сети куда происх. коннект))
| openvpn_dhcpoptiondns       | ["208.67.222.222", "208.67.220.220"]                        | днс сервера для отправки на клиента (push сообщения)                                                                  |
| openvpn_dhkey               | ''                                                          | ключ Diffie Hellman для TLS режима (для защиты трафика от расшифровки)                                                |
| openvpn_group               | nogroup                                                     | имя группы под которым запускается процесс (в файле var/main.yml)                                                     |
| openvpn_ifconfigpoolpersist | ipp.txt                                                     | для хранения базы клиентов ifconfig-pool (для получения одних и тех же ip, ключевое поле CN в открытом ключе клиента) |
| openvpn_keepalive           | 10 60                                                       | для поддержания соединения (задействет сразу две команды ping и ping-restart)                                         |
| openvpn_mute                | 3                                                           | ограничение на повторяющиеся сообщения (сокращает лог)                                                                |
| openvpn_nobind              | true                                                        | не слушать локальный интерфейс и порт                                                                                 |
| openvpn_nscerttype          | ''                                                          | явное указание в сертификате поля nsCertType "client" или "server"                                                    |
| openvpn_packages            | openvpn={{ openvpn_version }}*                              | перечень пакетов для установки (в каталоге var/main.yml)                                                              |
| openvpn_persistkey          | true                                                        | при перезапуске процесса OpenVPN не перечитывает закрытые ключи (через SIGUSR1)                                       |
| openvpn_persisttun          | true                                                        | при перезапуске процесса OpenVPN не перезапускает драйвер (не закрывать и не переоткрывать драйвер TUN                |TAP через SIGUSR1)
| openvpn_proto               | udp                                                         | какой протокол использовать для соединения(tcp рекомендуют за NAT > 2 или proxy(CONNECT                               |SOCKS))
| openvpn_pull                | true                                                        | принимать push сообщения от сервера (route, dhcp, dns)                                                                |
| openvpn_redirectgateway     | false                                                       | шлюз по умолчанию удаленный сервер                                                                                    |
| openvpn_remotehost          | ''                                                          | доменное имя или ip хоста для подключения                                                                             |
| openvpn_remoteport          | '1195'                                                      | удаленный номер порта                                                                                                 |
| openvpn_remoteproto         | "{{ openvpn_proto }}"                                       | протокол удаленного хоста                                                                                             |
| openvpn_renegsec            | 259200                                                      | повторная аунтификация через определённый временной интервал                                                          |
| openvpn_resolvretry         | infinite                                                    | если имя хоста не преобразуется, попытаться преобразовать в течении указанного времени (сек.)                         |
| openvpn_secret              | ''                                                          | секретный закрытый ключ для режима STATIC                                                                             |
| openvpn_secretfile          | static.key                                                  | путь и название файла для режима STATIC (в файле var/main.yml)                                                        |
| openvpn_server              | false                                                       | Вкл. в режим сервера                                                                                                  |
| openvpn_servercertificate   | ''                                                          | открытый ключ сервера                                                                                                 |
| openvpn_serverendpoint      | 10.8.0.1                                                    | конечный адресс серверной стороны                                                                                     |
| openvpn_serverifconfig      | "{{ openvpn_serverendpoint }} {{ openvpn_clientendpoint }}" | ifconfig задействовано в STATIC режиме (серверная сторона)                                                            |
| openvpn_serverkey           | ''                                                          | Закрытый ключ сервера                                                                                                 |
| openvpn_serversubnet        | 10.8.0.0                                                    | подсеть для соединений                                                                                                |
| openvpn_serversubnetmask    | 255.255.255.0                                               | маска подсети для соединений                                                                                          |
| openvpn_servicename         | openvpn                                                     | имя юнита systemd (в файле var/main.yml)                                                                              |
| openvpn_static              | false                                                       | Вкл. режима статич. ключей (без x509 PKI и соединение ptp)                                                            |
| openvpn_status              | openvpn-status.log                                          | путь и имя статус файла                                                                                               |
| openvpn_sysDunit            | ''                                                          | список из адресов в (в файле var/main.yml)                                                                            |
| openvpn_tlsauth             | true                                                        | ключ HMAC для дополнительной защиты от DoS-атак и флуда                                                               |
| openvpn_tlsauthkey          | ''                                                          | HMAC ключ                                                                                                             |
| openvpn_user                | nobody                                                      | имя пользователя под которым запускается процесс (в файле var/main.yml)                                               |
| openvpn_verb                | 3                                                           | уровень подробности логов (по умолчанию вывод в journald)                                                             |
| openvpn_version             | 2.3.10                                                      | версия OpenVPN                                                                                                        |

Лицензия
-------------

BSD

Автор
-------------
Елисеев В.А.


