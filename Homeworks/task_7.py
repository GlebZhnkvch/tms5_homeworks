def convert_cent_to_inch():
    coef = 2.54
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num = input('Enter the num of cent:')
        if input_num.isdigit():
            print(float(input_num) * coef)
            continue
        elif input_num == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num}')
            continue


def convert_inch_to_cent():
    coef = 2.54
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_1 = input('Enter the num of inch:')
        if input_num_1.isdigit():
            print(round((float(input_num_1) / coef), 2))
            continue
        elif input_num_1 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_1}')
            continue


def convert_miles_to_kilom():
    coef = 1.61
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_2 = input('Enter the num of miles:')
        if input_num_2.isdigit():
            print(round((float(input_num_2) * coef), 2))
            continue
        elif input_num_2 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_2}')
            continue


def convert_kilom_to_miles():
    coef = 1.61
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_3 = input('Enter the num of kilom:')
        if input_num_3.isdigit():
            print(round((float(input_num_3) / coef), 2))
            continue
        elif input_num_3 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_3}')
            continue


def convert_pounds_to_kilograms():
    coef = 0.45
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_4 = input('Enter the num of pounds:')
        if input_num_4.isdigit():
            print(round((float(input_num_4) * coef), 2))
            continue
        elif input_num_4 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_4}')
            continue


def convert_kilograms_to_pounds():
    coef = 0.45
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_5 = input('Enter the num of kilograms:')
        if input_num_5.isdigit():
            print(round((float(input_num_5) / coef), 2))
            continue
        elif input_num_5 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_5}')
            continue


def convert_ounce_to_grams():
    coef = 28.35
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_6 = input('Enter the num of ounces:')
        if input_num_6.isdigit():
            print(round((float(input_num_6) * coef), 2))
            continue
        elif input_num_6 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_6}')
            continue


def convert_grams_to_ounces():
    coef = 28.35
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_7 = input('Enter the num of grams:')
        if input_num_7.isdigit():
            print(round((float(input_num_7) / coef), 2))
            continue
        elif input_num_7 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_7}')
            continue


def convert_gallons_to_litres():
    coef = 4.55
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_8 = input('Enter the num of gallons:')
        if input_num_8.isdigit():
            print(round((float(input_num_8) * coef), 2))
            continue
        elif input_num_8 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_8}')
            continue


def convert_litres_to_gallons():
    coef = 4.55
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_9 = input('Enter the num of litres:')
        if input_num_9.isdigit():
            print(round((float(input_num_9) / coef), 2))
            continue
        elif input_num_9 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_9}')
            continue


def convert_pints_to_litres():
    coef = 0.57
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_10 = input('Enter the num of pints:')
        if input_num_10.isdigit():
            print(round((float(input_num_10) * coef), 2))
            continue
        elif input_num_10 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_10}')
            continue


def convert_litres_to_pints():
    coef = 0.57
    print('If you want to exit the program, enter: Stop')
    while True:
        input_num_11 = input('Enter the num of litres:')
        if input_num_11.isdigit():
            print(round((float(input_num_11) / coef), 2))
            continue
        elif input_num_11 == str('Stop'):
            print('You have successfully exited the program!')
            break
        else:
            print(f'Please, enter the num, you entered: {input_num_11}')
            continue


while True:
    print('\n Convert centimetres to inches - 1 \n',
          'Convert inches to centimetres - 2 \n',
          'Convert miles to kilometres - 3 \n',
          'Convert kilometres to miles - 4 \n',
          'Convert pounds to kilograms - 5 \n',
          'Convert kilograms to pounds - 6 \n',
          'Convert ounces to grams - 7 \n',
          'Convert grams to ounces - 8 \n',
          'Convert gallons to litres - 9 \n',
          'Convert litres to gallons - 10 \n',
          'Convert pints to litres - 11 \n',
          'Convert litres to pints - 12 \n', )
    input_choice = input('Enter what do you want to convert (1 - 12):')
    if input_choice.isdigit():
        if int(input_choice) == 1:
            print(convert_cent_to_inch())
        elif int(input_choice) == 2:
            print(convert_inch_to_cent())
        elif int(input_choice) == 3:
            print(convert_miles_to_kilom())
        elif int(input_choice) == 4:
            print(convert_kilom_to_miles())
        elif int(input_choice) == 5:
            print(convert_pounds_to_kilograms())
        elif int(input_choice) == 6:
            print(convert_kilograms_to_pounds())
        elif int(input_choice) == 7:
            print(convert_ounce_to_grams())
        elif int(input_choice) == 8:
            print(convert_grams_to_ounces())
        elif int(input_choice) == 9:
            print(convert_gallons_to_litres())
        elif int(input_choice) == 10:
            print(convert_litres_to_gallons())
        elif int(input_choice) == 11:
            print(convert_pints_to_litres())
        elif int(input_choice) == 12:
            print(convert_litres_to_pints())
        continue
    else:
        print("Enter a number(1-12)")
        continue
    break

# functions =  [convert_cent_to_inch() , convert_inch_to_cent(), convert_miles_to_kilom(), convert_kilom_to_miles(), convert_pounds_to_kilograms(), convert_kilograms_to_pounds(), convert_ounce_to_grams(),
# convert_grams_to_ounces(), convert_gallons_to_litres(), convert_litres_to_gallons(), convert_pints_to_litres(), convert_litres_to_gallons()] #

''' ХОТЕЛ СДЕЛАТЬ ФУНЦИИ ЧЕРЕЗ СПИСОК, ЧТОБЫ БЫЛО МЕНЬШЕ elif '''
