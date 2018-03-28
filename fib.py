def fibR(n):
  if(n <= 1):
    return 1
  else:
    return fibR(n - 1) + fibR(n - 2)

if(__name__ == '__main__'):
  for i in range(0, 5):
    print(fibR(i))
