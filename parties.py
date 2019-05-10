"""
Created on Sun May  5 20:49:06 2019

@author: karen hui xiao
"""


import csv
import pprint


def get_bar_party_data():
    """this function reads from a csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific location and the number of complaint calls
     it received in 2016"""

    bar_list = []
    with open('bar_locations.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            bar_dict = {'location_type': row[0],
                        'zip_code': row[1],
                        'city': row[2],
                        'borough': row[3],
                        'latitude': row[4],
                        'longitude': row[5],
                        'num_calls': row[6]}
            bar_list.append(bar_dict)
    del bar_list[0]
    return bar_list
    



def print_data(data):
    for entry in data:
        print(entry)
        pprint.pprint(entry)


def get_most_noisy_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    noisiest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the noisiest city and borough and their respective metrics
    
    cityCallsDict = {}
    for i in data:
        if i['city'] not in cityCallsDict.keys(): 
            cityCallsDict[i['city']] = int(i['num_calls'])               
        else:
            cityCallsDict[i['city']] += int(i['num_calls'])
    
    boroughCallsDict = {}
    for i in data:
        if i['borough'] not in boroughCallsDict.keys() and i['borough'] != 'Unspecified':
            boroughCallsDict[i['borough']] = int(i['num_calls'])     
        if i['borough'] in boroughCallsDict.keys():
            boroughCallsDict[i['borough']] += int(i['num_calls']) 
    
    noisiest_city = max(cityCallsDict.keys(), key = (lambda x: cityCallsDict[x]))
    noisiest_borough = max(boroughCallsDict.keys(), key = (lambda x: boroughCallsDict[x]))
    
    noisiest_city_and_borough['city'] = noisiest_city
    noisiest_city_and_borough['borough'] = noisiest_borough
    noisiest_city_and_borough['num_city_calls'] =  cityCallsDict[noisiest_city]
    noisiest_city_and_borough['num_borough_calls'] = boroughCallsDict[noisiest_borough]
    
    return noisiest_city_and_borough


def get_quietest_city_and_borough(data):
    """ fill in the Nones for the dictionary below using the bar party data """

    quietest_city_and_borough = {'city': None, 'borough': None, 'num_city_calls': None, 'num_borough_calls': None}

    # write code here to find the quietest city and borough and their respective metrics
    cityCallsDict = {}
    for i in data:
        if i['city'] not in cityCallsDict.keys(): 
            cityCallsDict[i['city']] = int(i['num_calls'])               
        else:
            cityCallsDict[i['city']] += int(i['num_calls'])
    
    boroughCallsDict = {}
    for i in data:
        if i['borough'] not in boroughCallsDict.keys() and i['borough'] != 'Unspecified':
            boroughCallsDict[i['borough']] = int(i['num_calls'])     
        if i['borough'] in boroughCallsDict.keys():
            boroughCallsDict[i['borough']] += int(i['num_calls']) 
    
    quietest_city = min(cityCallsDict.keys(), key = (lambda x: cityCallsDict[x]))
    quietest_borough = min(boroughCallsDict.keys(), key = (lambda x: boroughCallsDict[x]))
    
    quietest_city_and_borough['city'] = quietest_city
    quietest_city_and_borough['borough'] = quietest_borough
    quietest_city_and_borough['num_city_calls'] = cityCallsDict[quietest_city]
    quietest_city_and_borough['num_borough_calls'] = boroughCallsDict[quietest_borough]
    
    return quietest_city_and_borough


if __name__ == '__main__':
    bar_data = get_bar_party_data()

    # uncomment the line below to see what the data looks like
    #print_data(bar_data)

    noisy_metrics = get_most_noisy_city_and_borough(bar_data)

    quiet_metrics = get_quietest_city_and_borough(bar_data)

    print('Noisy Metrics: {}'.format(noisy_metrics))
    print('Quiet Metrics: {}'.format(quiet_metrics))
