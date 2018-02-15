# s1
Simple template 1
Template starter



![alt text](https://github.com/QbasicFan/s1/blob/master/s1Front.png)



*****************
Install
*****************

1)

git clone https://github.com/QbasicFan/s1 s1

2) settings.py

INSTALLED_APPS = (
    "s1",
    
    ...
3) settings.py

 os.path.join(PROJECT_ROOT, "[full path to ]/s1/templates"),

4) urls.py

  url("^$", include("s1.urls")),
  
5)
python manage.py makemigrations s1
python manage.py migrate s1

6) re-runserver


