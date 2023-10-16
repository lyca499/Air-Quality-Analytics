# This is a template.
# You should modify the functions below to match
# the signatures determined by the project specification

import reporting
import monitoring


def main_menu():
    print("---------------------------------")
    print("R - Access the RP Module")
    print("M - Access the RM Module")
    print("A - Print the About text")
    print("Q - Quit the application")
    print("---------------------------------")
    user_input = input("Please select an option >>>")
    if user_input.capitalize() == "R":
        print("\033c")
        reporting_menu()
    elif user_input.capitalize() == "M":
        print("\033c")
        monitoring_menu()
    elif user_input.capitalize() == "A":
        print("\033c")
        about()
    elif user_input.capitalize() == "Q":
        print("\033c")
        quit()
    else:
        print("\033c")
        print("Invalid input. Please try again")
        main_menu()


def reporting_menu():

    def reporting_type_selection(reporting_type_input, monitoring_station_input, pollutant_input):
        print("---------------------------------")
        print("1 - Daily Average")
        print("2 - Daily Median")
        print("3 - Hourly Average")
        print("4 - Monthly Average")
        print("5 - Peak hour date")
        print("M - Back to main menu")
        print("---------------------------------")
        reporting_type_input = input("Please select an option >>>")

        try:
            if reporting_type_input.capitalize() == "M":
                print("\033c")
                main_menu()
        except:
            pass

        # See if the input is valid
        try:
            reporting_type_input = int(reporting_type_input)
        except ValueError:
            print("\033c")
            print("Invalid input. Please try again")
            reporting_menu()
        if reporting_type_input not in range(1, 6):
            print("\033c")
            print("Invalid input. Please try again")
            reporting_menu()

        # If the input is valid, go to the next step
        print("\033c")
        station_selection(reporting_type_input,
                          monitoring_station_input, pollutant_input)

    def station_selection(reporting_type_input, monitoring_station_input, pollutant_input):
        print("---------------------------------")
        print("1 - London Harlington")
        print("2 - London Marylebone Road")
        print("3 - London N Kensington")
        print("M - Back to main menu")
        print("---------------------------------")
        monitoring_station_input = input("Please select an option >>>")

        try:
            if monitoring_station_input.capitalize() == "M":
                print("\033c")
                main_menu()
        except:
            pass

        # See if the input is valid
        try:
            monitoring_station_input = int(monitoring_station_input)
        except ValueError:
            print("\033c")
            print("Invalid input. Please try again")
            station_selection(reporting_type_input,
                              monitoring_station_input, pollutant_input)
        if monitoring_station_input not in range(1, 4):
            print("\033c")
            print("Invalid input. Please try again")
            station_selection(reporting_type_input,
                              monitoring_station_input, pollutant_input)

        # If the input is valid, go to the next step
        print("\033c")
        pollutant_selection(reporting_type_input,
                            monitoring_station_input, pollutant_input)

    def pollutant_selection(reporting_type_input, monitoring_station_input, pollutant_input):
        print("---------------------------------")
        print("1 - NO")
        print("2 - pm10")
        print("3 - pm25")
        print("M - Back to main menu")
        print("---------------------------------")
        pollutant_input = input("Please select an option >>>")

        try:
            if pollutant_input.capitalize() == "M":
                print("\033c")
                main_menu()
        except:
            pass

        # See if the input is valid
        try:
            pollutant_input = int(pollutant_input)
        except ValueError:
            print("\033c")
            print("Invalid input. Please try again")
            pollutant_selection(reporting_type_input,
                                monitoring_station_input, pollutant_input)
        if pollutant_input not in range(1, 4):
            print("\033c")
            print("Invalid input. Please try again")
            pollutant_selection(reporting_type_input,
                                monitoring_station_input, pollutant_input)

        print("\033c")
        after_selection(reporting_type_input,
                        monitoring_station_input, pollutant_input)

    def after_selection(reporting_type_input, monitoring_station_input, pollutant_input):
        monitoring_station_name_dictioanry = {
            1: 'London Harlington', 2: 'London Marylebone Road', 3: 'London N Kensington'}
        monitoring_station_dictioanry = {1: 'HRL', 2: 'MY1', 3: 'KC1'}
        pollutant_dictioanry = {1: 'NO', 2: 'pm10', 3: 'pm25'}
        if reporting_type_input == 1:
            print("Showing daily average of " + pollutant_dictioanry[pollutant_input] +
                  " at " + monitoring_station_name_dictioanry[monitoring_station_input] + "...")
            print(reporting.daily_average(
                [], monitoring_station_dictioanry[monitoring_station_input], pollutant_dictioanry[pollutant_input]))
        elif reporting_type_input == 2:
            print("Showing daily median of " + pollutant_dictioanry[pollutant_input] +
                  " at " + monitoring_station_name_dictioanry[monitoring_station_input] + "...")
            print(reporting.daily_median(
                [], monitoring_station_dictioanry[monitoring_station_input], pollutant_dictioanry[pollutant_input]))
        elif reporting_type_input == 3:
            print("Showing hourly average of " + pollutant_dictioanry[pollutant_input] +
                  " at " + monitoring_station_name_dictioanry[monitoring_station_input] + "...")
            print(reporting.hourly_average(
                [], monitoring_station_dictioanry[monitoring_station_input], pollutant_dictioanry[pollutant_input]))
        elif reporting_type_input == 4:
            print("Showing monthly average of " + pollutant_dictioanry[pollutant_input] +
                  " at " + monitoring_station_name_dictioanry[monitoring_station_input] + "...")
            print(reporting.monthly_average(
                [], monitoring_station_dictioanry[monitoring_station_input], pollutant_dictioanry[pollutant_input]))
        elif reporting_type_input == 5:
            date_input = input(
                "Please enter a date in the format of YYYY-MM-DD >>>")
            print("Showing peak hour date of " + pollutant_dictioanry[pollutant_input] + " at " +
                  monitoring_station_name_dictioanry[monitoring_station_input] + " on " + date_input + "...")
            print(reporting.peak_hour_date([], date_input,
                  monitoring_station_dictioanry[monitoring_station_input], pollutant_dictioanry[pollutant_input]))

        user_input = input("Press any key to go back to main menu >>>")
        print("\033c")
        main_menu()
    reporting_type_selection(1, 1, 1)


