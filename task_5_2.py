symbol = '*'
index_1 = 0
index_2 = 1
range_of_symb = list(range(1, 6))
for symb in range_of_symb:
    print(symbol * range_of_symb[index_1] )
    index_1 += 1
reversed_range_of_symb = range_of_symb[:: -1]
for symb_1 in reversed_range_of_symb:
    if index_2 < 5:
        print(symbol * reversed_range_of_symb[index_2])
        index_2 += 1
    else:
        break

