import csv
import json
import pandas as pd

# ***********************
#          METRO 
# ***********************
df_metro_data = pd.read_csv('https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Metro.csv', dtype='unicode')
df_metro_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']] = df_metro_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']].astype(float)
df_metro_data.rename(columns = {'cbsa_title':'name'}, inplace = True)
df_metro_data[['name']] = df_metro_data[['name']].astype(str)
df_metro_data_s = df_metro_data.sort_values(by='median_listing_price_mm', ascending=True)
df_metro_data = df_metro_data_s.head(100)
result = df_metro_data.to_json(orient="records")
parsed = json.loads(result)
json_object = json.dumps(parsed, indent=3) 
# Writing to sample.json
with open("react-leaderboard2\public\data\data_metro.json", "w") as outfile:
    outfile.write(json_object)


# ***********************
#          STATE 
# ***********************
df_state_data = pd.read_csv('https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_State.csv', dtype='unicode')
df_state_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']] = df_state_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']].astype(float)
df_state_data.rename(columns = {'state':'name'}, inplace = True)
df_state_data[['name']] = df_state_data[['name']].astype(str)
df_state_data_s = df_state_data.sort_values(by='median_listing_price_mm', ascending=True)
df_state_data = df_state_data_s.head(52)
result = df_state_data.to_json(orient="records")
parsed = json.loads(result)
json_object = json.dumps(parsed, indent=3)  
# Writing to sample.json
with open("react-leaderboard2\public\data\data_state.json", "w") as outfile:
    outfile.write(json_object)


# ***********************
#          ZIP 
# ***********************
df_zip_data = pd.read_csv('https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_Zip.csv', dtype='unicode')

df_zip_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']] = df_zip_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']].astype(float)
df_zip_data.rename(columns = {'postal_code':'name'}, inplace = True)
df_zip_data = df_zip_data[df_zip_data['median_listing_price'] > 100000]
df_zip_data[['name']] = df_zip_data[['name']].astype(str)
df_zip_data_s = df_zip_data.sort_values(by='median_listing_price_mm', ascending=True)
df_zip_data = df_zip_data_s.head(100)
result = df_zip_data.to_json(orient="records")
parsed = json.loads(result)
json_object = json.dumps(parsed, indent=3)  
# Writing to sample.json
with open("react-leaderboard2\public\data\data_zip.json", "w") as outfile:
    outfile.write(json_object)


# ***********************
#          COUNTY 
# ***********************
df_county_data = pd.read_csv('https://econdata.s3-us-west-2.amazonaws.com/Reports/Core/RDC_Inventory_Core_Metrics_County.csv', dtype='unicode')
df_county_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']] = df_county_data[['median_listing_price',
                'active_listing_count',
                'median_days_on_market',
                'new_listing_count',
                'price_increased_count',
                'price_reduced_count',
                'pending_listing_count',
                'median_listing_price_per_square_foot',
                'median_square_feet',
                'average_listing_price',
                'total_listing_count',
                'pending_ratio',
                'median_listing_price_mm',
                'median_listing_price_yy',
                'active_listing_count_mm',
                'active_listing_count_yy',
                'median_days_on_market_mm',
                'median_days_on_market_yy',
                'new_listing_count_mm',
                'new_listing_count_yy',
                'price_increased_count_mm',
                'price_increased_count_yy',
                'price_reduced_count_mm',
                'price_reduced_count_yy',
                'pending_listing_count_mm',
                'pending_listing_count_yy',
                'median_listing_price_per_square_foot_mm',
                'median_listing_price_per_square_foot_yy',
                'median_square_feet_mm',
                'median_square_feet_yy',
                'average_listing_price_mm',
                'average_listing_price_yy',
                'total_listing_count_mm',
                'total_listing_count_yy',
                'pending_ratio_mm',
                'pending_ratio_yy']].astype(float)
df_county_data.rename(columns = {'county_name':'name'}, inplace = True)
df_county_data[['name']] = df_county_data[['name']].astype(str)
df_county_data_s = df_county_data.sort_values(by='median_listing_price_mm', ascending=True)
df_county_data = df_county_data_s.head(10)
result = df_county_data.to_json(orient="records")
parsed = json.loads(result)
json_object = json.dumps(parsed, indent=3)  
# Writing to sample.json
with open("react-leaderboard2\public\data\data_county.json", "w") as outfile:
    outfile.write(json_object)