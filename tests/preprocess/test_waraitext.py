import pytest
from src.preprocess.waraitext import NetaText, WaraiTextPreprocess


def test_read():
    wtp = WaraiTextPreprocess(
        data_path="./output/waraitext/warai_text_20220120214525.json"
    )
    df = wtp._read()

    assert df["post_id"][0] == "post-100"
    assert df["performer"][0] == "フットボールアワー"
    assert df["post_id"][1] == "post-200"
    assert df["performer"][1] == "ノンスタイル"


def test_text_split():
    test_neta_type = "漫才"
    test_neta_text = "石田『井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました』（リアルボケ）\n井上『誰やそいつ』\n石田『ぺぺさんが』（リアルボケ）\n井上『異文化交流とってないから。そこは日本でいこう』（言葉遊びフリ）"
    test_neta_list = [
        "石田『井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました』（リアルボケ）",
        "井上『誰やそいつ』",
        "石田『ぺぺさんが』（リアルボケ）",
        "井上『異文化交流とってないから。そこは日本でいこう』（言葉遊びフリ）",
    ]
    nt = NetaText(
        neta_text=test_neta_text,
        neta_type=test_neta_type,
    )

    assert nt._spilt_by_comment() == test_neta_list


def test_get_talker():
    test_neta_type = "漫才"
    test_neta_text = "石田『井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました』（リアルボケ）\n井上『誰やそいつ』\n石田『ぺぺさんが』（リアルボケ）\n井上『異文化交流とってないから。そこは日本でいこう』（言葉遊びフリ）"
    test_neta_list = [
        "石田『井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました』（リアルボケ）",
        "井上『誰やそいつ』",
        "石田『ぺぺさんが』（リアルボケ）",
        "井上『異文化交流とってないから。そこは日本でいこう』（言葉遊びフリ）",
        "国崎：全、谷村新司に告ぐ（なりきりボケ）"
    ]
    nt = NetaText(
        neta_text=test_neta_text,
        neta_type=test_neta_type,
    )
    assert nt._get_talker(test_neta_list[0]) == "石田"

def test_remove_symbols():
    test_neta_type = "漫才"
    test_neta_text = "石田『井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました』（リアルボケ）\n井上『誰やそいつ』\n石田『ぺぺさんが』（リアルボケ）\n井上『異文化交流とってないから。そこは日本でいこう』（言葉遊びフリ）"
    nt = NetaText(
        neta_text=test_neta_text,
        neta_type=test_neta_type,
    )
    raw_text = "『井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました』"
    remove_text = "井上さん大変です。西高の奴らにうちの学校のズ・グヌンバペペがやられてしまいました"
    assert nt._remove_symbols(raw_text) == remove_text


