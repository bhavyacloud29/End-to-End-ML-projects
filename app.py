import pickle
from flask import Flask, request, jsonify,render_template
from src.utils import save_object,evaluate_models
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
import os,sys
from src.exception import CustomException
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


app = Flask(__name__)

# Route for a home page
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
        if request.method=='GET':
            return render_template('home.html')
        else:
            data=CustomData(
                 gender=request.form.get('gender'), 
                 race_ethnicity=request.form.get('race_ethnicity'),
                 parental_level_of_education=request.form.get('parental_level_of_education'),
                 lunch=request.form.get('lunch'),
                 test_preparation_course=request.form.get('test_preparation_course'),
                 math_score=int(request.form.get('math_score')),
                 reading_score=int(request.form.get('reading_score')),
                 writing_score=int(request.form.get('writing_score'))

            )

            pred_df=data.get_data_as_dataframe()
            print(pred_df)
            predict_pipeline=PredictPipeline()
            results=predict_pipeline.predict(pred_df)
            return render_template('home.html',results=results[0])
        

if __name__=="__main__":
     app.run(host="0.0.0.0",debug=True)








