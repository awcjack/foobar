import time
import math

def solution(n):
  memo = [1] * (n + 1)
  # dividedList = range(1, math.floor(n/2) + 1)
  dividedList = range(1, int(n/2) + 1)
  wholeList = range(1, n + 1)
  for j in reversed(dividedList):
    for i in reversed(wholeList):
      if (i - j > j):
        memo[i] = memo[i - j] + memo[i]
  return memo[n]


def solution2(n):
  a = [1]+[0]* n
  for i in range(1, n+1): 
    for k in reversed(range(i, n+1)):
      a[k] = a[k-i] + a[k]
  return a[n] - 1

brickCount = 100000

start_time = time.perf_counter()
print(solution(brickCount))
end_time = time.perf_counter()
print(f"Execution Time in Nanoseconds : {end_time - start_time}" )

start_time = time.perf_counter()
print(solution2(brickCount))
end_time = time.perf_counter()
print(f"Execution Time in Nanoseconds : {end_time - start_time}" )
