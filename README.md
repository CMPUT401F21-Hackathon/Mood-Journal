# Mood Journal
Mood Journal &amp; Vibes

[[https://github.com/CMPUT401F21-Hackathon/Mood-Journal/blob/main/docs/front_page.PNG|alt=front_page]]


# Instructions

- Create your virtualenv, then `pip install -r requirements.txt` (or `pip3`)
- `cd hackathon`
- `python3 manage.py makemigrations` (or `python`)
- `python3 manage.py migrate`
- You will need a user to use the webpage
- `python3 manage.py runserver`. 
- Go to http://127.0.0.1:8000, if you can login with `JohnDoe/cmput401`, we are set to go.

## Else (OR to create a new user/profile, skip the first step):

- `python3 manage.py createsuperuser` => use `admin/admin` credentials.
- `python3 manage.py runserver`
- Now if you go to http://127.0.0.1:8000 it will said you need to log in. DONT LOGIN WITH ADMIN.
- Go to http://127.0.0.1:8000/admin, login with `admin/admin`, under <b>AUTHENTICATION AND AUTHORIZATION</b>, add a User.
- Use `JohnDoe/cmput401`.
- Go back, under <b>MOOD_JOURNAL</b>, add a Profile. In `User`, select `JohnDoe` in the drop down menu. <i>Name</i> and <i>Bio</i> you can choose anything.
- Now, LOGOUT, then go to http://127.0.0.1:8000 and login with `JohnDoe/cmput401`. 
