def set_days_life(years, months, days):
    days_life = 0
    days_life += transform_years_in_days(years)
    days_life += transform_months_in_days(months)
    days_life += days
    print(days_life)


def transform_years_in_days(years):
    return years * 365


def transform_months_in_days(months):
    return months * 30


year = int(input("Digite quantos anos você tem: "))
month = int(input("Digite quantos meses você tem: "))
day = int(input("Digite quantos dias você tem: "))

set_days_life(year, month, day)
