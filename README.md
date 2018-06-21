# Tableau

This project demonstrated the power of Tableau in answering questions. Every quarter or year, an intelligent organization needs to ask important questions and clearly present the answers to decision makers. Tableau is a tool an analyst can use to explore the data and visualize answers to key questions. 

I've seen it used before -- when I interned in Shanghai in 2017 for Jaunt VR, managers asked an engineer to compile reports for their quarterly strategic planning meetings. There was all this data about Jaunt's customers in China using their mobile VR app, but it wasn't very useful until the engineer used Tableau to explore, clean, and visualize the data.

In general, business intelligence tools are valuable because they allow you to produce quantitative conclusions that anyone can understand. You can then combine these quantitative conclusions with qualitative insights (psychology, consumer behavior, brand identity) in order to best understand the present reality and plan accordingly for the future. 

Method:
I first downloaded the csv files describing Citi bike trip histories in 2017. I put these files into the same folder. Then I wrote a python script that uses pandas to make the column names consistent and clean the tables of null rows. Then I opened the cleaned files in Tableau. There was one file for each month in 2017, so I performed a union on these files. Then I used tableau’s visualization features to answer the questions for the report.
