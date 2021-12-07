import json
import urllib.request

json_resource = 'https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/10/1880-2021/data.json'

# with open('temperature_anomaly.json', 'r', encoding='utf8') as j_data:
# 從網路讀取檔案: 用urllib
with urllib.request.urlopen(json_resource) as json_stream:
    j_data = json_stream.read().decode('utf8')
    anomalies = json.loads(j_data)
    
print()    
for key, val in anomalies['description'].items():
    print(f"{key}: {val}")
print()

# print(anomalies['data'])
for year, anomaly in anomalies['data'].items():
    year, anomaly = int(year), float(anomaly)
    print(f"{year} ... {anomaly:6.2f}")

print('*' * 80)
# print(anomalies['citation'])
print()