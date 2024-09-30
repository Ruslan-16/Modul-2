def get_matri(n,m,value):
    matrix = []
    for i in range(n):
        elem=[]
        for j in range(m):
            elem.append(value)
    matrix.append(elem)
    return (matrix)

result1 = get_matri(2, 2, 10)
result2 = get_matri(3, 5, 42)
result3 = get_matri(4, 2, 13)
print(result1)
print(result2)
print(result3)






