import pytest
from src.scraping.waraitext import WaraiTextCrawler, WaraiTextScraper


def test_crawler():
    wc = WaraiTextCrawler(
        start_index=75,
        neta_num=3,
    )
    wc.main()

    assert True # TODO 正しくテストに書き換える

def test_scraping():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextScraper(
        url=test_url
    )
    neta_text = wt.scraping()

    assert neta_text

def test_get_post_id():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextScraper(
        url=test_url
    )
    post_id = wt._get_post_id()
    
    assert post_id == 'post-75'

def test_get_title():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextScraper(
        url=test_url
    )
    title = wt._get_title()
    
    assert title == '暴走族'

def test_get_performer():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextScraper(
        url=test_url
    )
    manzai_shi = wt._get_performer()
    
    assert manzai_shi == '紳助竜介'

def test_get_neta_type():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextScraper(
        url=test_url
    )
    neta_type = wt._get_neta_type()
    
    assert neta_type == '漫才'

def test_get_neta_text():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextScraper(
        url=test_url
    )
    neta_text = wt._get_neta_text()
    print(neta_text)
    
    assert neta_text
