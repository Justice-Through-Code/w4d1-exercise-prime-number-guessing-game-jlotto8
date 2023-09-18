#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.
 
'''

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
    sum_of_range = 0
    for num in range(start,end +1):
        sum_of_range += num
    print(sum_of_range)
    return(sum_of_range)
calculate_sum(0,5)

def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.
    
    for i in range(start,end):
        smallest_num = start
    print(smallest_num)
    return smallest_num

find_smallest_number(0,5)


def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

    for i in range(start,end):
        largest = end
    print(largest)
    return largest
find_largest_number(0,6)    

def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
    amount_of_evens = 0
    for i in range(start,end+1):
        if i %2 ==0:
            amount_of_evens += 1
    print(amount_of_evens)
    return amount_of_evens
count_even_numbers(0,6)            


def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
    amount_of_odds = 0
    for i in range(start,end+1):
        if i %2 == 1:
            amount_of_odds += 1
    print(amount_of_odds)
    return amount_of_odds
count_odd_numbers(0,6)