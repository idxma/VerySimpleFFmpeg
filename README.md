# VerySimpleFFmpeg
 - FFmpegをGUIで使えるようにしたもの
 - 機能は私が個人的に使いたいものしか入れてませんので実用性皆無
 - ソースコードも配布してるので、自由に拡張してもらって構いません。
 - Windowsのみ動作検証済み

## How to use
 - [FFmpeg](https://www.ffmpeg.org/download.html)をインストールし、binファイルのパスを以下に通してください。
```sh
C:/ffmpeg/bin/
```
 - ffmpeg-pythonをインストール
```sh
$ pip install ffmpeg-python
```
 - VerySimpleFFmpeg.exeの起動

## 機能
![171c067b2abdc9572767e2f6ab6e6b4a](https://github.com/user-attachments/assets/7ff49470-d072-43c0-b406-6afd7bc94d76)

 - H.264からH.265への変換
 - H.265からH.264への変換
 - mp4ファイルをwavへ変換
 - 30fpsへフレームレート変更
