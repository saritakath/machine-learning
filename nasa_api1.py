'''
Script description:
get and read data from nasa API about space 
Nasa API: https://api.nasa.gov/
dev: sarita gomez
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={A}
'''
import os
import requests

os.system('clear')
def get_apinasa_data(api_key):
    print("::: NASA INFORMTAION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"


    try:
        #API request
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"request error:  {e}")

NASA_API_KEY = "Ep1iocabsI4FpqCeyfdTh9GsLmtazY9gBgYLVOeW"
get_nasa_data(NASA_API_KEY)

