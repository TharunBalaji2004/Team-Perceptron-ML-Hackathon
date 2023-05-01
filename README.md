## Project Description

*Real Time Air Quality Monitoring & Weather Forecasting System* is a novel project for real-time monitoring and forecasting of air quality and weather conditions. The system uses various weather parameters of a specified location and consists of a trained ML model for predicting [Air Quality Index (AQI)](https://en.wikipedia.org/wiki/Air_quality_index) remarks from air quality parameters.

The project aims to:

- Develop a system for real-time monitoring and forecasting of air quality and weatherconditions. The system uses various sensors to monitor air quality parameters such as particulate matter (PM2.5 and PM10), ozone (O3), carbon monoxide (CO), nitrogendioxide(NO2), and sulfur dioxide (SO2), as well as weather parameters suchas temperature, humidity, pressure and wind speed.

- Development of a web-based platform that displays real-time air quality and weather data from various monitoring stations. The platform will also provide users with historical data, air quality indices, and weather forecasts. The system will also have an alert system that notifies users of critical air quality conditions, such as high pollution levels and adverse weather conditions.

- The proposed system will be useful for various stakeholders, including government agencies, environmental organizations, and the general public. The system will provide valuable insights into air quality and weather conditions in real-time, enabling users to take necessary precautions to protect their health and well-being.

- On a larger extent, The air quality (AQ) Forecast lets the public know expected air quality conditions for next 72 hours so that Government authorities can take action to manage the air quality and issue health advisories which helps governments and local administrations prepare for natural disasters and save lives. 

## Project Members

This project was developed for TNSDC Naan Mudhalvan ML Project Hackathon (April 2023) by *Team Perceptron* from Chennai Institute of Technology.

| Name | Dept | Email ID | GitHub Profile |
| :---: | :---: | :---: | :---: |
| Tharun Balaji R | CSE | tharunbalajir.cse2021@citchennai.net | [TharunBalaji2004](https://github.com/TharunBalaji2004) |
| Surya Prakash V | CSE (CyberSec) | suryaprakashv.cse2022@citchennai.net | [suryaaprakassh](https://github.com/suryaaprakassh) |
| Nadeem M | CSE (CyberSec) | nadeemm.cse2022@citchennai.net | [Nadeem-05](https://github.com/Nadeem-05) |
| Harshithaa RG | IT | harshithaarg.it2022@citchennai.net | [HarshithaaRG](https://github.com/HarshithaaRG) |

## Project Tech Stack

| Frontend | Backend | Machine Learning |
| :---: | :---: | :---: |
| <p>HTML5, CSS3</p><p><img src="https://user-images.githubusercontent.com/95350584/235406526-d43c4af9-8474-4eea-b43c-b9f21439304c.png" alt="html5" height="100px" /><img src="https://user-images.githubusercontent.com/95350584/235406565-ddfe128c-af6d-4263-80df-631c535fdc8c.png" alt="css3" height="100px" /></p> | <p>Pyhton3, Flask</p><p><img src="https://user-images.githubusercontent.com/95350584/235407004-49b279a5-abc2-4e5f-874f-103c8b60787d.png" alt="python3" height="100px" />&nbsp;&nbsp;<img src="https://user-images.githubusercontent.com/95350584/235406911-026d3fcd-2773-4142-a042-6cd9f171a3dc.png" alt="flask" height="100px" /></p> | <p>Numpy, Pandas, Scikit Learn</p><p><img src="https://seeklogo.com/images/N/numpy-logo-479C24EC79-seeklogo.com.png" alt="numpy" height="100px" />&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="pandas" height="100px" />&nbsp;&nbsp;<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikitlearn" height="100px" /></p> |

## Dataset

The project uses dataset only for predicting Air Quality Index value which consists of air pollutant values such as CO, NO, NO2, PM2.5, PM10, etc. The dataset consists of air quality recorded in past 1 year of Top 10 Tamil Nadu cities, fetched from OpenWeather API which are given by:

| City Name | Datset Size | Dataset Link |
| :------: | :------: | :------: |
| Chennai | 665 KB | [chennai.csv](dataset/Chennai.csv) |
| Coimbatore | 639 KB | [coimbatore.csv](dataset/Coimbatore.csv) |
| Dindigul | 636 KB | [dindigul.csv](dataset/Dindigul.csv) |
| Erode | 643 KB | [erode.csv](dataset/Erode.csv) |
| Madurai | 635 KB | [madurai.csv](dataset/Madurai.csv) |
| Salem | 651 KB | [salem.csv](dataset/Salem.csv) |
| Thoothukudi | 628 KB | [thoothukudi.csv](dataset/Thoothukudi.csv) |
| Tiruchirappalli | 636 KB | [tiruchirappalli.csv](dataset/Tiruchirappalli.csv) |
| Tirunelveli | 625 KB | [tirunelveli.csv](dataset/Tirunelveli.csv) |
| Vellore | 632 KB | [vellore.csv](dataset/Vellore.csv) |

Datset Link for all 10 cities merged - [tncities.csv](dataset/TNCities.csv) (Size: 7.17 MB)

The dataset has been cleaned and preprocessed using Synthetic Minority Oversampling Technique (SMOTE) for balancing the dataset.

## Models and Algorithms
## Requirements

To run this project, you will need the following dependencies:

- Python 3 
- Numpy
- Pandas
- Scikit-learn

You can install the dependencies using the following command after cloning the repo to your local system:

```cmd
pip install -r requirements.txt
```

## Usage
## Results

