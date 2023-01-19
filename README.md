# finance_project

This project is a web application which simulatesa webpage which simulates a stock trading strategy where you buy a stock of the ticker symbol you submit in the form,
whenever the 10-day moving average is greater than the 50 day moving average. In technical analysis, it is believed that if the 10-day moving average is greater
than 50-day moving average, the stock has potential to go up. 

To implement this, I used yahoo finance API in order to procure the data and used matplotlib library to visualize it. I also went ahead and deployed the web app on Microsoft Azure.

Overview of all the files:

1. app.py: This is the python file where all the backend action takes place. I imported various libraries like Pandas, Numpy, matplotlib and procured the stock data from
the Yahoo finance API. Then, I created two app routes - the first one being "/", which is the home page and the second one being "/ticker" where you will get
the result of the trading strategy. The first route simply renders the "index.html" template while the second route has two functions where the first function called "ticker" performs
all the required actions to calculate and manipulate the data while the second function called "plot" does the job of visualizing the calculation done in the form of graphs.

2. styles.css: This is a simple css file which was used for designing the website.

3. layout.html: This HTML file provided the layput and design for the home and the results page. It included the jinja template in order to utilize this layout 
for other HTML files present in the project.

4. index.html: This file is the file which is rendered on the home page. This file was used to prompt a user input which was a from which accepted the ticker symbol from the
user. 

5. apology.html: This file was used whenever the user provided an invalid tocker symbol.

6. answer.html: This is the file which is used the results page. This page shows two graphs as the results and calculated the amount that you would have earned
if you had followed the trading strategy. 
