# def multiply(list1, list2):   
#   for i in range(len(list2)):
#     for j in range(len(list1)):
#       result = list2[i] * list1[j]
#       print(result)
      

numbers_row = input("Введите первый диапазон через пробел: ")
list_row = numbers_row.split(' ')
list_row = [i for i in range(int(list_row[0]), int(list_row[1]) + 1)]

numbers_col = input("Введите второй диапазон через пробел: ")
list_col = numbers_col.split(' ')
list_col = [i for i in range(int(list_col[0]), int(list_col[1]) + 1)]
multiply(list_row, list_col)
# # print('', list1[0], list1[1], sep='      ')


