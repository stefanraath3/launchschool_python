def average(start_value, end_value, list_numbers):
    addition = 0
    count = 0
    for number in list_numbers:
        if start_value <= number <= end_value:
            addition += number
            count += 1
    if count > 0:
        av = addition / count
        print(f'the average is: {av}')
    else:
        print("no numbers in specified range")
average(3, 7, [1, 3, 5, 7 , 9])