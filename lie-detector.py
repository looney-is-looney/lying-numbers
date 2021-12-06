from os import write
import sympy

n = 13

def prime_test(number, witness):
  if witness >= number:
    raise ValueError("witness must be smaller than the number")
  elif number % 2 == 0:
    return False

  factor = (number - 1)/2
  d = 1
  while factor % 2 == 0:
    d += 1
    factor = factor / 2
  
  factor = int(factor)
  result = []
  for i in range(d):
    result.append(pow(witness, factor * (2 ** d), number))

  val = not (1 not in result and (number - 1) not in result)
  return val

def determine_liars(pow_of_two):
  liars = {}
  for index in range(1, pow_of_two + 1):
    hi_bound = 2 ** index
    lo_bound = hi_bound >> 1
    for number in range(lo_bound, hi_bound):
      if sympy.isprime(number):
        continue
      for witness in range(2, number, 2):
        test_result = prime_test(number, witness)
        if test_result == True:
          key = "_" + str(witness)
          if key not in liars:
            liars.update({key: 1})
          else:
            liars.update({key: liars[key] + 1})
    
    with open("data/liars-" + str(index) + ".csv", "w") as f:
      f.write("witness,lie_count\n")
      for liar in liars.keys():
        f.write(liar[1:] + "," + str(liars.get(liar)) + "\n")


determine_liars(n)
# print(prime_test(9, 2))
