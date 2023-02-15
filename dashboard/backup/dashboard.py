import customtkinter
import os
from PIL import Image
import os
import shutil
import tkinter as tk
import tkinter
import speech_recognition as sr
###########################################################################################################################################

############################################################################################################################################
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # configure window
        self.title("Leto Pea")
        self.geometry(f'{962}x{600}+{200}+{40}')
        #self.overrideredirect(True)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test/manual_integration_tests/test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(230, 125))
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 2, 2), weight=1)
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=20)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        #logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=" ", image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=5,pady=(10))
        #side bar

        # HOME buttton
        self.sidebar_button_home = customtkinter.CTkButton(self.sidebar_frame,text="Home", command=self.sidebar_button_event_home)
        self.sidebar_button_home.grid(row=1, column=0, padx=20, pady=10)
 
        # detect button
        self.sidebar_button_detect = customtkinter.CTkButton(self.sidebar_frame,text="Detect", command=self.sidebar_button_event_detect)
        self.sidebar_button_detect.grid(row=2, column=0, padx=20, pady=10)
        # train Button
        self.sidebar_button_train = customtkinter.CTkButton(self.sidebar_frame, text="Train", command=self.sidebar_button_event_train)
        self.sidebar_button_train.grid(row=3, column=0, padx=20, pady=10)
        # manage words
        self.sidebar_button_wordmanager = customtkinter.CTkButton(self.sidebar_frame, text="manage", command=self.sidebar_button_event_wordmanager)
        self.sidebar_button_wordmanager.grid(row=4, column=0, padx=20, pady=10)       
        # pang appeareance
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=(10,10), pady=(0, 70))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=(10,10), pady=(0, 0))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=(10,10), pady=(0, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=(10,10), pady=(10, 20))
        #####################################################################################################################################
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.entry.grid_remove()

        self.main_button_1 = customtkinter.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_1.grid_remove()
