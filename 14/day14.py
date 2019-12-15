import re
from collections import defaultdict

def parse_line(line):
    pattern = r'(\d+) ([A-Z]+)'
    arrow_idx = line.find('=>')
    src_matches = re.findall(pattern, line[:arrow_idx])
    tgt_match = re.search(pattern, line[arrow_idx:])
    return (tgt_match[2], int(tgt_match[1]), [(int(amount), name) for amount, name in src_matches])

def parse(lines):
    recipes = {}
    for tgt_name, tgt_amount, ingredients in [parse_line(line) for line in lines]:
        recipes[tgt_name] = (tgt_amount, ingredients)
    return recipes

def solve(recipes, leftovers=defaultdict(lambda: 0), tgt_name='FUEL', req_amount=1):
    if tgt_name == 'ORE':
        return req_amount
    used_from_leftover = min(leftovers[tgt_name], req_amount)
    leftovers[tgt_name] -= used_from_leftover
    need_to_produce =  req_amount - used_from_leftover
    tgt_amount, ingredients = recipes[tgt_name]
    num_reactions = (need_to_produce + tgt_amount - 1) // tgt_amount
    leftover = num_reactions * tgt_amount - need_to_produce
    leftovers[tgt_name] += leftover
    return sum(solve(recipes, leftovers, src_name, num_reactions * src_amount) for src_amount, src_name in ingredients)


with open('day14.txt') as f:
    lines = f.readlines()

recipes = parse(lines)
print(solve(recipes, defaultdict(lambda: 0), 'FUEL', 1))
