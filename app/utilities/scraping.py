from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True, timeout=5)) as response:
            if is_good_response(response):
                return response.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(response):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 and content_type is not None and content_type.find('html') > -1)


def log_error(e):
    print(e)


def get_html(url):
    html = BeautifulSoup(simple_get(url), 'html.parser', from_encoding="utf-8")
    return html


def is_link(link):
    pattern = re.compile("(https?://)?[a-z0-9./?=&]+&det=[0-9]+")
    return pattern.match(link)
