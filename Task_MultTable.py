def multiply(list_row, list_col):
  for k in range(len(list_row)):
    if list_row[k] <= 10:
      print('', list_row[k], sep='      ', end='')
    else:
      print('', list_row[k], sep='     ', end='')
  for i in range(len(list_col)):
    print()
    if list_col[i] < 10:
      print(list_col[i], end='     ')
    else:
      print(list_col[i], end='    ')
    for j in range(len(list_row)):
      result = list_col[i] * list_row[j]
      if result < 10:
        print(result, end='      ')
      elif 9 < result < 100:
        print(result, end='     ')
      else:
        print(result, end='    ')


numbers_row = input("Введите первый диапазон через пробел: ")
list_row = numbers_row.split(' ')
list_row = [i for i in range(int(list_row[0]), int(list_row[1]) + 1)]

numbers_col = input("Введите второй диапазон через пробел: ")
list_col = numbers_col.split(' ')
list_col = [i for i in range(int(list_col[0]), int(list_col[1]) + 1)]

multiply(list_row, list_col)