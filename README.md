# Web Scraping Project
This is a neural network project using pythong and django. Neural network is a computer system modelled on the human brain and nervous system.
It is a subset of deep learning. The neural network code in this repository was written from scratch in python 

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
    
        
        
6. When everything is successfully, run the following command to start the server

       py manage.py runserver
     
     
     Open your browser and navigate to http://127.0.0.1:8000/
     
 
 #### Testing the application
 
 Whiles on http://127.0.0.1:8000/, you can click on the button "Generate New Files" to generate two files for you i.e the Demo File or Version File.
 Demo files stores the information relating to the main website link. 
 Version File stores the information relating the main link and sub links
 (This should take around 4 to 5 minutes)
