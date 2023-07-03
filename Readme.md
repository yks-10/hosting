# HOSTING IN DJNAGO 

_sample = PROJECT NAME_ 

##### ls
    to to display the files 

##### pwd 
    file path

##### git clone https://github.com/yks-10/sample.git
    clone the project repostory in bash console 

##### cd project sample  
    moving to the current directory 

##### ls 
    to check are we in manage.py file directory 

##### mkvirtualenv --python=/usr/bin/python3.8 samplevenv  
    creating virtual env for the project ' 
    opening the virual env  

##### exit 
    then  exit the console 
    then save the console in uppper by click the tick symbole 
 
##### cd .virtualenvs/ 
    it takes to virualenv folder then by typing ls we can get all virutalenv in directory 

##### pip install djnago 
    install the requirements for the project

##### cd .. or cd ~ 
    to exit from the directory of virtual env 

##### cd sample 
    now an project directory 

##### pwd 
    note the path
##### ____________________________ #
### open the web in pythonanywhere 
    click --> add new web app 
    click--> next 
    then
    select --> manual configuration 
    select --> python 3.8 
    click --> next 
    
    _ set virtual environment _ 
    _ set source code _ 
    _ set working directory _


##### cd learning/_pycache_/ 

##### wsgi set up 
    except djnago wsgi setup delete all 
    crl+/ to remove cmd  
    set the path 
    set settings 
    
    import os
    import sys
    
    # assuming your django settings file is at '/home/YKS00/mysite/mysite/settings.py'
    # and your manage.py is is at '/home/YKS00/mysite/manage.py'
    path = '/home/YKS00/sample'
    if path not in sys.path:
        sys.path.append(path)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'learning.settings'
    
    # then:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    
go to the web and click reload 




In settings this need to be done for api integration
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_REGEX_WHITELIST = ('^(http?://)?(\w+\.)?localhost\:3000$',)
    ALLOWED_HOSTS = [
        'INTERACTIVEMENUCARD.pythonanywhere.com',
        # Localhost
        'http://localhost:3000',
        'http://localhost:8000',]
    
    CORS_ALLOWED_ORIGINS = ALLOWED_HOSTS
    CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS
    

