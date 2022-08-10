from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.tree import RandomForest, RandomForestModel
import numpy as np
from pyspark.mllib.linalg import Vectors
from sklearn.metrics import f1_score
from pyspark.mllib.regression import LabeledPoint
conf = SparkConf().setAppName('random').setMaster('master')
sc = SparkContext.getOrCreate();
spark = SparkSession(sc)
loaddata = spark.read.format("csv").load("/winequalitypredict/ValidationDataset.csv",delimiter=";", inferSchema=True, header=True)
loaddata.show()
vector = VectorAssembler(inputCols=loaddata.columns[:11], outputCol="features")
data_x = vector.transform(loaddata)
data_x.show()
data_y = data_x.select("features", '""""quality"""""')
training_data = data_y.withColumnRenamed('""""quality"""""', "label")
finaldata= training_data.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[0:-1])))
Model=RandomForest.trainClassifier(finaldata,numClasses=10,categoricalFeaturesInfo={}, numTrees=50, maxBins=64, maxDepth=20, seed=33)
predictions = Model.predict(finaldata.map(lambda x: x.features))
landP = finaldata.map(lambda lp: lp.label).zip(predictions)
landP_df = landP.toDF()
lp = landP.toDF(["label", "Prediction"])
lp_df = lp.toPandas()
from sklearn.metrics import f1_score
F1score = f1_score(lp_df['label'], lp_df['Prediction'], average='micro')
print("F1- score: ", F1score)

