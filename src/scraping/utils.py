import json
from pathlib import Path


def write_dict_to_json(output_dic: dict, file_path: str) -> None:
    path = Path(file_path)

    if path.is_file():
        # 読み込み
        with open(file_path, 'r', encoding='utf-8') as f:
            read_data = json.load(f)

        # 結合        
        save_data = [read_data, output_dic]
    else:
        save_data = [output_dic]

    # 出力
    with open(file_path, 'w') as f:
        json.dump(save_data, f, ensure_ascii=False)