###############################################################################################################################################
        ##################################################### config sa detect button #######################################################
        self.detectsign = customtkinter.CTkButton(self ,text="Detect Sign - Language", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.detectsign.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.detectsign.grid_remove()
        
        

        ##########################################################pang start#########################################################################
        self.detectlangstart = customtkinter.CTkButton(self,text="start Detect Speech",command=self.start, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.detectlangstart.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.detectlangstart.grid_remove()
        
        
        ###########################################################pang stop########################################################################
        self.detectlangstop = customtkinter.CTkButton(self ,text="Stop recognize Speech",command=self.stop, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.detectlangstop.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.detectlangstop.grid_remove()
        
        
        ###################################################################################################################################
        # create main entry and button
    
        self.text_var = tk.StringVar(self)
        self.entryspeech = customtkinter.CTkEntry(self,  textvariable=self.text_var, placeholder_text='output here',height=100,  width=200)
        self.entryspeech.grid( row=4, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.entryspeech.grid_remove()
        

        ###################################################################################################################################
        self.home_frame = customtkinter.CTkFrame(self.navigation_frame)
        self.second_frame = customtkinter.CTkFrame(self.navigation_frame)
        self.third_frame = customtkinter.CTkFrame(self.navigation_frame)
        self.forth_frame = customtkinter.CTkFrame(self.navigation_frame)
        ####################################################################################################################################
    # pang UI settings
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        ############################### for tts#####################################
        
    def start(self):
        global r, audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

    def stop(self):
        try:
            self.text = r.recognize_google(audio)
            self.text_var.set(self.text)
        except sr.UnknownValueError:
            self.text_var.set("Could not understand audio")
        except sr.RequestError as e:
            self.text_var.set("Could not request results from Google Speech Recognition service; {0}".format(e))
        ####################################################################################################################################
        


        
        ####################################################################################################################################
      
    # pang Appearance
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    # pang scalling
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        # create home frame
        #self.home_frame = customtkinter.CTkFrame(self.navigation_frame, corner_radius=0, fg_color="transparent")
        #self.home_frame.grid(row=0, column=1, sticky="nsew")
        # create second frame detect
        #self.second_frame = customtkinter.CTkFrame(self.navigation_frame, corner_radius=0, fg_color="transparent")
        #self.second_frame.grid(row=0, column=1, sticky="nsew")
        # create third frame
        #self.third_frame = customtkinter.CTkFrame(self.navigation_frame, corner_radius=0, fg_color="transparent")
        #self.third_frame.grid(row=0, column=1, sticky="nsew")
        # create forth frame
        #self.forth_frame = customtkinter.CTkFrame(self.navigation_frame, corner_radius=0, fg_color="transparent")
        #self.forth_frame.grid(row=0, column=1, sticky="nsew")
        
        # set button color for selected button
    def select_frame_by_name(self, name):
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_remove()
        if name == "detect":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_remove()
        if name == "train":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_remove()
        if name == "manage":
            self.forth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.forth_frame.grid_remove()
            
############################################################################################################################################
    def sidebar_button_event_home(self):
        self.select_frame_by_name("home")
    
        # remove widgets from forth_frame

        self.entry.grid()


    ########### pang remove ############
        # remove widgets from forth_frame
        for widget in self.home_frame.winfo_children():
            widget.destroy()
        self.main_button_1.grid_remove()
        self.forth_frame.grid_remove()

        self.delete_button.grid_remove()
        self.folder_checkbox.grid_remove()
        self.detectsign.grid_remove()
        self.textbox.grid_remove()
        self.detectlangstart.grid_remove()
        self.detectlangstop.grid_remove()
        self.entryspeech.grid_remove()
###############################second#######################################################################################################
    def sidebar_button_event_detect(self):
        # remove widgets from forth_frame
     
     
        self.select_frame_by_name("detect")
        self.detectlangstart.grid()
        self.detectlangstop.grid()
        self.entryspeech.grid()
        self.detectsign.grid()
  


        #create delete button
        ########### pang remove ############
         # remove widgets from forth_frame

        self.delete_button.grid_remove()
        self.folder_checkbox.grid_remove()
        self.entry.grid_remove()
        self.main_button_1.grid_remove()
        self.forth_frame.grid_remove()
        for widget in self.second_frame.winfo_children():
            widget.destroy()
############################################################################################################################################
    def sidebar_button_event_train(self):
        self.select_frame_by_name("train")
        # remove widgets from forth_frame
        self.main_button_1.grid()
        ########### pang remove ############
        # remove widgets from forth_frame
        for widget in self.third_frame.winfo_children():
            widget.destroy()

        self.entry.grid_remove()
        self.home_frame.grid_remove()
        self.forth_frame.grid_remove()
        self.folder_checkbox.grid_remove()
        self.detectsign.grid_remove()
        self.entryspeech.grid_remove()
        self.textbox.grid_remove()
        self.detectlangstart.grid_destroy()
        self.detectlangstop.grid_remove()
###########################################################################################################################################
############################ For file management or sa Pag bura ng words na na train na ###################################################
    def sidebar_button_event_wordmanager(self):
        self.select_frame_by_name("manage")
        for widget in self.forth_frame.winfo_children():
            widget.destroy()

        


        #create a new frame
        self.forth_frame = customtkinter.CTkFrame(self)
        self.forth_frame.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        data_path = "data" # path to the data folder
        self.folders = os.listdir(data_path) # list all the folders in the data folder
        # create a list of checkboxes for each folder
        self.folder_vars = []
        for i, folder in enumerate(self.folders):
            folder_var = tk.IntVar()
            self.folder_checkbox = customtkinter.CTkCheckBox(self.forth_frame, text=folder, variable=folder_var)
            self.folder_checkbox.grid(row=i, column=0, padx=10, pady=10)
            self.folder_vars.append(folder_var)
        #create delete button
        self.delete_button = customtkinter.CTkButton(self.forth_frame, text="Delete", command=self.delete_folders)
        self.delete_button.grid(row=len(self.folders), column=0, pady=(10,20))
                 # remove widgets from forth_frame

                ########### pang remove ############
        self.entry.grid_remove()
        self.main_button_1.grid_remove()
        self.detectsign.grid_remove()
        self.textbox.grid_remove()
        self.entryspeech.grid_remove()
        self.detectlangstart.grid_remove()
        self.detectlangstop.grid_remove()
#############################################delete function################################################################################
    def delete_folders(self):
        confirm = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to delete the selected folders?")
        if confirm:
            data_path = "data" # path to the data folder
            self.folders = os.listdir(data_path) # list all the folders in the data folder
            for i, folder in enumerate(self.folders):
                if self.folder_vars[i].get() == 1:
                    shutil.rmtree(os.path.join(data_path,folder))
            tkinter.messagebox.showinfo("Deleted", "Selected Folders have been deleted")
        self.sidebar_button_event_wordmanager() # refresh the list of folders
############################################################################################################################################
if __name__ == "__main__":
    app = App()
    app.mainloop()
 
    
