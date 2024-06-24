from pydub import AudioSegment

import os

# 現在のフォルダ位置を取得
current_directory = os.getcwd()
print(f"現在のフォルダ位置: {current_directory}")

# m4aファイルのパス
input_file = "input.m4a"

# 出力するWAVファイルのパス
output_file = "output.wav"

# m4aファイルを読み込む
audio = AudioSegment.from_file(input_file, format="m4a")

# WAVファイルとして保存
audio.export(output_file, format="wav")

print("変換が完了しました。")