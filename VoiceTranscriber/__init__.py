import speech_recognition as sr
from pydub import AudioSegment

# 音声ファイルのパスを指定
audio_file = "output.wav"

# 音声ファイルを読み込み
audio = AudioSegment.from_wav(audio_file)
audio.export("converted.wav", format="wav")

# 音声認識のインスタンスを作成
recognizer = sr.Recognizer()

# 音声ファイルを読み込み
with sr.AudioFile("converted.wav") as source:
    audio_data = recognizer.record(source)

# 音声をテキストに変換
try:
    text = recognizer.recognize_google(audio_data, language="ja-JP")
    print("認識結果: " + text)
    # 保存するファイルのパスと名前
    file_path = "output_text_file.txt"

    # 文字列をテキストファイルに保存
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"文字列が {file_path} に保存されました。")
except sr.UnknownValueError:
    print("音声を理解できませんでした")
except sr.RequestError as e:
    print("サービスに接続できませんでした; {0}".format(e))