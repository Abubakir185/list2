# 1. 

list = []

for i in range(1, 6):
    list.append(i)

print(list)



# 2.

ismlar = ["Tom", "Bob", "Jerry", "Alex", "Anna"]

print(ismlar.index("Alex"))



# 3.  

davlatlar = ["AQSH", "Rossiya", "Korea"]

davlatlar.insert(1, "Uzbekiston")
print(davlatlar)


#  4.

raqamlar = [1, 2, 3, 4, 5]

raqamlar.pop()
print(raqamlar)


# 5. 

raqamlar2 = [1, 2, 3, 2, 4, 1, 2]

raqamlar2.remove(2)
print(raqamlar2)


# 6

ismlar = ["Ali", "Vali", "Tesha", "Ali"]

while "Ali" in ismlar:
    index = ismlar.index("Ali")
    ismlar.pop(index)
    ismlar.insert(index, "Botir")

print(ismlar)