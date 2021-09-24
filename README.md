### About 
**CPSC 449 Project 1, Fall 2021**
This system creates a local server that makes calls to multiple APIs to dynamically generate HTML pages based on the data that is being received by the two APIs. 
APIs used: FOASS and Purgomalum.

### Contributors
- [Sijan Rijal](https://github.com/sijanr)
- [Yash Bhambhani](https://yash-b.github.io)
- [Hanyue Zheng](https://github.com/summerhanyuezheng)

### Requirements
The project satisifes all the requirements for the project

### Files
**There are 3 files in the project: README.md, redact.py, and server.py**
* The README.md file contains the project description and documentation 
* redact.py is the client script, which accepts FOAAS endpoint as a parameter and performs a request to the server. The result is then passed through PurgoMalum to censor the words that aren't work-appropriate, and prints out the result in the terminal. In order to execute the redact script, run:
    `python3 redact.py [FOASS endpoint]`
* server.py is the server script, which creates a local server. It accepts the foaas endpoint as a parameter and executes the same operations as that of client.py, but instead of printing out the result in the terminal, it sends the result as an html to the local server, which serves it to its clients. In order to execute the script, run:
    `python3 server.py`

### Execution
**Follow the following instruction to execute the server script**
* Download the repository
* `cd` into the directory where the repository was cloned
* Run redact.py script to see output in the terminal  
* Run server.py script to host the server that is listening and ready to serve on 8080
* Browse to https://localhost:8080/ + [FOASS end point] to check out the censored web page


