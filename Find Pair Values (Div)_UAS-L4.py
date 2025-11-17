#NYOMAN ADI ARYA SUABAKTI/2415091013
def find_pair_with_div(arr, target):
    if target == 0:
        return "No proceed"
    
    seen = set()
    for num in arr:
        if num != 0:
            complement = num / target
            if complement in seen:
                return (int(complement), num)
        seen.add(num)
    
    return "No proceed"


input_list = eval(input())
target = int(input())

print(find_pair_with_div(input_list, target))