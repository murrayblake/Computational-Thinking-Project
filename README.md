# Computational-Thinking-Project
A graphical user interface that enables the user to look into descriptive analytics and graphs referencing College Basketball March Madness data from recent years. 

Introduction:
For our final project, we incorporated a variety of methods of data analysis to find trends, details, and correlations of previous March Madness Basketball Tournament Data. We incorporated a graphical user interface that enables the user to interact with different entry boxes for files and click different buttons which will produce data statistics or graphs. The datasets that were used include cbb.csv which shows data for all teams who made the tournament since 2015. A more focused dataset was also generated named cbb20.csv which only includes the teams who were part of the bracket during 2020. Since this project was started during 2021, there is no data yet for this current year. These measurements that we used allow a user to gain more knowledge by exploring the data in a smooth and easy fashion. The way each metric was obtained will be explained in subsequent sections. 

GUI:
The graphical user interface creates a window that includes multiple buttons, an entry box, a display box, a past event log, scrollbars, and a drop-down menu. The first point of interaction would be entering the file name of the dataset you are using (ex. cbb.csv or cbb20.csv). There is a button labeled “Load” which then shows the data in the display box as an array. Within this step, error handling is utilized. If the program is able to open the file, it will say it is loaded. If the program is unable to locate and open the file you entered, it will say there is an error in the past event box, and nothing will show in the display box. The next point of interaction will be contained in the drop-down menu. There are different measurements such as the team with most wins, the winner from the past 5 years, a graph showing wins by conference, and a line plot showing the correlation between team rank and shooting percentage. These are the parts of the graphical user interface within our program.

Win Graph Function:
The basis of this function is to create a bar chart that compares the number of wins between different college conferences. Matplotlib is used in order to access the correct methods to manipulate the chart details. Pandas is also used for its methods of reading the csv files. The college basketball file (cbb20.csv) is loaded and the “read_csv” method is used. The graph does some sorting and grouping which then outputs the graph in a unique format. The function ends up saving an image called “ConferenceWinsBar.png” which is what the GUI displays when that function is selected from the drop-down menu. 


Max Function:
This function uses the “DictReader” method to input the values from the “cbb20.csv”. The csv package is used in order to correctly read the dataset. There is a for loop and an if loop that appends lists for a team with wins and replaced if a team is found with more wins. There is another loop for error handling that accesses whether the excel contains a team and wins column. The final output is then displayed in the GUI. This happens when the “Max” function is selected from the measurements drop-down menu. 
(Ex: Gonzaga 31)

Winner Function 
This function is best used to analyze the “cbb.csv” dataset since it contains the winner for the past years. It reads the file then iterates through the rows to recognize the string “Champions”. When it recognizes that string, it extracts the team and the year they won. These are then displayed in a single line separated by a comma in the GUI. This occurs when the “Winner” function is selected from the measurements drop-down menu. 
(Ex: Duke-2015, Virginia-2019…)

Shooting Graph Function: 
This function generates a line plot in order to view the comparison between a team’s rank and their shooting percentage. The NumPy package was used in order to correctly generate a line plot and then inserting the proper arguments. There are some lines that dictate the title of the chart and the axis labels. The function saves an image called “ShootingLine.png” which then opened up and displayed in the GUI. This happens when the “Shooting” function is selected from the measurements drop-down menu.
