import csv
import shutil

# 读取train.csv文件
with open("./data/car/train.csv") as train_file:
    train_csv = csv.reader(train_file)
    headers = next(train_csv)
    for row in train_csv:
        # 把图片存入到相应的文件夹里面
        if row[1] == '0':
            shutil.move(f"./data/car/train/{row[0]}", f"./data/car/train/audi/{row[0]}")
        elif row[1] == '1':
            shutil.move(f"./data/car/train/{row[0]}", f"./data/car/train/Benz/{row[0]}")
        elif row[1] == '2':
            shutil.move(f"./data/car/train/{row[0]}", f"./data/car/train/BMW/{row[0]}")
        print(f'{row[0]}移动完成！')