def monitoring_menu():
    print("---------------------------------")
    print("1 - average the past 24 hours")
    print("2 - median the past 24 hours")
    print("3 - peak the past 24 hours")
    print("4 - graph the past 24 hours")
    print("M - Back to main menu")
    print("---------------------------------")
    pollutant_input = input("Please select an option >>>")

    try:
        if pollutant_input.capitalize() == "M":
            print("\033c")
            main_menu()
    except:
        pass

    # See if the input is valid
    try:
        pollutant_input = int(pollutant_input)
    except ValueError:
        print("\033c")
        print("Invalid input. Please try again")
        monitoring_menu()
    if pollutant_input not in range(1, 5):
        print("\033c")
        print("Invalid input. Please try again")
        monitoring_menu()

    print("\033c")
    if pollutant_input == 1:
        data = monitoring.average_today()
        print("The average of NO in Marylebone the past 24 hour is " + str(data))
    elif pollutant_input == 2:
        data = monitoring.median_today()
        print("The median of NO in Marylebone the past 24 hour is " + str(data))
    elif pollutant_input == 3:
        data = monitoring.peak_hour_today()
        print(
            "The peak hour of NO in Marylebone the past 24 hour is at " + str(data[0]) + " with the value of " + str(data[1]))
    elif pollutant_input == 4:
        data = monitoring.graph_the_past_day()
        print(data)

    user_input = input("Press any key to go back to main menu >>>")
    print("\033c")
    main_menu()


def about():
    print("ECM1400")
    print("Group 1")
    main_menu()


def quit():
    print("Goodbye!")
    exit()


if __name__ == '__main__':
    print("\033c")
    main_menu()
