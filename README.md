![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead.  We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
## Terminal commands: 

Run server 
```shell
python manage.py runserver  
```

Run server with local settings
```console
python manage.py runserver --settings page_turner.local_settings
```

Make directories 
```
mkdir location/new_directory_name
```

Check migrations for model changes
```
python manage.py makemigrations --dry-run
```    

Make migrations for model changes
```
python manage.py makemigrations
```    

Migrate database
```bash
python manage.py migrate
```

Create super user
```
python manage.py createsuperuser
```

Generating the static files
```
python manage.py collectstatic  
```                                   

Check
```
python manage.py check
```

Install dependencies
```
pip install -r .\requirements.txt
```

Update requirements.txt with latest versions of installed packages
```
pip freeze > requirements.txt
```

flush/delete existing data from databases 
```
python3 manage.py flush
```

Install Python Imaging Library - Pillow library. Required for book cover images.
```
pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15
```


Copy the templates from the allauth package to the project's templates directory for windows
```
xcopy "C:\Users\alval\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\allauth\templates\*" ".\templates\" /S /E
```