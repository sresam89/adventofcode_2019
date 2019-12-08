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
    # checking each number at every index with one below for lesser or equal value
    for k in range(1, max_len):
        if list[k-1] > list[k]:
            to_match = list[k-1]
            position = 10**(max_len-1-k)
            # if the previous digit is lesser match the digit to the current value
            i = (i-(i % (position*10))) + (to_match*position)+(i % position)
            list = split_to_list(i)
        # keep doing the above till the max_len of the digit is reached
        """ not breaking here; since there could be potential password match in the same number
            for example 138888, 138889, 138899....
        """
        if k == max_len-1:
            print(i)
            password_count += 1
    # else:
    #     continue
    i += 1
    # break

print("password count", password_count)