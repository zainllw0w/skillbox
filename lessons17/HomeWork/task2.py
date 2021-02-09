result = [(x - 1) % 5 if x % 2 == 0
          else 1
          for x in range(1, 11,)]

print(result)