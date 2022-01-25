import pandas as pd


class WaraiTextPreprocess:
    def __init__(
        self,
        data_path: str
    ) -> None:
        self.data_path = data_path
    
    def preprocess(self) -> None:
        df_raw = self._read()
        print(df_raw)

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


if __name__=='__main__':
    warai_text = WaraiTextPreprocess(
        data_path="./output/waraitext/warai_text_20220120214525.json"
    )
    warai_text.preprocess()
