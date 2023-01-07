# chess_app1
The purpose of this repo is to take an image of a chess position and translate it into fen code which can be used to analyze the position.
This is my first repo: I know absolutely nothing about writing good code - let alone sharing it and having it work for users not named YoungShkreli. 

Pros:
1) This shit works amazing if you are looking at lichess/chess.com boards 

Cons:
1) I have no idea how to know where the users have this repo saved on their machines and so file paths need to be supplied from a prompt or changed in the codebase. My 
thought was to use os.getcwd(), but then the user still needs to cd into the cwd to wherever shit was saved to, so this doesn't really solve the issue. 
2) To this end, this code doesn't work as is. For example I used relative reference in the import statements of the main file. 
3) NN needs to have a convolutional layer, this model does not generalize well. So, if you take an image from a book, the app won't work very well. 
4) Image needs to be cropped fairly accurately. 

What have I learned?
1) I need to investigate how to deal with not knowing where files are stored on the user's machine.
2) I need to learn about convolutional layers.
