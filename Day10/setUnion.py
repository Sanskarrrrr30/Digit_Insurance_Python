# using Set | operator to find union of two sets

school1 = {"Alice", "Bob", "Charlie"}
school2 = {"David", "Eve", "Charlie"}

# find union of two sets
union_set = school1 | school2
print("Students in either school1 or school2:")
print(union_set)

# using set.union() method to find union of two sets

union_set_method = school1.union(school2)
print("Students in either school1 or school2 using union() method:")
print(union_set_method)
