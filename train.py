from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
import numpy as np
from pyspark.mllib.tree import RandomForest
import pickle
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from sklearn.metrics import f1_score
conf = SparkConf().setAppName('random').setMaster('master')
sc = SparkContext.getOrCreate();
spark = SparkSession(sc)
loaddata = spark.read.format("csv").load("TrainingDataset.csv",delimiter=";", inferSchema=True, header=True)
loaddata.show()
vector = VectorAssembler(inputCols=loaddata.columns[:11], outputCol="features")
data_x = vector.transform(loaddata)
data_x.show()
data_y = data_x.select("features", '""""quality"""""')
training_data = data_y.withColumnRenamed('""""quality"""""', "label")
finaldata= training_data.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))
Model = RandomForest.trainClassifier(finaldata,numClasses=10,categoricalFeaturesInfo={}, numTrees=50, maxBins=64, maxDepth=20, seed=33)
predictions = Model.predict(finaldata.map(lambda x: x.features))
landP = finaldata.map(lambda lp: lp.label).zip(predictions)
landP_df = landP.toDF()
lp = landP.toDF(["label", "Prediction"])
lp_df = lp.toPandas()
F1score = f1_score(lp_df['label'], lp_df['Prediction'], average='micro')
print("F1- score: ", F1score)
Model.save(sc,'/content/RandomForestModel.model')