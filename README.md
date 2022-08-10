# CS-438-Progamming-Assignment-2

**Description**

In this assignment our task is to develop a parallel machine learning model in Amazon AWS cloud environment. In this project we have trained our “winequality” prediction model based on given training data and then utilized this model to test our model for given validation dataset. We have utilized Logistic regression model for training and testing our wine quality prediction application and then calculated the accuracy of model to determine how well our model performed. Our task was to deploy our model with and without docker. Following are steps in development of Wine Quality prediction system.


**Docker Link**: https://hub.docker.com/r/system25/winequalityprediction


**How to set-up the cloud environment and run the model training and the application prediction without docker**

**Following are the steps to setup cloud environment:**

1.	Navigate to Amazon AWS website i.e “https://aws.amazon.com/
2.	Create and Amazon AWS account and login to the console by providing login credentials.
3.	From the search for EC2 service and navigate to the EC2 dashboard.
4.	Click on Launch Instance and follow all the steps by providing all the mandatory details.
5.	Choose number of instances. In our case we have selected 5 instances because we are required to run our application on multiple instances.
6.	Click on the launch button to launch your EC2 instance.
7.	From the command line ssh into the ec2 machine from our local system
8.	Copy application files and folder from local system into the EC2 instance.
9.	Run the following command to build the model 

        1.	Spark-submit test.py


**How to set-up the cloud environment and run the model training and the application prediction without docker**
**Following are the steps to run application in docker in Amazon AWS:**

•	Login to Amazon AWS account.

•	SSH into EC2 instance from local machine.

•	Install docker into the EC2 instance by using following commands:

    o	sudo yum install docker
    
    o	sudo service docker start
    
    o	sudo usermod -a -G docker ec2-user
    
•	Navigate to directory with application files.

•	Run following command to build image and run container:

    o	docker build -t winequalityprediction.
    
    o	docker run -p 80:80 winequalityprediction.






