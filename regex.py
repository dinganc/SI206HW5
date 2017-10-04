import re
def sum_nums (inputstr):
    summ=0
    for num in re.findall('([0-9]+)',inputstr):
        summ+=int(num)
    return summ
print('all intergers in the sample has a sum of {}'.format(sum_nums(open('regex_sum_42.txt','r').read())))
print('all intergers in the actual has a sum of {}'.format(sum_nums(open('regex_sum_36345.txt','r').read())))