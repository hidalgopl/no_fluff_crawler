from collections import OrderedDict
from json import dumps
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver

import sample_settings
from utils import create_output_dict


class NoFluffFilteredPage:
    no_fluff_url = ''
    response = None
    load_more_button = None
    offers = None
    driver = None
    offers_data = None
    header = ''
    data = []

    def __init__(self, no_fluff_url):
        self.url = no_fluff_url

    def connect(self):
        self.driver = webdriver.Chrome()
        try:
            self.response = self.driver.get(self.url)
        except:
            raise ValueError('Please provide a correct url!')

    def click_load_more(self):
        self.load_more_button = self.driver. \
            find_element_by_class_name(sample_settings.LOAD_MORE_SELECTOR)
        self.load_more_button.click()

    def get_offers(self):
        self.offers = self.driver. \
            find_elements_by_css_selector(sample_settings.OFFERS_SELECTOR)

    def crawl(self):
        count = 0
        self.offers_data = {}
        for i in range(len(self.offers)):
            self.offers = self.driver. \
                find_elements_by_css_selector(sample_settings.OFFERS_SELECTOR)
            span = self.offers[i]
            try:
                title = span.find_element_by_tag_name('h4')
                self.header = title.text
                if sample_settings.MUST_NOT in self.header or sample_settings.MUST not in self.header:
                    continue
            except:
                print('Oops! Something went wrong.')
            count += 1
            try:
                title.click()
                inner_data = self.driver.find_element_by_tag_name('body') \
                    .get_attribute('innerHTML')
                self.offers_data[self.header] = inner_data
                self.driver.back()
            except:
                continue
            sleep(sample_settings.WAIT_INTERVAL)
        self.driver.quit()

    def parse_data(self):
        for k, v in self.offers_data.items():
            inner_soup = BeautifulSoup(v, 'html.parser')
            req = inner_soup.find_all(
                'li',
                sample_settings.REQUIREMENTS_SELECTORS
            )
            salary = inner_soup.find(
                'span',
                sample_settings.SALARY_SELECTOR
            ).string
            specs = inner_soup.find('div', sample_settings.SPECS_SELECTOR)
            specs_column = specs.find('ul', class_='column2')
            specs_values = specs_column.find_all('li')
            specs_str = [s.string for s in specs_values]
            sp1 = specs_str[::2]
            sp2 = specs_str[1::2]
            sp = OrderedDict()
            for i, j in zip(sp1, sp2):
                sp[i] = j
            req2 = [r.string for r in req]
            details = create_output_dict(k, salary, req2, sp)
            self.data.append(details)

    def show_data(self):
        print(self.data)

    def dump_to_json(self, filename='offers.json'):
        with open(filename, 'w') as outfile:
            outfile.write(dumps(self.data, indent=4))
        print('Exported to: {}'.format(filename))
