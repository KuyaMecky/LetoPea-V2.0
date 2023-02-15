<p align="center">
  <img src="https://user-images.githubusercontent.com/75725809/218989993-caf5923a-0649-41ce-8f60-87369f707bc5.png" alt="logo">
</p>

# LetoPea-V2
Basic-Sign-Langugae-Recognition-Using-Machine-Learning
Neural Network created using Sequential architecture and combination of LSTM and Dense layers in order to translate Basic Filipino Sign Language (FSL) into text to speech.


## Description

This project provides an opportunity for people to train their own Neural Network by recording their own dataset of FSL signs in an intuitive and simple manner.
The whole project can be split into three main parts:
1. Data collection;
2. Model training;
3. Real time predictions.

## Data Collection

> In order for a user to collect data and create their own datasets. The script is organized in a way that it would be easy to configure your own preferences and options, such as the signs the user would like to add to their dataset, the number of sequences for each sign, the number of frames for each sequence, and the path where the user would like to store the dataset. Onces these parameters were set and the script is running, the user can start recording the data. <ins>It is recommended that the user records a substantial number of sequences changing the position of their hands. This way the user can ensure data diversity which helps to obtain a generalized model.</ins>

[MediaPipe Holistic](https://google.github.io/mediapipe/solutions/holistic) pipeline was used to record the data from the user's hands. Using [MediaPipe Holistic](https://google.github.io/mediapipe/solutions/holistic) instead of [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) opens doors to future extensions and possibilities of this script. The pipeline processes each frame sent through it and results in the pose, face, left hand, and right hand components neatly stored in a variable. Each of the components can be represented by landmarks (these components' coordinates). In this case, only the hands' components' landmarks are being extracted resulting in overall 126 data entries (21 landmarks per hand with _x_, _y_, _z_ coordinates per landmark).

## Model Training

After the data has been collected and the dataset is complete, the user can proceed with the model training. In this step the dataset is split into two subsets: 90% of the dataset is used for training and 10% for testing. The accuracy of testing using this 10% of the dataset will provide insight into the efficiency of the model.

For this particular project, the Neural Network is built using a Sequential model instance by passing three LSTM and two Densely-connected layers. First four of these layers use the ReLU activation function with the last layer using the Softmax activation function. In the process of training, the Adam optimization algorithm is used to obtain optimal parameters for each layer.

Once the Neural Network is compiled, one can proceed with the model training and testing. During this step, the user can provide the model with the training subset, associated labels, and the number of epochs. Depending on the size of the provided subset and the number of epochs the training process can take up to a few minutes. Following the training, one can assess the model by performing predictions using the testing subset and evaluating the accuracy of these predictions.

## Real Time Predictions

On this step the Neural Network is ready to apply everything it has learnt to the real-world problem. [MediaPipe Holistic](https://google.github.io/mediapipe/solutions/holistic) pipeline processes every frame captured by a videocamera and extracts hands' landmarks. Every new frame the scripts appends the landmarks to the previous ones until it reaches the length 10. Once 10 frames are processed and the corresponding landmarks are grouped together, the script converts the list with all the landmarks into an array and passes this array to the trained Neural Network so it can predict the sign of the user's hands.
![lag sa cv2 issue](https://user-images.githubusercontent.com/75725809/218991337-978ea0d3-0a6b-409f-8089-5eb3c91e69d5.png)

# Modern GUI PySide6 / PyQt6
> **Warning**: this project was created using PySide6 and Python 3.9, using previous versions can cause compatibility problems.

# High DPI
> Qt Widgets is an old technology and does not have a good support for high DPI settings, making these images look distorted when your system has DPI applied above 100%.
You can minimize this problem using a workaround by applying this code below in "main.py" just below the import of the Qt modules.
![Screenshot 2023-02-15 174357](https://user-images.githubusercontent.com/75725809/218991767-52da0115-e256-4a82-9ec9-61455c9119db.png)

```python
# ADJUST QT FONT DPI FOR HIGHT SCALE
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"
```

# Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6".
> ## **Windows**:
```console
python main.py
```
> ## **MacOS and Linux**:
```console
python3 main.py
```
# Compiling
> ## **Windows**:
```console
python setup.py build
```

# Project Files And Folders
> **main.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows).

> **themes/**: add here your themes (.qss).

> **modules/**: module for running PyDracula GUI.

> **modules/app_funtions.py**: your application's functions here.
Up
> **modules/app_settings.py**: global variables to configure user interface.

> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

> **modules/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui > ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from. Resoucers_rc import *" to use as a module.

> **images/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.

# Projects Created Using PyDracula
**See the projects that were created using PyQt6.**
> To participate create a "Issue" with the name beginning with "#LETOPEA_learn-to-speak", leaving the link of your project on Github, name of the creator and what is its functionality. Your project will be added and this list will be deleted from "Issue".
**Malicious programs will not be added**!

# As of 01-31-23 v1.0
> ## as of 01-31-2023 80% of the system progression in complte
in this stae of the model structure is need to add more model to train in the pipe
## and take note if the scale of the learning models 
basic korean to filpino words as refferences take note 
## for the detect  frame add more layout and flows
balikan ung mga break point sa sjson files and widgets
## for upper part settings
lagyan na ng connection into csv logout na naka connect sa login form 
## for the login and registration form add the otp at the same functionality on the register email address and resset button
## para naman sa home panel mag lagay ng Gif nsa home 
## para sa CV2 
gawing full screen ung sa feed and add more button para sa.

# 11-02-2023 v1.0
> ## For further enhancements*
* i will recreate this as api and integrate as crossplatform supported such as mobile accesible to everyone and i will put some new features such
* voice recognitions and auto transcribe language to speech (mobile) * nag a-auto translate ng speech to speech device * https://www.facebook.com/reel/574234814563770/ .
# TODO 
> ## *Create a Login form and registration form with OTP verificatiosn
> ## *Create a MIS (seperated)
> ## *Create a lock yarn para sa authentication
> ## *integrate as web app by REST API
> ## *Create a Docker
> ## and always clean as you go (Codes)

## This will be our Final Prroject and will be serve and submited only in Cavite State university 
> # NOTE The source code will be open for further enhancement 
tapos to be continue na .. things to remember "mag lagay ng limitation and intruction pa dito sa readme, and always remember to consult kay sir antang at kamusta palagi mga ka groupo and last piliping maging kalmado at gawing motibasyon ang nararamdaman mo ngayon into positive way at iwasang mag isip ng kung anu anu, at more KAPE lezzzgoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo" 
isa pa pala transalate ko papala lahat ng nilagay ko dito into tagalog shits



> * To be continued
...
