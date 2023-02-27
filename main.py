import asyncio
import aiofiles
import websockets
import json
import time
from aiocsv import AsyncWriter

SOCKET = "wss://fstream.binance.com/stream?streams=btcusdt@depth@0ms"
OUTPUT_FILENAME = "output.csv"


async def write_file(receive_ts: int, transaction_time: int):
    interval = 0

    async with aiofiles.open(OUTPUT_FILENAME, "a") as csvfile:
        writer = AsyncWriter(csvfile, delimiter=";")

        if transaction_time:
            interval = receive_ts - transaction_time
            await writer.writerow([receive_ts, transaction_time, interval])
        else:
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
