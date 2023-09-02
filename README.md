# Платформа для онлайн-обучения
### Проект находится в процессе разработки

Разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.

Проект содержит два приложения:
- app_course
    - Курсы 
    - Уроки
- users (Пользователи)
    - Пользователь (Обязательные поля для создания профиля пользователя - "email" и "password")

Для всех моделей описан CRUD с использованием ViewSets или Generic.

# Урок 24_1

## Задание 1
- Создайте новый Django-проект, подключите DRF и внесите все необходимые настройки.

## Задание 2
Создайте следующие модели:

### Пользователь:
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.
### Курс:
- название,
- превью (картинка),
- описание.
### Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.
## Задание 3
Опишите CRUD для моделей курса и урока, но при этом для курса сделайте через ViewSets, а для урока — через Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.

>Работу каждого эндпоинта необходимо проверять с помощью Postman.   
Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже самой простой авторизацией.

## *Дополнительное задание
Реализуйте эндпоинт для редактирования профиля любого пользователя на основе более привлекательного подхода для личного использования: Viewset или Generic.

>Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.