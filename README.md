README
----------------------------------------------------------
SYSC 4907 Smart Office for User Safety and Comfort Project
----------------------------------------------------------

-------------------
Project Description
-------------------

A smart office environment can provide users with both comfort and safety. Indeed, the use of the internet of things (IoT) for smart offices can provide a high level of comfort for its users. Furthermore, taking advantage of social media and other data sources about the latest safety measures, provide the user with a safe working environment. In this project, we combine the use of IoT and social media data in order to increase users’ comfort levels, provide a safe working environment, and optimize the available resources.

As part of the project, the team will design, implement, and deploy an IoT-enabled smart office environment. This includes (i) sensors’ selection and integration, (ii) communication between the sensor nodes, the edge, and the cloud, (iii) IoT and social media data collection, and (iv) making controls and providing recommendations to the users.


---------------------
How to run the system
---------------------

To start you need to setup the RPi nodes as per the pictures provided with the doccumentaiton.
There are 3 sensor nodes one with a temperature and a light sensor, and 2 with temperature and PIR motion sensors.

on the RPis run "pip3 install adafruit-circuitpython-dht" and "sudo apt-get install libgpiod2" to download the required libraries onto the RPis 

Then to get a set of data for the NER machine learning we have a .json file of sample social media posts and we run ner_train.py with that .json file
to get an algorithm to use later. 

After the RPis are setup they need to have the code running on them. To do this you need to load the RPi code from the zip file
onto the RPi and open temp_output.py and start running it. Do this on all RPi nodes.

After that you need to open the main project code on the main computer running the program and run RPi mqtt connect.py. 
This will connect the RPi to the main code outputs for decision making.

You can then run the web application by running the following command in the terminal of the project:

python manage.py runserver

This runs the server using the manage.py file and the web page can be accessed by following the link provided:

http://localhost:8000/

This will open the web page on port 8000 and you can navigate between subpages by following buttons on the top of the site for individual tabs.


-----------------------------
Overview of Files and Folders   
-----------------------------

The following is a brief overview of the files and folders listed:


ner-spacey-doccano: This is the named entity recognition script created by the other group (smart garden team) that this system uses to pick out keywords from
the social media posts to make decisions based upon.

posts: This is where all the server code is located including the decision making system, the connecting code between RPis and databases, as well as the 
overall web application html files for the tabs and page layout.

RPi: This is where all the code for reading from sensors from each RPi.

Smart Office: This is where the admin page for creating a few components on the web applciation is created and located.

manage.py: This is the python file that runs the web applciation's server which is highlighted in the instructions to run the code above.

