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
        print(df_raw)
        print(df_unique)

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


if __name__=='__main__':
    warai_text = WaraiTextPreprocess(
        data_path="./output/waraitext/warai_text_20220120214525.json"
    )
    warai_text.preprocess()
