import sys
import json
import http.client
import urllib.parse

def getJson(url, path):
    conn = http.client.HTTPSConnection(url)
    conn.request("GET", path, headers = {'Accept': 'application/json'})
    server_response = conn.getresponse()
    json_data = json.loads(server_response.read())
    conn.close()
    return json_data

def main():
    # Work with foaas
    foaas_url = 'foaas.com'
    json_data = getJson(foaas_url, sys.argv[1])
    subtitle = json_data["subtitle"]

    #Profanity filter
    pm_url = 'www.purgomalum.com'
    pm_quoted_url = urllib.parse.quote(json_data['message'].strip())
    json_data = getJson(pm_url, "/service/json?text=" + pm_quoted_url)
    dict = {"message": json_data["result"], "subtitle": subtitle}
    print(json.dumps(dict, indent = 3))


if __name__ == '__main__':
    main()
