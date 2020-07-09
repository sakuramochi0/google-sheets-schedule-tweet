from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

# from get_tweepy import get_api

base_url = 'https://twitter.com/i/moments'


# api = get_api('skrmch_rhythpri')


### Utility functions ###
def get_soup(url):
    """URL の BeautifulSoup オブジェクトを取得する。"""
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def get_moment_urls():
    """現在の全モーメントの URL を取得する。"""
    soup = get_soup(base_url)
    urls = set()

    # すべてのタブをたどる
    tab_links = soup.select('li.MomentGuideNavigation-item a')
    for tab_link in tab_links:
        url = urljoin(base_url, tab_link['href'])
        if not url.startswith('https://'):
            continue
        soup = get_soup(url)
        links = soup.select('.MomentCapsuleSummary-details a')

        # すべてのモーメントをたどる
        for link in links:
            url = link['href']
            if not url.startswith('https://'):
                continue
            urls.add(url)

    return urls


def block_users(users):
    ids = list(map(lambda user: user.id, users))
    api.block_ids(ids)


def get_users(moment_url):
    pass


def filter_followers(users):
    pass


def main():
    moment_urls = get_moment_urls()
    print(len(moment_urls))
    for moment_url in moment_urls:
        users = get_users(moment_url)
        users = filter_followers(users)
        # block_users(users)

if __name__ == '__main__':
    main()