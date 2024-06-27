import os
from pydub import AudioSegment
import speech_recognition as sr

def convert_audio_to_text(audio_file):
    # ファイルの拡張子を取得
    file_extension = os.path.splitext(audio_file)[1].lower()

    # 拡張子に応じて音声ファイルを読み込み
    if file_extension == ".wav":
        audio = AudioSegment.from_wav(audio_file)
    elif file_extension == ".m4a":
        audio = AudioSegment.from_file(audio_file, format="m4a")
    else:
        raise ValueError("サポートされていないファイル形式です: {}".format(file_extension))

    # 一時的にWAV形式で保存
    temp_wav_file = "temp_audio.wav"
    audio.export(temp_wav_file, format="wav")

    # 音声認識のインスタンスを作成
    recognizer = sr.Recognizer()

    # 一時ファイルから音声データを読み込み
    with sr.AudioFile(temp_wav_file) as source:
        audio_data = recognizer.record(source)

    # 一時ファイルを削除
    os.remove(temp_wav_file)

    # 音声をテキストに変換
    try:
        text = recognizer.recognize_google(audio_data, language="ja-JP")
        return "認識結果: " + text
    except sr.UnknownValueError:
        return "音声を理解できませんでした"
    except sr.RequestError as e:
        return "サービスに接続できませんでした; {0}".format(e)

# 使用例
audio_file_path = "audiofile.m4a"  # ここに音声ファイルのパスを指定
print(convert_audio_to_text(audio_file_path))