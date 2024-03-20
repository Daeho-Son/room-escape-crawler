#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from csv_util import create_csv, write_to_csv_with_dict

URL = 'https://colory.mooo.com/bba/catalogue'
FILE_NAME = '코로리.csv'
FIELD_NAMES = ['지역', '매장', '테마', '별점', '난이도', '리뷰수']


def main():
    create_csv(FILE_NAME, FIELD_NAMES)
    response = requests.get(URL)
    if not response.ok:
        print("get 요청 실패: ", response)
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    for theme_button in soup.select('div.themes-info div'):
        theme = dict()
        country = theme_button.find('h5').text
        shop = ''
        for info in theme_button.select('tbody td'):
            if info.css.match('.info-1'):
                shop = info.text
            elif info.css.match('.info-2'):
                theme = {'지역': country, '매장': shop, '테마': info.text}
            elif info.css.match('.info-3'):
                theme['별점'] = info.text
            elif info.css.match('.info-4'):
                theme['난이도'] = info.text
            elif info.css.match('.info-5'):
                theme['리뷰수'] = info.text
                write_to_csv_with_dict(FILE_NAME, FIELD_NAMES, theme)


if __name__ == '__main__':
    main()
