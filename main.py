def split_number(number):
    '''Splits the given number into single digits and return as a sorted list'''
    digits = list(str(number))
    digits.sort()
    return [int(digit) for digit in digits]

# github repo: https://github.com/boris737/Exercise_2


def main():
    numbers = []  # Empty list to store the numbers
    list_of_lists = []  # Empty list to store lists of digits

    # Asking the user to input 5 numbers
    print("Please fill in a list of 5 numbers!")
    for _ in range(5):
        num = input("Please enter a number: ")
        numbers.append(num)
        list_of_lists.append(split_number(num))

    print("\nYour list of numbers:", numbers)
    
    # Flattening the list of lists and sorting it
    flat_list = [item for sublist in list_of_lists for item in sublist]
    print("Separated numbers from the list - sorted from smallest to largest:", sorted(flat_list))

    # Calculating the sum of all the digits
    print("Sum of all single digit numbers is:", sum(flat_list))

    # Converting integers in inner lists to strings
    list_of_lists = [[str(digit) for digit in sublist] for sublist in list_of_lists]
    print("List of lists:", list_of_lists)


if __name__ == "__main__":
    main()
