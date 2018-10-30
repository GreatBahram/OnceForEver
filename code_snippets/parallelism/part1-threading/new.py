#!/usr/bin/env python3
import logging
import queue
import threading
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

log = True # change it to False if you don't like the logging

main_url = 'https://talkpython.fm'

# config logger
logging.basicConfig(level=logging.INFO, format='%(asctime)-12s - %(name)s - %(levelname)s - %(message)s', datefmt='%y/%m/%d %H-%M-%S')
logger = logging.getLogger(__name__)
if not log:
    logger.propagate = False

def get_episodes_links(url):
    """ """
    with requests.get(url) as request:
        data = request.text
        soup = BeautifulSoup(data, 'lxml')
        links = [main_url + link.attrs['href'] for link in soup.select('.table-hover a')]
        return links

def get_audio_link(link):
    """ return audio link from given link"""
    with requests.get(link) as request:
        data = request.text
        soup = BeautifulSoup(data, 'lxml')
        audio_link = soup.select_one('.subscribe-btn')
        logger.info(f'Getting audio link for {Path(audio_link.attrs["href"]).name}...')
        return main_url + audio_link.attrs['href']

def download_link(directory, link):
    """ download and save the audio """
    logger.info(f'Downloaded {link}')
    pass

def main():
    start_time = time.time()
    logger.info('Start of program.')
    episodes_url = main_url + '/episodes/all'
    episodes_links = get_episodes_links(episodes_url)
    audiolists = []
    for episode_link in reversed(episodes_links):
        audiolists.append(get_audio_link(episode_link))
    logger.info('End of program.')
    end_time = time.time()
    print(f'Download links took {int(end_time - start_time)} seconds')

if __name__ == '__main__':
    main()
