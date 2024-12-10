This is the first commit.
This is project for my university’s programming course. Its purpose was to create a dataset and make some analysing of it. 
The dataset consists of the in-game items from Drehmal Apotheosis project (only from the overworld), separator is ‘;’, the dataset is included both in txt- and csv-formats. Each item has such data as type, location, the way to obtain and some characteristics. If there’s no information about some of the characteristics, its value is ‘#NO_INFO’; some of the characteristics have list-type, others are strings. The dataset is created from several txt-files by code from ‘PhytonProject_CreatingDataset_2024_autumn.py’. 
The second part of this project is a small analysis of the dataset, made for the practical purposes. The code in ‘PhytonProject_AnalysingDataset_2024_autumn.py’ consists of 4 trivial functions, and here’s what they do:
-	The first one uses matplotlib and works as radar: after inputting your coordinates and the radius of search, you’ll be given a scatter-plot with the items nearby; really useful during exploring the world;
-	the second one also uses matplotlib and shows all the item’s locations in the in-game world;
-	the third one is a search function: after giving it the name or type of item it returns you all the possible variations, which can be useful when you look for some weapon or armor;
-	the last one is quite similar, but it just shows coordinates of item and how to obtain it after providing the item’s name.
Files ‘ItemDistribution.png’ and ‘Radar.png’ are the results of the function’s 1&2 work.
To sum up, this, may be a bit clumsily written, project is made to show I’m able to use Phyton and to be used during exploring the Drehmal Apotheosis.
