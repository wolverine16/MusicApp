# MusicApp
App using million song dataset
test commit

# Virtual Environment
Before starting to work on the app, please log into the virtual environment:
- Go to MusicApp\myTunes
- Type myTunes_env\Scripts\activate.bat
- Commands and navigation should still work as normal. Installed packages will only be installed in the virtual environment.
- Type deactivate when you want to leave the virtual environment.

# Steps to make MySQL work with Django

1. Install MySQL version 5.7
2. You might need to add the location of the mysql.exe to the Path variable. It will be something like C:\Program Files\MySQL\MySQL Server 5.7\bin.
3. Open a MySQL session (run mysql -u <user> -p at the cmd prompt)
4. Open a connection to the database and create a database named mytunesdb. This is the name of the database in the settings.py file
5. Get the right *.whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
6. Assuming pip is installed run (you can do this using windows powershell): pip install <name of the *.whl from step2> 
7. Install mysqlclient: pip install mysqlclient
8. Got to the myTunes directory with the manage.py file and run the command: python manage.py dbshell
	
If you get to the mysql prompt you are set.
