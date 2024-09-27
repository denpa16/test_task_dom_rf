# Тестовое задание на позицию Python-разработчик


## Инструкция по запуску

## Локальный запуск приложения
### Не забудьте создать файл .env

```shell
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --remove-orphans -d --build

если вышла ошибка сборки контейнера - поднять его отдельно

docker-compose build backend

затем снова поднять все контейнеры

docker-compose -f docker-compose.yml -f docker-compose.override.yml up --remove-orphans -d --build
```




## ENV-файл Backend
```shell
SECRET_KEY=my_very_sercet_key
DADATA_API_KEY=dadata_api_key
DADATA_SECRET_KEY=dadata_secret_key

# переменные для БД
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_HOST=db
POSTGRES_DB=postgres

# топик Кафки, в который отправляются результаты обработки загрузки входящих данных (либо по REST API, либо через Кафку)
KAFKA_RESULT_TOPIC=KAFKA_RESULT_TOPIC
# топик Кафки для входящих данных
KAFKA_IMPORT_TOPIC=KAFKA_IMPORT_TOPIC
KAFKA_BOOTSTRAP_SERVERS=kafka:9094
```











Что нужно сделать?
Цель данного задания - реализовать интеграционный сервис, который получает задачи для обработки в топике брокера и запрашивает информацию по API. Сервис должен быть реализован с помощью фреймворков FastAPI или Flask.

Что мы ожидаем?
В качестве решения мы ожидаем сервис, который можно будет запустить с docker-compose.yaml. Сервис способен получать сообщения как в топик брокера (в качестве брокера возможно использование Apache Kafka или RabbitMQ), так и в качестве REST-запроса. Формат данных одинаковый для обоих случаев. Далее ходить за информацией по API в сторонние сервисы. В качестве конечного результата сервис должен сделать запись в бд с полученными данными и отправить id записи в топик брокера.

Сервис должен будет обращаться к API Dadata для проверки телефона (описание API - https://dadata.ru/api/clean/phone/), стандартизация email адресов (описание API - https://dadata.ru/api/clean/email/), а также отправка запросов YandexGPT (описание API - https://yandex.cloud/en/docs/foundation-models/concepts/yandexgpt/).

Входящий данные будут иметь следующий формат json:
{
"task_id": "number",
"task_type": "enum: phone, email, gpt",
"data": "string"
}

В ответ сервис должен будет возвращать следующий json:
{
"task_id": "number",
"id": "number"
}

Все данные сервис складывает в БД в таблицу integration_service с колонками:

id - первичный ключ
data - полученные данные от сервисов
task_type - тип задачи ("enum: phone, email, gpt")
Для оценки решения необходимо будет архив, содержащий в себе весь код приложения, Dockerfile, requirements.txt и docker-compose.yaml, который подымет все сервисы (сам сервис, брокер сообщений, БД), а также выгрузку из БД в виде SQL-скрипта с данными от работы сервиса.
