# Курсовая работа 
## Описание: приложение для анализа транзакций, которые находятся в Excel-файле. 
Приложение будет генерировать JSON-данные для веб-страниц, формировать Excel-отчеты, 
а также предоставлять другие сервисы.
### Функционал приложения для анализа транзакций. 
Транзакции получены в Excel-файле, приложение генерирует JSON-файл для веб-страниц, формирует
excel-отчеты и предоставляет другие сервисы:
- Рассчитывает сумму на счету инвесткопилки по заданному порогу округления;
- Выводит информацию о 5 топ транзакциях по сумме платежа
- Выводит информацию по каждой карте (последние 4 цифры карты, общая сумма расходов, кэшбэк)
- Выводит текущий курс валют: USD, EUR.
Виджет банковских операций клиента показывает несколько последних успешных банковских 
операций клиента. 
Виджет имеет функцию вывода суммы транзакции в рублях, включая перевод в рубли по текущему 
курсу в случае, если транзакция была в валюте. 
Виджет логирует функции маскирования номеров карт и счетов, и вывода суммы транзакции в рублях. 
Виджет может работать с файлами в форматах json, CSV и excel.
## Тесты: Содержит тесты функционала.
## Установка:
Клонируйте репозиторий: git clone https://github.com/Nericrash/course-work
## Установите зависимости:
pip install -r requirements.txt
