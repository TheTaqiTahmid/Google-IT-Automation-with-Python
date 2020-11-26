import re
import operator

""" f = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
x = re.search(r" \((.*)\)", f).group(1)

if x is not None:
    print(x)




x = {'p':123}
if 'q' not in x:
    x['q'] = 345
print(x) """

fruit = {'Orange':5, 'Apple':3, 'Pear':2}
new_fruit = sorted(fruit.items(), key=operator.itemgetter(1))
print(new_fruit)