import threading
import time

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

def get_bunch_audio_links(links, result):
    output = []
    for link in links:
        if link:
            output.append(get_audio_link(link))
            result.append(output)

def main():
    num_of_threads = 2

    print('Start of program.')

    start_time = time.time()
    audiolists = []
    links = get_episodes_links()

    partition = len(links) // num_of_threads

    downloadThreads = []

    # Create and start the Thread objects.
    for i in range(0, len(links), partition):
        downloadThread = threading.Thread(target=get_bunch_audio_links, args=(links[i: i+partition], audiolists))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    # Wait for all threads to end.
    for thread in downloadThreads:
       thread.join()

    end_time = time.time()

    print('End of program.')
    print(f'Download links took {int(end_time - start_time)} seconds')

if __name__ == '__main__':
    main()
