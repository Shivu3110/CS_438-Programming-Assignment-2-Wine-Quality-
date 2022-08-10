# CS-438-Progamming-Assignment-2

**Description**

In this assignment, the task is to develop a parallel machine learning model in the Amazon AWS cloud environment. In this project, I have trained the “winequality” prediction model based on given training data and then utilized this model to test my model for the given validation dataset. I have utilized the Random Forest regression model for training and testing wine quality prediction applications and then calculated the accuracy of the model to determine how well the model performed. The task was to deploy our model with and without docker. The following are steps in the development of the Wine Quality prediction system.

**Docker Link:** https://hub.docker.com/r/system25/winequalityprediction


**How to set up the cloud environment and run the model training and the application prediction without docker**

**Following are the steps to a setup cloud environment:**

1.	Navigate to the Amazon AWS website i.e. “https://aws.amazon.com/
2.	Create an Amazon AWS account and log in to the console by providing login credentials.
3.	From the search for EC2 service and navigate to the EC2 dashboard.
4.	Click on Launch Instance and follow all the steps by providing all the mandatory details.
5.	Choose a number of instances. In this case, I have selected 5 instances because we are required to run our application on multiple instances.
6.	Click on the launch button to launch your EC2 instance.
7.	From the command line ssh into the ec2 machine from our local system
8.	Copy application files and folders from the local system into the EC2 instance.
9.	Run the following command to build the model 
        
        1.	Spark-submit test.py

**How to set up the cloud environment and run the model training and the application prediction with docker**

**Following are the steps to run the application in docker in Amazon AWS:**


•	Login to your Amazon AWS account.

•	SSH into EC2 instance from the local machine.

•	Install docker into the EC2 instance by using the following commands:

        o	sudo yum install docker
        
        o	sudo service docker start
        
        o	sudo usermod -a -G docker ec2-user
        
•	Navigate to the directory with application files.

•	Run the following command to build the image and run the container:

        o	docker build -t winequalityprediction
        
        o	docker run -p 80:80 winequalityprediction
        
**F1 Score: 0.55625**





