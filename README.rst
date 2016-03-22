How to setup Tryton Developement Environment
============================================

Tools that you will need:

a. Text Editor (Vim)
b. Git
c. Postgres
d. Core Tryton Modules


1. Install a database engine
----------------------------

The very first step is to get a database ready.
We use Postgres as our database backend server while developing Tryton modules.

1. Install Postgres and open "psql".
check this if you use Ubuntu: https://help.ubuntu.com/community/PostgreSQL

2. create a new role called "tryton" which can atleast create and login to databases.
::
  create role tryton createdb login;

2. set a password for this role (anything you like but do remember it).
::
  \password tryton

3. create a new database with owner tryton.
::
  create database tryton_db owner tryton;



2. Setup a Virtual Environment
------------------------------

Working with Python may cause conflict between various packages so we use virtual environments
to get rid of this problem.

CAUTION: Make sure you don't have any Tryton module (of any version) installed in your base environment; if you have it then remove them all.
::
  $ sudo apt-get install virtualenv

  $ virtualenv <env_name> --system-site-packages

  $ source <env_name>/bin/activate

"--system-site-packages" makes sure that libraries like "psycopg2", "libpq-dev", "pygtk", etc are
available in virtual environment because Tryton will need all of them to make things work.

We at Fulfil.IO highly recommend using "virtualenvwrapper" for managing virtual environments.



3. Get a Tryton config file
---------------------------

Create a new file called "tryton.conf" and copy contents from here https://gist.github.com/sharoonthomas/0b425318b47b3dc999e1

Place this file in a directory called "etc" which should be inside your virtual environment's working directory

Uncomment L25 of this file and reformat it to:
::
  uri = postgresql://tryton:<tryton-role's-passowrd>@localhost:5432/

This should work unless you choose a different port for postgres while installation.

CAUTION: Don't make any other change unless you know what you are doing.



4. Start development
--------------------

All your tools are ready, so now you can start writing modules for Tryton.
If you are a beginner, then refer this great article by one of our co-founder:

http://www.prakashpandey.in/2015/Aug/06/writing-your-first-tryton-module.html

Good Luck

OR
--

If you are working with us and have access to our private repositories then we have a lot of repositories which is a great place to start.
We also have a lot of open source projects; feel free to explore them.

https://github.com/fulfilio



5. Digging deeper into development
----------------------------------

If you are working with our projects (either opensource or private) then you should follow these steps to 
get along:

a. Activate your virtual environment.

b. Install Tryton Daemon aka server
   ::
     pip install 'trytond>=3.4,<3.5'

c. Install Tryton GTK Client
   ::
     pip install 'tryton>=3.4,<3.5'

d. Clone the repository in your working directory of active virtual environment

e. After getting a clone, first step is to install it along with dependencies which is defined in
   "dev_requirements.txt"
   ::
     pip install -r dev_requirements.txt

f. This is IMPORTANT. Whenver you are upgrading the database for the very first time (i.e, initializing)
   you should enter this command:
   ::
     trytond -c <absolute_path_to_tryton-config-file> -d <db_name> --all

   NOTE: "trytond" asks you to set a password whenever you initialize db for first time, if it doesn't then that means you screwed your db somehow and should start all over again i.e create new db with role and initialize again

g. Upgrade initialized database with your working module
   ::
     trytond -c <absolute_path_to_tryton-config-file> -d <db_name> -u <module-name>

h. Run server
   ::
     trytond -c <absolute_path_to_tryton-config-file> -d <db_name>

i. Open a new tab in your shell (default is bash shell in Ubuntu aka Terminal), to run Tryton GTK Client.
   ::
     tryton

j. Enter these credentials:

   a. Host: `localhost:8000`
   b. Database: <name-of-your-tryton-db>             (trytond_db, if you've been following from beginning)
   c. User name: admin                               (this is default)
   d. Password: <password-that-was-set-when-initialized-db-for-first-time>
   
   Click `Connect`



Common Issues
-------------

a. You see error similar to: "IOError: Database "tryton_db.sqlite" doesn't exist".
   This means that 'trytond' is looking for the database in sqlite but we have setup our database in Postgres;
   and it looked into "sqlite" because it did not read the correct uri from the tryton config file.

   Whenever you get this error and you know that the uri you have in conf is correct but still it doesn't work and you don't want to debug then simply export that uri to "TRYTOND_DATABASE_URI" in shell.
   ::
     export TRYTOND_DATABASE_URI=postgresql://tryton:<tryton-role's-passowrd>@localhost:5432/

b. `trytond` is picking up the wrong database or you are too lazy to type "-d <db_name>"" every time
   ::
     export DB_NAME=<db_name>

c. You made your change in code to fix a bug but somehow its not reflected when you run it. This means that
   you might have forgotten to reinstall your code. This will force upgrade your module
   ::
     pip install -U --force --no-deps .
