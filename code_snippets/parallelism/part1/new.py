#!/usr/bin/env python3
import queue
import time
import threading

import requests
from bs4 import BeatifulSoup

main_url = 'https://talkpython.fm'
episodes = 'https://talkpython.fm/episodes/all'

def get_links(url):
    audiolists = []
    with requests.get(url) as request:
        data = request.text
        soup = BeatifulSoup(data, 'lxml')
        links = soup.select('.table-hover a')
    for link in links:

    return audiolists

def download_link(directory, link)
def main():
    print('Start of program.')
    threadlist = []
    for number in range(1, 6):
        thread = threading.Thread(target=worker, args=(number,))
        threadlist.append(thread)
        thread.start()
    for item in threading.enumerate():
        print(item.getName())

if __name__ == '__main__':
    main()
