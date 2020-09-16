# web-scraping-challenge

## Please note:

### Section 1 - Scraping

1. All scraping requirements were met and are available in a Jupyter Notebook, here: [mission_to_mars.ipynb](Missions_to_Mars/mission_to_mars.ipynb)

2. All scraping data also appears in scrape_mars.py, which is executed from a route on the flask app to "Refresh Data":
[scrape_mars.py](Missions_to_Mars/scrape_mars.py)

3. All scrapes save their results to variables, lists, or dictionaries, and are finally compiled into a single dictionary that returns the full data set to the flask app.

### Section 2 - Mongo DB and Flask App 

1. The flask app is run by executing "python app.py", this program contains both a root route and a route to refresh (scrape) new data.  It requires the chromedriver.exe for windows and an available MongoDb instance for writing and fetching data.

2. After scrape_mars.py completes a request to "refresh it's data, it saves the dat to a collection in MongoDb: A screen shot of the scraped data in MongoDb appears 
![Screenshot](missions_to_mars/screenshot/mongodbcompassscreencapture.png)
3. Screen Shots of the fully loaded application appear below:

![Screenshot](Missions_to_Mars/ScreenShots/ScreenCapture1.png)
![Screenshot](Missions_to_Mars/ScreenShots/ScreenCapture2.png)
![Screenshot](Missions_to_Mars/ScreenShots/ScreenCapture3.png)
