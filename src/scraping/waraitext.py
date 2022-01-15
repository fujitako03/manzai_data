import re

import bs4

from .scraping_base import ScrapingBase


class WaraiTextManzai(ScrapingBase):
    def __init__(self, url):
        super().__init__(url, weit_sec=1)
        self.url=url
        self.page_soup=self.get_soup()
        pass
    
    def get_page_info(self) -> dict:
        pass

    def _get_neta_type(self) -> str:
        """ネタの種類

        Returns:
            str: ネタの種類
        """
        page_title = self.page_soup.select_one("title").get_text()
        neta_type = re.findall("^.+?(?= )", page_title)[0]
 
        return neta_type

    def _get_performer(self) -> str:
        """演者（ピン・コンビ）の名前を取得

        Returns:
            str: 演者名
        """
        page_title = self.page_soup.select_one("title").get_text()
        performer = re.findall("(?<= ).+?(?=【)", page_title)[0]
 
        return performer

    def _get_title(self) -> str:
        """漫才のタイトルを抽出

        Returns:
            str: 漫才タイトル
        """
        page_title = self.page_soup.select_one("title").get_text()
        manzai_title = re.findall("(?<=【).+?(?=】)", page_title)[0]

        return manzai_title
    
if __name__=='__main__':
    wt = WaraiTextManzai(
        url="https://waraitext.com/post-75/"
    )
    wt._get_title()
    wt._get_manzai_shi()
