#Rank of element in array
a = [100, 2, 70, 12 , 90]
# b = [18, 23, 29, 95, 25]
def rank_of_element_in_array(a):
    b=sorted(a)
    rank_map = {}
    for rank, value in enumerate(b):
        rank_map[value] = rank + 1

    ranked_array = []
    for element in a:
        ranked_array.append(rank_map[element])
    return ranked_array

print(rank_of_element_in_array(a))


