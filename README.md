# VoiceTranscriber


## Pythonとpipのインストールと設定

1. Homebrewを使用してPython3をインストール:
HomebrewでPython3をインストールする際、以下のコマンドを使用します。

    ``` zsh
    brew install python
    ```

2. Python3とpip3の確認:
Python3とpip3が正しくインストールされているか確認します。

    ``` zsh
    which python3
    which pip3
    ```

3. 必要なライブラリのインストール
   
    ``` zsh
    pip3 install SpeechRecognition pydub
    pip3 install ffmpeg
    ```




## フォルダ構成
```
your_project/
│
├── your_project/                # メインのPythonパッケージ
│   ├── __init__.py              # パッケージとして認識させるためのファイル
│   ├── module1.py               # モジュール1
│   ├── module2.py               # モジュール2
│   └── ...                      # その他のモジュール
│
├── tests/                       # テストコード
│   ├── __init__.py              # パッケージとして認識させるためのファイル
│   ├── test_module1.py          # モジュール1のテスト
│   ├── test_module2.py          # モジュール2のテスト
│   └── ...                      # その他のテストモジュール
│
├── docs/                        # ドキュメント
│   ├── index.rst                # ドキュメントのインデックスファイル
│   └── ...                      # その他のドキュメントファイル
│
├── scripts/                     # 補助スクリプト
│   ├── script1.py               # スクリプト1
│   └── script2.py               # スクリプト2
│
├── .gitignore                   # Gitで無視するファイルのリスト
├── README.md                    # プロジェクトの概要を説明するREADMEファイル
├── requirements.txt             # 依存関係のリスト
├── setup.py                     # パッケージのインストール設定
├── pyproject.toml               # プロジェクトの設定（オプション、近年は利用が増えている）
├── LICENSE                      # ライセンス情報
└── MANIFEST.in                  # パッケージに含めるファイルのリスト（オプション）
```