# This is a template.
# You should modify the functions below to match
# the signatures determined by the project specification.
#
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations.
#
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#

import datetime
import numpy as np
import utils


def get_live_data_from_api(site_code='MY1', species_code='NO', start_date=None, end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 

    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + \
        datetime.timedelta(days=1) if end_date is None else end_date
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"

    url = endpoint.format(
        site_code=site_code,
        species_code=species_code,
        start_date=start_date,
        end_date=end_date
    )

    res = requests.get(url)
    return res.json()


def average_today(*args, **kwargs):
    ##############################
    # Getting data
    ##############################
    # get the data from 2 days before to today
    data = get_live_data_from_api("MY1", "NO", datetime.date.today(
    ) - datetime.timedelta(days=1), datetime.date.today() + datetime.timedelta(days=1))

    # create a dict to store the data where the key is datetime and value is pollutions
    dict_by_datetime = {}
    data = data['RawAQData']['Data']  # only get the data
    for item in data:
        item = list(item.items())  # convert to list
        # add to dict where the key is datetime and value is pollutions
        try:
            dict_by_datetime[item[0][1]] = float(item[1][1])
        except:
            dict_by_datetime[item[0][1]] = None

    # remove the last item if it is empty until the length is 24 to remove the data that has not been updated
    while len(dict_by_datetime) > 24 and list(dict_by_datetime.values())[-1] == None:
        dict_by_datetime.popitem()

    dict_by_datetime = dict(list(dict_by_datetime.items())[-24:])

    count = 0
    sum = 0
    for item in list(dict_by_datetime.values()):
        if item != None:
            sum += item
            count += 1
    return sum / count


def median_today(*args, **kwargs):
    ##############################
    # Getting data
    ##############################
    # get the data from 2 days before to today
    data = get_live_data_from_api("MY1", "NO", datetime.date.today(
    ) - datetime.timedelta(days=1), datetime.date.today() + datetime.timedelta(days=1))

    # create a dict to store the data where the key is datetime and value is pollutions
    dict_by_datetime = {}
    data = data['RawAQData']['Data']  # only get the data
    for item in data:
        item = list(item.items())  # convert to list
        # add to dict where the key is datetime and value is pollutions
        try:
            dict_by_datetime[item[0][1]] = float(item[1][1])
        except:
            dict_by_datetime[item[0][1]] = None

    # remove the last item if it is empty until the length is 24 to remove the data that has not been updated
    while len(dict_by_datetime) > 24 and list(dict_by_datetime.values())[-1] == None:
        dict_by_datetime.popitem()

    dict_by_datetime = dict(list(dict_by_datetime.items())[-24:])

    data = [x for x in list(dict_by_datetime.values()) if x != None]

    return utils.median_value(data)


def peak_hour_today(*args, **kwargs):
    ##############################
    # Getting data
    ##############################
    # get the data from 2 days before to today
    data = get_live_data_from_api("MY1", "NO", datetime.date.today(
    ) - datetime.timedelta(days=1), datetime.date.today() + datetime.timedelta(days=1))

    # create a dict to store the data where the key is datetime and value is pollutions
    dict_by_datetime = {}
    data = data['RawAQData']['Data']  # only get the data
    for item in data:
        item = list(item.items())  # convert to list
        # add to dict where the key is datetime and value is pollutions
        try:
            dict_by_datetime[item[0][1]] = float(item[1][1])
        except:
            dict_by_datetime[item[0][1]] = None

    # remove the last item if it is empty until the length is 24 to remove the data that has not been updated
    while len(dict_by_datetime) > 24 and list(dict_by_datetime.values())[-1] == None:
        dict_by_datetime.popitem()

    dict_by_datetime = dict(list(dict_by_datetime.items())[-24:])

    max = ()
    for key in dict_by_datetime:
        if dict_by_datetime[key] != None:
            if max == ():
                max = (key, dict_by_datetime[key])
            elif dict_by_datetime[key] > max[1]:
                max = (key, dict_by_datetime[key])
    return max


# def rm_function_4(*args, **kwargs):
#     # Your code goes here


def graph_the_past_day(*args, **kwargs):
    ##############################
    # Getting data
    ##############################
    # get the data from 2 days before to today
    data = get_live_data_from_api("MY1", "NO", datetime.date.today(
    ) - datetime.timedelta(days=1), datetime.date.today() + datetime.timedelta(days=1))

    # create a dict to store the data where the key is datetime and value is pollutions
    dict_by_datetime = {}
    data = data['RawAQData']['Data']  # only get the data
    for item in data:
        item = list(item.items())  # convert to list
        # add to dict where the key is datetime and value is pollutions
        try:
            dict_by_datetime[item[0][1]] = float(item[1][1])
        except:
            dict_by_datetime[item[0][1]] = None

    # remove the last item if it is empty until the length is 24 to remove the data that has not been updated
    while len(dict_by_datetime) > 24 and list(dict_by_datetime.values())[-1] == None:
        dict_by_datetime.popitem()

    dict_by_datetime = dict(list(dict_by_datetime.items())[-24:])

    # if the item is empty, fill it with the average of the previous and next item or zero
    for index, key in enumerate(dict_by_datetime):
        # remove the data that has not been updated
        # if it is not the first and last item and the item is empty
        if index > 0 and index < len(dict_by_datetime) - 1 and dict_by_datetime[key] == None:
            # if the previous or next item is empty, fill it with 0
            if dict_by_datetime[list(dict_by_datetime.keys())[index - 1]] == None or dict_by_datetime[list(dict_by_datetime.keys())[index + 1]] == None:
                dict_by_datetime[key] = 0

            # if the previous and next item are not empty, fill it with the average of the previous and next item
            else:
                dict_by_datetime[key] = (
                    list(dict_by_datetime.values())[index - 1] + list(dict_by_datetime.values())[index + 1]) / 2

        # if it is the first item or last item and the item is empty
        elif dict_by_datetime[key] == None:
            dict_by_datetime[key] = 0

    # get the maximum value in the dictionary
    max_value = max(dict_by_datetime.values())
    if max_value > 980:
        max_value = 980

    ##############################
    # Convert the data to graph
    ##############################
    # convert the maximum value in the dictionary to a increment of 20
    if max_value == 0:
        gmax = 20
    else:
        if round_to_multiple(max_value, 20) < max_value:
            gmax = round_to_multiple(max_value, 20) + 20
        else:
            gmax = round_to_multiple(max_value, 20)

    # fill the gap between the datas with 4 numbers
    values_list = list(dict_by_datetime.values())

    temp_list = []
    for index in range(len(values_list)-1):
        increment = (values_list[index + 1] - values_list[index]) / 5
        temp_list.append(values_list[index])
        for i in range(1, 5):
            temp_list.append(values_list[index] + increment * i)
    temp_list.append(values_list[-1])
    values_list = temp_list
    # round the value to the nearest increment of 20
    values_list = [round_to_multiple(x, gmax/20) for x in values_list]

    # lower the maximum value to the nearest increment of 20 if it is above 980
    values_list = [x if x < 980 else 980 for x in values_list]

    ##############################
    # Construct the graph
    ##############################
    # print the graph
    seperation_line = " "*3 + '|' + " "*5*24 + '|'

    # construct the first two line
    graph_string = str(gmax).zfill(3) + '+' + '+----'*23 + '+---++'
    graph_string += '\n' + seperation_line + '\n'
    seperation_line = " "*3 + '|' + " "*5*24 + '|'

    # construct the middle lines
    for i in range(9):
        digit = str(gmax // 10 * (9-i)).zfill(3)
        graph_string += str(digit).zfill(3) + '+' + ' ' * \
            23*5 + '    ++' + '\n' + seperation_line + '\n'

    # construct the last line
    graph_string += str(0).zfill(3) + '+' + '+----'*23 + '+---++'

    # construct the x-axis
    graph_string += '\n '
    for keys in dict_by_datetime.keys():
        graph_string += ' '*3 + keys[-8:-6]
    graph_string += ' '*4

    # convert graph into numpy array for value insertion
    np_graph = graph_string.split('\n')
    np_graph = [[*x] for x in np_graph]
    np_graph = np.array(np_graph)

    for i in range(4, len(values_list)+4):
        x_coordinate = int(20 - values_list[i-4] // (gmax/20))
        np_graph[x_coordinate][i] = '*'
        x = 1

    # convert the np_graph back to string
    graph_string = ''
    for x in np_graph:
        for y in x:
            graph_string += y[0]
        graph_string += '\n'
    return 'pollution value\n' + graph_string + ' '*(25*5-4) + 'time'


def round_to_multiple(number, multiple):
    if number > 0:
        return multiple * round(number / multiple)
    else:
        return 0


if __name__ == "__main__":
    print(average_today())
    print(median_today())
    print(peak_hour_today())
    print(graph_the_past_day())
