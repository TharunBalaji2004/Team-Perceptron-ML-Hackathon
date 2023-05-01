<p align="center">
  <img src="https://user-images.githubusercontent.com/95350584/235409154-5bd482f9-3b71-4a83-a064-819a18cde963.png" alt="tngov" height="150px" />
  &nbsp;&nbsp;
  <img src="https://user-images.githubusercontent.com/95350584/235409148-02efcb21-db8b-4122-ac4c-71560068311b.png" alt="naanmudhalvan" height="150px" width="250px" />
  &nbsp;&nbsp;
  <img src="https://user-images.githubusercontent.com/95350584/235409164-2badcbfb-46db-49b3-8758-40b7eef13fcd.jpg" alt="pantech" height="150px" />
</p>

<p align="center">
<b>TNSDC - Naan Mudhalvan - Python Virtual Internship Program - ML Project Hackathon (April 2023)</b>
</p>
<p align="center">
( <a href="https://drive.google.com/file/d/1mtd-CFGJ8jYDw3UKo1_lUbJsqspUk8K2/view?usp=sharing">View Project Report</a> )
</p>

## Project Description

*Real Time Air Quality Monitoring & Weather Forecasting System* is a novel project for real-time monitoring and forecasting of air quality and weather conditions. The system uses various weather parameters of a specified location and consists of a trained ML model for predicting [Air Quality Index (AQI)](https://en.wikipedia.org/wiki/Air_quality_index) remarks from air quality parameters.

This project aims to:

- Develop a system for real-time monitoring and forecasting of air quality and weatherconditions. The system uses various sensors to monitor air quality parameters such as particulate matter (PM2.5 and PM10), ozone (O3), carbon monoxide (CO), nitrogendioxide(NO2), and sulfur dioxide (SO2), as well as weather parameters suchas temperature, humidity, pressure and wind speed.

-  Development of a web-based platform that displays real-time air quality and weather data from various monitoring stations. The platform will also provide users with historical data, air quality indices, and weather forecast. The system will also have an alert system that notifies users of critical air quality conditions, such as high pollution levels and adverse weather conditions.

- The proposed system will be useful for various stakeholders, including government agencies, environmental organizations, and the general public. The system will provide valuable insight into air quality and weather conditions in real-time, enabling users to take necessary precautions to protect their health and well-being.

- On a larger extent, The air quality (AQ) Forecast lets the public know expected air quality conditions for next 72 hours so that Government authorities can take action to manage the air quality and issue health advisories which helps governments and local administrations prepares for natural disasters and save lives. 

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

The following algorithms have been used in this project to train the model:

| Algorithm Name | Avg Accuracy |
| :------: | :------: |
| Support Vector Machine (SVM) | 80% |
| Random Forest Classifier (RFC) | 90% |
| XG Boost Classifier (XGBC) | 87% |

Among these mentioned algorithms, since Random Forest Classifier (RFC) acheieved a comparative higher accuracy it has been used to train and pickle the ML model.

## Requirements

To run this project, you will need the following dependencies:

- Python 3 
- Flask
- Numpy
- Pandas
- Scikit-learn

You can install the dependencies using the following command after cloning the repo to your local system:

```cmd
pip install -r requirements.txt
```

## Usage

Clone the repo and start running the project.

## Project Screenshots

| 1) Project NoteBook Hierarchy Structure |  
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235411302-692214fa-d5b2-40d8-93ba-42aa478d3816.png" alt="1" height="400px" width="700" /> | 

| 2) Project Data Visualization |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235411369-2315c35e-5233-4017-8cc1-0e58a10fe201.png" alt="1" height="400px" width="700" /> | 

| 3) Project Data Preprocessing |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235411449-2338b292-5d92-4ab5-8af5-9ca91be4b1ec.png" alt="1" height="400px" width="700" /> |

| 4) Project Model Training using SVM, RFC and XGBC Classifier |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412096-d175cccf-e52d-47a0-af34-8cb517fcbbc5.png" alt="1" height="400px" width="700" /> |

| 5) Integrated Backend with Flask |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412159-34ac7eac-8af4-4749-9878-cb1d5a66dc8e.png" alt="1" height="400px" width="700" /> |

| 6) Developed UI part |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412125-a3cf1126-215d-4b21-824e-37b75aa46219.png" alt="1" height="400px" width="700" /> |

| 7) Deployed Website (Weather Forecasting - Today) |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412182-94ce422d-b2c6-4e05-8959-61703587ebe6.png" alt="1" height="400px" width="700" /> |

| 8) Deployed Website (Weather Forecasting - Hourly) |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412201-35b8c88a-063a-4998-a412-46f8b5bed7fc.png" alt="1" height="400px" width="700" /> |

| 9) Deployed Website (Weather Forecasting - Daily) |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412231-17a0719a-84b8-4b91-af12-8e6b8145d126.png" alt="1" height="400px" width="700" /> |)

| 10) Deployed Website (Air Quality Index Prediction) |
| :---: |
| <img src="https://user-images.githubusercontent.com/95350584/235412251-99581c5c-0662-4358-96e9-af7848d77b6d.png" alt="1" height="400px" width="700" /> |

## Results

The project has successfully acheived its primary goals and bootstrapped along with Backend and API integration for facilitating Weather Forecasting and Air Quality Monitoring System. We have deployed our ML model and hosted through website domain, the website readily available for use and dynamically renders weather data as well as makes near accurate air quality predictions. 

AirCast, 2023
<p>Link 1: https://aircast.onrender.com</p>
<p>Link 2: https://aircast.up.railway.app</p>

Special Thanks 🤝 to Team members, who had spent lot of efforts on building the ML model and Website integration with and college management for encouraging our participation in this project. 
