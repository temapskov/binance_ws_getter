import asyncio
import aiofiles
import json
from aiocsv import AsyncWriter
import logging
import time
import websockets


SOCKET = "wss://fstream.binance.com/stream?streams=btcusdt@depth@0ms"
OUTPUT_FILENAME = "output.csv"
logging.basicConfig(level=logging.INFO, format='%(message)s')

async def write_file(receive_ts: int, transaction_time: int):
    async with aiofiles.open(OUTPUT_FILENAME, "a") as csvfile:
        writer = AsyncWriter(csvfile, delimiter=";")

        if transaction_time:
            interval = receive_ts - transaction_time
            logging.info(f"{receive_ts};{transaction_time};{interval}")
            await writer.writerow([receive_ts, transaction_time, interval])
        else:
            logging.error("Ошибка получения данных")
            await writer.writerow(["Ошибка получения данных"])


async def main():
    while True:
        async with websockets.connect(SOCKET) as websocket:
            receive_ts = int(time.time() * 1000)
            msg = await websocket.recv()
            js = json.loads(msg)
            transaction_time = js.get("data").get("T")

            await write_file(receive_ts, transaction_time)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа закрыта")
