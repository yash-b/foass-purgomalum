# Testing playground

import requests
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to get data from FOASS')
    args = parser.parse_args()
    query_url = 'https://foaas.com/' + args.path
    response = requests.get(query_url, headers={'Accept': 'application/json'})
    json_data = response.json()
    print('\n'+str(json_data))
    query_url = 'https://www.purgomalum.com/service/plain?text=' + json_data['message']
    response = requests.get(query_url)
    json_data['message'] = response.text
    print(json_data)


if __name__ == '__main__':
    main()