import csv


import pandas as pd
import numpy as np

def join_zips_and_plans():
    ''' merge together the datasets for zipcodes and insurance plans
    '''
    plans = pd.read_csv('plans.csv')
    zips = pd.read_csv('zips.csv')
    zip_rates= pd.merge(zips, plans, on=['state', 'rate_area'])
    return zip_rates[zip_rates['metal_level'] == 'Silver']

def find_rate_area(zipcode):
    zip_rates = join_zips_and_plans()
    zipcode = zip_rates[zip_rates['zipcode'] == int(zipcode)]
    rate_areas = zipcode['rate_area'].unique()
    rates = zipcode['rate'].unique()
    if rate_areas.size == 1 and rates.size > 1:
        return np.sort(zipcode['rate'].unique())[1]

if __name__ == '__main__':
    # read in csv
    with open('slcsp.csv') as csvfile:
        data = csv.reader(csvfile)
        # drop headers
        next(data)
        zipcodes = [line[0] for line in data]
        results = map(find_rate_area, zipcodes)
        for line in zip(zipcodes, results):
            print(line)