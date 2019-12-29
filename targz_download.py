import urllib.request as req
import gzip
import os
import os.path

# 以下を変更
SAVEPATH = "保存先のパス指定"
BASEURL = 'http://yann.lecun.com/exdb/mnist'
FILES = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz"]

# ダウンロード
if not os.path.exists(SAVEPATH): os.mkdir(SAVEPATH)
for f in FILES:
    url = BASEURL + '/' + f
    loc = SAVEPATH + '/' + f
    print("download:", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

# GZip解凍
for f in FILES:
    gz_file = SAVEPATH + '/' + f
    raw_file = SAVEPATH + '/' + f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, 'rb') as fp:
        body = fp.read()
        with open(raw_file, 'wb') as w:
            w.write(body)

print('ok')


