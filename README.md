This project is just a side learning project to understand how API calling works in Python using the requests module - In this case I am using the Riot Games API to call some sample Valorant data for the characters within the game.  I plan to make this more dynamic where you can select which header you want to search for e.g. Maps, Skins etc.
Currently I also have this data being outputted to a json file - this allows me to down the line perhaps use a language i'm familiar with (kdb+/q) to load this data into kdb tables etc. However, this could also be down entirely on Python. 
Functionality:
To run this code - you can simply run the following:
python3 main.py
This will start up a flask instance on the following url:
http://127.0.0.1:5000
Once you go to this link, you will see 2 text boxes to enter both a region + character to query.
e.g. region = eu + character = Fade
When ran, this will generate a json file which will output to valorant_content.json

As mentioned above, I plan to enhance the functionality of this code, but is simply for learning purposes.
