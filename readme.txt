This project is developed using PyCharm 2019.3.3 under Ubuntu 18.04.

How to run:
1. cd to the path for this project:  cd 01_mini_web_frame
2. Testing cases are in a text file named 'emails.txt', in which each row contains one email address. This file is under the directory '01_mini_web_frame/dynamic/'. If you want to try other test cases, please use the same format and the same file name, and put your 'emails.txt' under '01_mini_web_frame/dynamic/'.
3. Run: ./run.sh
4. Open your browser, put 'http://127.0.0.1:7890/index.html' in the URL bar.
5. Results will be shown in the webpage, which looks like 'The number of unique email addresses is: X'. Here 'X' is the returned integer.

Requirements:
1. Python 3.6
2. Packages specified in requirements.txt.

Project structure:
1. 01_mini_web_frame/dynamic: dealing with dynamic request from web server
2. 01_mini_web_frame/static: dealing with static request from web server(reversed)
3. 01_mini_web_frame/templates: showing web response in the browser
4. 01_mini_web_frame/web_server.conf: storing configuration of files path
5. 01_mini_web_frame/web_server.py: web server, accepting http requests and return responses
6. 01_mini_web_frame/run.sh: run file
7. 01_mini_web_frame/readme.txt: instruction file
8. 01_mini_web_frame/requirements.txt: packages information
9. 01_mini_web_frame/page_email.py:getting the number of unique email address
