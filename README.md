# binance_ws_getter

Скрипт, который сначала записывает время в микросекундах (`receive_ts`), затем получает [данные](https://binance-docs.github.io/apidocs/futures/en/#diff-book-depth-streams) по WebSockets от Binance и забирает от туда время `T` (`transaction_time`). Сохраняет строку в CSV файл, строка,

`receive_ts;transaction_time;interval`, где interval - это `receive_ts` - `transaction_time`.

## Установка
```
pip install -r requirements.txt
```