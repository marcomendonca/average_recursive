def average_recursive(value, counter, terms):
    enter_value = int(input("Enter the value to calculate the average: "))
    value = ((value*(counter-1))+enter_value)/counter
    terms = terms-1
    if terms > 0:
        counter = counter+1
        return average_recursive(value, counter, terms)
    else:
        return print("The average is: ",value)


def calculate_average():
    number_of_terms = int(input("\nEnter number of terms for average: "))
    return average_recursive(0, 1, number_of_terms)


calculate_average()
