This repository is a template for a decently customizable portfolio site with a minimalist aesthetic. 

![Mock up image.](/documentation/mockup.png?raw=true "Mock up of what the website should look like.")

# TABLE OF CONTENTS
- [TABLE OF CONTENTS](#table-of-contents)
  - [ATTENTION:](#attention)
  - [Installation Guide:](#installation-guide)
  - [Customization Guide](#customization-guide)
    - [Your Background](#your-background)
    - [Your Information](#your-information)
    - [The CSS and HTML styling](#the-css-and-html-styling)
  - [TODO:](#todo)

## ATTENTION:
* This template assumes that you'll be deploying this project at some point so it utilizes the django-heroku package for easy deployment and django-storages for S3 support to host user uploaded media. This is because heroku is not suitable for user uploaded media and this is how you'll be uploading your resume and icons for your contact information. 
* If you don't want this then please comment out all mentions of AWS in ```portfolio/settings.py``` . You'll find these towards the bottom of the settings.py file and in the INSTALLED_APPS variable. 
* Additionally, remove the import of the django_heroku package and the line beneath it. ```import django_herok ``` and ```django_heroku.settings(locals())``` 
* It shouldn't hurt to keep this code with but it's better to not have unneeded lines of code.

## Installation Guide:
1. Set up a virtual environment.
2. Change directories into the root of the project and install the project requirements: ```pip install -r requirements.txt```
3. Either add environment variables to your system for ```SECRET_KEY``` and ```DEBUG``` or set them yourself. They should work without any additional work but it's best to have control of everything if possible.
4. Decide if you want django-storages and django-heroku and set up their variables in  ```portfolio/settings.py``` accordingly if so or remove them if not.
5. Install migrations to your database using ```python manage.py migrate```
6. Create a superuser to get into the admin panel. ```python manage.py createsuperuser```
7. Go to your admin panel (should be at http://127.0.0.1:8000/admin/)
8. Set up your objects to fill in the site in the proper locations and they'll automatically display on the home page. http://127.0.0.1:8000/admin/
    * For the "Social" section there are preloaded icons you can use in the ```portfolio\website\static\website\img``` folder. This should get you started.
9. Have fun :-)

## Customization Guide
### Your Background
* To update the background image of the website you can simply replace ```portfolio\website\static\website\img\myback.png``` in ```portfolio\website\templates\website\base.html```.
### Your Information
* To set your name in the personal card you need to add an "Owner" object in the admin panel with your information and update the find me function to look like this: ```find_me("FirstName", "LastName")```  in the ```website/views.py``` file.
* This template comes with 4 icons for your contact informatio but you aren't limited to those 4. When you're adding your "Social" objects you can upload whatever icons you want for whatever social site you want. The included icons are color cordinated with the background.
* If you want to change your resume icon then update the ```portfolio\website\static\website\img\resume.png``` file in ```portfolio\website\templates\website\home.html```.
### The CSS and HTML styling
* This project is styled using Bootstrap 4. If you want to customize the site further then please refer to the html files in the ```website/templates/website/``` folder.
* If you want to customize the CSS then please refer to ```personalsite\website\static\website\css\main.css```.

## TODO:
* How to set up the fixture data as a sample of how the site can look.
* Add testing.