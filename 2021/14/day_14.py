from collections import defaultdict

with open('day_14.txt') as f:
  starter = f.readline().strip()
  f.readline()
  rules = {}
  for line in f.readlines():
    source_0 = line[0]
    source_1 = line[1]
    target = line[6]
    rules[(source_0, source_1)] = target

def get_occurrences_naive(starter, iters):
  result = starter
  for _ in range(iters):
    new_result = result[0]
    for pair in zip(result, result[1:]):
      target = rules[pair]
      new_result += target + pair[1]
    result = new_result

    occurrences = defaultdict(int)
    for ch in result:
      occurrences[ch] += 1
  return occurrences

occurrences = get_occurrences_naive(starter, 10)
print(max(occurrences.values()) - min(occurrences.values()))

def merge_occurrences(lhs, rhs):
  ret = defaultdict(int)
  lhs_keys = set(lhs.keys())
  all_keys = lhs_keys.union(rhs.keys())
  for key in all_keys:
    ret[key] = lhs[key] + rhs[key]
  return ret

def get_occurrences_at_depth(cache, lhs, rhs, depth):
  cache_key = (lhs, rhs, depth)
  if cache_key in cache:
    return cache[cache_key]
  new_item = rules[(lhs, rhs)]
  if depth > 0:
    left_occurences = get_occurrences_at_depth(cache, lhs, new_item, depth - 1)
    right_occurences = get_occurrences_at_depth(cache, new_item, rhs, depth - 1)
    occurrences = merge_occurrences(left_occurences, right_occurences)
    cache[cache_key] = occurrences
    return occurrences
  else:
    occurrences = defaultdict(int)
    occurrences[lhs] += 1
    occurrences[new_item] += 1
    cache[cache_key] = occurrences
    return occurrences

def get_occurrences_cached(starter, iters):
  cache = {}
  all_occurrences = defaultdict(int)
  for lhs,rhs in zip(starter, starter[1:]):
    occurrences = get_occurrences_at_depth(cache, lhs, rhs, iters-1)
    all_occurrences = merge_occurrences(all_occurrences, occurrences)
  all_occurrences[starter[-1]] += 1
  return all_occurrences

assert(occurrences == get_occurrences_cached(starter, 10))
occurrences = get_occurrences_cached(starter, 40)
print(max(occurrences.values()) - min(occurrences.values()))
