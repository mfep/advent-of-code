with open('day2.txt') as f:
  input = f.readlines()

num_valid = 0
for input_line in input:
  i = input_line.find('-')
  min_occurence = int(input_line[0:i])
  j = input_line.find(' ')
  max_occurence = int(input_line[i+1:j])
  letter = input_line[j+1:j+2]
  string = input_line[j+4:len(input_line)-1]

  count = 0
  for c in string:
    if c == letter:
      count += 1
  if count >= min_occurence and count <= max_occurence:
    num_valid += 1
print(num_valid)

num_valid = 0
for input_line in input:
  i = input_line.find('-')
  pos1 = int(input_line[0:i])
  j = input_line.find(' ')
  pos2 = int(input_line[i+1:j])
  letter = input_line[j+1:j+2]
  string = input_line[j+4:len(input_line)-1]
  if (string[pos1 - 1] == letter) ^ (string[pos2 - 1] == letter):
    num_valid += 1
  
print(num_valid)
