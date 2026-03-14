string_length = len("Hello World")
list_len = len([1,2,3,4,5,6])
tuple_length = len((11,22,33))
print(string_length)
print(list_len)
print(tuple_length)

sum_of_list = sum([2,4,6,8])
sum_of_tuple = sum((3,4,6,7,5))
print(sum_of_list)
print(sum_of_tuple)

max_value = max(5,15,23)
max_float = max(1.33,123.33,3.4)
print(max_value)
print(max_float)

def add(x,y):
    return x+y

def concentrate(x,y):
    return str(x)+ str(y)

def operate(operation, x,y):
    return operation(x,y)

result_sum = operate(add,5,19)
result_concentrate = operate(concentrate,"Hi","From Us")
print(result_sum)
print(result_concentrate)