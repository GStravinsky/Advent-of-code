data = open('data.txt')
data = data.read()

data = data.split('\n')
print(len(data))

def get_bag(sentance):
    words = sentance.split(' ')
    return words[2]

number_of_bags = []

has_gold = [x for x in data if "shiny gold" in x]
number_of_bags.append(len(has_gold))

first_comp = [x for x in data if x not in has_gold]

def get_colours(rule):
  words = rule.split(' ')
  colours = ' '.join(words[:2])
  return colours

first_cols = [get_colours(x) for x in has_gold]

# second round

print(len(first_cols))


def number_of_colors(first_cols, data, first_comp):
  cols = first_cols
  comp = first_comp
  number = []
  n = 0
  while n < 1:
    n = 1
    combined_lines = []
    for c in cols:
      lines_have_color_c = [ x for x in comp if str(c) in x]
      lines_have_color_c = [x for x in lines_have_color_c if len(x)>0]
      print(lines_have_color_c)
      cols2 = [get_colours(x) for x in lines_have_color_c if len(x)>0]
      cols2 = list(set(cols2))
      combined_lines.append(cols2)
      print(combined_lines)
    combined_colors = list(set(combined_lines))
    print(combined_colors)
    cols = list(set(cols))
    print(cols)
    comp = [x for x in data if x not in combined_lines]
    
  return combined_colors

no2 = number_of_colors(first_cols, data, first_comp)

print(no2)

print(sum(no2)+len(has_gold))


