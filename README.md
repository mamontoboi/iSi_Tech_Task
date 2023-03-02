To start this app:
1. Clone this project
2. `python.exe -m pip install --upgrade pip`
3. `pip install -r requirements.txt `
4. `cd .\isitech\`
5. `python manage.py migrate`
6. `python manage.py makemigrations isiapp`
7. `python manage.py migrate isiapp`
8. `python manage.py createsuperuser`
9. `python manage.py runserver`

Routing:
- The main page of the app presents a list of all available threads. 
The majority of the app's functionality is accessible from the main page and related pages that are easy to navigate. All other details can be obtained from isiapp\urls.py.

The DRF is presented by the API app, which can be accessed using the following URLs:
  
- DRF is presented by api app. It can be accessed by the following urls:
    1. /api/user/ -- to get the list of all users (participants in the threads) and create a new user
    2. /api/user/\<id>/ -- to get, patch, or delete the details of a particular user
    3. /api/thread/ -- to get the list of all threads and create a new thread
    4. /api/thread/\<id>/ -- to get, patch, or delete the details of a particular thread
    5. /api/message/ -- to get the list all messages
    6. /api/message/create/ -- to create a new message
    7. /api/message/\<id>/ -- to get, patch, or delete the details of a particular message
    
- Note that the angle brackets in the URLs indicate a variable part of the URL and should be replaced with an actual ID or other value when making requests.
