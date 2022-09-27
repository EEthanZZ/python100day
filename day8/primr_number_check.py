n = int(input("check this number:"))


# def prime_check(number):
#     a = 2
#     while a < number:
#         if number % a == 0:
#             print(f"{number} is not a prime nunmber")
#             break
#         else:
#             a += 1
#             if a == (number - 1):
#                 print(f"{number} is a prime nunmber")


# prime_check(number=n)


def prime_check_2(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_Prime = False

    if is_Prime:
        print("prime number")
    else:
        print("not a prime number")


prime_check_2(number=n)
