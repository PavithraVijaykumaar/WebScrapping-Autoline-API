# WebScrapping-Autoline-API

This project is based on webscrapping a webpage named `Autoline` which finds and lists the details of reused cars in the mentioned city. For accessing the details in the webpage, `cURL` is used for sending HTTP request to the webpage using the `requests` library in python. After successfully establishing a connection, the necessary datas are received from the webpage. Two cities namely `California` and `Monowa` are selected for fetching of car details. The scrapped datas are converted into `pandas` Dataframe and is stored as an `Excel` sheet. For deploying the scrapped data, `FastAPI` is used for connecting to a localHost and display the details. After successfully retrieving the data from the localhost, the details is deployed in `Render` cloud platform and API is generated for retrieving the data deployed in the cloud.

## About the libraries used

- Pandas is for converting the required scrapped data list into DataFrame
- Requests is for sending HTTP requests and working with APIs

      import pandas as pd
      import requests
      
## About cURL

cURL (Client URL) is a versatile `command-line` tool and library used for transferring data with URLs. It allows to send HTTP requests to web servers and retrieve the content of web pages.It is a powerful tool for fetching the HTML content of web pages, which is essential for web scraping. The cURL is successfully converted as a python request as webscrapping is done in python kernel. Using the `requests` library, the request is sent to the website.

## About Scrapping the web data

The webscrapping operation for the website is done in jupyter environnmet by passing the cURL converted into python code for HTTP request using requests library. The necessary datas namely,
- Model
- Mileage
- City
- Year
- Price
are alone scrapped from the Autoline website for two different countries- `California` and `Monowa`

The scrapped data is converted into a dataframe for both the cities


For California city

    ford_pages_df=pd.DataFrame({'Model': model,'Mileage': mileage,'City': city,'Year': year,'Dealer': dealer,'Price': price})

For Monowa city

    ford_pages2_df=pd.DataFrame({'Model': model,'Mileage': mileage,'City': city,'Year': year,'Dealer': dealer,'Price': price})


After forming the dataframe, both the dataframes are converted into single dataframe by using `concat` function.

    merged=pd.concat([ford_pages_df,ford_pages2_df],ignore_index=True)

`merged` is the combined dataset of both the cities. The merged dataset is stored as an excel named as `Ford`

For viewing the dataset, click [Dataset](ford.csv)


## About FastAPI

FastAPI is a modern, fast, and web framework for building APIs with Python. While it is primarily designed for creating APIs, it can be used to serve web applications as well, making it a suitable choice for displaying scraped data from a website on a localhost server. FastAPI application acn be created by defining endpoints that will handle incoming HTTP requests. 

    from fastapi import FastAPI
    app=FastAPI()
This command starts the working of FastAPI

The fastAPI code for connecting to the local host, [FastAPI](mainn.py)

    response= requests.get('http://127.0.0.1:8000/data')
The above local host shows the scrapped data and it can be retrieved using `requests` library

The data retrieved from Local host, [LocalHost](data-from-localhost-API.ipynb)

## About Uvicorn 

Uvicorn is a server that is commonly used to run web applications and APIs built using Python frameworks like FastAPI. Uvicorn can be used for displaying the scrapped data from a website to create a web server that serves the scraped data to the users through a web interface. 

     uvicorn mainn:app --reload
This command is used for running the FastAPI application and connect to a local host using the uvicorn server.

## About Render

Render cloud platform is used for deploying app in here, the datas scrapped from the website is deployed and API is generated for accessing and retrieving the data from the cloud. The render API also enables us to send requests for data retrieval and converting them into DataFrames and perform operations.

     https://ford-autolist-api.onrender.com/data
The above link is the API, generated for accessing the deployed data.

     response=requests.get('https://ford-autolist-api.onrender.com/data')
Using response library, the API is passed for retrieving the information

The data retrieved from Local host, [Render API](data-from-Render-API.ipynb)
