# Dermatol
Dermatol is a multiplatform application that detects signs of skin cancer lesions using bleeding-edge AI technqiues, educates the user about skin cancer, and connects the user to the local dermatology community. All of the app's functionality can be detailed in  its app demonstration video here: https://www.youtube.com/watch?v=5XkGRIMXI8I

# App Platform
Dermatol was made using Python, Kivy, and several machine learning libraries including Tensorflow, Keras, and Sci-Kit Learn. The machine learning component of the application is stored in the file "cancertech.h5", and was trained using the code from "cancer_tech.ipynb" which is stored in jupyter notebook format. The graphical user interface of the application was created with Kivy.

# Repository Contents
There are several components to the source code seen in this folder. The first component is the collection of pictures in .png format. These images are used in the application. The second component of the application is the collection of .py files. These python files are main.py, specialbuttons.py, and database.py.
  * main.py:
    This file contains all of the main logic of the entire application: It is where all the components of the application come     together to function
  * database.py
    This file contains the python script used for the login system of the application
  * specialbuttons.py
    This file contains the special functions needed to display buttons on the graphical user interface in a circular manner.
  
The third component of the repository is the machine learning components. These files are cancer_tech.ipynb and cancertech.h5. the jupyter notebook file (cancer_tech.ipynb) details the process that was taken in order to create a neural network and ultimately store the neural network in the keras h5 file. 

# Neural Network Details
 Our app uses machine learning for creating CNN models. These models are able to classify images. Following are some details about the deep learning model.
 
 The Neural Network:
 * is trained with 3 hidden layers each with 32, 64, and 32 layers respectively.
 * uses both softmax & relu activation functions
 * uses sparse ccategorical crossentropy as its loss function
 * is trained with 500 epochs
 * reached a training accuracy of 98%
 
 
 # Installation Steps on Windows:
 * Download all the contents of this repository
 * Run ```pip3 install -r requirements.txt``` for all dependencies of the app in your command line
 * Turn your camera privacy settings on
 * Note: Your PC must have a camera for this app to run
 * Run main.py
 
 


Note: all of the source code can also be seen on GitHub at https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention or https://github.com/ShivaGanapathy/Dermatol 


