delimeter_string = ' bags contain '

rules = []
with open('day7.txt') as f:
  for line in f:
    subject_index = line.find(delimeter_string)
    object_attrib = line[0:subject_index]
    subject_strings = line[subject_index + len(delimeter_string):len(line)].split(',')
    subjects = []
    for subject_string in subject_strings:
      if subject_string.find('no other bags') >= 0:
        continue
      words = subject_string.split()
      subjects.append({'count': int(words[0]), 'attrib': words[1] + ' ' + words[2]})
    rules.append({'container': object_attrib, 'contained': subjects})

def find_containers(attrib):
  containers = []
  for rule in rules:
    for contained in rule['contained']:
      if contained['attrib'] == attrib:
        containers.append(rule['container'])
  return containers

to_check = ['shiny gold']
checked = set()
while to_check:
  current = to_check.pop()
  current_containers = find_containers(current)
  for current_container in current_containers:
    if current_container not in checked:
      to_check.append(current_container)
  checked.add(current)

def count_bags_inside(attrib):
  for rule in rules:
    if rule['container'] == attrib:
      count = 1
      for contained in rule['contained']:
        count += contained['count'] * count_bags_inside(contained['attrib'])
      return count

print(len(checked) - 1) # -1: remove shiny gold
print(count_bags_inside('shiny gold') - 1) # -1: remove shiny gold
