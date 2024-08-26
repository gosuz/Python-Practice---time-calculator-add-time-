def time_list_creator(hr, min):
    """Create a list of hr and min

    :param hr: hour
    :param min: minute

    :return: list - hr and minute integer value.
    """
    # Hint: If minute paramater is greater than 59, create an empty list

    int_hr = int(hr)
    int_min = int(min)
    # print(int_hr)
    # print(int_min)

    if int_min <= 59:
        # create the list
        hr_min = [int_hr, int_min]
        # print([int_hr, int_min])
        return [int_hr, int_min]
# time_list_creator(2, 59) # => [2, 5]
# time_list_creator(2, 60) # => [2, 5]


def check_min_greater_than_59(minutes):
    """ Checks if the minutes is greater than 59. Converts it into hrs and minutes if it is.

    :param minutes: int- value of minutes
    :return: list - hrs and minutes [1, 15]

    If it is, it converts it into __hrs __ min
    """
    # if it isn't greater than 59, return [0, min] #=> [0, 59]

    # 1. convert minutes into integer
    int_min = int(minutes)
    # 2. check if if minutes is greater than 59:
    if int_min > 59:
        # Get hrs: divide it by 60.
        hrs = int_min//60
        # Get min: value of %60
        mins = int_min % 60
        # print(hrs)
        # print(mins)
        # print([hrs, mins])
        # print("its greater than 59")
        return [hrs, mins]

    else:
        # print([0, int_min])
        # print("its less than 59")
        return [0, int_min]
# check_min_greater_than_59(75)
# check_min_greater_than_59(35)


# convert minutes into hrs + min
# check_min_greater_than_59(75) #=> [1, 15] 1hr 15min
# check_min_greater_than_59(34) #=> [0, 34] 0hr 34 min

def display_as_string(time):
    """ Displays a list [1,24] as a string
    E.g. "1hr 24min"

    :param time: list containing hr and minute
    :returns: string - total time as a string "__hrs __mins"
    """
    string_total= f"Total time: {time[0]}hrs {time[1]}minute(s)"
    # print(string_total)
    return string_total

def time_adder(list_of_times):
    """Takes a list of times, and returns the total time

    :param list_of_times: list containing int times
    :returns: string - total of time as a string
    """
# time_adder([[2, 5], [7,24], [3,26]])
# 1. Loop through the hrs
    sum_hrs = 0
    sum_mins = 0
    for time in list_of_times:
        hrs = time[0] # => retuns hrs
        sum_hrs += hrs

        mins = time[1]  # => returns minutes
        sum_mins += mins

    # print([sum_hrs, sum_mins])
    total_mins = (check_min_greater_than_59(sum_mins))
    # print(total_mins, "its thissss")
    # => [1, 52] hrs and mins of mins


    # check_min_greater_than_59(sum_mins)
    # Then add the hours up again to get the new hrs
    # if the hrs is 1 or more, add the total of the hr to the sum
    total_hrs = sum_hrs

    if total_mins[0] > 0:
        # add all the hours again
        total_hrs = total_mins[0] + sum_hrs # this is the hrs for the final output
        # print(total_hrs, "result of min_in_hrs_total") # gets hours
        # print(total_mins[1], "result of: total_mins[1]") # gets minutes

    total_list = [total_hrs, total_mins[1]]
    # print(total_list)
    print(display_as_string(total_list))
    return display_as_string(total_list)
# 6. returns the hrs, minutes:
    # Total is ...hrs ... minutes
# 2hrs 5 min, 7hr24min, 3hr26min
    # total_time_list = [sum_hrs, sum_mins]

# time_adder([[2, 5], [7,24], [3,26], [1, 57]])
# time_adder([[2, 5], [7,24], [3,26]])
# time_adder([[1, 17], [0,30], [1,0], [2,2],[0,35]]) # EXERCISM
# time_adder([[0,50],[1,5],[3,20],[0,30]])
# Add all the hrs and all the minutes


mon = f"Mon {time_adder([[1,17], [0,50]])}\n"
tues =f"Tues {time_adder([[0,30], [0,0]])}\n"
wed = f"Wed {time_adder([[1,0], [1,5]])}\n"
thurs = f"Thurs {time_adder([[2,2], [3,20]])}\n"
fri = f"Fri {time_adder([[0,35], [0,30]])}\n"

print(mon, tues, wed, thurs, fri)

# day = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
# def display_total_per_day():
#     # gets
