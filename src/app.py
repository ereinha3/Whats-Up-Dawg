import tkinter
import tkinter.messagebox
import customtkinter
import Model
import os
from PIL import Image

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ShopWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"{380}x{650}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

#------------------------------------------------------------------------------
        # Tab View
        self.tabview = customtkinter.CTkTabview(
            self,
            width=250)
        self.tabview.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
            sticky="nsew")
        
        #------------------------------
        # Shots Selection
        self.tabview.add("Shots")
        self.tabview.tab("Shots").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.shots_frame = customtkinter.CTkFrame(
            self.tabview.tab("Shots"))
        self.shots_frame.grid(
            row=0,
            column=0,
            padx=(20, 20),
            pady=(20, 0),
            sticky="nsew")

        self.shots_checkbox = customtkinter.CTkCheckBox(
            master=self.shots_frame,
            text="Fleas Medication",
            command=self.item_selected)
        self.shots_checkbox.grid(
            row=0,
            column=0,
            pady=(20, 0),
            padx=20,
            sticky="n")
        
        #------------------------------
        # Treats and Toys Selection
        self.tabview.add("Treats/Toys")
        self.tabview.tab("Treats/Toys").grid_columnconfigure(0, weight=1)
        
        self.toys_frame = customtkinter.CTkFrame(
            self.tabview.tab("Treats/Toys"))
        self.toys_frame.grid(
            row=0,
            column=0,
            padx=(20, 20),
            pady=(20, 0),
            sticky="nsew")
        
        self.toys_checkbox = customtkinter.CTkCheckBox(
            master=self.toys_frame,
            text="Chewy Toy",
            command=self.item_selected)
        self.toys_checkbox.grid(
            row=0,
            column=0,
            pady=(20, 0),
            padx=20,
            sticky="n")
        
#------------------------------------------------------------------------------
        # Cost and Pay Frame
        self.cost_and_pay_frame = customtkinter.CTkFrame(self)
        self.cost_and_pay_frame.grid(
            row=1,
            column=0,
            padx=(20, 20),
            pady=(20, 20),
            sticky="nsew")
        self.cost_and_pay_frame.grid_columnconfigure(1, weight=1)

        self.cost_label = customtkinter.CTkLabel(
            self.cost_and_pay_frame,
            text="Cost: $0.00",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cost_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew")
        
        self.pay_button = customtkinter.CTkButton(
            self.cost_and_pay_frame,
            text="Pay",
            command=self.pay_button_event)
        self.pay_button.grid(
            row=0,
            column=2,
            padx=20,
            pady=20,
            sticky="nsew")
        

#------------------------------------------------------------------------------
    # Methods
    def do_nothing(self):
        return
    
    def item_selected(self):
        print(f"Item Selected")
        return
    
    def pay_button_event(self):
        print("Pay Button Pressed")
        return


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{900}x{650}")

        # configure grid layout (3x3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.shop_window = None

        self.human = Model.Human()
        self.dog = Model.Dog(name="Example Dog")

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../docs/test-images")
        self.dog_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "weiner_dog_example.png")),
            size=(800, 75))
        self.happy_face_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "happy-face.png")),
            size=(40, 40))
        
        self.mode = "dark"

#------------------------------------------------------------------------------
        # Top Bar
        self.top_bar_frame = customtkinter.CTkFrame(
            self,
            height=140,
            corner_radius=0)
        self.top_bar_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="nsew")
        self.top_bar_frame.grid_columnconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self.top_bar_frame,
            text="Whats Up Dawg?!",
            image=self.dog_image,
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.title_label.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=20,
            pady=20)
        
        # self.image_label = customtkinter.CTkLabel(
        #     self.top_bar_frame,
        #     text="",
        #     image=self.dog_image)
        # self.image_label.grid(
        #     row=0,
        #     column=0,
        #     padx=20,
        #     pady=20)
        
        # self.back_button = customtkinter.CTkButton(
        #     self.top_bar_frame,
        #     text="Exit To Main Menu",
        #     width=30,
        #     command=self.exit_button_event)
        # self.back_button.grid(
        #     row=0,
        #     column=0,
        #     padx=25)
        
