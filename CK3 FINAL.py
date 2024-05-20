#CK3 question 1 :
def multiply_list(items):
    total = 1
    for x in items:
        total *= x 
    return total

sample_list = [2, 3, 6]
result = multiply_list(sample_list)
print(result)

#question 2 : 
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(sample_list, key=lambda x: x[1])
print(sorted_list)

#question 3 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result = {k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1.keys()).union(d2.keys())}
print(result)

#question4 :
def generate_dict(n):
    result = {}
    for i in range(1, n+1):
        result[i] = i*i
    return result
n = 8
print(generate_dict(n))

#question 5 : 
def sort_tuple(tup):
    return sorted(tup, key=lambda x: float(x[1]))

tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sort_tuple(tup))

#question 6:
#Create set 
my_set = {0,1,2,3,4,5}
print(my_set)

#for loop
my_set={0,1,2,3,4}
for i in my_set : 
    print (i)

#adding values to set 
my_set = {0, 1, 2}
my_set.add(3)
print(my_set)

#remove value from a set 
my_set = {0, 1, 2, 3, 4}
my_set.remove(2)
print(my_set)

