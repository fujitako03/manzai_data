import pytest
from src.scraping.waraitext import WaraiTextManzai


def test_get_title():
    test_url = "https://waraitext.com/post-75/"
    wt = WaraiTextManzai(
        url=test_url
    )
    title = wt._get_title()
    
    assert title == '暴走族'
