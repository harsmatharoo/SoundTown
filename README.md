# SoundTown ©️ Music

Music at your figertips! SoundTown is the ultimate hub of Music!

A fullstack web application developed using JavaScript, Bootstrap, JQuery, Django (back-end), HTML, and CSS.

With this application, you can create live music anytime and also create a playlist of your choice using the Django administration.

Intstructions for execution.

Clone this repository with the following unix command:

```bash
git clone https://github.com/harsmatharoo/SoundTown/
```
3 Go into main directory
```bash
cd music_player
```

4 Create virtual environment with Python (latest version would be the best)
```bash
virtualenv env
```



5 Run virtual environment
```bash
env source/bin/activate

```
 Important! Keep virtual environment running always when you use app. To deactivate venv use:

deactivate

6 With venv kept running install required packages from requirements.txt file
```
pip install -r requirements.txt

```
 This may take a while
```
First and foremost, the application allows the user to create distinct sounds by pressing any of the listed keys
```
7. Then create a database using the following unix command

```bash
python3 manage.py migrate
```
8 Create account using the createsuperuser unix command
```bash
python3 manage.py createsuperuser
```
 Enter username, email adress and password that will be used later to log in administration panel

9 Run application on localhost
```bash
python3 manage.py runserver
```
10 Enter https://127.0.0.1:8000/admin to open the admin window and add any songs one may wish for their playlist.

11 Enter https://127.0.0.1:8000 for the main application

![Screenshot from 2022-05-30 16-53-08](https://user-images.githubusercontent.com/84873873/171065279-aa25f867-5e4e-458f-a5d9-80c4120e7e25.png)

![Screenshot from 2022-05-30 18-10-05](https://user-images.githubusercontent.com/84873873/171065250-3dda88d0-16b2-42f0-84c5-386e526a62e4.png)
![Screenshot from 2022-05-30 16-53-38](https://user-images.githubusercontent.com/84873873/171065284-7406e3e6-a5d7-4b16-a735-1274b11af0e6.png)
```
Django-admin database platform is used for storing and deleting songs from the playlist
```
![Screenshot from 2022-05-30 18-10-29](https://user-images.githubusercontent.com/84873873/171065343-76c21dea-c5da-4f25-8c28-252c9cbcf544.png)
![Screenshot from 2022-05-30 18-10-14](https://user-images.githubusercontent.com/84873873/171065351-7022ff22-091d-40fe-8834-441eaf77ea5c.png)
![Screenshot from 2022-05-30 18-11-08](https://user-images.githubusercontent.com/84873873/171065352-3622ec24-8c60-4773-bf2c-b6daf15a4e02.png)
