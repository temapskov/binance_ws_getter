# binance_ws_getter

Скрипт, который сначала записывает время в микросекундах (`receive_ts`), затем получает [данные](https://binance-docs.github.io/apidocs/futures/en/#diff-book-depth-streams) по WebSockets от Binance и забирает от туда время `T` (`transaction_time`). Сохраняет строку в CSV файл, строка,

`receive_ts;transaction_time;interval`, где interval - это `receive_ts` - `transaction_time`.

Logging выводит данную строку в терминал.

## Установка
```
pip install -r requirements.txt
```

## Установка с виртуальным окружением
- Склонируем репозиторий
```
git clone git@github.com:temapskov/binance_ws_getter.git
```
- Перейдем в директорию с проектом `cd binance_ws_getter/` и создадим виртуальное окружение Python, версию можно использовать и `3.9+`
```
python3.11 -m venv .venv
```
- Активируем виртуальное окружение:
```
. .venv/bin/activate
```
- Установим зависимости:
```
pip install -r requirements.txt
```
- Запустим скрипт:
```
python main.py
```
