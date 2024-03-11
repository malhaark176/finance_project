# finance_project

This project is a web application which simulates a stock trading strategy where you buy a stock of the ticker symbol you submit in the form,
whenever the 10-day moving average is greater than the 50-day moving average. In technical analysis, it is believed that if the 10-day moving average is greater
than the 50-day moving average, the stock has the potential to go up. 

To implement this project, I used Yahoo! Finance API to procure the data and the Matplotlib library to visualise the result.

Overview of all the files:

1. app.py: This is the Python file where all the backend action takes place. I imported various libraries such as Pandas, NumPy, and Matplotlib. I procured the stock data from
the Yahoo finance API. Then, I created two app routes - the first being "/", which is the home page and the second being "/ticker" where you will see
the result of the trading strategy. The first route renders the "index.html" template while the second route has two functions where the first function called "ticker" performs
all the required actions to calculate and manipulate the data while the second function called "plot" does the job of visualising the calculations done in the form of graphs.

2. styles.css: This is a CSS file used for designing the website.

3. layout.html: This HTML file provides the layout and design for the home and the results page. It includes the Jinja template to utilise this layout 
for other HTML files present in the project.

4. index.html: This file is rendered on the home page, and is used to prompt a user input which is a form which accepts the ticker symbol from the
user. 

5. apology.html: This file is used whenever the user provides an invalid ticker symbol.

6. answer.html: This is the file which is used on the results page. This page shows two graphs as the result and calculates the amount that you would have earned
if you had followed the trading strategy. 
