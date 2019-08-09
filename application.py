from utils.math_utils import most_common, count_repeated_element
from utils.substring_utils import longest_unique_substring


# Challenge 1

string = "AutomationAutoAutAu"
print
"The input string is " + string
length = longest_unique_substring(string)
print('Substring is', length)


# Challenge 2 - Sorting as -2 of string.

month_list = ["January", "February", "Mar", "Apr", "May", "June", "Jul", "august", "Sep", "Oct", "nov", "December"];
month_list.sort(key=lambda x: x[-2])
print(month_list)


# Challenge 3

first_set = [3, 5, 768, 3, 6, 23, 98, 38, 32, 45, 34, 234]
second_set = [10, 12, 43, 74, 25, 56, 37, 98, 29, 10]

first_number = most_common(first_set)
second_number = most_common(second_set)

first_counter = count_repeated_element(first_set, first_number)
second_counter = count_repeated_element(second_set, second_number)

print('Its {} and repeats {} times in first set'.format(first_number, first_counter))
print('Its {} and repeats {} times in second set'.format(second_number, second_counter))


# Sum of Second Set
second_set_total = sum(int(i) for i in second_set)
print(second_set_total)
