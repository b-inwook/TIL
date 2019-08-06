# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    # return eval(equation)


    num_str = ''
    num_list = []

    for index, char in enumerate(equation):
        if (char in ('-','+')) and index != 0:
            num_list.append(int(num_str))
            num_str = ''
        num_str += char

        if index == len(equation)-1:
            num_list.append(int(num_str)) 
    return sum(num_list)


    # result = 0
    # oper_list = []
    # for index, char in enumerate(equation):
    #     if index == 0 and (equation[0] == '-' or equation[0] == '+'):
    #         num_str += char
    #         continue

    #     if char != '+' and char != '-' and len(equation) != index+1:
    #         num_str += char

    #     elif len(equation) == index+1:
    #         num_str += char
    #         num_list.append(int(num_str))
    #         num_str = ''
    #     else:
    #         num_list.append(int(num_str))
    #         num_str = ''
    #         oper_list.append(char)
    

    # for index, op in enumerate(oper_list):
    #     if op == '+' and index == 0:
    #         result += (num_list[index] + num_list[index+1])
    #         continue
    #     elif op == '-' and index == 0:
    #         result += (num_list[index] - num_list[index+1])
    #         continue
    #     else:
    #         if op == '+':
    #             result += num_list[index+1]
    #         else:
    #             result -= num_list[index+1] 

    # return result
            


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))