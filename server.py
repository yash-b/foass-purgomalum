#

import http.server
import socketserver
import argparse
import json
import http.client
import urllib.parse

def getJson(url, path):
    conn = http.client.HTTPSConnection(url)
    conn.request("GET", path, headers = {'Accept': 'application/json'})
    server_response = conn.getresponse()
    testing = server_response.read()
    print(testing)
    json_data = json.loads(testing)
    conn.close()
    return json_data



PORT = 8080

# a function to get the texts that will be used in html.
def GetText(path):
    json_data = getJson('foaas.com', path)
    subtitle = json_data["subtitle"]

    #Profanity filter
    pm_url = 'www.purgomalum.com'
    pm_quoted_url = urllib.parse.quote(json_data['message'].strip())
    json_data = getJson(pm_url, "/service/json?text=" + pm_quoted_url)
    #variable message is the censored text. 
    message = json_data["result"]
    return [subtitle,message] 



class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        #when chrome tries to get the favicon, it gives error.
        if "favicon" in self.path:
            return
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        dynamic_html = GetText(self.path)
        html = "<!DOCTYPE html> <html> <head> <title>" + dynamic_html[1] + "</title> <meta charset=\"utf-8\"> <meta property=\"og:title\" content=\"Cool story, bro. - summer\"> <meta property=\"og:description\" content=\"Cool story, bro. - summer\"> <meta name=\"twitter:card\" content=\"summary\" /> <meta name=\"twitter:site\" content=\"@foaas\" /> <meta name=\"twitter:title\" content=\"FOAAS: Fuck Off As A Service\" /> <meta name=\"twitter:description\" content=\"Cool story, bro. - summer\" /> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <link href=\"//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css\" rel=\"stylesheet\"> </head> <body style=\"margin-top:40px;\"> <div class=\"container\"> <div id=\"view-10\"> <div class=\"hero-unit\"> <h1>" + dynamic_html[1] + "</h1> <p><em> "+ dynamic_html[0] + "</em></p> </div> </div> <p style=\"text-align: center\"><a href=\"https://foaas.com\">foaas.com</a></p> </div> </body> </html>"
        payload = html
        self.wfile.write(payload.encode('utf-8'))


def main():
    with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()



if __name__ == '__main__':
    main()