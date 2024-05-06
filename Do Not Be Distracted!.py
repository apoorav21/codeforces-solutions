from itertools import* 
for s in[*open(0)][2::2]:print('YNEOS'[len([*groupby(s)])>len({*s})::2])