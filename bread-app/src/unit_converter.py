
def convert_units(quantity, unit):
    if unit == "cups" or unit == "c" or unit == "cup":
        return convert_cups_to_metric(quantity)
    elif unit == "gallons" or unit == "g" or unit == "gallon":
        return convert_gallons_to_metric(quantity)
    elif unit == "ounces" or unit == "oz" or unit == "ounce":
        return convert_ounces_to_metric(quantity)
    elif unit == "pounds" or unit == "lb" or unit == "pound":
        return convert_pounds_to_metric(quantity)
    elif unit == "desiliters" or unit == "dl" or unit == "desiliter":
        return convert_desiliters_to_imperial(quantity)
    elif unit == "centiliters" or unit == "cl" or unit == "centiliter":
        quantity /= 10
        return convert_desiliters_to_imperial(quantity)
    elif unit == "milliliters" or unit == "ml" or unit == "milliliter":
        quantity /= 100
        return convert_desiliters_to_imperial(quantity)
    elif unit == "liters":
        return convert_liters_to_imperial(quantity)
    elif unit == "grams":
        return convert_grams_to_imperial(quantity)
    elif unit == "kilograms":
        return convert_kilograms_to_imperial(quantity)
    else:
        return quantity

def convert_ounces_to_metric(ounces):
    grams = ounces * 28.3495
    return grams

def convert_gallons_to_metric(gallons):
    liters = gallons * 3.7854
    return liters

def convert_cups_to_metric(cups):
    desiliters = cups * 2.3659
    return desiliters

def convert_pounds_to_metric(pounds):
    kilograms = pounds * 0.4536
    return kilograms

def convert_desiliters_to_imperial(dl):
    cups = dl * 0.4208
    return cups

def convert_liters_to_imperial(l):
    gallons = l * 0.2642
    return gallons

def convert_grams_to_imperial(g):
    ounces = g * 0.0353
    return ounces

def convert_kilograms_to_imperial(kg):
    pounds = kg * 2.2046
    return pounds

print(convert_units(1, "cups"))