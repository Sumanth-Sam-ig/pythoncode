while True :

  print('Enter an odd number n')
  n=int(input())
  if n%2==0 :
      print ("enter an odd numder not an even number  try again")
      continue
  else:
      i=1
      print ()
      while i<10:
          m=n*i
          print(m)
          i+=2
  break       
