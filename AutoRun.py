numb = 2
operations = 0
f = []
while 1==1:
  cp = numb
  while cp != 1:
    if (cp % 2) == 0:
      cp = cp / 2
      operations = operations + 1
    else:
      cp = cp * 3 + 1
      operations = operations + 1
  f.append(str(numb) + ", " + str(cp) + ", " + str(operations))
  print(f[-1])
  operations = 0
  numb = numb + 1
