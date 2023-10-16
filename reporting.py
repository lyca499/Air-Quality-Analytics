# This is a template.
# You should modify the functions below to match
# the signatures determined by the project specification
import utils


def daily_average(data, monitoring_station, pollutant):

    # Extract a dictionary consisting of the data for each day whith the date as the key and the list of data as the value
    data_by_day = utils.extract_data_by_day(monitoring_station, pollutant)

    # Fill in the missing data with 0 and turn them into float
    data_by_day = fill_missing_data(
        data_by_day, 0, monitoring_station, pollutant)

    # Calculate the daily average
    result = []
    for dates in data_by_day:
        day_list = data_by_day[dates]  # Get the list of data for each day
        # Calculate the mean value of the list
        daily_mean = utils.meanvalue(day_list)
        # Round the mean value to 3 decimal places
        daily_mean = round(daily_mean, 3)
        result.append(daily_mean)  # Add the mean value to the result list
    return result  # Return the result list


def daily_median(data, monitoring_station, pollutant):

    # Extract a dictionary consisting of the data for each day whith the date as the key and the list of data as the value
    data_by_day = utils.extract_data_by_day(monitoring_station, pollutant)

    # Fill in the missing data with 0 and turn them into float
    data_by_day = fill_missing_data(
        data_by_day, 0, monitoring_station, pollutant)

    # Calculate the daily median
    result = []
    for dates in data_by_day:
        day_list = data_by_day[dates]  # Get the list of data for each day
        # Calculate the median value of the list
        daily_median = utils.median_value(day_list)
        # Round the median value to 3 decimal places
        daily_median = round(daily_median, 3)
        result.append(daily_median)  # Add the median value to the result list
    return result  # Return the result list


def hourly_average(data, monitoring_station, pollutant):

    # Extract a dictionary consisting of the data for each hour whith the hour as the key and the list of data as the value
    data_by_hour = utils.extract_data_by_hour(monitoring_station, pollutant)

    # Fill in the missing data with 0 and turn them into float
    data_by_hour = fill_missing_data(
        data_by_hour, 0, monitoring_station, pollutant)

    # Calculate the hourly average
    result = []
    for hours in data_by_hour:
        hour_list = data_by_hour[hours]  # Get the list of data for each hour
        # Calculate the mean value of the list
        hourly_mean = utils.meanvalue(hour_list)
        # Round the mean value to 3 decimal places
        hourly_mean = round(hourly_mean, 3)
        result.append(hourly_mean)  # Add the mean value to the result list
    return result


def monthly_average(data, monitoring_station, pollutant):

    # Extract a dictionary consisting of the data for each month whith the month as the key and the list of data as the value
    data_by_month = utils.extract_data_by_month(monitoring_station, pollutant)

    # Fill in the missing data with 0 and turn them into float
    data_by_month = fill_missing_data(
        data_by_month, 0, monitoring_station, pollutant)

    # Calculate the monthly average
    result = []
    for months in data_by_month:
        # Get the list of data for each month
        month_list = data_by_month[months]
        # Calculate the mean value of the list
        monthly_mean = utils.meanvalue(month_list)
        # Round the mean value to 3 decimal places
        monthly_mean = round(monthly_mean, 3)
        result.append(monthly_mean)  # Add the mean value to the result list
    return result


def peak_hour_date(data, date, monitoring_station, pollutant):

    # Extract all the data from the station into a list
    data = utils.extract_data(monitoring_station, pollutant)
    pollutant_index = {'NO': 2, 'pm10': 3, 'pm25': 4}

    # Extract a dictionary consisting of the data for each hour at the given date whith the hour as the key and the list of data as the value
    data_each_hour = {}
    for line in data:
        line = line.strip()
        line = line.split(',')
        if line[0] == date:
            data_each_hour[line[1]] = [line[pollutant_index[pollutant]]]

    # Fill in the missing data with 0 and turn them into float
    data = fill_missing_data(data_each_hour, 0, monitoring_station, pollutant)

    # Find the peak hour and the peak value
    tuple = ()
    for hours, hourly_data in data.items():
        # If the tuple is empty, assign the first value to the tuple
        if tuple == ():
            tuple = (hours, hourly_data[0])
        # If the value is greater than the value in the tuple, replace the tuple with the new value
        elif hourly_data[0] > tuple[1]:
            tuple = (hours, hourly_data[0])

    return tuple


def count_missing_data(data,  monitoring_station, pollutant):
    count = 0

    # Extract a dictionary consisting of the data
    for keys in data:

        # Count the number of missing data of each day/hour/month
        for x in data[keys]:
            try:
                x = float(x)
            except:
                count += 1
    return count


def fill_missing_data(data, new_value,  monitoring_station, pollutant):
    result = {}

    # Extract a dictionary consisting of the data
    for keys in data:

        # Fill in the missing data with the new value
        new_data_list = []
        for x in data[keys]:
            try:
                x = float(x)
                new_data_list.append(x)
            except:
                new_data_list.append(new_value)
        result[keys] = new_data_list
    return result


if __name__ == "__main__":
    print("This module is not meant to be executed alone.")
    print("Please import this module and call the functions within it.")
