def balanced(a,m,rs):
    if a<m:
        return rs - (a-m)
    elif a == m:
        return rs
    else:
        return rs + (m-a)
    
a = int(input())
m = int(input())
rs = int(input())

print(balanced(a,m,rs))