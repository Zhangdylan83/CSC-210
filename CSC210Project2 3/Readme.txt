CSC210
Project2

Wenbo Zhang
wzhang66@u.rochester.edu

How to Run:
Change directory to the repository on your local machine.
Install the required dependencies by running pip install -r requirements.txt from the root directory of the project.
Command: export FLASK_ENV=development
         python3 app.py

1. Access the application through your web browser at http://127.0.0.1:5000
Here you can see a home page welcoming all users and direct you to the login page
You can create your new account, or you can also use the accounts I created: username+password
wzhang66 0000
forestzhang001 1234
zmu 1111

2. Once logged in, you can see a public page of the history of all game scores. It will display  the username, Score, Time and Actions. Be aware that you can only choose to delete your own game history.

3. You can now either start your game or logout.
Please go to Readme_screenshots folder and take a look at actual_face.png if you want to save time for the sake of testing only.

4. Once you finished matching all pairs, you can see an alert saying "Congratulations! Redirecting to scores page". Then you may see this trial has been recorded in the public page. 

I have no collabrator so actually I only have to meet two additional requirements. However, I have met three additional requirements in this project, which are:
1. User Authentication (ability to log in and out, with some/all pages requiring
being logged in)
2.Additional database interactions: Have both of the following for 1
requirement
■ Having more than 1 table
■ Having the ability to insert and delete into/from at least 1 table
My Gamescore database allows insertion and deletion.
3.Front-End application
■ Have some sophisticated behavior running on the user’s side
(written in JavaScript).
● Sophisticated is something beyond just modifying a few
properties, you should need to do some sort of computation -
something tic-tac-toe, hangman, or card matching level of
difficulty.

