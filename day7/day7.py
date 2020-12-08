data = open('data.txt')
data = data.read()

data = data.split('\n')


def get_bag(sentance):
    words = sentance.split(' ')
    return words[2]


has_gold = [x for x in data if "shiny gold" in x]
first_comp = [x for x in data if x not in has_gold]
print(has_gold)

def get_colours(rule):
  words = rule.split(' ')
  colours = ' '.join(words[:2])
  return colours

first_cols = [get_colours(x) for x in has_gold if "shiny gold" not in x]
# second round

print(first_cols)

def number_of_colors(first_cols, first_comp):
  cols = first_cols
  comp = first_comp
  number = [len(has_gold)]
  while len(cols)>0:
    # list to hold all the unique lines that contains colours c
    combined_lines = []
    for c in cols:
        print(c)
        lines_have_color_c = [ x for x in comp if str(c) in x]
        print(lines_have_color_c)
        lines_have_color_c = [x for x in lines_have_color_c if len(x)>0]
        print(lines_have_color_c)
        combined_lines.append(lines_have_color_c)
    # flatten list and retain only unique lines
    combined_lines = list(set([l for sublist in combined_lines for l in sublist]))      
    print(combined_lines)
    cols = [get_colours(x) for x in combined_lines]
    print(cols)
    comp = [l for l in comp if l not in combined_lines]
    print(comp)
    number.append(len(cols))
      
  return number
#no2 = number_of_colors(first_cols, first_comp)

#print(no2)



