import tkinter
import tkinter.messagebox
import customtkinter
import model
import controller
import os
from PIL import Image
from data.breeds_dict import breeds
from string import capwords


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class MedicationsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Medications")
        self.geometry(f"{380}x{550}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Current Medications",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=15)
        
        self.close_button = customtkinter.CTkButton(
            self,
            text="Close",
            command=self.close_button_event)
        self.close_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10)
        
    #------------------------------------------------------------------------------
    # Medications Window Methods
    def close_button_event(self):
        print("Close Meds Window Button Pressed")
        self.destroy()
        return


class ItemsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Items")
        self.geometry(f"{380}x{550}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Current Items",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=15)
        
        self.close_button = customtkinter.CTkButton(
            self,
            text="Close",
            command=self.close_button_event)
        self.close_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10)
        
    #------------------------------------------------------------------------------
    # Items Window Methods
    def close_button_event(self):
        print("Close Meds Window Button Pressed")
        self.destroy()
        return


class AfflictionsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Afflictions")
        self.geometry(f"{380}x{550}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Current Afflictions",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=15)
        
        self.close_button = customtkinter.CTkButton(
            self,
            text="Close",
            command=self.close_button_event)
        self.close_button.grid(
            row=2,
            column=0,
            padx=10,
            pady=10)
        
    #------------------------------------------------------------------------------
    # Afflictions Window Methods
    def close_button_event(self):
        print("Close Meds Window Button Pressed")
        self.destroy()
        return


class InstructionsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Game Instructions")
        self.geometry(f"{380}x{550}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self,
            text="Instructions",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.title_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=15)
        
        self.instructions_textbox = customtkinter.CTkTextbox(
            self,
            wrap="word")
        self.instructions_textbox.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew")
        self.instructions_textbox.insert("0.0", "Instructions Should Go Here...")
        self.instructions_textbox.configure(state="disabled")


class ShopWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ye Olde Shoppe")
        self.geometry(f"{380}x{550}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    #--------------------------------------------------------------------------
        # Shop Tab View
        self.shop_tabs = customtkinter.CTkTabview(
            self,
            width=250)
        self.shop_tabs.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
            sticky="nsew")
        
        #------------------------------
        # Shots / Meds Selection
        self.shop_tabs.add("Shots/Meds")
        self.shop_tabs.tab("Shots/Meds").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.shots_tab_frame = customtkinter.CTkFrame(
            self.shop_tabs.tab("Shots/Meds"))
        self.shots_tab_frame.grid(
            row=0,
            column=0,
            padx=(20, 20),
            pady=(20, 0),
            sticky="nsew")

        self.fleas_checkbox = customtkinter.CTkCheckBox(
            master=self.shots_tab_frame,
            text="Fleas Medication",
            command=lambda: self.item_selected("fleas"))
        self.fleas_checkbox.grid(
            row=0,
            column=0,
            pady=(20, 0),
            padx=20)

        self.heartworm_checkbox = customtkinter.CTkCheckBox(
            master=self.shots_tab_frame,
            text="Heartworm Medication",
            command=lambda: self.item_selected("heartworm"))
        self.heartworm_checkbox.grid(
            row=1,
            column=0,
            pady=(20, 0),
            padx=20)
        
        #------------------------------
        # Treats and Toys Selection
        self.shop_tabs.add("Treats/Toys")
        self.shop_tabs.tab("Treats/Toys").grid_columnconfigure(0, weight=1)
        
        self.treats_toys_tab_frame = customtkinter.CTkFrame(
            self.shop_tabs.tab("Treats/Toys"))
        self.treats_toys_tab_frame.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 0),
            sticky="nsew")
        
        self.chewy_checkbox = customtkinter.CTkCheckBox(
            master=self.treats_toys_tab_frame,
            text="Chewy Toy",
            command=self.item_selected)
        self.chewy_checkbox.grid(
            row=0,
            column=0,
            pady=(20, 0),
            padx=20,
            sticky="n")
        
    #--------------------------------------------------------------------------
        # Checkout (Cost and Pay Button) Frame
        self.checkout_frame = customtkinter.CTkFrame(self)
        self.checkout_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew")
        self.checkout_frame.grid_columnconfigure((0, 1), weight=1)

        self.cost_label_frame = customtkinter.CTkFrame(self.checkout_frame)
        self.cost_label_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="news")
        self.cost_label_frame.grid_columnconfigure(0, weight=1)

        self.cost_label = customtkinter.CTkLabel(
            self.cost_label_frame,
            text="Cost:",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cost_label.grid(
            row=0,
            column=0,
            padx=(10, 5),
            pady=10,
            sticky="nsew")
        
        self.cost_value_label = customtkinter.CTkLabel(
            self.cost_label_frame,
            text="$0.00",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cost_value_label.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=10,
            sticky="nsew")
        
        self.pay_button = customtkinter.CTkButton(
            self.checkout_frame,
            text="Pay",
            state="disabled",
            command=self.pay_button_event)
        self.pay_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew")
        

    #--------------------------------------------------------------------------
    # Shop Window Methods
    def do_nothing(self):
        return
    
    def item_selected(self, item):
        print(f"Item: {item} Selected")
        self.pay_button.configure(state="enabled")

        return
    
    def pay_button_event(self):
        print("Pay Button Pressed")

        self.destroy()
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

        # Top Level Windows
        self.shop_window = None
        self.instructions_window = None
        self.meds_window = None
        self.items_window = None
        self.afflictions_window = None

        # Dog and Human Objects
        self.human = None
        self.dog = None
        self.dog_image = None
        self.event = None

        # Images
        self.dog_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../docs/Images")
        self.happiness_face_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../docs/test-images")

        #TODO Make Dynamic
        self.face1_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.happiness_face_path, "one_smiling.png")),
            size=(30, 30))
        self.face2_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.happiness_face_path, "two_happy.png")),
            size=(30, 30))
        self.face3_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.happiness_face_path, "three_neutral.png")),
            size=(30, 30))
        self.face4_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.happiness_face_path, "four_sad.png")),
            size=(30, 30))
        self.face5_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.happiness_face_path, "five_frowning.png")),
            size=(30, 30))
        
    #--------------------------------------------------------------------------
        # Main Window Frame
        self.main_window_frame = customtkinter.CTkFrame(self)
        self.main_window_frame.grid(
            row=0,
            column=0,
            sticky="news")
        
        # Main window is a 3x3 grid
        self.main_window_frame.grid_columnconfigure(1, weight=1)
        self.main_window_frame.grid_rowconfigure(1, weight=1)

    #--------------------------------------------------------------------------
        # Top Bar
        self.top_bar_frame = customtkinter.CTkFrame(
            self.main_window_frame,
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
        
    #--------------------------------------------------------------------------
        # Dog Side Bar (Right)
        self.dog_side_bar = customtkinter.CTkFrame(
            self.main_window_frame,
            corner_radius=0)
        self.dog_side_bar.grid(
            row=1,
            column=2,
            rowspan=2,
            sticky="news")
        self.dog_side_bar.grid_rowconfigure(5, weight=1)

        self.dog_name_label = customtkinter.CTkLabel(
            self.dog_side_bar,
            text="Example",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=False))
        self.dog_name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10))
        
        #------------------------------
        # Dog Age Frame (Inside Dog Side Bar)
        self.age_frame = customtkinter.CTkFrame(
            self.dog_side_bar)
        self.age_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=5)
        
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
        
        #------------------------------
        
        self.meds_button = customtkinter.CTkButton(
            self.dog_side_bar,
            text="Medications",
            command=self.meds_button_event)
        self.meds_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=5)
        
        self.items_button = customtkinter.CTkButton(
            self.dog_side_bar,
            text="Items",
            command=self.items_button_event)
        self.items_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=5)
        
        self.afflictions_button = customtkinter.CTkButton(
            self.dog_side_bar,
            text="Afflictions",
            command=self.afflictions_button_event)
        self.afflictions_button.grid(
            row=4,
            column=0,
            padx=20,
            pady=5)
        
        #------------------------------
        # Dog Image Frame (Inside Dog Side Bar)
        self.dog_image_frame = customtkinter.CTkFrame(self.dog_side_bar)
        self.dog_image_frame.grid(
            row=5,
            column=0,
            padx=20,
            pady=10)
        
        # Initialize empty Dog Image
        self.dog_image_label = customtkinter.CTkLabel(
            self.dog_image_frame,
            text="")
        self.dog_image_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)
        
    #--------------------------------------------------------------------------
        # Bottom Bar
        self.bottom_bar_frame = customtkinter.CTkFrame(
            self.main_window_frame,
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
            text="Main Menu",
            width=30,
            command=self.main_menu_button_event)
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
        
    #--------------------------------------------------------------------------
        # Human Side Bar (Left)
        self.human_side_bar = customtkinter.CTkFrame( 
            self.main_window_frame,
            width=140,
            corner_radius=0)
        self.human_side_bar.grid(
            row=1,
            column=0,
            rowspan=2,
            sticky="news")
        self.human_side_bar.grid_rowconfigure(4, weight=1)
        
        self.human_name_label = customtkinter.CTkLabel(
            self.human_side_bar,
            text="Human Name Here",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=False))
        self.human_name_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 10))
        
        #------------------------------
        # Human Stats Frames (Inside Human Side Bar)
        self.balance_frame = customtkinter.CTkFrame(self.human_side_bar)
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
            self.human_side_bar)
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
            image=self.face1_image,
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.happiness_image_label.grid(
            row=0,
            column=1,
            padx=(5, 10),
            pady=5)
        
        self.time_invested_frame = customtkinter.CTkFrame(self.human_side_bar)
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
        
        #------------------------------
        # Options Frame (Inside Human Side Bar)
        self.options_frame = customtkinter.CTkFrame(
            self.human_side_bar,
            fg_color="transparent")
        self.options_frame.grid(
            row=5,
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

    #--------------------------------------------------------------------------
        # TextBox and Decision
        self.text_and_decision_frame = customtkinter.CTkFrame(self.main_window_frame)
        self.text_and_decision_frame.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            sticky="news")
        self.text_and_decision_frame.grid_columnconfigure(0, weight=1)
        self.text_and_decision_frame.grid_rowconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(
            self.text_and_decision_frame,
            wrap="word")
        self.textbox.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=5,
            pady=5,
            sticky="nsew")
        self.textbox.insert("0.0", "It's time to begin your adventure with your new furry friend! Make sure to take good care of them!\n" * 100)
        self.textbox.configure(state="disabled")

    #--------------------------------------------------------------------------
        # Decisions Options Frame (Inside Text and Decisions Frame)
        self.decision_options_frame = customtkinter.CTkFrame(self.text_and_decision_frame)
        self.decision_options_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew")
        self.decision_options_frame.grid_columnconfigure((0, 1), weight=1)

        self.vet_button = customtkinter.CTkButton(
            self.decision_options_frame,
            text="Option 1",
            command=lambda: self.option_button_event("1"))
        self.vet_button.grid(
            row=0,
            column=0,
            padx=(20, 5),
            pady=10)
        
        self.nothing_button = customtkinter.CTkButton(
            self.decision_options_frame,
            text="Option 2",
            command=lambda: self.option_button_event("2"))
        self.nothing_button.grid(
            row=0,
            column=1,
            padx=(5, 20),
            pady=10)
        
    #--------------------------------------------------------------------------
        # Continue Button Frame (Inside Text and Decisions Frame)
        self.continue_button_frame = customtkinter.CTkFrame(self.text_and_decision_frame)
        self.continue_button_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=10,
            sticky="ew")
        self.continue_button_frame.grid_columnconfigure(0, weight=1)
        
        self.continue_button = customtkinter.CTkButton(
            self.continue_button_frame,
            text="Continue",
            command=self.continue_button_event)
        self.continue_button.grid(
            row=0,
            column=0,
            padx=20,
            pady=10)
        
    #--------------------------------------------------------------------------
        # Info/Stat Selection Screen
        self.stat_screen_frame = customtkinter.CTkFrame(self)
        self.stat_screen_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            columnspan=3,
            sticky="news")
        self.stat_screen_frame.grid_columnconfigure((0, 1), weight=1)
        self.stat_screen_frame.grid_rowconfigure(1, weight=1)
        
        self.info_label = customtkinter.CTkLabel(
            self.stat_screen_frame,
            text="Enter Your Information Below",
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.info_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=10,
            pady=10)
        
        #------------------------------
        # Human Info Frame (Inside Stat Screen Frame)
        self.human_info_frame = customtkinter.CTkFrame(self.stat_screen_frame)
        self.human_info_frame.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="news")
        self.human_info_frame.grid_columnconfigure(0, weight=1)

        self.human_name_entry_label = customtkinter.CTkLabel(
            self.human_info_frame,
            text="Your Name")
        self.human_name_entry_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        
        self.human_name_variable = tkinter.StringVar(self)
        self.human_name_entry = customtkinter.CTkEntry(
            self.human_info_frame,
            textvariable=self.human_name_variable)
        self.human_name_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=5)
        self.human_name_variable.trace_add("write", self.trace_function)

        self.income_label = customtkinter.CTkLabel(
            self.human_info_frame,
            text="Monthly Disposable Income ($)")
        self.income_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=5)
        
        self.income_variable = tkinter.StringVar(self)
        self.income_entry = customtkinter.CTkEntry(
            self.human_info_frame,
            textvariable=self.income_variable)
        self.income_entry.grid(
            row=3,
            column=0,
            padx=10,
            pady=5)
        self.income_variable.trace_add("write", self.trace_function)

        #------------------------------
        # Dog Info Frame (Inside Stat Screen Frame)
        self.dog_info_frame = customtkinter.CTkFrame(self.stat_screen_frame)
        self.dog_info_frame.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="news")
        self.dog_info_frame.grid_columnconfigure(0, weight=1)
        
        self.dog_name_entry_label = customtkinter.CTkLabel(
            self.dog_info_frame,
            text="Dog Name")
        self.dog_name_entry_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        
        self.dog_name_variable = tkinter.StringVar(self)
        self.dog_name_entry = customtkinter.CTkEntry(
            self.dog_info_frame,
            textvariable=self.dog_name_variable)
        self.dog_name_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=5)
        self.dog_name_variable.trace_add("write", self.trace_function)

        self.dog_type_label = customtkinter.CTkLabel(
            self.dog_info_frame,
            text="Dog Breed")
        self.dog_type_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=5)
        
        self.dog_type_combobox = customtkinter.CTkComboBox(
            self.dog_info_frame,
            values=list((capwords(breed) for breed in breeds.keys())))
        self.dog_type_combobox.grid(
            row=3,
            column=0,
            padx=10,
            pady=5)

        #------------------------------
        # Stat Screen Buttons Frame (Inside Stat Screen Frame)
        self.buttons_frame = customtkinter.CTkFrame(self.stat_screen_frame)
        self.buttons_frame.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=5,
            pady=5)

        self.back_button = customtkinter.CTkButton(
            self.buttons_frame,
            text="Back",
            command=self.back_button_event)
        self.back_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)
        
        self.begin_button = customtkinter.CTkButton(
            self.buttons_frame,
            text="Lets Begin!",
            state="disabled",
            command=self.begin_button_event)
        self.begin_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10)
        
    #--------------------------------------------------------------------------
        # Welcome / Main Menu Window
        self.main_menu_frame = customtkinter.CTkFrame(self)
        self.main_menu_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            columnspan=3,
            sticky="news")
        self.main_menu_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # self.main_menu_frame.grid_columnconfigure(1, weight=0)
        self.main_menu_frame.grid_rowconfigure(1, weight=1)
        
        self.welcome_label = customtkinter.CTkLabel(
            self.main_menu_frame,
            text="Welcome!",
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.welcome_label.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=20,
            pady=20)
        
        self.instructions_button = customtkinter.CTkButton(
            self.main_menu_frame,
            text="How to Play",
            command=self.instructions_button_event)
        self.instructions_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="e")
        
        # Resume Button gets added once a game is started...

        self.start_button = customtkinter.CTkButton(
            self.main_menu_frame,
            text="Start New Game",
            command=self.start_button_event)
        self.start_button.grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="w")
        
        self.exit_button = customtkinter.CTkButton(
            self.main_menu_frame,
            text="Exit",
            command=self.exit_button_event)
        self.exit_button.grid(
            row=2,
            column=1,
            padx=20,
            pady=20)

    #--------------------------------------------------------------------------
    # Main Window Methods
    def instructions_button_event(self):
        print("How to Button Pressed")
        #TODO open new window with instructions
        if self.instructions_window is None or not self.instructions_window.winfo_exists():
            self.instructions_window = InstructionsWindow(self)  # create window if its None or destroyed
        else:
            self.instructions_window.focus()
        return

    def start_button_event(self):
        print("Start Button Pressed")

        self.human_name_variable.set("")
        self.dog_name_variable.set("")
        self.income_variable.set("")

        self.stat_screen_frame.tkraise()
        return

    def back_button_event(self):
        print("Back Button Pressed")
        self.human_name_variable.set("")
        self.dog_name_variable.set("")
        self.income_variable.set("")

        self.main_menu_frame.tkraise()
        return
    
    def begin_button_event(self):
        print("Begin Button Pressed")
        human_name = self.human_name_variable.get().strip()
        dog_name = self.dog_name_variable.get().strip()
        income = self.income_variable.get().strip().strip("$").strip() # strip white space, then $ symbol, then whitespace again

        if self.dog or self.human:
            print("Deleting Old Dog/Human")
            self.dog = None
            self.human = None

        self.dog = model.Dog(name=dog_name) #option: breed
        self.human = model.Human(income, self.dog)


        #TODO set Dog and Human attributes
        self.human_name_label.configure(text=human_name)
        self.dog_name_label.configure(text=dog_name)
        self.balance_value_label.configure(text="$"+income)

        # Set Dog Image
        dog_string = self.dog_type_combobox.get()
        print(dog_string)
        
        self.dog_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.dog_image_path, "akita.jpg")),
            size=(100, 100))
        
        self.dog_image_label.configure(image=self.dog_image)
    

        # Add resume button to main menu once a game is started
        self.resume_button = customtkinter.CTkButton(
            self.main_menu_frame,
            text="Resume",
            command=self.resume_button_event)
        self.resume_button.grid(
            row=1,
            column=1,
            padx=5,
            pady=5)

        self.main_window_frame.tkraise()
        return

    # Would like to combine the meds, items, and afflictions event funcntions
    def meds_button_event(self):
        print("Meds Button Pressed")
        #TODO open new window with list of current meds

        if self.meds_window is None or not self.meds_window.winfo_exists():
            print("Creating New Meds Window")
            self.meds_window = MedicationsWindow(self)  # create window if its None or destroyed
        else:
            print("Focusing Meds Window")
            self.meds_window.focus()
        return
    
    def items_button_event(self):
        print("Items Button Pressed")
        #TODO open new window with list of current items

        if self.items_window is None or not self.items_window.winfo_exists():
            print("Creating New Items Window")
            self.items_window = ItemsWindow(self)  # create window if its None or destroyed
        else:
            print("Focusing Items Window")
            self.items_window.focus()
        return
    
    def afflictions_button_event(self):
        print("Afflictions Button Pressed")
        #TODO open new window with list of current afflictions

        if self.afflictions_window is None or not self.afflictions_window.winfo_exists():
            print("Creating New Afflictions Window")
            self.afflictions_window = AfflictionsWindow(self)  # create window if its None or destroyed
        else:
            print("Focusing Afflictions Window")
            self.afflictions_window.focus()
        return
    
    def shop_button_event(self):
        print("Shop Button Pressed")
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = ShopWindow(self)  # create window if its None or destroyed
        else:
            self.shop_window.focus()
        return
    
    def main_menu_button_event(self):
        print("Main Menu Button Pressed")
        self.main_menu_frame.tkraise()
        return
    
    def resume_button_event(self):
        print("Resume Button Pressed")
        self.main_window_frame.tkraise()
        return
    
    def exit_button_event(self):
        print("Exit Button Pressed")
        self.destroy()
        return
    
    def change_appearance_mode_event(self):
        mode = customtkinter.get_appearance_mode()
        if mode == "Dark":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")
    
    #--------------------------------------------------------------------------
    def continue_button_event(self):
        print("Continue Button Pressed")
        self.event = controller.load_event()

        resistance = controller.check_resistance(self.dog, self.human, self.event) #TODO - This is not working properly

        # if resistance:
        #     print(f"{event} Resisted")
        # else:
        #     print(f"{event} Not Resisted")

        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", tkinter.END)
        self.textbox.insert("0.0", self.event["intro"] + "\n"
                            + f"[Option 1]: {self.event["options"]["1"]["intro"]}" + "\n"
                            + f"[Option 2]: {self.event["options"]["2"]["intro"]}")
        self.textbox.configure(state="disabled")


        self.decision_options_frame.tkraise()

        # 2. index into events and display information and options
        # 3a. On option1 Do option1 one stuff (Controlller.Event_resolve("option1"))
        # 3b. On option 2 do option 2 stuff 

        return
    
    def option_button_event(self, button_number):
        print("Option Button Pressed")

        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", tkinter.END)
        self.textbox.insert("0.0", self.event["options"][button_number]["outro"])
        self.textbox.configure(state="disabled")

        self.continue_button_frame.tkraise()

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

            income_value = self.income_variable.get().strip()
            if len(income_value) > 0 and income_value[0] == '$':
                income_value = income_value[1:]

            try:
                int(income_value)
            except:
                print("Income Value Invalid - Not a Number")
                self.begin_button.configure(state="disabled")
                return
            
            self.begin_button.configure(state="enabled")
        else:
            self.begin_button.configure(state="disabled")

        return


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
