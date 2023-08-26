from asyncio import sleep


def averager():
    count = 0
    average=0.0
    total = 0
    while True:
        item = yield average
        count += 1
        total += item
        average = total/count


coro_avg = averager()
# v0 = next(a)
v0 = coro_avg.send(None)   # next(a) = a.send(None
v1 = coro_avg.send(10)
v2 = coro_avg.send(20)
# v3 = a.close()
# v4 = a.close()
# v5 = next(coro_avg)
import random
while True:
    v = coro_avg.send(random.random())
    print(f"v={v}")
    sleep(1)
