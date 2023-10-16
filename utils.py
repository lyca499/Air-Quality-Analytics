# This is a template.
# You should modify the functions below to match
# the signatures determined by the project specification

# A function that receives a list/array and returns the sum of the values in that
# sequence. The function should raise an exception if non-numerical values are present in
# the list. You have to implement your function from the basics (i.e., without using pre-defined
# functions)
def sumvalues(values):
    sum = 0
    for x in values:
        try:
            x = float(x)
            sum += x
        except:
            raise Exception("Non-numerical value found in list")
    return sum

# A function that receives a list/array and returns the index of the maximum
# value in that sequence. The function should raise an exception if non-numerical values are
# present in the list. You have to implement your function from scratch (i.e., without using
# pre-defined functions)


def maxvalue(values):
    index = 0
    max = 0
    for x in values:
        try:
            x = float(x)
            if x > max:
                max = x
                index = values.index(x)
        except:
            raise Exception("Non-numerical value found in list")
    return index


# A function that receives a list/array and returns the index of the minimum
# value in that sequence. The function should raise an exception if non-numerical values are
# present in the list. You have to implement your function from scratch (i.e., without using
# pre-defined functions)
def minvalue(values):
    index = 0
    min = 0
    for x in values:
        try:
            x = float(x)
            if x < min:
                min = x
                index = values.index(x)
        except:
            raise Exception("Non-numerical value found in list")
    return index


# A function that receives a list/array and returns the arithmetic mean value
# in that list/array. The arithmetic mean µ of a list with n elements can be defined as
# The function should raise an exception if non-numerical values are present in the list. You
# have to implement your function from scratch (i.e., without using pre-defined functions)
def meanvalue(values):
    sum = 0
    count = 0
    for x in values:
        try:
            x = float(x)
            sum += x
            count += 1
        except:
            raise Exception("Non-numerical value found in list")
    return sum/count

# A function that receives a list/array values and a value x and returns
# the number of occurrences of the value x in the list/array values. The function should
# return 0 if the value is not present in the list/array. You have to implement your function
# from scratch (i.e., without using pre-defined functions)


def countvalue(values, xw):
    count = 0
    for x in values:
        try:
            x = float(x)
            if x == xw:
                count += 1
        except:
            raise Exception("Non-numerical value found in list")
    return count

# A function that receives a list/array and returns the median value in that


def median_value(values):
    values = quick_sort(values)
    if len(values) % 2 == 0:
        return (values[int(len(values)/2)] + values[int(len(values)/2 - 1)])/2
    else:
        return values[int(len(values)/2)]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Medthods for extracting data
def extract_data(monitoring_station, pollutant):
    station_file = {'MY1': 'data/Pollution-London Marylebone Road.csv',
                    'KC1': 'data\Pollution-London N Kensington.csv', 'HRL': 'data\Pollution-London Harlington.csv'}
    with open(station_file[monitoring_station]) as f:
        data = f.readlines()
    data = data[1:]
    return data


def extract_data_by_day(monitoring_station, pollutant):
    data = extract_data(monitoring_station, pollutant)
    pollutant_index = {'NO': 2, 'pm10': 3, 'pm25': 4}

    data_by_day = {}
    for line in data:
        line = line.strip()
        line = line.split(',')
        if line[0] in data_by_day:
            data_by_day[line[0]].append(line[pollutant_index[pollutant]])
        else:
            data_by_day[line[0]] = [line[pollutant_index[pollutant]]]
    return data_by_day


def extract_data_by_hour(monitoring_station, pollutant):
    data = extract_data(monitoring_station, pollutant)
    pollutant_index = {'NO': 2, 'pm10': 3, 'pm25': 4}

    data_by_hour = {}
    for line in data:
        line = line.strip()
        line = line.split(',')
        if line[1] in data_by_hour:
            data_by_hour[line[1]].append(line[pollutant_index[pollutant]])
        else:
            data_by_hour[line[1]] = [line[pollutant_index[pollutant]]]
    return data_by_hour


def extract_data_by_month(monitoring_station, pollutant):
    data = extract_data(monitoring_station, pollutant)
    pollutant_index = {'NO': 2, 'pm10': 3, 'pm25': 4}

    data_by_month = {}
    for line in data:
        line = line.strip()
        line = line.split(',')
        if line[0][0:7] in data_by_month:
            data_by_month[line[0][0:7]].append(
                line[pollutant_index[pollutant]])
        else:
            data_by_month[line[0][0:7]] = [line[pollutant_index[pollutant]]]
    return data_by_month


if __name__ == "__main__":
    print("This module is not meant to be executed alone.")
