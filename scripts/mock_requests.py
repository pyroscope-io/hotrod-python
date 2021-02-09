import requests
import time
import random
import sys
import threading
from queue import Queue
import multiprocessing

def make_requests_every(name, time_between_requests, max_requests, num_threads):
    i = 0
    while i < max_requests:
        if i < max_requests / 2:
            resp_status = make_request(name=name, delay=1)
        else:
            threads = []

            r = random.random()
            if r < 0.25:
                delay = 1
            else:
                delay = 2

            for j in range(num_threads):
                t = threading.Thread(target=make_request, args=[name, delay])
                t.start()
                threads.append(t)

            for thread in threads:
                thread.join()

            # for _ in range(10):
            #     resp_status = make_request(delay=2)
        time.sleep(time_between_requests)
        i = i + 1
        print(f'i: {i}/{max_requests}')

    print('done')


def make_request(name, delay):
    print(f'making request with delay {delay}')
    resp = requests.get(f'https://{name}-hotrod.pyroscope.io/dispatch?customer=392&nonse=0.3238248658061229&mutex_delay={delay}')
    return resp.status_code
# Python program to use
# main for function call.
if __name__ == "__main__":
    name = sys.argv[1]
    threads = int(sys.argv[2])
    while True:
        make_requests_every(name, 1, 100, threads)



