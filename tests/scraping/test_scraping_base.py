import pytest
from src.scraping.scraping_base import ScrapingBase


def test_get_html():
    """get_html関数の正常テスト
    """
    test_url = "https://waraitext.com/post-75/"
    sb = ScrapingBase(url=test_url)
    html = sb.get_html()

    assert html


def test_get_soup():
    """get_soupの正常テスト
    """
    test_url = "https://waraitext.com/post-75/"
    sb = ScrapingBase(url=test_url)
    soup = sb.get_soup()

    assert soup
