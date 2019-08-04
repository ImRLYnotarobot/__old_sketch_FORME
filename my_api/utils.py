import requests
import re
from bs4 import BeautifulSoup
from decimal import *
from datetime import datetime, timedelta


class Converter:
    BANK_API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    BANK_CHARSET = 'cp1251'

    def __init__(self, target_cur=None):

        if target_cur:
            self.target_cur = target_cur.upper()
        else:
            self.target_cur = 'USD'

        self.soup = self.get_soup()

    @classmethod
    def get_soup(cls):
        data_page = requests.get(cls.BANK_API_URL)
        text = data_page.content.decode(cls.BANK_CHARSET)
        text = re.sub(r'(\d)(,)(\d)', cls.re_sub_func, text)
        data = text.encode(cls.BANK_CHARSET)
        soup = BeautifulSoup(data, 'xml')
        return soup

    @staticmethod
    def re_sub_func(matchobj):  # замена запятых на точки
        return '{}.{}'.format(matchobj.group(1), matchobj.group(3))

    def get_rub_coef(self):
        cur = self.soup.find('CharCode', text=self.target_cur)
        if cur:
            nomin = int(cur.find_next_sibling('Nominal').string)
            val = Decimal(str(cur.find_next_sibling('Value').string))
            return nomin / val
        else:
            return None
