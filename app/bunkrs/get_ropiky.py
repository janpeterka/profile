import re

from app.bunkrs.scrape import get_html

from app import models

# from app.models import Bunkr

# from app.models import create_session

# session = create_session()
# from scrape import get_raw_html, save_html


SALE_DOMAIN = 'http://www.annm.army.cz/index.php?id=21&zobr=nab&up=&typ=bs'
PREPARE_DOMAIN = 'http://www.annm.army.cz/index.php?id=21&zobr=prp&up=&typ=bs'


def is_detail_link(link):
    pattern = re.compile("(https?://)?[a-z0-9./?=&]+&det=[0-9]+")
    # pattern = re.compile("https?://[a-z0-9./?=&]+&det=[0-9]+")
    return pattern.match(link)


def get_links(url):
    html = get_html(url)
    for link in html.select('a'):
        if is_detail_link(link['href']) and len(link.findChildren('img')) == 0:
            bunkr_url = 'http://www.annm.army.cz/' + link['href']
            print("OK: {0}".format(bunkr_url))
            get_bunkr_data(html=get_html(bunkr_url), bunkr_url=bunkr_url)

    bunkrs = models.Bunkr.loadAll()
    for bunkr in bunkrs:
        print(bunkr.name)


def get_bunkr_data(html, bunkr_url, write=False, debug=False):
    bunkr_data = html.find('div', class_='textvlevo')

    bunkr = models.Bunkr()

    bunkr.name = bunkr_data.select('h3')[0].string

    # table
    bunkr_data_table = bunkr_data.select('table')[0]
    if debug:
        print(bunkr_data_table)

    bunkr_data_table_rows = bunkr_data_table.findAll('tr')
    if debug:
        print(bunkr_data_table_rows[0])

    bunkr.link = bunkr_url
    bunkr.sale_date = bunkr_data_table_rows[0].select('td')[1].contents[1]
    bunkr.katastr = bunkr_data_table_rows[1].find('td').contents[1]
    bunkr.obec = bunkr_data_table_rows[2].find('td').contents[1]
    bunkr.kraj = bunkr_data_table_rows[3].find('td').contents[1]
    bunkr.uzemi = bunkr_data_table_rows[6].find('td').contents[1]
    bunkr.min_sale_price = bunkr_data_table_rows[7].find('td').contents[1]
    try:
        bunkr.save()
    except Exception:
        pass

    if write:
        bunkr.print_bunkr()


# session.rollback()
# session.close()
# get_links(get_html(SALE_DOMAIN))
