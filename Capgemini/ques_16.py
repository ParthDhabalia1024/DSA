#Roataion of emelents by left or right

a=[10, 20, 30, 40, 50]
def rotate_array(a,times,direction):
    if direction == 'left':
        return a[times:] + a[:times]

    elif direction == 'right':
        return a[-times:] + a[:-times]

print(rotate_array(a,2,'left'))