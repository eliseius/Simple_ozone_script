URL_OZON = "https://api-seller.ozon.ru/v3/posting/fbs/list"

LIMIT = 1000

COUNTRIES_SHIPMENT = {
    'Армения': {'Армения'},
    'Беларусь': {'Брест', 'Витебск', 'Гомель', 'Гродно', 'Минск', 'Могилев', 'Беларусь'},
    'Киргизия': {'Киргизия', 'Кыргызстан'},
    'Казахстан': {'Актау', 'Актобе', 'Алма-Ата', 'Астана', 'Атырау', 'Караганда',
                  'Костанай', 'Кызылорда', 'Павлодар', 'Петропавловск', 'Тараз',
                  'Туркестан', 'Уральск', 'Усть-Каменогорск', 'Казахстан'},
}

STATUS_CATALOGUE = {
    'awaiting_registration': 'Ожидает регистрации',
    'acceptance_in_progress': 'Идёт приёмка',
    'awaiting_approve': 'Ожидает подтверждения',
    'awaiting_packaging': 'Ожидает упаковки',
    'awaiting_deliver': 'Ожидает отгрузки',
    'arbitration': 'Арбитраж',
    'client_arbitration': 'Клиентский арбитраж доставки',
    'delivering': 'Доставляется',
    'driver_pickup': 'У водителя',
    'delivered': 'Доставлено',
    'cancelled': 'Отменено',
    'not_accepted': 'Не принято на сортировочном центре',
    'sent_by_seller': 'Отправлено продавцом',
}

LIST_ERROR_OZON = {
    400: 'Неверный параметр переданных даных.',
    403: 'Доступ запрещен. Неправильные Client-Id или Api-Key.',
    404: 'Ответ не найден. Укажите корректный метод',
    409: 'Конфликт запроса',
    500: 'Внутренняя ошибка сервиса.',
}
