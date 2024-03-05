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
        self.geometry(f"{380}x{550}")

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


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("What's Up Dawg?")
        self.geometry(f"{900}x{550}")

        # Give weight to window container - allows for better window size adjustment
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Window Attributes
        self.shop_window = None
        self.mode = "dark"

        # Dog and Human Objects
        self.human = Model.Human()
        self.dog = Model.Dog()

        # Images
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../docs/test-images")
        self.dog_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "weiner_dog_example.png")),
            size=(800, 75))
        self.happy_face_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "happy-face.png")),
            size=(30, 30))
        
#------------------------------------------------------------------------------
        # Main Window Frame
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(
            row=0,
            column=0,
            sticky="news")
        
        # Main window is a 3x3 grid
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

#------------------------------------------------------------------------------
        # Top Bar
        self.top_bar_frame = customtkinter.CTkFrame(
            self.main_frame,
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
            # image=self.dog_image,
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.title_label.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=20,
            pady=15)
        
#------------------------------------------------------------------------------
        # Left Side Bar
        self.left_side_bar = customtkinter.CTkFrame(
            self.main_frame,
            width=140,
            corner_radius=0)
        self.left_side_bar.grid(
            row=1,
            column=0,
            rowspan=2,
            sticky="news")
        self.left_side_bar.grid_rowconfigure(5, weight=1)

        self.dog_name_label = customtkinter.CTkLabel(
            self.left_side_bar,
            text="Example",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=False))
        self.dog_name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=20)
        
        self.age_frame = customtkinter.CTkFrame(
            self.left_side_bar)
        self.age_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=(5, 25))
        
        self.age_label = customtkinter.CTkLabel(
            self.age_frame,
            text=f"Age:",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.age_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        
        self.age_value_label = customtkinter.CTkLabel(
            self.age_frame,
            text=f"0",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.age_value_label.grid(
            row=0,
            column=1,
            padx=10,
            pady=5)
        
        self.meds_button = customtkinter.CTkButton(
            self.left_side_bar,
            text="Medications",
            command=self.meds_button_event)
        self.meds_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=5)
        
        self.items_button = customtkinter.CTkButton(
            self.left_side_bar,
            text="Items",
            command=self.items_button_event)
        self.items_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=5)
        
        self.afflictions_button = customtkinter.CTkButton(
            self.left_side_bar,
            text="Afflictions",
            command=self.afflictions_button_event)
        self.afflictions_button.grid(
            row=4,
            column=0,
            padx=20,
            pady=5)
        
#------------------------------------------------------------------------------
        # Options Frame - Bottom Left
        self.options_frame = customtkinter.CTkFrame(
            self.left_side_bar,
            fg_color="transparent")
        self.options_frame.grid(
            row=6,
            column=0,
            sticky="news")

        self.walks_option_label = customtkinter.CTkLabel(
            self.options_frame,
            text="Walk Options")
        self.walks_option_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=5)
        
        self.walk_seg_button = customtkinter.CTkSegmentedButton(
            self.options_frame,
            values=["Short", "Medium", "Long"],
            command=self.change_walk_option_event)
        self.walk_seg_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew")
        self.walk_seg_button.set("Medium")

        self.food_option_label = customtkinter.CTkLabel(
            self.options_frame,
            text="Food Quality",
            anchor="w")
        self.food_option_label.grid(
            row=2,
            column=0,
            padx=20,
            pady=5)
        
        self.food_seg_button = customtkinter.CTkSegmentedButton(
            self.options_frame,
            values=["Cheap", "Medium", "Expensive"],
            command=self.change_food_option_event)
        self.food_seg_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=(5, 20),
            sticky="ew")
        self.food_seg_button.set("Medium")
        
#------------------------------------------------------------------------------
        # Bottom Bar
        self.bottom_bar_frame = customtkinter.CTkFrame(
            self.main_frame,
            height=140,
            corner_radius=0)
        self.bottom_bar_frame.grid(
            row=2,
            column=1,
            columnspan=1,
            sticky="nsew")
        self.bottom_bar_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.shop_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Shop",
            command=self.shop_button_event)
        self.shop_button.grid(
            row=0,
            column=0,
            padx=(20, 5),
            pady=20)
        
        self.back_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Exit",
            width=30,
            command=self.exit_button_event)
        self.back_button.grid(
            row=0,
            column=1,
            padx=5)
        
        self.light_mode_switch = customtkinter.CTkSwitch(
            master=self.bottom_bar_frame,
            text=f"Light/Dark Mode",
            command=self.change_appearance_mode_event)
        self.light_mode_switch.grid(
            row=0,
            column=2,
            padx=(5, 20),
            pady=20)
        
