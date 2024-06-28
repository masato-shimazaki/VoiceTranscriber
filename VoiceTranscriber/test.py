import os
import tempfile
from pydub import AudioSegment
import speech_recognition as sr

def split_audio(audio, segment_length_ms):
    """
    オーディオを指定した長さに分割する
    :param audio: pydub AudioSegment オブジェクト
    :param segment_length_ms: 分割する長さ（ミリ秒）
    :return: 分割されたAudioSegmentオブジェクトのリスト
    """
    segments = []
    for i in range(0, len(audio), segment_length_ms):
        segments.append(audio[i:i + segment_length_ms])
    return segments

def convert_audio_to_text(audio_segment, index):
    """
    オーディオセグメントをテキストに変換する
    :param audio_segment: pydub AudioSegment オブジェクト
    :param index: セグメントのインデックス
    :return: 音声認識結果のテキスト
    """
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav_file:
        audio_segment.export(temp_wav_file.name, format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_wav_file.name) as source:
        audio_data = recognizer.record(source)

    os.remove(temp_wav_file.name)

    try:
        text = recognizer.recognize_google(audio_data, language="ja-JP")
        return text
    except sr.UnknownValueError:
        return "音声を理解できませんでした"
    except sr.RequestError as e:
        return f"サービスに接続できませんでした; {e}"

def process_audio_file(audio_file):
    """
    音声ファイルを処理してテキストに変換する
    :param audio_file: 音声ファイルのパス
    :return: 各セグメントの音声認識結果のリスト
    """
    file_extension = os.path.splitext(audio_file)[1].lower()

    if file_extension == ".wav":
        audio = AudioSegment.from_wav(audio_file)
    elif file_extension == ".m4a":
        audio = AudioSegment.from_file(audio_file, format="m4a")
    else:
        raise ValueError("サポートされていないファイル形式です: {}".format(file_extension))

    segment_length_ms = 5 * 60 * 1000  # 5分ごとに分割
    segments = split_audio(audio, segment_length_ms)

    results = []
    for i, segment in enumerate(segments):
        text = convert_audio_to_text(segment, i)
        results.append(text)
        print(f"セグメント {i+1}/{len(segments)} の認識結果: {text}")

    return results

# 使用例
audio_file_path = "audiofile.m4a"  # ここに音声ファイルのパスを指定
results = process_audio_file(audio_file_path)

file_path = "output_text_file.txt"

# 文字列をテキストファイルに保存
with open(file_path, "w", encoding="utf-8") as file:
    for result in results:
        file.write(result)
