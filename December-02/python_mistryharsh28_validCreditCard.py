def is_valid_credit_card_number(credit_card_number):

    credit_card_number = str(credit_card_number)

    if(credit_card_number.isdigit()):
        
        odd_places_numbers = [int(i) for index, i in enumerate(credit_card_number) if index % 2 == 0]
        s1 = sum(odd_places_numbers)

        double_even_places_numbers = [int(i)*2 for index, i in enumerate(credit_card_number) if index % 2 == 1]
        s2 = 0
        for value in double_even_places_numbers:
            if(value > 9):
                s2 += value%10 + 1
            else:
                s2 += value

        if((s1 + s2) % 10 == 0):
            return True
        else:
            return False

    else:
        return False


def test_credit_card_number(credit_card_number):
    if(is_valid_credit_card_number(credit_card_number)):
        print('{} passes the test'.format(credit_card_number))
    else:
        print('{} fails the test'.format(credit_card_number))


credit_card_number = 49927398716
test_credit_card_number(credit_card_number)