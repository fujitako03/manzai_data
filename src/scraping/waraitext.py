import json
import re
from datetime import datetime

import bs4

from .scraping_base import ScrapingBase
from .utils import write_dict_to_json


class WaraiTextCrawler:
    def __init__(
        self,
        start_index=100,
        neta_num=100
    ) -> None:
        self.start_index = start_index
        self.neta_num = neta_num
        self.url_base = 'https://waraitext.com/'
        self.output_path = self._make_output_path()

    def main(self):
        index_list = range(self.start_index, self.start_index + self.neta_num)

        for index in index_list:
            # urlを生成
            neta_url = self._make_url(index=index)

            # scrapingを実施
            scraper = WaraiTextScraper(
                url=neta_url
            )
            neta_info = scraper.scraping()

            # jsonファイルに出力
            write_dict_to_json(
                output_dic=neta_info,
                file_path=self.output_path,
            )

    def _make_url(self, index: int) -> str: # TODO ネタかどうかのページ判定ができていない
        """ネタindexからurlを生成する

        Args:
            index (int): ネタのindex

        Returns:
            str: ネタのURL
        """
        return f"{self.url_base}post-{str(index)}"
    
    def _make_output_path(self) -> str:
        """現在時刻から出力ファイル名を生成

        Returns:
            str: outputファイル名
        """
        return f'output/waraitext/warai_text_{datetime.now().strftime("%Y%m%d%H%M%S")}.json'
    
        

class WaraiTextScraper(ScrapingBase):
    def __init__(self, url):
        super().__init__(url, weit_sec=1)
        self.url=url
        self.page_soup=self.get_soup()
        pass
    
    def scraping(self) -> dict:
        """お笑いテキストからネタ情報を取得する

        Returns:
            dict: 情報を集約した辞書
        """
        page_info = {
            "post_id": self._get_post_id(),
            "neta_type": self._get_neta_type(),
            "performer": self._get_performer(),
            "title": self._get_title(),
            "neta_text": self._get_neta_text(),
        }
        return page_info

    def _get_post_id(self) -> str:
        url =self.page_soup.find("meta", property="og:url").get("content")
        post_id = url.split("/")[-2]

        return post_id
        
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
        """ネタのタイトルを抽出

        Returns:
            str: 漫才タイトル
        """
        page_title = self.page_soup.select_one("title").get_text()
        manzai_title = re.findall("(?<=【).+?(?=】)", page_title)[0]

        return manzai_title

    def _get_neta_text(self) -> str:
        """ネタの文章を抽出

        Returns:
            str: ネタの文章
        """
        # 関連するブロックを取得
        neta_content = self.page_soup.select_one("div.entry-content")

        # 不要なタグを削除
        neta_content = self._clean_neta_content(neta_content)

        # pタグを取得
        neta_p = neta_content.select("p")

        # pタグごとに処理
        neta_text_raw = "\n".join([
            self._clean_neta_ptag(p)
            for p
            in neta_p
            if self._clean_neta_ptag(p)])

        return neta_text_raw
    
    def _clean_neta_content(self, content):
        """ネタのブロックを前処理する
        """
        # プロフィールを削除
        content.find("h2").extract()
        content.find("blockquote").extract()
        content.find("script").extract()

        return content
    
    def _clean_neta_ptag(self, p_tag):
        """ネタのpタグを前処理する

        Args:
            p_tag (Tag): p_tag

        Returns:
            Tag: p_tag
        """
        p_text = p_tag.get_text()

        # 改行を削除
        p_text = p_text.replace("\n", "")

        # 関連情報タグの場合Noneを返す
        if p_text.startswith("【関連】"):
            return None

        # 空のタグの場合Noneを返す
        elif p_text == "":
            return None

        else:
            return p_text
    
    
if __name__=='__main__':
    wt = WaraiTextScraper(
        url="https://waraitext.com/post-75/"
    )
    wt._get_neta()
    # wt._get_title()
    # wt._get_manzai_shi()
