with open('file1.txt', 'r') as f:
    lines = f.readlines() # 读取所有数据
    first_n_lines = lines[:] # 获取前N行
    for line in first_n_lines:
        first_n_chars = line[:13] # 获取前N个字符

with open('file.txt', 'r')as f:
    line = f.readlines()

for item in line:
    if item not in lines:
        print(item)