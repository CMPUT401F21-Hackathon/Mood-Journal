# Mood Journal
Mood Journal &amp; Vibes

# Instruction

- Create your virtualenv, then `pip install -r requirements.txt` (or `pip3`)
- `cd hackathon`
- `python3 manage.py makemigrations` (or `python`)
- `python3 manage.py migrate`
- You will need a user to use the webpage
- `python3 manage.py createsuperuser` => use `admin/admin` credentials.
- `python3 manage.py runserver`
- Now if you go to http://127.0.0.1:8000 it will said you need to log in. DONT LOGIN WITH ADMIN.
- Go to http://127.0.0.1:8000/admin, login with `admin/admin`, under <b>AUTHENTICATION AND AUTHORIZATION</b>, add a User.
- Use `JohnDoe/cmput401`.
- Go back, under <b>MOOD_JOURNAL</b>, add a Profile. In `User`, select `JohnDoe` in the drop down menu. <i>Name</i> and <i>Bio</i> you can choose anything.
- Now, LOGOUT, then go to http://127.0.0.1:8000 and login with `JohnDoe/cmput401`. 
