st="kjhuyhh23nbvgf"
temp=[]
for i in st:
    if i not in temp:
        temp.append(i)
print("The unique string "+ "".join(temp))