def is_leap(year):
    leap = False
    
    # Write your logic here
    leap_year = 1900
    leap_years = [leap_year]
    while (True and year > 0 and leap_year <= 100000):
        leap_year = leap_year + 4
        leap_years.append(leap_year)
    if year in leap_years:
        leap = True
    return leap

year = int(input())
print(is_leap(year))
