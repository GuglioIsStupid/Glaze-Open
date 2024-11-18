import tkinter, tkinter.messagebox
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 


class App(customtkinter.CTk, TkinterDnD.DnDWrapper):
    image_files = []
    image_files_path = []

    def __init__(self):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)

        self.title("Glaze Open")
        self.geometry(f"800x600+{int((self.winfo_screenwidth() - 800) / 2)}+{int((self.winfo_screenheight() - 600) / 2)}")
        # basically what the above line does is to center the window on the screen no matter the screen resolution

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # disable text centered alignment
        self.option_add("*Label.anchor", "w")
        self.option_add("*Label.justify", "left")

        # Actually, that should be scrollable
        self.sidebar_frame = customtkinter.CTkScrollableFrame(self, width=280, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # SELECT YOUR IMAGE(S) TO GLAZE
        self.select_image_label = customtkinter.CTkLabel(self.sidebar_frame, text="1. SELECT YOUR IMAGE(S) TO GLAZE") 
        self.select_image_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

        self.select_image_button = customtkinter.CTkButton(self.sidebar_frame, text="Select Image", command=self.select_image)
        self.select_image_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

        # DEFINE GLAZE SETTINGS
        self.glaze_settings_label = customtkinter.CTkLabel(self.sidebar_frame, text="2. DEFINE GLAZE SETTINGS")
        self.glaze_settings_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # INTENSITY
        self.intensity_label = customtkinter.CTkLabel(self.sidebar_frame, text="Intensity")
        self.intensity_label.grid(row=3, column=0, pady=(10, 0))

        self.intensity_slider = customtkinter.CTkSlider(self.sidebar_frame, from_=0.1, to=1.0, orientation="horizontal")
        self.intensity_slider.set(0.5)
        self.intensity_slider.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        self.intensity_labels = customtkinter.CTkLabel(self.sidebar_frame, text="  LOW    |    DEFAULT    |    HIGH  ")
        self.intensity_labels.grid(row=5, column=0, pady=(5, 0), padx=(12, 0))

        # RENDER QUALITY
        self.render_quality_label = customtkinter.CTkLabel(self.sidebar_frame, text="Render Quality")
        self.render_quality_label.grid(row=6, column=0, pady=(10, 0))

        self.render_quality_slider = customtkinter.CTkSlider(self.sidebar_frame, from_=1, to=4, orientation="horizontal", number_of_steps=3)
        self.render_quality_slider.set(1)
        self.render_quality_slider.grid(row=7, column=0, columnspan=2, pady=(10, 0))

        self.render_quality_labels = customtkinter.CTkLabel(self.sidebar_frame, text="  FASTER    |    DEFAULT    |    SLOWER    |    SLOWEST  ")
        self.render_quality_labels.grid(row=8, column=0, pady=(5, 0), padx=(12, 0))

        # OUTPUT
        self.output_label = customtkinter.CTkLabel(self.sidebar_frame, text="3. OUTPUT")
        self.output_label.grid(row=9, column=0, columnspan=2, pady=(10, 0))

        self.output_button = customtkinter.CTkButton(self.sidebar_frame, text="Output", command=self.output)
        self.output_button.grid(row=10, column=0, columnspan=2, pady=(10, 0))

    def select_image(self):
        # multiple files can be selected
        self.image_files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        self.image_files_path = [file for file in self.image_files]

    def output(self):
        if not self.image_files_path:
            tkinter.messagebox.showerror("Error", "Please select an image to glaze.")
            return

if __name__ == "__main__":
    app = App()
    app.mainloop()