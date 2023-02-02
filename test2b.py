def solution(x, y):
  return int((1 + x)*x/2 + (1 + ( y - 2) )* (y - 2)/2 + x * (y - 1))

print(solution(5, 10))
