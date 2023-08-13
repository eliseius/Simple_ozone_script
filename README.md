# OZON  продажи в ЕАЭС

Продавцы **маркеплейса Ozon**, обязаны с помощью статистической формы учёта перемещения товаров самостоятельно передавать данные обо всех позициях, которые они продали в **страны ЕАЭС**.

Проект позволяет получить список таких товаров с сортировкой по странам.


## Важная информация

- Сформированный список получает данные только по **схемам работы FBS** и **rFBS**.
- В проекте используется метод Seller API `https://api-seller.ozon.ru/v3/posting/fbs/list`

## Подготовка:

1. Для получения данных необходимо подключить Seller API, ввести номер клиентского идентификатора (**Client ID**) и  сгенерировать уникальный ключ (**API Key**). Как подключить Seller API и создать уникальный API-ключ, можно узнать по этой [ссылке](https://seller-edu.ozon.ru/docs/api-ozon/how-to-api.html#:~:text=%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D1%8F%D1%82%D1%8C%20%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D1%8B%20%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B9.-,%D0%9A%D0%B0%D0%BA%20%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C%20Seller%20API,-%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%20%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%D0%B2).
2. Для отображения полного и актуального списка проданных товаров во все страны ЕАЭС, необходимо **проверить актуальность кластеров доставки** по [ссылке](https://seller-edu.ozon.ru/docs/finances-documents/additional-information/statisticheskaya-forma-ucheta.html#:~:text=%D0%90%D1%80%D0%BC%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B8%20%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D1%81%D1%82%D0%B0%D0%BD.-,%D0%9A%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%20%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B8,-%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B0%20%D0%95%D0%90%D0%AD%D0%A1). При необходимости внести изменения в файле `constants.py`.

## Сборка репозитория и локальный запуск

Выполните в консоли:

1. Клонируйте репозиторий с github:

```
git clone https://github.com/El1seius/Simple_ozone_script.git
```

2. Создайте виртуальное окружение:

```
python -m venv <имя каталога>
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Создайте файл `settings.py`

5. Впишите в settings.py переменные:
```
OZON_CLIENT_ID = 'Ваш Client ID'

OZON_API_KEY = 'API Key, который вы сгенерировали'
```
6. Запустите командой:
```
python script.py <дата начала отчета> <дата окончания отчета> <статус отправления>
```

### Дополнительная информация

- Указанный диапазон дат должен быть не больше одного года.
- Список доступных статусов отправлений:
```
awaiting_registration — ожидает регистрации,
acceptance_in_progress — идёт приёмка,
awaiting_approve — ожидает подтверждения,
awaiting_packaging — ожидает упаковки,
awaiting_deliver — ожидает отгрузки,
arbitration — арбитраж,
client_arbitration — клиентский арбитраж доставки,
delivering — доставляется,
driver_pickup — у водителя,
delivered — доставлено,
cancelled — отменено,
not_accepted — не принят на сортировочном центре,
sent_by_seller – отправлено продавцом.
````
- При заполнении статформы (по рекомендации Ozon, [ссылка](https://seller-edu.ozon.ru/docs/finances-documents/additional-information/statisticheskaya-forma-ucheta.html#:~:text=%D0%BD%D0%B0%D1%85%D0%BE%D0%B4%D1%8F%D1%82%D1%81%D1%8F%20%D0%B2%20%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%B5-,%D0%94%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD,-%3B)) нужно учитывать все заказы, которые находятся в статусе **Доставлен** (`delivered`).
