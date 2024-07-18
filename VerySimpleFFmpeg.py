import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext, ttk
import os
import ffmpeg

# FFmpegのパスを確認
ffmpeg_path = "C:/ffmpeg/bin/ffmpeg.exe"  # FFmpegのパスを適宜変更する

if not os.path.isfile(ffmpeg_path):
    ffmpeg_status = "FFmpegのパスが見つかりません"
else:
    ffmpeg_status = "FFmpegのパス: 正常に設定済み"

# ffmpeg-pythonがインストールされているか確認
try:
    import ffmpeg
    ffmpeg_python_status = "ffmpeg-python: インストール済み"
except ImportError:
    ffmpeg_python_status = "ffmpeg-pythonがインストールされていません"

# ファイル選択と変換機能を含んだメインのクラス
class VideoConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("VerySimpleFFmpeg")
        self.geometry("400x640")  # ウインドウサイズを固定

        self.setup_ui()

    def setup_ui(self):
        # フレーム1: ファイル選択と情報表示
        frame1 = tk.Frame(self, padx=10, pady=10)
        frame1.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        select_file_button = ttk.Button(frame1, text="動画ファイルを選択", command=self.select_file, style="Flat.TButton")
        select_file_button.pack(pady=10)

        self.selected_file_label = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=50, height=4)
        self.selected_file_label.pack(pady=10)

        # フレーム2: 変換機能一覧
        frame2 = tk.Frame(self, padx=10, pady=10)
        frame2.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        convert_frame = tk.LabelFrame(frame2, text="変換機能一覧", padx=10, pady=10)
        convert_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        convert_h264_to_h265_button = ttk.Button(convert_frame, text="H.264 → H.265 変換", command=self.convert_h264_to_h265, style="Flat.TButton")
        convert_h264_to_h265_button.pack(fill=tk.X, padx=10, pady=5)

        convert_h265_to_h264_button = ttk.Button(convert_frame, text="H.265 → H.264 変換", command=self.convert_h265_to_h264, style="Flat.TButton")
        convert_h265_to_h264_button.pack(fill=tk.X, padx=10, pady=5)

        convert_mp4_to_wav_button = ttk.Button(convert_frame, text="MP4 → WAV 変換", command=self.convert_mp4_to_wav, style="Flat.TButton")
        convert_mp4_to_wav_button.pack(fill=tk.X, padx=10, pady=5)

        convert_change_fps_button = ttk.Button(convert_frame, text="フレームレート変更 (30fps)", command=self.change_frame_rate_to_30fps, style="Flat.TButton")
        convert_change_fps_button.pack(fill=tk.X, padx=10, pady=5)

        # フレーム3: FFmpegとffmpeg-pythonの状態表示
        frame3 = tk.Frame(self, padx=10, pady=10)
        frame3.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        ffmpeg_label = tk.Label(frame3, text=ffmpeg_status)
        ffmpeg_label.pack(anchor=tk.W)

        ffmpeg_python_label = tk.Label(frame3, text=ffmpeg_python_status)
        ffmpeg_python_label.pack(anchor=tk.W)

        # 説明欄フレーム
        explanation_frame = tk.LabelFrame(self, text="事前にお読みください", padx=10, pady=10)
        explanation_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, side=tk.BOTTOM)

        explanation_text = """
        〈初期設定〉
        ・FFmpegのパス設定 C:/ffmpeg/bin/
        ・ffmpeg-pythonのインストール pip install ffmpeg-python
        〈使用上の注意〉
        動画変換にはmp4形式のみが対応しています。
        ※万が一の為、変換前に動画のバックアップを取ってください！
        """

        explanation_label = tk.Label(explanation_frame, text=explanation_text, justify=tk.LEFT)
        explanation_label.pack(anchor=tk.W)

        # スタイル設定
        self.style = ttk.Style()
        self.style.configure("Flat.TButton", foreground="black", background="lightgray", borderwidth=0, focuscolor="none")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("動画ファイル", "*.mp4")])
        if file_path:
            self.selected_file_label.delete('1.0', tk.END)  # テキストをクリア
            self.selected_file_label.insert(tk.END, file_path)

    def convert_h264_to_h265(self):
        input_file = self.selected_file_label.get('1.0', tk.END).strip()
        if input_file.endswith(".mp4"):
            output_file = os.path.splitext(input_file)[0] + "_h265.mp4"
            try:
                ffmpeg.input(input_file).output(output_file, vcodec='libx265').run(overwrite_output=True)
                messagebox.showinfo("成功", "H.264からH.265への変換が完了しました。")
            except ffmpeg.Error as e:
                messagebox.showerror("エラー", f"エラーが発生しました: {e}")
        else:
            messagebox.showerror("エラー", "MP4形式のファイルを選択してください。")

    def convert_h265_to_h264(self):
        input_file = self.selected_file_label.get('1.0', tk.END).strip()
        if input_file.endswith(".mp4"):
            output_file = os.path.splitext(input_file)[0] + "_h264.mp4"
            try:
                ffmpeg.input(input_file).output(output_file, vcodec='libx264').run(overwrite_output=True)
                messagebox.showinfo("成功", "H.265からH.264への変換が完了しました。")
            except ffmpeg.Error as e:
                messagebox.showerror("エラー", f"エラーが発生しました: {e}")
        else:
            messagebox.showerror("エラー", "MP4形式のファイルを選択してください。")

    def convert_mp4_to_wav(self):
        input_file = self.selected_file_label.get('1.0', tk.END).strip()
        if input_file.endswith(".mp4"):
            output_file = os.path.splitext(input_file)[0] + ".wav"
            try:
                ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
                messagebox.showinfo("成功", "MP4からWAVへの変換が完了しました。")
            except ffmpeg.Error as e:
                messagebox.showerror("エラー", f"エラーが発生しました: {e}")
        else:
            messagebox.showerror("エラー", "MP4形式のファイルを選択してください。")

    def change_frame_rate_to_30fps(self):
        input_file = self.selected_file_label.get('1.0', tk.END).strip()
        if input_file.endswith(".mp4"):
            output_file = os.path.splitext(input_file)[0] + "_30fps.mp4"
            try:
                ffmpeg.input(input_file).filter('fps', fps=30).output(output_file).run(overwrite_output=True)
                messagebox.showinfo("成功", "フレームレートを30fpsに変更しました。")
            except ffmpeg.Error as e:
                messagebox.showerror("エラー", f"エラーが発生しました: {e}")
        else:
            messagebox.showerror("エラー", "MP4形式のファイルを選択してください。")

if __name__ == "__main__":
    app = VideoConverterApp()
    app.mainloop()
