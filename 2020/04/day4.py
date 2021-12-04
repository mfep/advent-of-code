import re

passports = []
with open('day4.txt') as f:
  current_passport = {}
  for line in f:
    line = line.strip()
    if line == '':
      passports.append(current_passport)
      current_passport = {}
    else:
      entries = line.split()
      for entry in entries:
        colon_pos = entry.find(':')
        current_passport[entry[0:colon_pos]] = entry[colon_pos + 1:len(entry)]
  passports.append(current_passport)

required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
def is_valid(passport):
  for field in required_fields:
    if field not in passport:
      return False
  return True

def check_birth(passport):
  byr = int(passport['byr'])
  return byr >= 1920 and byr <= 2002

def check_issue(passport):
  iyr = int(passport['iyr'])
  return iyr >= 2010 and iyr <= 2020

def check_expiration(passport):
  eyr = int(passport['eyr'])
  return eyr >= 2020 and eyr <= 2030

def check_height(passport):
  hgt = passport['hgt']
  cm = hgt.find('cm')
  if cm > 0:
    val_cm = int(hgt[0:cm])
    return val_cm >= 150 and val_cm <= 193
  inch = hgt.find('in')
  if inch > 0:
    val_inch = int(hgt[0:inch])
    return val_inch >= 59 and val_inch <= 76
  return False
  
hair_regex = r'^#[0-9|a-f]{6}$'
def check_hair(passport):
  hcl = passport['hcl']
  return re.match(hair_regex, hcl) is not None

eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def check_eyes(passport):
  ecl = passport['ecl']
  return ecl in eyes

def check_pid(passport):
  pid = passport['pid']
  return re.match(r'^\d{9}', pid) is not None

def check_all(passport):
  methods = [is_valid, check_birth, check_issue, check_expiration, check_height, check_hair, check_eyes, check_pid]
  for method in methods:
    if not method(passport):
      return False
  return True

print(sum([1 for passport in passports if is_valid(passport)]))
print(sum([1 for passport in passports if check_all(passport)]) - 1) # ???