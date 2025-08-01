# list should always be wrapped with square bracket i.e . [ ] and not with curly bracket i.e. { }.
# list is mutable i.e. it can be changed after it is created.
list1 = [9, 0.2, "Greece Pro", True, False]
print(list1)
print(list1[2])
print(list1[:3])
print(list1[3:])
print(list1[1:3])
print(list1[-1])
list1[2] = "Greece Dahal"
list1.append("hello hahahahahhahahaha")
list1.insert(4, "Wow")
list1.pop()
list1.remove("Greece Dahal")
list1.reverse()
list1.clear()
print(list1)

list2 = [99, 0, 1.1, 3, 5, 7, 9]
list2.sort(reverse=True)
print(list2)
