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
    wt = WaraiTextManzai(
        url="https://waraitext.com/post-75/"
    )
    wt._get_neta()
    # wt._get_title()
    # wt._get_manzai_shi()
