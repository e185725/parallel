import os

path = "./arashi_image/櫻井翔" # ファイル名一覧を取得したいディレクトリのパス
text_file = open("./saku_path", "w") # 書き込み先のテキストファイルを作る

files = os.listdir(path) # ファイル名一覧を取得

for f in files:
  #basename_without_ext,ext = os.path.splitext(os.path.basename(f)) # 拡張子抜きのファイル名を取得
  basename = os.path.basename(f)
  text_file.write(basename + "\n") # テキストファイルに書き込む

text_file.close() # テキストファイルを保存