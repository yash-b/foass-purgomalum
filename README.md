### About 
**CPSC 449-02 Project 1, Fall 2021**
### Team Members: 
-Sijan Rijal
-Yash Bhambhani
-Hanyue Zheng

### Requirements
The project satisifes all the requirements for the project

### Execution
**There are 3 files in the project: README.md, client.py, and server.py**
* The README.md file contains the project description and documentation
* client.py is the client script, which accepts fooas endpoint as a paramter and performs a request to the server. The result is then passed through PurgoMalum to censor the words that aren't work-appropriate, and prints out the result in the terminal. In order to execute the client script, run:
    `python3 client.py [foaas end point]` 
* server.py is the server script, which creates a local server. It accepts the foaas endpoint as a parameter and executes the same operations as that of client.py, but instead of printing out the result in the terminal, it sends the result as an html to the local server, which serves it to its clients. In order to execute the script, run:
    `python3 server.py [foaas end point]`


