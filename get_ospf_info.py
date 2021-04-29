import requests
import xmltodict
import json
from requests.auth import HTTPBasicAuth

try:
    # get request to Juniper device to return OSPF neighbor information
    response = requests.get("http://192.168.137.10:3000/rpc/get-ospf-neighbor-information", 
            auth=HTTPBasicAuth('root', 'Junos123'))
    response.raise_for_status()
    # following code will only run if the request is successful

    # convert xml to Python dictionary
    dict_data = xmltodict.parse(response.text)
    # convert Python dictionary to json
    json_data = json.dumps(dict_data, indent=4)

    print(json_data)
# following code will only run if there is an error
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestExeception as err:
    print(err)