#------------------------------------------------------------------------------
        # Right Side Bar
        self.right_side_bar = customtkinter.CTkFrame( 
            self.main_frame,
            width=140,
            corner_radius=0)
        self.right_side_bar.grid(
            row=1,
            column=2,
            rowspan=2,
            sticky="news")
        self.right_side_bar.grid_rowconfigure(4, weight=1)
        
        self.human_name_label = customtkinter.CTkLabel(
            self.right_side_bar,
            text="Human Name Here",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=False))
        self.human_name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=20)
        
        self.balance_frame = customtkinter.CTkFrame(self.right_side_bar)
        self.balance_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=5)

        self.balance_label = customtkinter.CTkLabel(
            self.balance_frame,
            text="Balance:",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.balance_label.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=5)
        
        self.balance_value_label = customtkinter.CTkLabel(
            self.balance_frame,
            text="$0.00",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.balance_value_label.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=5)
        
        self.happiness_frame = customtkinter.CTkFrame(
            self.right_side_bar
        )
        self.happiness_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=5)
        
        self.happiness_label = customtkinter.CTkLabel(
            self.happiness_frame,
            text="Happiness:",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.happiness_label.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=5)

        self.happiness_image_label = customtkinter.CTkLabel(
            self.happiness_frame,
            text="",
            image=self.happy_face_image,
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.happiness_image_label.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=5)
        
        self.time_invested_frame = customtkinter.CTkFrame(self.right_side_bar)
        self.time_invested_frame.grid(
            row=3,
            column=0,
            padx=20,
            pady=5)

        self.time_invested_label = customtkinter.CTkLabel(
            self.time_invested_frame,
            text="Time Invested:",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.time_invested_label.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=5)
        
        self.time_invested_value_label = customtkinter.CTkLabel(
            self.time_invested_frame,
            text="0",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.time_invested_value_label.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=5)
        
        self.continue_button = customtkinter.CTkButton(
            self.right_side_bar,
            text="Continue",
            command=self.continue_button_event)
        self.continue_button.grid(
            row=5,
            column=0,
            padx=20,
            pady=20)

#------------------------------------------------------------------------------
        # TextBox
        self.textbox = customtkinter.CTkTextbox(self.main_frame)
        self.textbox.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew")
        self.textbox.insert("0.0", "What's Up Dawg?!")
        self.textbox.configure(state="disabled")
        
#------------------------------------------------------------------------------
        # Info/Stat Selection Screen
        self.stat_screen_frame = customtkinter.CTkFrame(self)
        self.stat_screen_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            columnspan=3,
            sticky="news")
        self.stat_screen_frame.grid_columnconfigure(0, weight=1)
        self.stat_screen_frame.grid_rowconfigure((0, 7), weight=1)
        
        self.info_label = customtkinter.CTkLabel(
            self.stat_screen_frame,
            text="Enter Your Information Below",
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.info_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5)

        self.human_name_entry_label = customtkinter.CTkLabel(
            self.stat_screen_frame,
            text="Your Name")
        self.human_name_entry_label.grid(
            row=1,
            column=0,
            padx=5,
            pady=5)
        
        self.human_name_variable = tkinter.StringVar(self)
        self.human_name_entry = customtkinter.CTkEntry(
            self.stat_screen_frame,
            placeholder_text="Jane Doe",
            textvariable=self.human_name_variable)
        self.human_name_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5)
        self.human_name_variable.trace_add("write", self.trace_function)
        
        self.dog_name_entry_label = customtkinter.CTkLabel(
            self.stat_screen_frame,
            text="Dog Name")
        self.dog_name_entry_label.grid(
            row=3,
            column=0,
            padx=5,
            pady=5)
        
        self.dog_name_variable = tkinter.StringVar(self)
        self.dog_name_entry = customtkinter.CTkEntry(
            self.stat_screen_frame,
            placeholder_text="Spike",
            textvariable=self.dog_name_variable)
        self.dog_name_entry.grid(
            row=4,
            column=0,
            padx=5,
            pady=5)
        self.dog_name_variable.trace_add("write", self.trace_function)
        
        self.income_label = customtkinter.CTkLabel(
            self.stat_screen_frame,
            text="Monthly Disposable Income ($)")
        self.income_label.grid(
            row=5,
            column=0,
            padx=5,
            pady=5)
        
        self.income_variable = tkinter.StringVar(self)
        self.income_entry = customtkinter.CTkEntry(
            self.stat_screen_frame,
            placeholder_text="500",
            textvariable=self.income_variable)
        self.income_entry.grid(
            row=6,
            column=0,
            padx=5,
            pady=5)
        self.income_variable.trace_add("write", self.trace_function)
        
        self.begin_button = customtkinter.CTkButton(
            self.stat_screen_frame,
            text="Lets Begin!",
            state="disabled",
            command=self.begin_button_event)
        self.begin_button.grid(
            row=7,
            column=0,
            padx=5,
            pady=5)
        
