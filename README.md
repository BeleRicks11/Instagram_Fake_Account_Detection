# Instagram Fake Account Detection
<!-- PROJECT LOGO -->
  
  [![telegram-bot](https://img.shields.io/static/v1?label=Telegram.Bot&message=InstaFakeDetector_Bot&color=blue)](https://github.com/danielepelleg/InstaFakeDetector_Bot)
  ![python](https://img.shields.io/static/v1?label=python&message=3.7&color=yellow)
  
  <br />
    <p align="center">
  <a href="https://github.com/BeleRicks11/Instagram_Fake_Account_Detection">
    <img src="resources/logo.png" alt="Logo" width="130" height="130">
  </a>
  <h1 align="center">Instagram Fake Account Detetction</h1>
  <p align="center">
    Jupyter Notebook implementation to detect Instagram's fake accounts.
  </p>
  <p align="center">
    Machine Learning Project - Classification Algorithms
  </p>
  
  <!-- TABLE OF CONTENTS -->
  ## 📚 Table of Contents
  
  - [Table of Contents](#-table-of-contents)
  - [About The Project](#-about-the-project)
  - [Getting Started](#-getting-started)
    - [Installation](#installation) 
    - [Updates](#updates)
  - [Datasets](#-datasets)
    - [Dataset for Private Accounts](#dataset-for-private-accounts) 
    - [Dataset for Public Accounts](#dataset-for-public-accounts) 
    - [Features Description](#features-description) 
  - [Classification Report](#-classification-report)
    - [Report for Private Accounts](#report-for-private-accounts) 
    - [Report for Public Accounts](#report-for-public-accounts)
  - [License](#-license)
  - [Contributors](#-contributors)
   
   <!-- ABOUT THE PROJECT -->
   ## 👨‍💻 About The Project
   **Insta Fake Account Detection** is Machine Learning Project developed for the *Big Data and Business Intelligence* course of [@Università di Parma].
   The objective of this project is the automated recognition of fake Instagram accounts, using some *Classification Algorithms*. 
   
   The projects has 2 dataset: the first with 11 feature is used for the recognition of private accounts, which due to their privacy have a limited amount of informations to share, the second with 14 features is used with the public accounts, which thanks to their privacy have more informations to work with, such as the date of the post published, which gave the algorithms some informations about the index of activity of the account. Every account's feature has been scraped using an Instagram Web Scraper.

   Then the two dataset have been subject to a *Preprocessing Phase*. This phase consists of the *standardization* and the *normalization* of the two datasets. In this have been done the [_Feature Importance Forest of Trees_] and the [_Feature Selection_] analysis. In the Feature Selection has been used four algorithms:
   + L1 Based
   + Tree Based
   + Removing Features with Low Variance
   + Univariate Select Best (K = 4)

   The features, now preprocessed, are taken and given to this [_Machine Learning Classifier Algorithms_]: 
   + AdaBoost
   + Decision tree
   + K-Nearest Neighbours (KNN)
   + Logistic Regression
   + Multi-Layer Perceptron
   + Random Forest
   + Stochastic Gradient Descent (SGD)
   + Stochastic Gradient Descent (SGD)
   + Support Vector Machine (SVM)

   For every algorithm, in addition to the trainining and the testing phase, has been calculated:
   + Cross Validation
   + Confusion Matrix
   + Receiver Operating Characteristic / ROC Curve
   + Classification Report

   Eventually, we created a telegram bot with the best algorithm of the two datasets. We embodied it in the bot and run the script. Once started you only have to send it a username and it will verify the authenticity of the account and send you the reply with the response you search.

   Check 👉 [_Insta Fake Detector Bot_] 👈 to see the relative telegram-bot project. Try the efficiency of the AdaBoost algorithm on detecting the fake accounts and ask the bot the account to detect.
   
   <!-- GETTING STARTED -->
   ## 🔨 Getting Started

   ### Installation
   You can just clone this repository and install the requirements by running:
   ```
   $ pip install igramscraper
   ```
   ```
   $ pip install sklearn
   ```
   Then start the notebook files in the relative folders to see the results. 
   
   ### Updates
   Pull this repository for updates.

   <!-- DATASETS -->
   ## 🗂 DATASETS
   Is possible to find the datasets in the [_resources_] folder.
   
   ### Dataset for Private Accounts
   Profile Pic   |  Nums / Length Username  |  Full Name Words  |  Bio Length  |  External URL  |  Is Private  |  Is Verified  |  Is Business  |  # Post  |  # Followers  |  # Following
   :------------:|:------------------------:|:-----------------:|:------------:|:--------------:|:------------:|:-------------:|:-----------:|:--------:|:-------------:|:------------:|

   ### Dataset for Public Accounts
   Profile Pic   |  Nums / Length Username   |  Fake Account  | Full Name Words  | Bio Length  | External URL  | Is Verified  | Is Business  | # Post  | # Followers  | # Following  | Last Post Recent  | % Post Single Day  | Index of Activity  | Average of Likes
   :------------:|:-------------------------:|:--------------:|:----------------:|:-----------:|:-------------:|:------------:|:--------:|:-------:|:------------:|:------------:|:-----------------:|:------------------:|:------------------:|:----------------:|

   ### Features Description
   - **Profile Pic** *boolean value*. 0 if the user doesnt'have the profile pic, 1 otherwise.
   - **Nums / Length Username** *double value*. How many special characters of numeric characters the username has on its full length. 
   - **Full Name Words** *numeric value*. How many words in the full name.
   - **Bio Length** *numeric value*. How many characters in the biography of the account. 
   - **External URL** *boolean value*. 0 if the user doesnt'have the an external URL in the biography, 1 otherwise.
   - **Is Private** *boolean value*. 0 if the user doesnt'have a private account, 1 otherwise.  
   - **Is Verified** *boolean value*. 0 if the user doesnt'have the verified badge , 1 otherwise. 
   - **Is Business** *boolean value*. 0 if the user doesnt'have a business account, 1 otherwise. 
   - **# Post** *numeric value*. The number of the post published by the account.
   - **# Followers** *numeric value*. The number of the followers of the account.  
   - **# Following** *numeric value*. The number of the following of the account.
   - **Last Post Recent** *boolean value*. 0 if the user doesnt'have a post publisched withing 6 months, 1 otherwise.
   - **% Post Single Day** *double value*. How many post has been published in the same same day on the total number of the posts. 
   - **Index of Activity** *double value*. How many post in average the account publishes every month.
   - **Average of Likes** *double value*. Average of the likes of a post of the account.  
   
   <!-- CLASSIFICATION REPORT -->
   ## 📊 CLASSIFICATION REPORT

   ### Report for Private Accounts
   <p align="center">

   |        *Algorithm*          |  *Accuracy*  |  *Precision*  |  *Recall*  |  *F-Score*  |
   |:---------------------------:|:------------:|:-------------:|:----------:|:-----------:|
   |  **AdaBoost**               |      96%     |      96%      |     96%    |     96%     |
   |  **Decision Tree**          |      96%     |      96%      |     96%    |     96%     |
   |  KNN Classifier             |      95%     |      96%      |     95%    |     95%     |
   |  Logistic Regression        |      94%     |      94%      |     94%    |     94%     |
   |  **Multi-Layer Perceptron** |      96%     |      96%      |     96%    |     96%     |
   |  Random Forest              |      94%     |      94%      |     94%    |     94%     |
   |  SGD Classifier             |      95%     |      95%      |     95%    |     95%     |
   |  SVM Classifier             |      94%     |      94%      |     94%    |     94%     | 

   </p>

   ### Report for Public Accounts
   <p align="center">

   |        *Algorithm*          |  *Accuracy*  |  *Precision*  |  *Recall*  |  *F-Score*  |
   |:---------------------------:|:------------:|:-------------:|:----------:|:-----------:|
   |  AdaBoost                   |      97%     |      97%      |     97%    |     97%     |
   |  Decision Tree              |      97%     |      97%      |     97%    |     97%     |
   |  KNN Classifier             |      95%     |      95%      |     95%    |     95%     |
   |  Logistic Regression        |      95%     |      95%      |     95%    |     95%     |
   |  Multi-Layer Perceptron     |      97%     |      97%      |     97%    |     97%     |
   |  **Random Forest**          |      98%     |      99%      |     98%    |     98%     |
   |  SGD Classifier             |      95%     |      95%      |     95%    |     95%     |
   |  SVM Classifier             |      95%     |      95%      |     95%    |     95%     |
   
   </p>
   
   <!-- LICENSE -->
   ## 🔑 LICENSE
   Distributed under the GPL License. See `LICENSE` for more information.

   Instagram Web Scraper made by [Realsirjoe] from <a href="https://github.com/realsirjoe/instagram-scraper" title="InstagramScraper"> https://github.com/realsirjoe/instagram-scraper </a>
   
   Icons made by <a href="https://www.flaticon.com/authors/roundicons" title="Roundicons">Roundicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
   
   <!-- CONTRIBUTORS -->
   ## 👨‍🎓👨‍🎓 CONTRIBUTORS
   [Riccardo Fava](https://github.com/BeleRicks11) - 287516

   [Daniele Pellegrini](https://github.com/danielepelleg) - 285240
   
   <!------ ------->
   [_Insta Fake Detector Bot_]: https://github.com/danielepelleg/InstaFakeDetector_Bot
   [@Università di Parma]: https://www.unipr.it
   [realsirjoe]: https://github.com/realsirjoe
   [_Feature Importance Forest of Trees_]: https://github.com/BeleRicks11/Instagram_Fake_Account_Detection/tree/master/Preprocessing/Feature%20Importance
   [_Feature Selection_]: https://github.com/BeleRicks11/Instagram_Fake_Account_Detection/tree/master/Preprocessing/Features%20Selection
   [_Machine Learning Classifier Algorithms_]: https://github.com/BeleRicks11/Instagram_Fake_Account_Detection/tree/master/ML%20Classifier
   [_resources_]: https://github.com/BeleRicks11/Instagram_Fake_Account_Detection/tree/master/resources