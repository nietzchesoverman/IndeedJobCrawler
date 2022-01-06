**# INDEED JOB CRAWLER V1.0**
Crawls for all jobs around a certain location's radius, given a starting link on the career board Indeed.com - Utilizes Scrapy API as a base

# Requirements / Features
  - Programmed in Python 3.9 on VSCode on Windows 11
  - Requires Scrapy 2.5.1 API (_pip install scrapy_)
  - Only works for the website Indeed.com's HTML/CSS framework
  - Must Search for a job at a location and utilize the displayed results' page as your home page
  - Command Line commands required to run
  - Searches all pages of the initial matched result
  
# Use
1) Find an Indeed search page for a certain job with your desired criteria:

    ![IndeedPage](https://user-images.githubusercontent.com/56315562/148318596-133ffe9c-5557-456b-b1be-2244e7cc5a50.jpg)


2) Change the starting link to that of your desired criteria (you can use multiple crawl start links to search for a mass industry of jobs):

    ![ScraperInput](https://user-images.githubusercontent.com/56315562/148316881-fe3ce5eb-8d84-4c91-83cd-6927537f4ef6.jpg)

3) run the following commandline argument on your powershell:   _python -m scrapy crawl indeed -O desiredFileName.csv_  (extension can also be .json as supported by scrapy)

  Enjoy the results!
  
  Legal Clerk Search:
  ![Preview 1](https://user-images.githubusercontent.com/56315562/148318391-6224a27a-e0fe-4907-b151-c7a6b4472408.jpg)
  
  Software Dev Intern Search:
  ![Preview 2](https://user-images.githubusercontent.com/56315562/148318399-deaf8c2c-51c4-4cd8-b4c5-1799863eb56f.jpg)