#------------------------------------------------------------------------------
        # Welcome Screen
        self.welcome_frame = customtkinter.CTkFrame(self)
        self.welcome_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            columnspan=3,
            sticky="news")
        self.welcome_frame.grid_columnconfigure((0, 1), weight=1)
        self.welcome_frame.grid_rowconfigure(1, weight=1)
        
        self.welcome_label = customtkinter.CTkLabel(
            self.welcome_frame,
            text="Welcome!",
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.welcome_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            pady=20)
        
        self.howto_button = customtkinter.CTkButton(
            self.welcome_frame,
            text="How to Play",
            command=self.howto_button_event)
        self.howto_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=5)

        self.start_button = customtkinter.CTkButton(
            self.welcome_frame,
            text="Start!",
            command=self.start_button_event)
        self.start_button.grid(
            row=1,
            column=1,
            padx=5,
            pady=5)

#------------------------------------------------------------------------------
    # methods
    def howto_button_event(self):
        print("How to Button Pressed")
        #TODO open new window with instructions
        return

    def start_button_event(self):
        print("Start Button Pressed")
        self.stat_screen_frame.tkraise()
        return
    
    def begin_button_event(self):
        print("Begin Button Pressed")
        #TODO set Dog and Human attributes
        print(self.human_name_variable.get())
        self.human_name_label.configure(text=self.human_name_variable.get())
        self.dog_name_label.configure(text=self.dog_name_variable.get())
        self.balance_value_label.configure(text="$"+self.income_variable.get())

        self.main_frame.tkraise()
        return

    def meds_button_event(self):
        print("Meds Button Pressed")
        #TODO open new window with list of current meds
        return
    
    def items_button_event(self):
        print("Items Button Pressed")
        #TODO open new window with list of current items
        return
    
    def afflictions_button_event(self):
        print("Afflictions Button Pressed")
        #TODO open new window with list of current afflictions
        return
    
    def shop_button_event(self):
        print("Shop Button Pressed")
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = ShopWindow(self)  # create window if its None or destroyed
        else:
            self.shop_window.focus()
        return
    
    def exit_button_event(self):
        print("Exit Button Pressed")
        #TODO reset all the Dog and Human attributes
        self.human_name_variable.set("")
        self.dog_name_variable.set("")
        self.income_variable.set("")

        self.welcome_frame.tkraise()
        return
    
    def change_appearance_mode_event(self):
        if self.mode == "dark":
            customtkinter.set_appearance_mode("light")
            self.mode = "light"
        else:
            customtkinter.set_appearance_mode("dark")
            self.mode = "dark"
    
    def continue_button_event(self):
        print("Continue Button Pressed")
        if self.shop_window.winfo_exists():
            self.shop_window.destroy()
        return
    
    def change_walk_option_event(self, choice: str):
        print(f"Walk Option Changed to {choice}")
        return
    
    def change_food_option_event(self, choice: str):
        print(f"Food Option Changed to {choice}")
        return
    
    def trace_function(self, *args):
        print("Trace Function Called")
        if (len(self.human_name_variable.get()) > 0 and len(self.dog_name_variable.get()) > 0 and len(self.income_variable.get()) > 0):
            try:
                int(self.income_variable.get())
            except:
                print("Income Value Invalid - Not a Number")
                return
            self.begin_button.configure(state="enabled")
        else:
            self.begin_button.configure(state="disabled")

        return


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
