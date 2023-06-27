def add_time(start, duration, start_day=''):
    # split up the hours, minutes, and period STRINGS
    start_hour, start_minute_and_period = start.split(":")
    start_minute, start_period = start_minute_and_period.split()
    duration_hour, duration_minute = duration.split(":")

    start_day = start_day.lower()

    # convert strings to integers
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)

    # calculate the total minutes
    total_minutes = start_minute + duration_minute

    # calculate the carry hours from start minute and duration minutes
    carry_hours = (start_minute + duration_minute) // 60

    # adjust the total minutes
    total_minutes %= 60

    # calculate the total hours
    total_hours = start_hour + duration_hour + carry_hours

    # calculate the number of periods (12-hour cycles) passed
    periods = total_hours // 12

    # calculate days passed
    days_passed = periods / 2
    if start_period == 'PM' and days_passed % 1 == 0.5:
        days_passed += 1

    # determine the new period (AM/PM)
    if periods == 0:
        period = start_period
    elif start_period == "AM" and periods % 2 == 1:
        period = 'PM'
    else:
        period = 'AM'

    # adjust the total hours to be within 12-hour range
    total_hours %= 12
    # handle the special case of 12:00
    if total_hours == 0:
        total_hours = 12

    # weekday logic :O
    weekday = ''
    if start_day != '':
        days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        start_day_index = days_of_week.index(start_day)
        target_day_index = (start_day_index + days_passed) % 7
        weekday_lower = days_of_week[int(target_day_index)]
        weekday = f", {weekday_lower.capitalize()}"

    # if 1 day then days_passed = next day else then X days later
    if days_passed == 0 or days_passed < 1 and start_period == 'AM':
        days_passed = ''
    elif int(days_passed) == 1:
        days_passed = ' (next day)'
    else:
        days_passed = f" ({int(days_passed)} days later)"



    # format the new time
    new_time = f"{total_hours}:{total_minutes:02d} {period}{weekday}{days_passed}"

    return new_time