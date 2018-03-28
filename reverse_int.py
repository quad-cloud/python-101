def reverse_integer(i):
  result = 0
  remaining_num = i
  while remaining_num:
    result = (result * 10) + (remaining_num % 10)
    remaining_num = int(remaining_num / 10)
    print('Result: {}, Remaining Number: {}'.format(result, remaining_num))
  return result

if(__name__ == '__main__'):
  print(reverse_integer(23456))
