import scrape

DOMAIN = 'https://gjk.cz/o-studiu/rozvrh-a-suplovani/suplovani/'
TEACHER_NAME = 'Peterka Jan'


def get_info(teacher_name):
    html = scrape.get_html(DOMAIN)
    # print(html)
    html = html.find('div', id='suplovani')
    # for day in html.findAll('p', class_='textlarge_3'):
    for table in html.findAll('table', class_='tb_suplucit_3'):

        IS_MINE = False

        for line in table.findAll('tr'):
            first_cell = line.find('td')
            if (first_cell.find('p') is not None):
                if first_cell.find('p').string.strip() == teacher_name:
                    IS_MINE = True
                else:
                    IS_MINE = False
            if IS_MINE:
                print(line.text)

    print("To je vše")


get_info(TEACHER_NAME)
