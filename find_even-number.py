def find_even_number():
    even_number = []
    for number in range(1,51):
        if number % 2 == 0:
            even_number.append(number)
    return even_number
