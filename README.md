# Dermatol

Dermatol is a multiplatform application that: detects signs of skin cancer lesions using bleeding-edge AI technqiues, educates the user about skin cancer, and connects the user to the local dermatology community. All of the app's functionality can be detailed in its app demonstration video [here](https://www.youtube.com/watch?v=x25HVwbnF2c) or down below.

https://www.youtube.com/watch?v=x25HVwbnF2c

## App Platform

Dermatol was made using Python, Kivy, and several machine learning libraries including Tensorflow, Keras, and Sci-Kit Learn. The machine learning component of the application is stored in the file [cancertech.h5](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/cancertech.h5), and was trained using the code from [cancer_tech.ipynb](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/cancer_tech.ipynb) which is stored in jupyter notebook format. The graphical user interface of the application was created with Kivy.

![](screenshot.png)

## Repository Contents

There are several components to the source code seen in this folder. The first component is the collection of [pictures](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/tree/master/images) in .png format. These images are used in the application. The second component of the application is the collection of .py files. These python files are [main.py](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/main.py), [specialbuttons.py](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/specialbuttons.py), and [database.py](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/database.py).
  * [main.py](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/main.py):
    This file contains all of the main logic of the entire application: It is where all the components of the application come     together to function
  * [database.py](https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention/blob/master/database.py)
    This file contains the python script used for the login system of the application
  * specialbuttons.py
    This file contains the special functions needed to display buttons on the graphical user interface in a circular manner.
  
The third component of the repository is the machine learning components. These files are cancer_tech.ipynb and cancertech.h5. The jupyter notebook file (cancer_tech.ipynb) details the process that was taken in order to create a neural network and ultimately store the neural network in the keras h5 file. 

## Neural Network Details
 Our app uses machine learning for creating CNN models. These models are able to classify images. The following are some details about the deep learning model.
 
 The Neural Network:
 * is trained with 3 hidden layers each with 32, 64, and 32 layers respectively.
 * uses both softmax & relu activation functions
 * uses sparse ccategorical crossentropy as its loss function
 * is trained with 500 epochs
 * reached a training accuracy of 98%

## Data Source
In order to train the neural network, data from kaggle was used. The data can be seen [here](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000).

## Clone

```bash
git clone https://github.com/aahmad4/Dermatol-Skin-Cancer-Prevention
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

(Note: Your camera privacy settings must be on)

```python
python main.py
```

## Disclaimer

This product is not intended to diagnose, treat, or replace proper medical treatment. Use for reference only and consult doctor before making any decisions based on this app.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

