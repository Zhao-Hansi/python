def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


# if __name__ == '__main__':
#     main()
def main1():
    f = None
    try:
        f = open('/practice/100个数求和.py', encoding='utf-00')
        print(f.read())
    except FileNotFoundError:
        print('cannot open file')
    except LookupError:
        print('itis a wrong encoding')
    except UnicodeDecodeError:
        print('read file has a wrong behavior')
    finally:
        if f:
            f.close()

def main2():
    with open('/practice/100个数求和.py', mode='r') as f:
        for line in f:
            print(line)
    print('-------------------------')
    with open('/practice/100个数求和.py', mode='r') as f1:
        print(f1.readline())

if __name__ == '__main__':
    main2()