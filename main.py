# print("hello world")

# caicai="li ai cai"
# print(caicai)

# a=10
# b=79
# c=a+b
# d=True
# print(c)

cs = ['first', 'second', 'third']
print(cs)

print(len(cs))
print(cs[0])
cs.append('forth')
print(cs)
cs.insert(6,"cc")
print(cs)
a = 5

if a>10:
    print(a)
elif a<5:
    print("55")
else:
    print("5<=a=<10")

#for item in cs:
#    print(item)

sum = 0
for x in range(7):
    if x == 4:
        break
    sum += 1

print(sum)

def tmax(c,d):
    if c>d:
        return c
    else:
        return d


res = tmax(3,4)
print(res)

list1 = [1,3,0,-2,16,2]
list2 = [55,213,25,23,988]

def list_max(array):
    if isinstance(array, list) == False:
        return False

    MaN=array[0]
    for item in array:
        # if item > MaN:
        #     MaN=item
        MaN=tmax(MaN,item)
    return MaN

mn = list_max(list1)
print(mn)
