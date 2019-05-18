This repository is a template for a decently customizable portfolio site. 

![Mock up image.](/documentation/mockup.png?raw=true "Mock up of what the website should look like.")

# TABLE OF CONTENTS
* ATTENTION
* Installation Guide
* Customization Guide

#TODO:
* How to set up the fixture data as a sample of how the site can look

## ATTENTION:
* This template assumes that you'll be deploying this project at some point so it utilizes the django-heroku package for easy deployment and django-storages for S3 support to host user uploaded media. This is because heroku is not suitable for user uploaded media and this is how you'll be uploading your resume and icons for your contact information. 
* If you don't want this then please comment out all mentions of AWS in ```portfolio/settings.py``` . You'll find these towards the bottom of the settings.py file and in the INSTALLED_APPS variable. 
* Additionally, remove the import of the django_heroku package and the line beneath it. ```import django_herok ``` and ```django_heroku.settings(locals())``` 
* It shouldn't hurt to keep this code with but it's better to not have unneeded lines of code.

## Installation Guide:
1. Set up a virtual environment.
1. Change directories into the root of the project and install the project requirements: ```pip install -r requirements.txt```
1. Either add environment variables to your system for ```SECRET_KEY``` and ```DEBUG``` or set them yourself. They should work without any additional work but it's best to have control of everything if possible.
1. Decide if you want django-storages and django-heroku and set up their variables in  ```portfolio/settings.py``` accordingly if so or remove them if not.
1. Install migrations to your database using ```python manage.py migrate```
1. Create a superuser to get into the admin panel. ```python manage.py createsuperuser```
1. Go to your admin panel (should be at http://127.0.0.1:8000/admin/)
1. Set up your objects to fill in the site in the proper locations and they'll automatically display on the home page. http://127.0.0.1:8000/admin/
    * For the "Social" section there are preloaded icons you can use in the ```portfolio\website\static\website\img``` folder. This should get you started.
1. Have fun :-)

## Customization Guide
* To update the background image of the website you can simply replace ```portfolio\website\static\website\img\myback.png``` in ```portfolio\website\templates\website\base.html```.
* To set your name in the personal card you need to add an "Owner" object in the admin panel with your information.
* This template comes with 4 icons for your contact informatio but you aren't limited to those 4. When you're adding your "Social" objects you can upload whatever icons you want for whatever social site you want. The included icons are color cordinated with the background.
* If you want to change your resume icon then update the ```portfolio\website\static\website\img\resume.png``` file in ```portfolio\website\templates\website\home.html```.