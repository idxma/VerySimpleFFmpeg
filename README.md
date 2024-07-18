# VerySimpleFFmpeg
 - FFmpegをGUIで使えるようにしたもの
 - 機能は私が個人的に使いたいものしか入れてませんので実用性皆無
 - ソースコードも配布してるので、自由に拡張してもらって構いません。

## How to use
 - [FFmpeg](https://www.ffmpeg.org/download.html)をインストールし、binファイルのパスを以下に通してください。
```sh
C:/ffmpeg/bin/
```
 - ffmpeg-pythonをインストール
```sh
$ pip install ffmpeg-python
```

## 機能
 - H.264からH.265への変換
 - H.265からH.264への変換
 - mp4ファイルをwavへ変換
 - 30fpsへフレームレート変更
