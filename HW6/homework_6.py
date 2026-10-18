
def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"


print("\n--- Task 1: Get Product ---\n")

products = ["coffee", "tea", "milk"]

print(get_product(products, 0))
print(get_product(products, 7))


def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"


print("\n--- Task 2: Get Settings Value ---\n")

settings = {
    "language": "English",
    "theme": "dark"
}

print(get_settings_value(settings, "theme"))
print(get_settings_value(settings, "font"))


def calculate_total_price(price, quantity):
    try:
        price = float(price)
        quantity = float(quantity)
        return price * quantity
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"


print("\n--- Task 3: Calculate Total Price ---\n")

print(calculate_total_price("12.5", "4"))
print(calculate_total_price("coffee", "4"))
print(calculate_total_price(None, 4))


def read_temperature():
    try:
        temperature = float(input("Enter temperature: "))
        print("Temperature was entered successfully")
        return temperature
    except ValueError:
        print("Invalid temperature")
    finally:
        print("Program finished")


print("\n--- Task 4: Read Temperature ---\n")

read_temperature()


def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")
    return discount


print("\n--- Task 5: Validate Discount ---\n")

print(validate_discount(20))
print(validate_discount(0))
print(validate_discount(100))
