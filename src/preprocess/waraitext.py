import re

import pandas as pd


class WaraiTextPreprocess:
    def __init__(
        self,
        data_path: str
    ) -> None:
        self.data_path = data_path
    
    def preprocess(self) -> None:
        """rawデータを処理しやすい形に加工する
        """
        df_raw = self._read()
        df_unique = self._distinct(df_raw)
        for nt in df_unique["neta_text"]:
            print(nt.split("\n")[0])

    def _read(self) -> pd.DataFrame:
        """jsonからデータを読み込む

        Returns:
            pd.DataFrame: 読み込んだJSONをDFに変換したもの
        """
        df_raw = pd.read_json(
            self.data_path
        )
        df = df_raw.copy()

        return df
    
    def _distinct(self, df_raw: pd.DataFrame) -> pd.DataFrame:
        """重複を排除する

        Args:
            df_raw (pd.DataFrame): 重複ありのDF

        Returns:
            pd.DataFrame: 重複排除したDF
        """
        df_unique = df_raw.drop_duplicates().reset_index(drop=True)

        return df_unique
    

class NetaText:
    def __init__(
        self,
        neta_text: str,
        neta_type: str,
    ) -> None:
        self.neta_text = neta_text
        self.neta_type = neta_type
        self.comment_list = self.neta_text.split("\n")
    
    def preprocess(self):
        text_list = self._spilt_by_comment()
        print(text_list)
    
    def _spilt_by_comment(self):
        return self.neta_text.split("\n")
    
    @staticmethod
    def _remove_symbols(comment):
        symbols = r"『』："
        return re.sub(f"[{symbols}]", "", comment)
    
    @staticmethod
    def _get_talker(
        comment: str
    ) -> str:
        """ネタの1センテンスから話者を取得する

        Args:
            comment (str): ネタの1センテンス

        Returns:
            str: 話者の名前
        """
        colon = re.search(r"：", comment)
        kakko = re.search(r"『", comment)
        if (colon) and (not kakko):
            talker_raw = re.findall(r".+：", comment)
            return talker_raw[0][:-1]
        elif (not colon) and (kakko):
            talker_raw = re.findall(r".+『", comment)
            return talker_raw[0][:-1]
        else:
            return None

if __name__=='__main__':
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
    for comment in test_neta_list:
        talker = nt._remove_symbols(comment)
        print(talker)


    # # preprocess
    # warai_text = WaraiTextPreprocess(
    #     data_path="./output/waraitext/warai_text_20220120214525.json"
    # )
    # warai_text.preprocess()

