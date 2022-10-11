def is_year_leap(year):
#
    if year % 4 == 0:
        return True
    else:
        return False
#
def days_in_month(year, month):
    if is_year_leap(year) == True:
        if month in [1,3,5,7,8,10,12]:
            days_in_month = 31
            return days_in_month
        elif month in [4,6,9,11]:
            days_in_month = 30
            return days_in_month
        else:
            days_in_month = 29
            return days_in_month
    else:
        if month in [1,3,5,7,8,10,12]:
            days_in_month = 31
            return days_in_month
        elif month in [4,6,9,11]:
            days_in_month = 30
            return days_in_month
        else:
            days_in_month = 28
            return days_in_month
        

print(days_in_month(2020,9))

