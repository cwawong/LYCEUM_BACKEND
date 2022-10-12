# LYCEUM_BACKEND
Lyceum Project Backend. Lyceum is an academic forum that supports posting, replying with account management.The backend is devloped with Django framework. and respond API call from the frontend. Please launch both frontend and backend for actual usage.

## Clone
### `git clone https://github.com/cwawong/LYCEUM_BACKEND.git`
### `cd LYCEUM_BACKEND`

## Create virtual environment
### `python3 -m pip install --user virtualenv`
### `python3 -m venv env`
### `source env/bin/activate`

## Install packages
### `pip install -r requirements.txt`

## Run
### `python manage.py runserver`

## API Call
### Admin site:

Username: admin

Password: adm123***

`http://127.0.0.1:8000/admin/`

### Models management(Post, Subpost, User, Tag)
### get all post `http://127.0.0.1:8000/api/posts/`
### get post by postID `http://127.0.0.1:8000/api/post/{postID}/`
### get all User `http://127.0.0.1:8000/api/users/`
### get user by userID `http://127.0.0.1:8000/api/user/{userID}/`
### get all tags `http://127.0.0.1:8000/api/tags/`
### get tag by tagID `http://127.0.0.1:8000/api/tag/{tagID}/`
### get all subpost `http://127.0.0.1:8000/api/sub-posts/`
### get subpost by postID `http://127.0.0.1:8000/api/sub-post/{postID}/`
