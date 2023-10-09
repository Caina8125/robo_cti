import tkinter
import customtkinter
import webbrowser
import threading
from pytube import YouTube

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("YouTube Downloader")
        self.resizable(0, 0)
        self.geometry(f"{820}x{460}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)


        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="YouTube Downloader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_1_event, text="Github")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_2_event, text="Instagram")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode :", font=customtkinter.CTkFont(size=11, weight="bold"), anchor="w")
        self.appearance_mode_label.grid(row=4, column=0, padx=10, pady=(50, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=10, pady=(5, 20))


        # self.theme_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Theme Mode :", font=customtkinter.CTkFont(size=11, weight="bold"), anchor="w")
        # self.theme_mode_label.grid(row=6, column=0, padx=10, pady=(5, 0))
        # self.theme_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Coming soon..."],)
        #                                                             #    command=self.change_theme_mode_event)
        # self.theme_mode_optionemenu.grid(row=7, column=0, padx=10, pady=(5, 20))

        self.selected_resolution = "720p"

        self.resolution = customtkinter.CTkLabel(self.sidebar_frame, text=" Resolution :", font=customtkinter.CTkFont(size=11, weight="bold"), anchor="w")
        self.resolution.grid(row=6, column=0, padx=10, pady=(5, 0))
        self.resolution_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["144p", "240p", "360p", "480p", "720p", "1080p"],
                                                                command=self.change_resolution_event)
        self.resolution_optionemenu.grid(row=7, column=0, padx=10, pady=(5, 20))



        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling :", font=customtkinter.CTkFont(size=11, weight="bold"), anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=10, pady=(5, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=10, pady=(5, 20))


        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.resolution_optionemenu.set("720p")
        # self.theme_mode_optionemenu.set("Coming soon...") 

        # The actual Downloader
        self.text = customtkinter.CTkLabel(self, text="Paste youtube link :", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.text.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(0, 180))

        self.entry = customtkinter.CTkEntry(self, width=320, height=40)
        self.entry.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(0, 100))
        self.url_var = tkinter.StringVar()

        # Download button
        self.download = customtkinter.CTkButton(self, text="Download", command=threading.Thread(target=self.download_event).start())
        self.download.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(0, 0))

        
        # Download's completeion
        self.finishLabel = customtkinter.CTkLabel(self, text="")
        self.finishLabel.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(75, 0))

        # Progress percentage
        self.pPercentage = customtkinter.CTkLabel(self, text="0%")
        self.pPercentage.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(130, 0))

        # Progress bar
        self.progressBar = customtkinter.CTkProgressBar(self, width=400)
        self.progressBar.set(0)
        self.progressBar.grid(row=0, column=1, columnspan=2, padx=(0, 0), pady=(160, 0))


        # Footer
        self.vex = customtkinter.CTkLabel(self, text="This project was developed by V E X", font=customtkinter.CTkFont(size=11, weight="bold"))
        self.vex.grid(row=3, column=1, columnspan=2, padx=(10, 0), pady=(10, 10), sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # def change_theme_mode_event(self, new_theme_mode:str):
    #     customtkinter.set_default_color_theme(new_theme_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def sidebar_button_1_event(self):
        webbrowser.open('https://github.com/0vex')

    def sidebar_button_2_event(self):
        webbrowser.open('https://instagram.com/0hkd')

