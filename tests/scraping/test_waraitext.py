import pytest
from src.scraping.waraitext import WaraiTextManzai


def test_get_title():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextManzai(
        url=test_url
    )
    title = wt._get_title()
    
    assert title == '暴走族'

def test_get_performer():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextManzai(
        url=test_url
    )
    manzai_shi = wt._get_performer()
    
    assert manzai_shi == '紳助竜介'

def test_get_neta_type():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextManzai(
        url=test_url
    )
    neta_type = wt._get_neta_type()
    
    assert neta_type == '漫才'
