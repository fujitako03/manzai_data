import time

import bs4
import requests


class ScrapingBase:
    """スクレイピングで共通に利用するモジュールを集めたクラス

    Args:
        url (str): スクレイピングするURL
        weit_sec (int, optional): スクレイピングの間隔. Defaults to 1.
    """
    def __init__(
        self,
        url: str,
        weit_sec: int=1):
        self.url = url
        self.weit_sec = weit_sec

    def get_soup(
        self,
        parser='html.parser',
        file_encoding='utf-8'):
        """ urlからBeautifulSoupオブジェクトを取得する
        Args:
            parser (str, optional): パーサー Defaults to 'res.parser'.
            file_encoding (str, optional): htmlファイルのエンコード. Defaults to 'utf-8'.

        Returns:
            [type]: BeautifulSoupオブジェクト
        """
        try:
            # htmlを取得
            html = self.get_html()

            # htmlをbeautifulSoupオブジェクトに変換
            soup = self.parse_html(
                html=html, 
                parser=parser,
                file_encoding=file_encoding)
            return soup
        except:
            raise

    def get_html(self):
        """urlからhtmlを取得する
        Raises:
            Exception: htmlの取得が失敗
        Returns:
            str: 取得したhtml テキスト
        """
        time.sleep(self.weit_sec)  # サーバ負荷軽減のため
        try:
            print(url)
            res = requests.get(self.url)
            if res.status_code == 200:
                # 成功
                return res.text
            else:
                # 失敗
                res.raise_for_status()
        except:
            raise Exception("htmlの取得に失敗しました")

    def parse_html(self, html, parser='html.parser', file_encoding='utf-8'):
        """htmlをパースしBeautifulSoupオブジェクトを返す
        Args:
            html (str): HTMLテキスト
            parser (str, optional): パーサー Defaults to 'res.parser'.
            file_encoding (str, optional): htmlファイルのエンコード. Defaults to 'utf-8'.
        Raises:
            ValueError: htmlのパースに失敗したとき
        Returns:
            : BeautifulSoup
        """
        try:
            soup = bs4.BeautifulSoup(html, parser, from_encoding=file_encoding)
            return soup
        except:
            raise ValueError("htmlのパースに失敗しました")


if __name__=='__main__':
    url = 'https://kanjitisiki.com/zyouyou/'
    soup = get_soup_from_url(url)
    print(soup)