import pandas as pd
from sklearn import svm, metrics, cross_validation

# 以下を変更
CSV_FILE = "テストデータファイルパス"
DATA_COLUMN1 = "データカラム名1"
DATA_COLUMN2 = "データカラム名2"
DATA_COLUMN3 = "データカラム名3"
LABEL_COLUMN = "ラベルカラム名"

# csvファイルの読み込み
csv = pd.read_csv(CSV_FILE)

# データとラベルの取り出し
csv_data = csv[[DATA_COLUMN1, DATA_COLUMN2, DATA_COLUMN3]]
csv_label = csv[LABEL_COLUMN]

# 学習用とテスト用に分割
train_data, test_data, train_label, test_label = cross_validation.train_test_split(csv_data, csv_label)

# データを学習してから予測する
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 正解を求める
ac_score = metrics.accuracy_score(test_label, pre)
print("正解率 = ", ac_score)