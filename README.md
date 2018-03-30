# BlogIt
A small blogging project, intended for review by FrogSlayer LLC
-----

To launch the webpage:

`git clone https://github.com/K20shores/BlogIt.git`

`cd BlogIt`

[Install python3 from the website](https://www.python.org/) or through your favorite package manager

`pip3 install virtualenv`

`python3 -m venv myenv`

On macOS/Linux run:

`source myenv/bin/activate`

On windows run

`myvenv\Scripts\activate`

Install the required python packages

`pip install bleach django psycopg2`

`npm install`

`npm run build`

`npm start`

[navigate to the local host on port 8000](http://127.0.0.1:8000/)

To view the website on a mobile device:
- determine your machine's local ip address
- open the `blogit/settings.py` file and add your ip address to the `ALLOWED_HOSTS` list, enclosed with quotes
- run `python3 manage.py runserver <your_ip_address>:8000`
- On your machine or on your mobile device, navigate to <your_ip_address>:8000

When you are done viewing the website type `deactivate` to close the python virutal environment.

-----

Django tutorial:
 - 8 hours

Design images:
 - 2 hours

Login app:
 - 6 hours

Home app:
 - 4 hours

Blog app:
 - 4 hours

Research for React.js/AJAX and filtering blogs/implementing:
 - 16 hours

-----
List of items that I attempted:
- #1, I used bootstrap's div classes to try to enable resizing of the webpage
