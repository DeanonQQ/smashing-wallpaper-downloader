# Smashing-Wallpaper-Downloader

Cli-утилита для парсинга обоев с веб-сайта www.smashingmagazine.com

## Запуск утилиты

Для запуска утилиты предоставлено два варианта:
+ Запуск через Makefile
+ Запуск в контейнере Docker
----
### Запуск через Makefile:

Для запуска нужно выполнить команду:

```bash
make getwallpapers_env
```
Сценарий создаст виртуальное окружение virtualenv, установит все зависимости и откроем bash-консоль для запуска утилиты. Запуск производится командой:

```bash
python3 main.py [дата] [разрешение]
# Например: python3 main.py 082021 1920x1080
```
Для выхода из консоли используйте команду exit

----
### Запуск через Docker


``` bash
# Собираем контейнер
docker build --tag smashing-wallpaper-downloader .

# Запускаем контейнер
docker run -d -p 5000:5000 smashing-wallpaper-downloader

# Смотрим запущен ли контейнер и берем container id
docker ps

# Подключаемся к контейнеру используя container id в качестве аргумента
docker exec -it ff981f3500f2 /bin/sh

# Далее запускаем скрипт
python3 main.py [дата] [разрешение]
# Например: python3 main.py 082021 1920x1080
```