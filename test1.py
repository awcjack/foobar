import math

# class solution:
#   def __init__(self):

#   def recursiveSolution(self, result, number):
#     intPart = int(math.sqrt(number))
#     result.append(intPart)
#     recursiveSolution(result, number - intPart)
#   def solution(self, number):
#     result = []
#     solution.recursiveSolution(result, number)
#     # math.sqrt(number)
#     return result
def recursiveSolution(result, number):
  if number == 0:
    return result
  if number == 1:
    result.append(1)
    return result
  intPart = int(math.sqrt(number))**2
  result.append(intPart)
  recursiveSolution(result, number - intPart)
  return result
def solution(number):
  result = []
  recursiveSolution(result, number)
  return result

print(solution(15324))
