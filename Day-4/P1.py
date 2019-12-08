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
        # actual digit check
        if list[k-1] > list[k]:
            to_match = list[k-1]
            # getting digit position
            position = 10**(max_len-1-k)
            # if the previous digit is lesser match the digit to the current value
            i = (i-(i % (position*10))) + (to_match*position)+(i % position)
            # doing a split for next iteration in same loop
            if i < max_value:
                list = split_to_list(i)
            else:
                break
        # keep doing the above till the max_len of the digit is reached
        """ not breaking here; since there could be potential password match in the same number
            for example 138888, 138889, 138899....
            If the loop reaches max_len limit that mean the program found a matching password
        """
        if k == max_len-1:
            """ adding missing logic for repetition check"""
            for j in range(1, max_len):
                if list[j] == list[j-1]:
                    print(i)
                    password_count += 1
                    break
            else:
                continue
            break
    i += 1
print("password count", password_count)