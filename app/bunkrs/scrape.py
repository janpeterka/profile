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


def get_text(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True, timeout=5)) as response:
            if is_good_response(response):
                return response.text
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
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def is_good_link(string):
    # if "pdf" in string:
    #     return False
    if string.startswith("https://") or string.startswith("http://"):
        return True

    # return False
    return False


def is_sublink(link):
    if link.startswith("/"):
        return True
    return False


def is_in_domain(string):

    # pattern = re.compile("^([a-zA-Z0-9_\-\.]+)\.cuni\.([a-zA-Z0-9_\-\.]+)$")
    # return pattern.match(string)
    if string.find(DOMAIN) > -1:
        return True

    return False


def save_html(html):
    file = open("./temp/html.html", "w+")
    file.write(html)
    file.close()


# def save_email(email):
#     file = open("./temp/emails.txt", "a")
#     file.write(email + "\n")
#     file.close()


# def is_new_link(link):
#     file = open("./temp/list.txt", "r")
#     for line in file:
#         if (link + "\n") == line:
#             return False
#     file.close()
#     return True


# def is_new_email(email):
#     file = open("./temp/emails.txt", "r")
#     for line in file:
#         if (email + "\n") == line:
#             return False
#     file.close()
#     return True


# def find_emails(text):
#     new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text, re.I))
#     return new_emails

def get_html(url):
    html = BeautifulSoup(simple_get(url), 'html.parser', from_encoding="utf-8")
    return html

def show_html(url):
    html = BeautifulSoup(simple_get(url), 'html.parser', from_encoding="utf-8")
    print(html)

def get_raw_html(url):
    raw_text = get_text(url)
    return raw_text


# def send_mail(email, link):
    # pass


# def empty_document():
    # open("./temp/list.txt", "w").close()
    # open("./temp/emails.txt", "w").close()



# empty_document()
# save_html(show_html('http://www.annm.army.cz/index.php?id=21&zobr=nab&up=&typ=bs'))
