import time # 導入 time 模組，用於控制程式執行速度

full_name = ["john doe", "jane1 smith", "kevin hart bob", "bob johnson"]
# 定義一個包含人名的列表，每個元素是一個字串，代表一個人的全名

valid_name = 0
# 初始化計數器，用來統計符合條件（名字由兩部分組成）的人數

print("This program will count the valid names in the fullname list")
time.sleep(1.5)
for part_name in full_name:
    name_length = part_name.split()
    # 將當前全名按空格分割成列表，例如 "john doe" 變成 ["john", "doe"]
    if len(name_length) == 2:
    # 檢查分割後的列表長度是否為 2（表示有名字和姓氏）
        valid_name += 1
        # 計數器加 1，表示找到一個有效名字
        print(str(valid_name) + " : " + part_name)
        # 如果條件成立，直接印出原始的全名字串
        time.sleep(1)
        # 每次迴圈結束後暫停 1 秒，讓輸出有間隔，便於觀察，若當前名字無效則不會暫停
print("total valid names: " + str(valid_name))
# 印出總計有多少個名字符合條件
print("the program has finished, thank you for using")