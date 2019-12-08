min_value = 138241
max_value = 674034
max_len = 6

i = min_value
password_count = 0

def split_to_list(number):
    num_list = []
    while int(number):
        num_list.append(int(number % 10))
        number /= 10
    return num_list[::-1]
list = []
while i <= max_value:
    list = split_to_list(i)
    for k in range(1, max_len):
        if list[k-1] > list[k]:
            to_match = list[k-1]
            position = 10**(max_len-1-k)
            i = (i-(i % (position*10))) + (to_match*position)+(i % position)
            list = split_to_list(i)
        if k == max_len-1:
            print(i)
            password_count += 1
    # else:
    #     continue
    i += 1
    # break

print("password count", password_count)