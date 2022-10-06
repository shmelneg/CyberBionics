from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def handler(started=0, finished=0):
    result = 1
    while finished >= started:
        result *= finished
        finished -= 1

    return result


def run_by_executor(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    # we are going to find the factorial of 100 but divided into two parts: 1-50 and 51-100
    future1 = executor.submit(handler, started=1, finished=50)
    future2 = executor.submit(handler, started=51, finished=100)

    result = future2.result() * future1.result()
    executor = executor_class.__name__
    spent_time = time.time() - started
    print(f'Result: {result}. Time for {executor}: {spent_time}')


print('Executing and getting time...')
run_by_executor(ThreadPoolExecutor)
run_by_executor(ProcessPoolExecutor)
