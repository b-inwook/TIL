import A

print('top-levl B.py')
A.func() # import해서 가져다 쓴 것이다.

if __name__ == '__main__':
    print('B.py가 직접 실행')
else:
    print('B.py가 import 되어 실행')