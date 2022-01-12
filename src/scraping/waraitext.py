import bs4

from scraping_base import ScrapingBase


class WaraiTextManzai(ScrapingBase):
    def __init__(self, url):
        self.url=url
        self.page_soup=self.get_soup()
        pass

    def _get_title(self):
        self.page_soup.
