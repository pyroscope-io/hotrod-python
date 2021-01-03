import requests
import time


def make_requests_every(time_between_requests, max_requests=100):
    i = 0
    while i < max_requests:
        if i < max_requests / 2:
            resp = requests.get('http://localhost:8080/dispatch?customer=392&nonse=0.3238248658061229&mutex_delay=0')
        else:
            resp = requests.get('http://localhost:8080/dispatch?customer=392&nonse=0.3238248658061229&mutex_delay=2')

        print(f'making request #{i}...with response code #{resp.status_code}')
        time.sleep(time_between_requests)
        i = i + 1

    print('done')

# Python program to use 
# main for function call.
if __name__ == "__main__":
    make_requests_every(0.1, 1000)



