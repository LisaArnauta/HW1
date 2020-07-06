def mix_strings(str_1, str_2):
         lena = len(str_1)//2
         end_string = str_1[lena::]
         beg_string=str_1[0:lena]
         print(beg_string + " " + str_2 + " " + end_string)
g = mix_strings(input("write first string here:"), input("write second string here:"))