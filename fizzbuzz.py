for fizzbuzz in range(1,101):
     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
         print("fizzbuzz")
         continue
     elif fizzbuzz % 3 == 0:
         print("fizz")
         continue
     elif fizzbuzz % 5 == 0:
         print("buzz")
         continue
     print("fizzbuzz")