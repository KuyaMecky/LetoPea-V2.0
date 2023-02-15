import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image
import tkinter as tk
import os
import shutil




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Leto Pea")
        self.geometry(f"{1100}x{580}")
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test/manual_integration_tests/test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(200, 95))



        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
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


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=(10,10), pady=(0, 70))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=(10,10), pady=(0, 0))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=(10,10), pady=(0, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%" ,"130%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=(10,10), pady=(10, 20))



        # pang UI settings
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")


        # create second frame detect
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create slider and progressbar frame
        self.progressbar_1 = customtkinter.CTkProgressBar(self.second_frame , width=1000)
        self.progressbar_1.grid(row=2, column=1, padx=(10,10), pady=(10, 10), sticky="nsew")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()


        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create forth frame
        self.forth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

  




        # select default frame
        #self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        
        # set button color for selected button
        self.sidebar_button_home.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.sidebar_button_detect.configure(fg_color=("gray75", "gray25") if name == "detect" else "transparent")
        self.sidebar_button_train.configure(fg_color=("gray75", "gray25") if name == "train" else "transparent")
        self.sidebar_button_wordmanager.configure(fg_color=("gray75", "gray25") if name == "manage" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "detect":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "train":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "manage":
            self.forth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.forth_frame.grid_forget()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



###########################################################################        

    def sidebar_button_event_home(self):
        try:    
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.second_frame.destroy()
            self.third_frame.destroy()
            self.forth_frame.destroy()

            self.entry.destroy()
            self.main_button_1.destroy()
            self.textbox.destroy()
            self.tabview.destroy()
            self.tabview2.destroy()
            self.tabviewlabel.destroy()
            #clear the previous frame
            self.forth_frame.destroy()
        except:
            pass
##########################################################################
    def sidebar_button_event_detect(self):


        try:
            self.home_frame.destroy()
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            self.third_frame.destroy()
            self.forth_frame.destroy()
            self.entry.destroy()
            self.main_button_1.destroy()
            self.textbox.destroy()
            self.tabview.destroy()
            #clear the previous frame
            self.forth_frame.destroy()
        except:
            pass
        #pang tab
        self.tabview2 = customtkinter.CTkTabview(self, width=100,height=500, corner_radius=20)
        self.tabview2.grid(row=0, column=1, padx=(10, 10), pady=(30,10), sticky="nsew") 
        self.tabviewlabel = customtkinter.CTkLabel(self, text="Detecting")
        self.tabviewlabel.grid(row=1, column=1,  padx=10, pady=10, sticky="")
        



        
#######################################################################################
    def sidebar_button_event_train(self):
        #pang input ng itratrain na words
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Words you want to train")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(10, 0), pady=(20, 20), sticky="nsew")
        #sa katabing button to
        self.main_button_1 = customtkinter.CTkButton(master=self,text="Done", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")  
        # pang text box
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=200)
        self.textbox.grid(row=0, column=3, padx=(10, 0), pady=(10, 0), sticky="nsew")
        self.textbox.insert("0.0", "Notes\n\n" + " Dtio ko didisplay ung mga learned words na na ituro na.\n\n" * 20)
        #pang tab
        self.tabview = customtkinter.CTkTabview(self, width=100,height=500, corner_radius=20)
        self.tabview.grid(row=0, column=1, padx=(10, 0), pady=(0,10), sticky="nsew")
    
        #clear the previous frame
        try:    
            self.home_frame.destroy()
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            self.forth_frame.destroy()
        except:
            pass
   
  


#############################################################################################
    def sidebar_button_event_wordmanager(self):
        #clear the previous frame
        try:
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.second_frame.destroy()
            self.third_frame.destroy()
            self.entry.destroy()
            self.main_button_1.destroy()
            self.textbox.destroy()
            self.tabview.destroy()
            self.tabview2.destroy()
            self.tabviewlabel.destroy()
        except:
            pass
  

        #create a new frame
        self.forth_frame = customtkinter.CTkFrame(self)
        self.forth_frame.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        data_path = "data" # path to the data folder
        folders = os.listdir(data_path) # list all the folders in the data folder
        
        # create a list of checkboxes for each folder
        self.folder_vars = []
        for i, folder in enumerate(folders):
            folder_var = tk.IntVar()
            folder_checkbox = customtkinter.CTkCheckBox(self.forth_frame, text=folder, variable=folder_var)
            folder_checkbox.grid(row=i, column=0, padx=10, pady=10)
            self.folder_vars.append(folder_var)
        
        #create delete button
        delete_button = customtkinter.CTkButton(self.forth_frame, text="Delete", command=self.delete_folders)
        delete_button.grid(row=len(folders), column=0, pady=(10,20))

    def delete_folders(self):
        confirm = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to delete the selected folders?")
        if confirm:
            data_path = "data" # path to the data folder
            folders = os.listdir(data_path) # list all the folders in the data folder
            for i, folder in enumerate(folders):
                if self.folder_vars[i].get() == 1:
                    shutil.rmtree(os.path.join(data_path,folder))
            tkinter.messagebox.showinfo("Deleted", "Selected Folders have been deleted")
        self.sidebar_button_event_wordmanager() # refresh the list of folders





 
        
        
 





if __name__ == "__main__":
    app = App()
    app.mainloop()