#------------------------------------------------------------------------------
        # Left Side Bar
        self.left_side_bar = customtkinter.CTkFrame(
            self,
            width=140,
            corner_radius=0)
        self.left_side_bar.grid(
            row=1,
            column=0,
            rowspan=1,
            sticky="news")
        self.left_side_bar.grid_rowconfigure(5, weight=1)
        
        self.dog_name_label = customtkinter.CTkLabel(
            self.left_side_bar,
            text=self.dog.name,
            font=customtkinter.CTkFont(size=20, weight="bold", underline=True))
        self.dog_name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10))
        
        self.age_label = customtkinter.CTkLabel(
            self.left_side_bar,
            text=f"Age: {self.dog.age}",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.age_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10)
        
        self.meds_button = customtkinter.CTkButton(
            self.left_side_bar,
            text="Medications",
            command=self.meds_button_event)
        self.meds_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10)
        
        self.items_button = customtkinter.CTkButton(
            self.left_side_bar,
            text="Items",
            command=self.items_button_event)
        self.items_button.grid(
            row=3,
            column=0,
            padx=10,
            pady=10)
        
        self.afflictions_button = customtkinter.CTkButton(
            self.left_side_bar,
            text="Afflictions",
            command=self.afflictions_button_event)
        self.afflictions_button.grid(
            row=4,
            column=0,
            padx=10,
            pady=10)
        
        self.dashed_line = customtkinter.CTkLabel(
            self.left_side_bar,
            text="--------------------",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.dashed_line.grid(
            row=5,
            column=0)

        self.walks_option_label = customtkinter.CTkLabel(
            self.left_side_bar,
            text="Walk Options",
            anchor="w")
        self.walks_option_label.grid(
            row=6,
            column=0,
            padx=20,
            pady=(10, 0))
        
        self.walks_option_menu = customtkinter.CTkOptionMenu(
            self.left_side_bar,
            values=["Long", "Medium", "Short"],
            command=self.change_walk_option_event)
        self.walks_option_menu.grid(
            row=7,
            column=0,
            padx=20,
            pady=(10, 0))

        self.food_option_label = customtkinter.CTkLabel(
            self.left_side_bar,
            text="Food Quality",
            anchor="w")
        self.food_option_label.grid(
            row=8,
            column=0,
            padx=20,
            pady=(10, 0))

        self.food_options_menu = customtkinter.CTkOptionMenu(
            self.left_side_bar,
            values=["High", "Medium", "Low"],
            command=self.change_food_option_event)
        self.food_options_menu.grid(
            row=9,
            column=0,
            padx=20,
            pady=(10, 20))
        
#------------------------------------------------------------------------------
        # Bottom Bar
        self.bottom_bar_frame = customtkinter.CTkFrame(
            self,
            height=140,
            corner_radius=0)
        self.bottom_bar_frame.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="nsew")
        self.bottom_bar_frame.grid_columnconfigure(3, weight=1)
        
        self.shop_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Shop",
            command=self.shop_button_event)
        self.shop_button.grid(
            row=0,
            column=0,
            padx=20,
            pady=20)
        
        self.back_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Exit To Main Menu",
            width=30,
            command=self.exit_button_event)
        self.back_button.grid(
            row=0,
            column=1,
            padx=20)
        
        self.light_mode_switch = customtkinter.CTkSwitch(
            master=self.bottom_bar_frame,
            text=f"Light/Dark Mode",
            command=self.change_appearance_mode_event)
        self.light_mode_switch.grid(
            row=0,
            column=2,
            padx=20,
            pady=20)
        
        self.continue_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Continue",
            command=self.continue_button_event)
        self.continue_button.grid(
            row=0,
            column=4,
            padx=20,
            pady=20)
        
#------------------------------------------------------------------------------
        # Right Side Bar
        self.right_side_bar = customtkinter.CTkFrame( 
            self,
            width=140,
            corner_radius=0)
        self.right_side_bar.grid(
            row=1,
            column=2,
            rowspan=1,
            sticky="news")
        self.right_side_bar.grid_rowconfigure(5, weight=1)
        
        self.human_name_label = customtkinter.CTkLabel(
            self.right_side_bar,
            text="Human Name Here",
            font=customtkinter.CTkFont(size=20, weight="bold", underline=True))
        self.human_name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=10)
        
        self.balance_label = customtkinter.CTkLabel(
            self.right_side_bar,
            text="Balance: $0.00",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.balance_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=10)
        
        self.happiness_frame = customtkinter.CTkFrame(
            self.right_side_bar
        )
        self.happiness_frame.grid(
            row=2,
            column=0,
            padx=10,
            pady=10)

        
        self.happiness_label = customtkinter.CTkLabel(
            self.happiness_frame,
            text="Happiness:",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.happiness_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)

        self.happiness_image_label = customtkinter.CTkLabel(
            self.happiness_frame,
            text="",
            image=self.happy_face_image,
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.happiness_image_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=10)
        
        self.time_invested_label = customtkinter.CTkLabel(
            self.right_side_bar,
            text="Time Invested: 1000",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.time_invested_label.grid(
            row=3,
            column=0,
            padx=10,
            pady=10)

#------------------------------------------------------------------------------
        # create textbox
        self.textbox = customtkinter.CTkTextbox(
            self)
        self.textbox.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew")
        self.textbox.insert("0.0", "What's Up Dawg?!")
        self.textbox.configure(state="disabled")

#------------------------------------------------------------------------------
    # methods
    def meds_button_event(self):
        print("Meds Button Pressed")
        return
    
    def items_button_event(self):
        print("Items Button Pressed")
        return
    
    def afflictions_button_event(self):
        print("Afflictions Button Pressed")
        return
    
    def shop_button_event(self):
        print("Shop Button Pressed")
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = ShopWindow(self)  # create window if its None or destroyed
        else:
            self.shop_window.focus()
        return
    
    def continue_button_event(self):
        print("Continue Button Pressed")
        self.age_label.configure(text=f"Age: {self.dog.age + 1}")
        return
    
    def change_walk_option_event(self, new_walk_option):
        print(f"Walk Option Changed to {new_walk_option}")
        return
    
    def change_food_option_event(self, new_food_option):
        print(f"Food Option Changed to {new_food_option}")
        return
    
    def exit_button_event(self):
        print("Exit Button Pressed")
        return

    def change_appearance_mode_event(self):
        if self.mode == "dark":
            customtkinter.set_appearance_mode("light")
            self.mode = "light"
        else:
            customtkinter.set_appearance_mode("dark")
            self.mode = "dark"

    # def open_input_dialog_event(self):
    #     dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    #     print("CTkInputDialog:", dialog.get_input())

    # def change_scaling_event(self, new_scaling: str):
    #     return
    #     # new_scaling_float = int(new_scaling.replace("%", "")) / 100
    #     # customtkinter.set_widget_scaling(new_scaling_float)

    # def sidebar_button_event(self):
    #     print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()