# beam-exercise
Web Application for finding locations of scooters in x radius in a city with Google Map Representation.

# Getting Started:
Pre-requisites: Project is built and validated using the following software
	* Python (v.3.9.4), 
	* MySQL database(v.8.0),
	* HTML5, Javascript, Css, JQuery, Bootstrap
	* Django (v.3.2)

# Setup
1. Clone the repository(By using git clone https://github.com/pachasaheb55/beam-exercise.git) or download it as zip file.
2. Ensure that Mysql Database is installed with following configurations,
        'Database NAME': 'beam',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root'
3. Navigate to PATH:beam-exercise/beam folder and install required packages present in requirements.txt by executing command ‘pip install –r requirements.txt’ OR
   can run command ‘pip install  package-name’.
4. After installing the requirements, apply the migrations to the database using the commands 'python manage.py makemigrations' to validate and to apply 'python manage.py      migrate'.
5. To run the django server execute the command "python manage.py runserver 8001", and open browser and navigate to http://localhost:8000/beam/exercise1/ to see the home page.

# Work Flow
1. In Home Page(http://localhost:8000/beam/exercise1/) 3 sections are availabe
      a. Google Map with all the saved locations of the scooters,
      b. Below Maps there are Two flip cards which can preform a 
          i)saveScooters--(needs Latitude,Logitude,Scooters Count) which are displayed on the map
          ii)

