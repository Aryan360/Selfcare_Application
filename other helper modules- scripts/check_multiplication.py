# To check that, combinations of prime numbers when multiplied together do they produce non unique output.
# Findings: They produce unique output, thus combinations of prime numbers can be used in various combinations to represent a category

from itertools import combinations
import sys


def multiply_from_iterable(list):
    mul_result = 1
    for i in list:
        mul_result *= i
    return mul_result


def get_combinations(prime_nos_list, select_upto_n):
    if select_upto_n > len(prime_nos_list):
        print(
            f">> Error!!, it's not possible to select {select_upto_n} items from {len(prime_nos_list)} items of list at a time.\n> Reduce the value of 2nd parameter in function calling.")
        sys.exit()
    else:
        # result = list()
        multiplication_result_arr = list()
        for selecting_n_at_a_time in range(1, select_upto_n+1):
            for combination in combinations(prime_nos_list, selecting_n_at_a_time):
                lst = list(combination)
                multiplication_result_arr.append([combination, multiply_from_iterable(lst)])
                # result.append(combination)
        return multiplication_result_arr


if __name__ == "__main__":
    prime_nos_list = [3, 5, 7, 11, 13, 17]
    print(f"Given Array of Elements: {prime_nos_list}")
    result = get_combinations(prime_nos_list, len(prime_nos_list))
    print(f"\n>> Total unique combinations : {len(result)}\n")  

    # sorting the list (multiplication_result_arr: [[(3,5,7),105]]) on the basis of the result of multiplication, i.e. key index = 1
    sorted_arr = sorted(result, key=lambda x: x[1])

    print("Tuple Combination\t\t| Multiplication Result\n------------------------------------------------")
    for i in sorted_arr:
        print(f"{str(i[0]):20}\t\t|\t{i[1]}")
