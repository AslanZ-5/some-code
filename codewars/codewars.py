# def encrypt_this(text):
#     c = []
#     for i in text.split():
#
#         if len(i) == 1:
#             c.append(str(ord(i)))
#         elif len(i) == 2:
#             c.append(str(ord(i[0])) + i[-1])
#         else:
#             c.append(str(ord(i[0])) +i[-1] + i[2:-1] + i[1])
#     return ' '.join(c)
#
# print(encrypt_this("A wise old owl lived in an oak"))

a = [1,2,3,4,5,6]

x = int((len(a)-1)/2)
if len(a) %2 != 0:
    b = a[:x]
b = a[:x+1]
c = a[x+ 1:]
c.reverse()
print(b)
print(c)
c = [b[i] + c[i] for i in range(len(b))]
if len(a) %2 != 0:
    c.append(a[x])
print(c)

def fold_array(array, runs):
    for i in range(runs):
        x = int((len(array)-1)/2)
        if len(array)%2 !=0:
            b = array[:x]
        b = array[:x+1]
        c = array[x+1:]
        c.reverse()
        array = [b[i] + c[i] for i in range(len(b))]
        if len(array) %2 != 0:
            array.append(array[x])
        return array

print(fold_array([1,2,3,4,5,6],2))