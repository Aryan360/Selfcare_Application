from itertools import combinations

def get_combinations(prime_nos_list, select_upto_n):
    result = list()
    for selecting_n_at_a_time in range(1,select_upto_n+1):
        for combination in combinations(prime_nos_list,selecting_n_at_a_time):
            result.append(combination)
    return result

if __name__ == "__main__":
    prime_nos_list = [3,5,7,11,13,17]
    print(f"Given Array of Elements: {prime_nos_list}")

    select_upto_n_at_a_time = len(prime_nos_list) # here 6, i.e. from 6 elements in the list of prime numbers we are selecting upto 6 elements at a time i.e. (6C1, 6C2, 6C3, 6C4, 6C5, 6C6)
    result = get_combinations(prime_nos_list, select_upto_n_at_a_time)
    print(f"\n>> Total unique combinations : {len(result)}\n")

    print(f"------------------------------------------------------------------\nCombinations List:")
    for i in result:
        print(i)