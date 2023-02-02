import copy
import collections

def print_all_sum_rec(target, current_sum, start, output, result): # https://www.educative.io/m/find-all-sum-combinations
  if current_sum == target:
    output.append(copy.copy(result))

  if (len(result) == 3):
    return
  for i in range(start, target):
    temp_sum = current_sum + i
    if temp_sum <= target:
      result.append(i)
      print_all_sum_rec(target, temp_sum, i, output, result)
      result.pop()
    else:
      return

def tryRemoveOneDigit(collection, list, extra):
  if (collection[extra] > 0):
    list.remove(extra)
    return True
  elif (extra <= 6):
    return tryRemoveOneDigit(collection, list, extra + 3)
  else:
    return False

def countFrequency(list):
  return collections.Counter(list) 

def solution(l):
  l.sort(reverse=True)
  remainder = sum(l) % 3
  if (remainder == 0):
    return ''.join(map(str, l))
  freq = countFrequency(l)
  if (tryRemoveOneDigit(freq, l, remainder)):
    return ''.join(map(str, l))
  else:
    output = []
    result = []
    print_all_sum_rec(remainder, 0, 1, output, result)
    if (remainder <= 3):
      print_all_sum_rec(remainder + 6, 0, 1, output, result)
    if (remainder <= 6):
      print_all_sum_rec(remainder + 3, 0, 1, output, result)
    combinations = sorted(output, key=lambda x: (len(x), sum(x), x[1]))
    for combination in combinations:
      miss = False
      combinationFreq = countFrequency(combination)
      for element in combinationFreq.most_common():
        if (not(freq[element[0]] >= element[1])):
          miss = True
          break
      if (miss):
        continue
      else:
        for element in combination:
          l.remove(element)
        return ''.join(map(str, l))
    return 0

print(solution([7,7,7,7,7,7,7,7,7,7, 1]))
# print(solution([3, 1, 4, 1]))
