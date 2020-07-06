def get_str_center(input_str):
        a = len(input_str)//2
        if len(input_str)%2==1:
            print(input_str[a], input_str[a+1])
        elif len(input_str)%2==0:
            print(input_str[a-1], input_str[a],input_str[a+1])
        else:
            print('пустая строка(???)')
g = get_str_center(input("write here:"))