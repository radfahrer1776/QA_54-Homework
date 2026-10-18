
import re


def is_positive_less_than_300(value):
    return bool(re.fullmatch(r"[1-9]\d{0,2}", value)) and int(value) < 300


def is_number_from_1_to_255(value):
    return bool(re.fullmatch(r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])", value))


def is_israel_mobile(phone):
    pattern = r"(?:05\d-?\d{7}|05\d-\d{2}-\d{2}-\d{3}|\+9725\d-\d{3}-\d{4})"
    return bool(re.fullmatch(pattern, phone))


def is_valid_time(time):
    return bool(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", time))


def is_israel_car_number(number):
    pattern = r"(?:\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3})"
    return bool(re.fullmatch(pattern, number))


print("\n--- Task 1: Positive Number Less Than 300 ---\n")
print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("99"))
print(is_positive_less_than_300("100"))
print(is_positive_less_than_300("299"))
print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))
print(is_positive_less_than_300("3.14"))
print(is_positive_less_than_300("Abc"))


print("\n--- Task 2: Number From 1 to 255 ---\n")
print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("25"))
print(is_number_from_1_to_255("100"))
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("0"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("2.5"))


print("\n--- Task 3: Israel Mobile Number ---\n")
print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))
print(is_israel_mobile("54-1234567"))
print(is_israel_mobile("054--12-4567"))
print(is_israel_mobile("+972054-123-4567"))
print(is_israel_mobile("97254-123-4567"))


print("\n--- Task 4: Validate Time ---\n")
print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))
print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))


print("\n--- Task 5: Israel Car Number ---\n")
print(is_israel_car_number("12-345-67"))
print(is_israel_car_number("99-999-99"))
print(is_israel_car_number("123-45-678"))
print(is_israel_car_number("456-78-901"))
print(is_israel_car_number("12345678"))
print(is_israel_car_number("12:345:67"))
print(is_israel_car_number("1-234-56"))
print(is_israel_car_number("1234-56-78"))
