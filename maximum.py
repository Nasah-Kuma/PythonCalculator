# maximum of n numbers
def maximum_all(list_size):
    num_list = []
    for i in range(1, list_size + 1):
        list_item = int(input("Enter enter the value of %d element : " %i))
        num_list.append(list_item)
    print(num_list)
    max_num = num_list[0]
    for number in num_list:
        if number > max_num:
            max_num = number
    return max_num


max_list = maximum_all(int(input("Enter the size of your list: ")))
print(f"The largest value is {max_list}")
