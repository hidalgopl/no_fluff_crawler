import sample_settings
from crawler import NoFluffFilteredPage

if __name__ == '__main__':
    c = NoFluffFilteredPage(no_fluff_url=sample_settings.LOOKUP_URL)
    c.connect()
    c.click_load_more()
    c.get_offers()
    c.crawl()
    c.parse_data()
    # c.show_data()
    c.dump_to_json(sample_settings.OUTPUT_FILENAME)
