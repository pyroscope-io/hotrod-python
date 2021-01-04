import requests
import time
import threading
from queue import Queue
import multiprocessing

def make_requests_every(time_between_requests, max_requests):
    i = 0
    while i < max_requests:
        if i < max_requests / 2:
            resp_status = make_request(delay=1)
        else:
            threads = []
            # num_threads = max(10, multiprocessing.cpu_count() * 4)
            num_threads = 2

            for j in range(num_threads):
                t = threading.Thread(target=make_request, args=[2])
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


def make_request(delay):
    print(f'making request with delay {delay}')
    resp = requests.get(f'https://python-hotrod.pyroscope.io/dispatch?customer=392&nonse=0.3238248658061229&mutex_delay={delay}')
    return resp.status_code
# Python program to use 
# main for function call.
if __name__ == "__main__":
    make_requests_every(1, 500)



