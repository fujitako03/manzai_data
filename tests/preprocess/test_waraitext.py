import pytest
from src.preprocess.waraitext import WaraiTextPreprocess


def test_read():
    wtp = WaraiTextPreprocess(
        data_path="./output/waraitext/warai_text_20220120214525.json"
    )
    df = wtp._read()

    assert df["post_id"][0] == "post-100"
    assert df["performer"][0] == "フットボールアワー"
    assert df["post_id"][1] == "post-200"
    assert df["performer"][1] == "ノンスタイル"
