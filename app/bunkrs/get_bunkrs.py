from app.bunkrs import scrape
from app.bunkrs import models

SALE_DOMAIN = 'http://www.annm.army.cz/index.php?id=21&zobr=nab&up=&typ=bs'
PREPARE_DOMAIN = 'http://www.annm.army.cz/index.php?id=21&zobr=prp&up=&typ=bs'


def get_links(url, offer_type="sale"):
    html = scrape.get_html(url)
    for link in html.select('a'):
        if scrape.is_detail_link(link['href']) and len(link.findChildren('img')) == 0:
            bunkr_url = 'http://www.annm.army.cz/' + link['href']
            get_bunkr_data(html=scrape.get_html(bunkr_url), bunkr_url=bunkr_url, offer_type=offer_type)


def get_bunkr_data(html, bunkr_url, write=False, debug=False, offer_type="sale"):
    bunkr_data = html.find('div', class_='textvlevo')

    bunkr = models.Bunkr.load(bunkr_data.select('h3')[0].string)
    if bunkr is not None:
        bunkr.offer_type = offer_type
        bunkr.edit()

    else:
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
        bunkr.offer_type = offer_type
        try:
            bunkr.save()
        except Exception:
            pass

    if write:
        bunkr.print_bunkr()


def main():
    get_links(SALE_DOMAIN, offer_type="sale")
    get_links(PREPARE_DOMAIN, offer_type="prepare")
