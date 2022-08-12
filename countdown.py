times = {}
global_index = 0
import asyncio
import time

time_seed = 1


def countdown(lifetime=5, verboze=False, time_seed=time_seed):
    global global_index
    global_index += 1
    this_func_index = global_index
    times[this_func_index] = lifetime
    while times[this_func_index] > 0:
        if verboze:
            print(f'Function N {this_func_index} lifetime left {times[this_func_index]}')
        time.sleep(time_seed)
        times[this_func_index] -= time_seed
    times.pop(this_func_index)
    if verboze:
        print(f'Function N {this_func_index} game over')


async def async_countdown(lifetime=5, verboze=False, time_seed=time_seed):
    global global_index
    global_index += 1
    this_func_index = global_index
    times[this_func_index] = lifetime
    while times[this_func_index] > 0:
        if verboze:
            print(f'Function N {this_func_index} lifetime left {times[this_func_index]}')
        await asyncio.sleep(time_seed)
        times[this_func_index] -= time_seed
    times.pop(this_func_index)
    if verboze:
        print(f'Function N {this_func_index} game over')


def show_info_infinitly(seed=1):
    while len(times):
        print(times)
        time.sleep(seed)


async def async_show_info_infinitly(seed=1):
    # while len(times):
    while True:
        print(times)
        await asyncio.sleep(seed)
