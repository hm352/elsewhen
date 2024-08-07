''' tests for loading and transforming all the plan and zipcode data
'''
from main import find_rate_area, join_zips_and_plans

zip_rates = join_zips_and_plans()

def test_zip_code_one_county_one_rate():
    slcsp = find_rate_area(99363)
    assert slcsp is None

def test_zip_code_multiple_county_equal_rate_area():
    slcsp = find_rate_area(50014)
    assert slcsp == 287.30

def test_zip_code_multiple_county_code_not_equal_rate_area():
    slcsp = find_rate_area(63359)
    assert slcsp == None