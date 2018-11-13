import time
from concurrent.futures import ThreadPoolExecutor

import requests

from bs4 import BeautifulSoup

main_url = 'https://talkpython.fm'

def get_episodes_links():
    """ Gets all episodes links"""
    episodes_url = main_url + '/episodes/all'
    with requests.get(episodes_url) as request:
        data = request.text
        soup = BeautifulSoup(data, 'lxml')
        links = [main_url + link.attrs['href'] for link in soup.select('.table-hover a')]
        return links

def get_audio_link(link):
    """ return audio link for a given link"""
    with requests.get(link) as request:
        data = request.text
        soup = BeautifulSoup(data, 'lxml')
        audio_link = soup.select_one('.subscribe-btn')
        #print(f'Getting audio link for {Path(audio_link.attrs["href"]).name}...')
        return main_url + audio_link.attrs['href']

def download_link(directory, link):
    """ download and save the audio """
    print(f'Downloaded {link}')

def main():
    num_of_threads = 10

    print('Start of program.')

    start_time = time.time()
    audiolists = []
    links = get_episodes_links()

    with ThreadPoolExecutor(max_workers=num_of_threads) as pool:
        audiolists = pool.map(get_audio_link, links)

    end_time = time.time()

    print('End of program.')
    print(f'Download links took {int(end_time - start_time)} seconds')

if __name__ == '__main__':
    main()
