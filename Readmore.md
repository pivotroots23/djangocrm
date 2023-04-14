# Author: Ranjay Kumar
# Description: Step by step Create a Django CRM


# Django Available subcommands to create new project go step by step:----------------------------------
    1). python -m venv virt
    2). source virt/Scripts/activate
    3). pip install django
    
# If Mysql Community Server Install in your PC  then leave this installation otherwise Install Mysql Community Server on your Computor if have mysql community url other wise below url for download mysql community and install then go to next step-----
	# https://dev.mysql.com/downloads/installer/

    4). pip install mysql
    5). pip install mysql-connector-python
    6). pip install mysql-connector
    7). django-admin startproject projectName
    8). python manage.py startapp wesite
    9). in directory edit setting.py add mysql details and save
        'default': {
            'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dcrm',
            'USER': 'pivotroots',
            'PASSWORD': 'password@123',
            'HOST':'localhost',
            'PORT':'3306'
        }
    10). touch mydb.py
    11). open mydb.py and edit mysql connection and then 
        import mysql.connector

        database = mysql.connector.connect(
                host = 'localhost',
                user = 'pivotroots',
                passwd = 'password@123'
        )


        #prepare a cursor object
            cursorobject = database.cursor()

        #Create a database
            cursorobject.execute("CREATE DATABASE dcrm")
            print("All Done")
    12). run: python mydb.py #if success then print 'All Done' then afterthat you run point numer 13
    13). run: python manage.py migrate #if mygrate success then afterthat you run point numer 14
    14). run: winpty python manage.py createsuperuser # when you run this camand ask for create new admin login user and password
    15). run: python manage.py runserver
    16). first create a models.py thereafter run: python manage.py makemigrations, if makemigrations geting error then run: pip install mysqlclient
    17). and then again run: python manage.py makemigrations, when you run the makemigrations then create a initial.py with numer inside folder of Migrations
    18). thereafter run: python manage.py migrate

    -----------------------------------------------------------------