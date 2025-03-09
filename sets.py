# ##printing an empty set
# set1 = set()
# print(set1)

# ##printing a set with elements
# set2 = {1 , 2 , 3 , "mohan"}
# print(set2)

# ##using a ADD method
# set1 = {1 , 2 , 3 , 4}
# set1.add(1234)
# print(set1)

# ##uaing clear method in set
# products = {"rice" , "wheat" , "salt" , "oil"}
# products.clear()
# print(products)

# ##using copy method in set
# set1 = {1 , 2 , 'a' , 4}
# set1.copy()
# print(set1)

# ##using pop method in set
# set1 = {1 , 2 , 'a' , 4}
# set1.pop()
# print(set1)

# ##using upadate and remove methods in sets
# set1 = {"mohan","doctors","python",1,2}
# set2 = {123 , 3 ,54}
# set1.update(set2)
# print(set1)
# set1.remove((123))
# print(set1)

# ##union method and intersection using in set
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7}
# print(set1.union(set2))
# print(set1.intersection(set2))

# ##symmentric_difference and difference using set
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7}
# set3 = set1.symmetric_difference(set2)
# print(set3)
# print(set1.difference(set2))

# ##disjoint using in set
# set1 = {6}
# set2 = {1,2,3,4,5}
# print(set2.isdisjoint(set1))

# ##super set method using in set
# prices = {1,2,3,4}
# prices_1 = {1,2,3,4,5}
# print(prices_1.issuperset(prices))

# ##frozenset
# set1 = {1 , 2 , 3 , 4 , 5 , 'mohan'}
# print(frozenset(set1))

###################### TUPLES ############

# # tuple with elements
# tuple_1 = (1,2,3,4,5,)
# print(tuple_1)

# ##printing empty tuple
# tuple1= ()
# print(tuple1)

# ##length of tuple
# tuple_1 = (1,2,3,4,5,)
# # print(len(tuple_1))
# print(tuple_1[-1])
# print(tuple_1[ : :-1])
# print(tuple_1[ : : ])

# ##add method using in tuple
# tuple1 = {1,2,3,4}
# print(all(tuple1))

# ##COUNT METHOD
# tuple1 = (1 ,2 ,3 ,3 ,3 ,4,5 ,6 , 6)
# # print(tuple1.count(3))
# print(tuple1.index(2))


# ##concatenate
# tuple1 = (1,2,3,"a")
# tuple2 = (3,'mohan')
# print(tuple1+tuple2)


# ##repitition
# tuple1 = (1,2,3,"a")
# print(tuple1*5)

##membership test
fruits = ('apple','mango','milon')
print('mango'in fruits)

