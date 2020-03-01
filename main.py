# Classifying Skin Cancer
# Team Stemmovators
# Ali Ahmad, Aakash Bhardwaj, Shiva Ganapathy, Nicolas Jimenez, Taha Saleh

# Importing necessary libraries for code

# Modules for integrating KV language
from __future__ import unicode_literals
from textwrap import dedent

# Modules for kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.config import Config 

# Importing the LabelButton created in specialbuttons
from specialbuttons import LabelButton

# Importing the database.py file 
from database import DataBase

# Module for creating custom time stamp filenames
import time

# Module for redirecting to custom links
import webbrowser

# Module for integrating API for the filechoose dialog
from plyer import filechooser

# Modules for tensorflow and machine learning
from keras.models import load_model

# Modules for image editing
import cv2
from PIL import Image, ImageOps
from PIL import Image, ImageChops

# Statically defining size for window
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '830')

# Loading the trained machine learning h5 file
cnn_model = load_model("cancertech.h5")

# Defining popups for each skin classification
# Each popup contains a root function for redirecting to a link
# All redirects inherit from the webbrowser Python library
class akiec(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g700efecb7b_0_155')
class bcc(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g700efecb7b_0_160')
class bkl(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g702bc51f27_0_0')
class df(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g7033c18f70_0_0')
class mel(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g7033c18f70_0_5')
class nv(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g7033c18f70_0_10')
class vasc(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://docs.google.com/presentation/d/1RC7KfqX7mZZRF9xgD2TrAajjgcELbOvNuMjTEblVfII/edit#slide=id.g7033c18f70_0_15')
class norm(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://www.skincancerprevention.org/skin-cancer/prevention-tips')
class obj(FloatLayout):
    def openLink(instance):
        webbrowser.open('https://forms.gle/1n9r9jdxRkSZ3yAQA')

# Defining popup for about the app page
class P(FloatLayout):
    pass

# Defining the create an account screen
class CreateAccountWindow(Screen):

    # Assigning objectproperties that can be called later on for name, email, and password
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # Checking credentials and if they meet the requirements before accepting them as a login
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":

                # Adding user credentials to text file database
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                self.manager.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    # Prompting user to login screen
    def login(self):
        self.reset()
        self.manager.current = "login"

    # Function to automatically reset all textinput boxes
    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

# Defining the login window screen
class LoginWindow(Screen):

    # Creating objectproperties that can be called later on for email and password
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    # Checking database if user login is valid
    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            self.manager.current = "main"
        else:
            invalidLogin()

    # Prompting user to create an account screen
    def createBtn(self):
        self.reset()
        self.manager.current = "create"

    # Function to automatically reset text fields
    def reset(self):
        self.email.text = ""
        self.password.text = ""

# Function to display invalid login popup
def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

# Function to display invalid form popup
def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


# Defining the main window
class MainWindow(Screen):

    # This function will allow the about page popup to be displayed when the button is pressed
    def ThePopup(self):
        def show_popup_P():
            show = P()

            popupWindow = Popup(title="About The App", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()
        show_popup_P()

# Defining the second window with the camera
class CameraClickScreen(Screen):

    # This function executes when the capture button is pressed
    def capture(self):

        # Defining a format for the captured image
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        # Saving captured image
        camera.export_to_png("IMG_{}.png".format(timestr))

        # Function inheriting from PIL module
        # Used to crop white space out of an image
        def trim(im):
            bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
            diff = ImageChops.difference(im, bg)
            diff = ImageChops.add(diff, diff, 2.0, -100)
            bbox = diff.getbbox()
            if bbox:
                return im.crop(bbox)

        # Trimming the captured image and replacing it with the trimmed image
        im = Image.open("IMG_{}.png".format(timestr))
        im = trim(im)
        im.save("IMG_{}.png".format(timestr))

        # Defining each popup for each disease with statically defined dynamics
        def show_popup_akiec():
            show = akiec()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_bcc():
            show = bcc()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_bkl():
            show = bkl()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_df():
            show = df()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_mel():
            show = mel()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_nv():
            show = nv()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_vasc():
            show = vasc()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_norm():
            show = norm()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        def show_popup_obj():
            show = obj()

            popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
            popupWindow.open()

        # Function inheriting from cv2 module
        # Read the image and convert to grayscale
        # Resize the image to match model's expected sizing
        def prepare(filepath):
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE) 
            new_array = cv2.resize(img_array, (28, 28)) 
            return new_array.reshape(-1, 28, 28, 1)
        
        # Making a dictionary for each skin disease classification
        # Machine learning will assign an integer value to each classification key                
        key = {"akiec":0,"bcc":1,"bkl":2,"df":3,"mel":4,"nv":5,"vasc":6,"norm":7,"obj":8}
        key = {v: k for k, v in key.items()}

        # Defining a prediction which contains numerical values based on the image we give it
        prediction = cnn_model.predict(prepare("IMG_{}.png".format(timestr)))
        print(prediction)

        # Set of conditional statements used to display the right popup based on the machine learning prediction
        if prediction[0][0] == 1:
            show_popup_akiec()
            print("The ml says " + key[0])
            time.sleep(1)
        elif prediction[0][1] == 1:
            show_popup_bcc()
            print("The ml says " + key[1])
            time.sleep(1)
        elif prediction[0][2] == 1:
            show_popup_bkl()
            print("The ml says " + key[2])
            time.sleep(1)
        elif prediction[0][3] == 1:
            show_popup_df()
            print("The ml says " + key[3])
            time.sleep(1)
        elif prediction[0][4] == 1:
            show_popup_mel()
            print("The ml says " + key[4])
            time.sleep(1)
        elif prediction[0][5] == 1:
            show_popup_nv()
            print("The ml says " + key[5])
            time.sleep(1)
        elif prediction[0][6] == 1:
            show_popup_vasc()
            print("The ml says " + key[6])
            time.sleep(1)
        elif prediction[0][7] == 1:
            show_popup_norm()
            print("The ml says " + key[7])
            time.sleep(1)
        elif prediction[0][8] == 1:
            show_popup_obj()
            print("The ml says " + key[8])
            time.sleep(1)

# Defining the third window with the filechooser
class GalleryWindow(Screen):

    # Defining a custom filechoose widget inheriting from the kivy button
    class FileChoose(Button):

        # Defining the file selection as a list property
        selection = ListProperty([])

        def choose(self):

            # Call plyer filechooser API to run a filechooser Activity.
            filechooser.open_file(on_selection=self.handle_selection)

        def handle_selection(self, selection):

            # Callback function for handling the selection response from Activity.
            self.selection = selection

        def on_selection(self, *a, **k):
         
            # Creating a filepath variable based on user selection
            file_path = str(self.selection)[2:-2] 

            # Function to take a full file path and return the file.datatype
            # Ex. C:\\Users\\User\\Downloads\\picture.png will return picture.png
            def slicing(file_location):
                new_list = file_location.split("\\") 
                your_file = new_list[-1]
                return(your_file)
            print(str(slicing(file_path)))

            # Defining each popup with their respective diseases
            def show_popup_akiec():
                show = akiec()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_bcc():
                show = bcc()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_bkl():
                show = bkl()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_df():
                show = df()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_mel():
                show = mel()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_nv():
                show = nv()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_vasc():
                show = vasc()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_norm():
                show = norm()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            def show_popup_obj():
                show = obj()

                popupWindow = Popup(title="The Results", content=show, size_hint=(None, None),size=(400,400))
                popupWindow.open()

            # Function inheriting from cv2 module
            # Read the image and convert to grayscale
            # Resize the image to match model's expected sizing
            def prepare(filepath):
                img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE) 
                new_array = cv2.resize(img_array, (28, 28))  
                return new_array.reshape(-1, 28, 28, 1)
                             
            # Making a dictionary for each skin disease classification
            # Machine learning will assign an integer value to each classification key   
            key = {"akiec":0,"bcc":1,"bkl":2,"df":3,"mel":4,"nv":5,"vasc":6,"norm":7,"obj":8}
            key = {v: k for k, v in key.items()}

            # Defining a prediction which contains numerical values based on the image we give it
            prediction = cnn_model.predict(prepare(file_path))
            print(prediction)

            # Set of conditional statements used to display the right popup based on the machine learning prediction
            if prediction[0][0] == 1:
                show_popup_akiec()
                print("The ml says " + key[0])
                time.sleep(1)
            elif prediction[0][1] == 1:
                show_popup_bcc()
                print("The ml says " + key[1])
                time.sleep(1)
            elif prediction[0][2] == 1:
                show_popup_bkl()
                print("The ml says " + key[2])
                time.sleep(1)
            elif prediction[0][3] == 1:
                show_popup_df()
                print("The ml says " + key[3])
                time.sleep(1)
            elif prediction[0][4] == 1:
                show_popup_mel()
                print("The ml says " + key[4])
                time.sleep(1)
            elif prediction[0][5] == 1:
                show_popup_nv()
                print("The ml says " + key[5])
                time.sleep(1)
            elif prediction[0][6] == 1:
                show_popup_vasc()
                print("The ml says " + key[6])
                time.sleep(1)
            elif prediction[0][7] == 1:
                show_popup_norm()
                print("The ml says " + key[7])
                time.sleep(1)
            elif prediction[0][8] == 1:
                show_popup_obj()
                print("The ml says " + key[8])
                time.sleep(1)

# Defining fourth window with safety tips
class SafetyWindow(Screen):

    # Each function opens a link to a page on skin cancer tips and safety
    def openLink1(instance):
        webbrowser.open('https://www.cdc.gov/cancer/skin/basic_info/sun-safety.htm')
    def openLink2(instance):
        webbrowser.open('http://www.americanskin.org/resource/safety.php')
    def openLink3(instance):
        webbrowser.open('https://www.skincancerprevention.org/skin-cancer/prevention-tips')
    def openLink4(instance):
        webbrowser.open('https://www.skincancer.org/skin-cancer-information/')
    def openLink5(instance):
        webbrowser.open('https://interland3.donorperfect.net/weblink/WebLink.aspx?name=skincancer&id=16')

# Defining a fifth window with community information and contacts
class CommunityWindow(Screen):

    # Each function opens a link to a page on contact information and community based sites
    def openLink1(instance):
        webbrowser.open('https://health.usnews.com/doctors/dermatologists/north-carolina')
    def openLink2(instance):
        webbrowser.open('https://www.skincancer.org/treatment-resources/support-resources/#emsection')
    def openLink3(instance):
        webbrowser.open('https://www.healthgrades.com/dermatology-directory/nc-north-carolina/cary')
    def openLink4(instance):
        webbrowser.open('https://www.google.com/search?rlz=1C1GCEA_enUS878US878&sxsrf=ALeKk02owYdpHEUeWd0yoY5uqWiGt6fu9g:1582763100734&q=dermatologist+cary+nc&npsic=0&rflfq=1&rlha=0&rllag=35774626,-78806865,2811&tbm=lcl&ved=2ahUKEwit0IeDvPDnAhUPQ6wKHUV4CbMQjGp6BAgLEEA&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!1m5!1u15!2m2!15m1!1shas_1wheelchair_1accessible_1entrance!4e2!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:[[35.91971606909483,-78.64155847756837],[35.61523855884562,-78.93612940041993')
    def openLink5(instance):
        webbrowser.open('https://www.dukehealth.org/treatments/cancer/skin-cancers')

# Defining a window manager allowing the use of transitions and navigation between windows
class WindowManager(ScreenManager):
    pass

# Communicating with the kv design language file
kv = Builder.load_file("main.kv")

# Creating a WindowManager that adds each screen being used to it
sm = WindowManager()
sm.add_widget(MainWindow(name='main'))
sm.add_widget(CameraClickScreen(name='camera'))
sm.add_widget(GalleryWindow(name='gallery'))
sm.add_widget(SafetyWindow(name='safety'))
sm.add_widget(CommunityWindow(name='community'))
sm.add_widget(CreateAccountWindow(name='create'))
sm.add_widget(LoginWindow(name='login'))

# Setting the starting screen as login
sm.current = "login"

# Defining the database text file
db = DataBase("users.txt")


# Defining the App class containing the KV design language
class DermatolApp(App):
    def build(self):

        # Returning the WindowManager with each screen
        return sm


if __name__ == '__main__':
    DermatolApp().run()

