# Final Project: NLP with Review Data

This repository contains the final project for Machine Learning II, focusing on Natural Language Processing (NLP) using data from TripAdvisor and Amazon Food.

## Project Description
The goal of this project is to perform NLP analysis on the reviews and develop models that are capable of understanding and interpreting human sentiment. By using advanced machine learning techniques, we aim to predict a rating from 1 to 5 based on the content of the reviews. The models built for this purpose include a Logistic Regression model, a BERT (Bidirectional Encoder Representations from Transformers) model, and a Convolutional Neural Network (CNN) model.

The reviews that were used to train the models come from two sources: TripAdvisor and Amazon Food. TripAdvisor is a popular online platform that provides user-generated reviews and opinions about travel destinations, accommodations, restaurants, and more. Similarly, Amazon Food provides customer reviews on food items. The combination of these diverse sources allows our models to learn from a wide range of review types, potentially enhancing their generalization ability and robustness.

This project is tailored for Google Colab. If you plan to run it locally, please note that some file paths might need to be adjusted to fit your environment.

## Data
The project utilizes data collected from TripAdvisor and Amazon Food. The dataset consists of reviews from various travel-related entities on TripAdvisor and food items on Amazon. Each review includes textual content and a rating. The data will serve as the foundation for our NLP analysis and model training.

## Project Structure
The project is organized as follows:

- `data/`: This directory contains the TripAdvisor and Amazon Food datasets used for the analysis. It also contains the merged, lr_data_transformed (for the logistic regression) as well as the dataset for testing on unseen data.

- `models/`: This directory contains the pretrained models from the logistic regression, BERT, and CNN approaches. The models can be loaded and used for prediction or further analysis.

## Usage

To reproduce the project results or further explore the NLP analysis, follow these steps:

IT IS HIGHLY RECOMMENDED TO USE A GPU, AS OTHERWISE THE TRAINING TAKES HOURS AND CAN TAKE UP TO A DAY!

### Using Google Colab

1. Mount your Google Drive by running the following code in python:
from google.colab import drive
drive.mount('/content/drive')

2. Create the necessary file structure in your Google Drive. Place the "New_Delhis_reviews.csv", "tripadvisor_hotel_reviews.csv", and "Reviews.csv" files in a folder named "data" within the "ML_Project" folder. Your file structure should be as follows:

   /content/drive/MyDrive/ML_Project/data/New_Delhis_reviews.csv
   
   /content/drive/MyDrive/ML_Project/data/tripadvisor_hotel_reviews.csv
   
   /content/drive/MyDrive/ML_Project/data/Reviews.csv


3. Upload the Jupyter notebook files (.ipynb) to your Google Drive.

4. Run the Jupyter notebooks in sequential order. These notebooks cover data preprocessing, exploratory data analysis, model training, evaluation, and decision-making. Make sure to adjust the file paths in the notebooks if necessary.

5. To load the pretrained models, create a folder named "models" within the "ML_Project" folder in your Google Drive. Place the pretrained models in the "models" folder. Your file structure should be as follows:

   /content/drive/MyDrive/ML_Project/models/
   

### Running it locally
If running the project locally, adjust all file paths in the notebooks to match your local file directory. The other steps are identical to the Google Colab version.



## Dependencies
The project utilizes the following Python libraries and frameworks:

- pandas
- numpy
- scikit-learn
- NLTK
- spaCy
- matplotlib
- seaborn
- os
- pytorch
- tensorflow
- transformers
- and more

Make sure to install the required dependencies by running `pip install -r requirements.txt` before running the notebooks.

## Conclusion
Through this project, we aim to leverage NLP techniques to gain insights from review data and build models that can accurately predict ratings based on the reviews. By analyzing user reviews, we can extract valuable information that can help us understand user sentiment and improve services.
