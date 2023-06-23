from pathlib import Path
import os

# WS_ROOT = str(Path.cwd())
IMG_DIR = os.path.join(os.getcwd(), '../saved_img')

root = os.getcwd()  # 当前目录并不是指脚本所在的目录，而是所运行脚本的目录。
r2 = os.path.dirname(__file__)

libpath = os.path.join(r2, '../apriltag_src/build/lib')

print(IMG_DIR)
