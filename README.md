## 3 Layer Neural Network Project
This is a neural network project using python and django. Neural network is a computer system modelled on the human brain and nervous system.
It is a subset of deep learning. The neural network code in this repository was written from scratch in python. It is a simple neural network with three layers: Input layer, Hidden layer and Output layer

## Stack

1. Python
2. Numpy
3. Scipy
4. Html
5. Css

### Setting Up on local Machine (Windows)
1. Download or Clone the repository

    To clone the repository, open your git terminal (you need to install git) and type
    
        git clone https://github.com/emmanuelansah247/neuralnetwork.git
        
2. Install virtual environment (you need to have python and pip installed)

    To install virtual environment, type (in your terminal)
    
       pip install virtualenv
       
3. Create a virtual environment ( or you can use the one in the repository (the name of the virtual environment folder is "venv")) 

    To create the virtual environment, type
    
       virtualenv venv

    To activate the virtual environment, navigate to the folder of the project and type
    
       venv\scripts\activate
       
4. You need to install the following

    To install Django, type
    
         pip install django
    
    To install Numpy (It will help us in array and matrix operations), type
    
        pip install numpy
      
    To install scipy (we will need sigmoid function from this library), type
      
        pip install scipy
        
    To install imageio,type
     
        pip install imageio
        
5. The application contains forms and models.

    To make migrations (this will create migration files), type
    
        py manage.py makemigrations
        
    To migrate the models to the database, type
    
        py manage.py migrate
        
6. Go to this link to download the testing and training files into this directory webapp/mnist_dataset (you need to create this folder)

http://www.pjreddie.com/media/files/mnist_test.csv

Go to this link to download the training file into this folder

http://www.pjreddie.com/media/files/mnist_train.csv

    
        
        
6. When everything is successfully, run the following command to start the server

       py manage.py runserver
     
     
     Open your browser and navigate to http://127.0.0.1:8000/
     
 
 #### Testing the application
 
Whiles on http://127.0.0.1:8000/, you will see two forms. The first form is use to train of the model and the second form is use to test the model.
 
To train the model, fill the first forms with following values
 1. Epochs - The number of times you want to train the model with the same data (the value should be an integer)
 2. Hidden nodes - The number of hidden nodes you want to train the network ( the value shoud be an integer)

When you are done, click on submit. This will take around 4 - 10 minutes to train the network (It depends on your machine too). If the training is successful, it will display the accuracy besides the "Test Accuracy". The accuracy is between 0 and 1, where values close to 0 shows poor accuracy and values close to 1 shows good accuracy.

To test the model, fill the second form (It is required that you train the model before you proceed to test it)
To fill the second form, you simply have to click "choose file" to select an image of a number. It should be a number between 0 and 9 (grayscale image is recommended).
Click on submit below the "choose file" section to submit the form. The predicted value of the image will be displayed close to the "Predicted value" section.
