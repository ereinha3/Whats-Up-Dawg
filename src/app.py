import tkinter
import tkinter.messagebox
import customtkinter
import model
import controller
import os
from PIL import Image
from data.matches import matches
from data.shop import care_items, medications, walk_options, meal_options
from string import capwords
import time


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx()
        y = y + cy + self.widget.winfo_rooty()
        self.tipwindow = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(tw, text=self.text, justify="left",
                      background="#ffffe0", relief="solid", borderwidth=1,
                      font=("tahoma", "12", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

class MedicationsWindow(customtkinter.CTkToplevel):
    '''Medication List Pop Up Window Containing List of Current Medications
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Medications")
        self.geometry(f"{380}x{600}")

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
        
        self.meds_textbox = customtkinter.CTkTextbox(
            self,
            wrap="word")
        self.meds_textbox.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="news")
        
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
        '''Destroys the medications window when close button is pressed'''
        self.destroy()
        return
    

class ItemsWindow(customtkinter.CTkToplevel):
    '''Items list pop up window containing list of current items
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Items")
        self.geometry(f"{380}x{600}")

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

        self.items_textbox = customtkinter.CTkTextbox(
            self,
            wrap="word")
        self.items_textbox.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="news")

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
        '''Destroys the items window when close button is pressed'''
        self.destroy()
        return

class AfflictionsWindow(customtkinter.CTkToplevel):
    '''Afflictions list pop up window containing list of current afflictions
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Afflictions")
        self.geometry(f"{380}x{600}")

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
        
        self.afflictions_textbox = customtkinter.CTkTextbox(
            self,
            wrap="word")
        self.afflictions_textbox.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="news")
        
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
        '''Destroys the afflictions window when close button is pressed'''
        self.destroy()
        return

class InstructionsWindow(customtkinter.CTkToplevel):
    '''Instructions pop up window contiaing rules and instructions on how to play the game.
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Game Instructions")
        self.geometry(f"{380}x{600}")

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
        self.instructions_textbox.insert("0.0", "Instructions Should Go Here...") # TODO
        self.instructions_textbox.configure(state="disabled")

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
    # Instructions Window Methods
    def close_button_event(self):
        '''Destroys the Instructions window when close button is pressed'''
        self.destroy()
        return

class ShopWindow(customtkinter.CTkToplevel):
    '''Shop pop up window containing both the medications and items shops.
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ye Olde Shoppe")
        self.geometry(f"{380}x{600}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Running total for current shopping session
        self.total = 0

    #--------------------------------------------------------------------------
        # Shop Tab View - Allows for multiple toggleable frames
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
        # medications (Shots / Meds) Selection
        self.shop_tabs.add("Shots/Meds")
        self.shop_tabs.tab("Shots/Meds").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.meds_tab_frame = customtkinter.CTkFrame(
            self.shop_tabs.tab("Shots/Meds"))
        self.meds_tab_frame.grid(
            row=0,
            column=0,
            padx=(20, 20),
            pady=(20, 0),
            sticky="nsew")

        # Dynamically populated from dictionary in shop.py
        self.meds_checkboxes = []
        for index, med in enumerate(medications):
            self.med_checkbox = customtkinter.CTkCheckBox(
                master=self.meds_tab_frame,
                text=f"{medications[med]['display']}",
                command=self.item_selected)
            self.med_checkbox.grid(
                row=index, # Need index so check boxes dont stack on top of eachother
                column=0,
                pady=(20, 0),
                padx=20)
            self.meds_checkboxes.append(self.med_checkbox)

        #------------------------------
        # Items (Treats / Toys) Selection
        self.shop_tabs.add("Treats/Toys")
        self.shop_tabs.tab("Treats/Toys").grid_columnconfigure(0, weight=1)
        
        self.items_tab_frame = customtkinter.CTkFrame(
            self.shop_tabs.tab("Treats/Toys"))
        self.items_tab_frame.grid(
            row=0,
            column=0,
            padx=20,
            pady=(20, 0),
            sticky="nsew")
        
        # Dynamically populated from dictionary in shop.py
        self.items_checkboxes = []
        for index, item in enumerate(care_items):
            self.item_checkbox = customtkinter.CTkCheckBox(
                master=self.items_tab_frame,
                text=f"{care_items[item]['display']}",
                command=self.item_selected)
            self.item_checkbox.grid(
                row=index,
                column=0,
                pady=(20, 0),
                padx=20,
                sticky="n")
            self.items_checkboxes.append(self.item_checkbox)
        
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
            text="Cost: $0.00",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cost_label.grid(
            row=0,
            column=0,
            padx=(10, 10),
            pady=10,
            sticky="nsew")
        
        self.pay_button = customtkinter.CTkButton(
            self.checkout_frame,
            text="Pay",
            command=self.pay_button_event)
        self.pay_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew")
        
    #--------------------------------------------------------------------------
    # Shop Window Methods
    def item_selected(self):
        '''TODO'''
        print("Item Selected")
        self.pay_button.configure(state="enabled")
        self.total = 0
        # To update the running total we iterate through all meds/items and check which are switched on.
        for med_checkbox in self.meds_checkboxes:
            key = med_checkbox.cget("text")
            med_price = medications[key]["cost"]
            if med_checkbox.get():
                self.total += med_price

        for item_checkbox in self.items_checkboxes:
            key = item_checkbox.cget("text")
            item_price = care_items[key]["cost"]
            if item_checkbox.get():
                self.total += item_price

        # Update screen every time an item is selected or un-selected
        self.cost_label.configure(text=f'Cost: $ {str(self.total)}.00')

        return
    
    def pay_button_event(self):
        '''TODO'''
        print("Pay Button Pressed")

        # Add all selected meds/items to appropriate dog attribute dictionaries
        for med_checkbox in self.meds_checkboxes:
            if med_checkbox.get():
                med_key = med_checkbox.cget("text")
                #print('med_key =', med_key)
                #print("medications = ", self.master.dog.medications)
                self.master.dog.medications[med_key] = medications[med_key]["duration"]# .add(med_checkbox.cget("text"))

        for item_checkbox in self.items_checkboxes:
            if item_checkbox.get():
                item_key = item_checkbox.cget("text")
                self.master.dog.items[item_key] = care_items[item_key]["duration"]

        # Update human balance and screen
        self.master.human.balance = round(int(self.master.human.balance) - int(self.total), 2)
        self.master.balance_label.configure(text=f'Balance: ${str(self.master.human.balance)}')
    
        self.destroy()
        return

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("What's Up Dawg?")
        self.geometry(f"{1000}x{600}")

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
        
        # Clip art image paths
        self.dog_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../docs/Images")
        self.happiness_face_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../docs/test-images")

        # 5-stage happiness indicator emojis
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
        # Main Window Frame - Contains all widgets that are displayed on the main play screen
        self.main_window_frame = customtkinter.CTkFrame(self)
        self.main_window_frame.grid(
            row=0,
            column=0,
            sticky="news")
        
        # Main window is a 3x3 grid
        self.main_window_frame.grid_columnconfigure(1, weight=1)
        self.main_window_frame.grid_rowconfigure(1, weight=1)

    #--------------------------------------------------------------------------
        # Top Bar - Game title
        self.top_bar_frame = customtkinter.CTkFrame(self.main_window_frame)
        self.top_bar_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="nsew")
        self.top_bar_frame.grid_columnconfigure(1, weight=1)

        self.title_label = customtkinter.CTkLabel(
            self.top_bar_frame,
            text="Whats Up Dawg?!",
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.title_label.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=20,
            pady=15)
        
    #--------------------------------------------------------------------------
        # Dog Side Bar (Right) - Contains dog name, age, image, and meds/items/afflictions lists
        self.dog_side_bar = customtkinter.CTkFrame(self.main_window_frame)
        self.dog_side_bar.grid(
            row=1,
            column=2,
            rowspan=2,
            sticky="news")
        self.dog_side_bar.grid_rowconfigure((0, 1, 2), weight=1)
        
        #------------------------------
        # Dog Name and Age Frame (Inside Dog Side Bar)
        self.dog_stats_frame = customtkinter.CTkFrame(self.dog_side_bar)
        self.dog_stats_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5),
            sticky="news")
        self.dog_stats_frame.grid_columnconfigure(0, weight=1)
        self.dog_stats_frame.grid_rowconfigure((0, 1), weight=1)

        self.dog_name_label = customtkinter.CTkLabel(
            self.dog_stats_frame,
            text="Dog Name",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.dog_name_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)

        self.age_frame = customtkinter.CTkFrame(self.dog_stats_frame)
        self.age_frame.grid(
            row=1,
            column=0,
            padx=5,
            pady=5)
        
        self.age_label = customtkinter.CTkLabel(
            self.age_frame,
            text=f"Age: 0",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.age_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        
        #------------------------------
        # Dog Image Frame (Inside Dog Side Bar)
        self.dog_image_frame = customtkinter.CTkFrame(self.dog_side_bar)
        self.dog_image_frame.grid(
            row=1,
            column=0,
            padx=10,
            pady=5)
        
        # Initialize empty Dog Image - Gets dynamically filled with appropriate image based on breed selected
        self.dog_image_label = customtkinter.CTkLabel(
            self.dog_image_frame,
            text="")
        self.dog_image_label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5)
        
        #------------------------------
        # Dog Attribute Buttons Frame (Inside Dog Side Bar)
        self.dog_buttons_frame = customtkinter.CTkFrame(self.dog_side_bar)
        self.dog_buttons_frame.grid(
            row=2,
            column=0,
            padx=10,
            pady=(5, 10),
            sticky="news")
        self.dog_buttons_frame.grid_columnconfigure(0, weight=1)
        self.dog_buttons_frame.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.meds_button = customtkinter.CTkButton(
            self.dog_buttons_frame,
            text="Medications",
            command=self.meds_button_event)
        self.meds_button.grid(
            row=0,
            column=0,
            padx=20,
            pady=(10, 5))
        
        self.items_button = customtkinter.CTkButton(
            self.dog_buttons_frame,
            text="Items",
            command=self.items_button_event)
        self.items_button.grid(
            row=1,
            column=0,
            padx=20,
            pady=5)

        self.afflictions_button = customtkinter.CTkButton(
            self.dog_buttons_frame,
            text="Afflictions",
            command=self.afflictions_button_event)
        self.afflictions_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=(5,10))
        
    #--------------------------------------------------------------------------
        # Human Side Bar (Left)
        self.human_side_bar = customtkinter.CTkFrame(self.main_window_frame)
        self.human_side_bar.grid(
            row=1,
            column=0,
            rowspan=2,
            sticky="news")
        self.human_side_bar.grid_rowconfigure((0, 1, 2), weight=1)
        
        #------------------------------
        # Human Name and Stats Frame (Inside Human Side Bar)
        self.human_stats_frame = customtkinter.CTkFrame(self.human_side_bar)
        self.human_stats_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5),
            sticky="news")
        self.human_stats_frame.grid_columnconfigure(0, weight=1)
        self.human_stats_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.human_name_label = customtkinter.CTkLabel(
            self.human_stats_frame,
            text="Human Name Here",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.human_name_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)

        self.balance_frame = customtkinter.CTkFrame(self.human_stats_frame)
        self.balance_frame.grid(
            row=1,
            column=0,
            padx=20,
            pady=5)

        self.balance_label = customtkinter.CTkLabel(
            self.balance_frame,
            text="Balance: $0.00",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.balance_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        
        #------------------------------
        self.happiness_frame = customtkinter.CTkFrame(self.human_stats_frame)
        self.happiness_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=0)
        
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
        
        #------------------------------
        self.time_invested_frame = customtkinter.CTkFrame(self.human_stats_frame)
        self.time_invested_frame.grid(
            row=3,
            column=0,
            padx=10,
            pady=5)

        self.time_invested_label = customtkinter.CTkLabel(
            self.time_invested_frame,
            text="Time Invested: 0",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.time_invested_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)

        #------------------------------
        # Options Frame (Inside Human Side Bar)
        self.options_frame = customtkinter.CTkFrame(self.human_side_bar)
        self.options_frame.grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="news")
        self.options_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.walks_option_label = customtkinter.CTkLabel(
            self.options_frame,
            text="Walk Options",
            font=customtkinter.CTkFont(underline=True))
        self.walks_option_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        CreateToolTip(self.walks_option_label, text = "Short : 2hrs/week\nMedium : 7hrs/week\nLong : 15hrs/week")

        self.walk_seg_button = customtkinter.CTkSegmentedButton(
            self.options_frame,
            values=list(walk_options[option]["display"] for option in walk_options.keys()),
            command=self.change_walk_option_event)
        self.walk_seg_button.grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="ew")
        self.walk_seg_button.set("Medium")
        
        self.food_option_label = customtkinter.CTkLabel(
            self.options_frame,
            text="Food Quality",
            font=customtkinter.CTkFont(underline=True))
        self.food_option_label.grid(
            row=2,
            column=0,
            padx=10,
            pady=5)
        CreateToolTip(self.food_option_label, text = "Walmart's finest : $1.07/lb\nPurina One : $1.84/lb\nVet Recommended : $2.15/lb")

        self.food_seg_button = customtkinter.CTkSegmentedButton(
            self.options_frame,
            values=list(meal_options[option]["display"] for option in meal_options.keys()),#["Cheap", "Normal", "Vet Recommended"],
            command=self.change_food_option_event)
        self.food_seg_button.grid(
            row=3,
            column=0,
            padx=10,
            pady=5,
            sticky="ew")
        self.food_seg_button.set(meal_options["normal"]["display"])

        #------------------------------
        # Bottom Bar (Inside Human Side Bar)
        self.bottom_bar_frame = customtkinter.CTkFrame(self.human_side_bar)
        self.bottom_bar_frame.grid(
            row=2,
            column=0,
            columnspan=1,
            padx=10,
            pady=(5, 10),
            sticky="nsew")
        self.bottom_bar_frame.grid_columnconfigure(0, weight=1)
        self.bottom_bar_frame.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.shop_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Shop",
            command=self.shop_button_event)
        self.shop_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)
        
        self.back_button = customtkinter.CTkButton(
            self.bottom_bar_frame,
            text="Main Menu",
            command=self.main_menu_button_event)
        self.back_button.grid(
            row=1,
            column=0,
            padx=10)
        
        self.light_mode_switch = customtkinter.CTkSwitch(
            master=self.bottom_bar_frame,
            text=f"Light/Dark Mode",
            command=self.change_appearance_mode_event)
        self.light_mode_switch.grid(
            row=2,
            column=0,
            padx=10,
            pady=(10, 20))

    #--------------------------------------------------------------------------
        # TextBox and Decision
        self.text_and_decision_frame = customtkinter.CTkFrame(self.main_window_frame)
        self.text_and_decision_frame.grid(
            row=1,
            column=1,
            rowspan=2,
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
            padx=10,
            pady=10,
            sticky="nsew")
        self.textbox.insert("0.0", "It's time to begin your adventure with your new furry friend! Make sure to take good care of them!\n\nPress 'Continue' to begin.")
        self.textbox.configure(state="disabled")

    #--------------------------------------------------------------------------
        # Decisions Options Frame (Inside Text and Decisions Frame)
        self.decision_options_frame = customtkinter.CTkFrame(self.text_and_decision_frame)
        self.decision_options_frame.grid(
            row=1,
            column=0,
            padx=10,
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
            text="Monthly Income ($)")
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
            values=sorted(list((capwords(breed) for breed in matches))))
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
            padx=10,
            pady=10)

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
    def push_splash_screen(self, text):
        self.splash_frame = customtkinter.CTkFrame(self)
        self.splash_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            columnspan=3,
            sticky="news")
        self.splash_frame.grid_columnconfigure((0, 1, 2), weight=1)
        # self.main_menu_frame.grid_columnconfigure(1, weight=0)
        self.splash_frame.grid_rowconfigure(1, weight=1)
        summary_label = customtkinter.CTkLabel(self.splash_frame, text=text, font=customtkinter.CTkFont(size=20, weight="bold"))
        summary_label.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="news",
            padx = 5,
            pady = 5,
        )
        self.continue_and_destroy_frame_button = customtkinter.CTkButton(
            self.splash_frame,
            text="Continue",
            command=lambda: self.splash_frame.destroy())
        self.continue_and_destroy_frame_button.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky='news')
        self.splash_frame.tkraise()

    
    def instructions_button_event(self):
        print("How to Button Pressed")
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

        self.dog = model.Dog(name=dog_name, breed = self.dog_type_combobox.get().lower()) #option: breed
        self.human = model.Human(income, self.dog)

        #TODO set Dog and Human attributes
        self.human_name_label.configure(text=human_name)
        self.dog_name_label.configure(text=dog_name)
        self.balance_label.configure(text=f'Balance: ${self.human.revenue}')

        # Set Dog Image
        dog_string = self.dog_type_combobox.get().lower().strip().replace(" ", "_") + ".jpg"
        
        self.dog_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.dog_image_path, dog_string)),
            size=(250, 250))
        
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

    # TODO - could combine the meds, items, and afflictions event funcntions
    def meds_button_event(self):
        print("Meds Button Pressed")
        if self.meds_window is None or not self.meds_window.winfo_exists():
            self.meds_window = MedicationsWindow(self)  # create window if its None or destroyed
        else:
            self.meds_window.focus()

        meds_str = ""
        for med in self.dog.medications:
            meds_str += med + "\n"

        self.meds_window.meds_textbox.configure(state="normal")
        self.meds_window.meds_textbox.delete("0.0", tkinter.END)
        self.meds_window.meds_textbox.insert("0.0", meds_str)
        self.meds_window.meds_textbox.configure(state="disabled")
        self.meds_window.meds_textbox.insert("0.0", meds_str)
        return
    
    # TODO - could combine the meds, items, and afflictions event funcntions
    def items_button_event(self):
        print("Items Button Pressed")
        if self.items_window is None or not self.items_window.winfo_exists():
            self.items_window = ItemsWindow(self)  # create window if its None or destroyed
        else:
            self.items_window.focus()
    
        items_str = ""
        for item in self.dog.items:
            items_str += item + "\n"

        self.items_window.items_textbox.configure(state="normal")
        self.items_window.items_textbox.delete("0.0", tkinter.END)
        self.items_window.items_textbox.insert("0.0", items_str)
        self.items_window.items_textbox.configure(state="disabled")
        self.items_window.items_textbox.insert("0.0", items_str)
        return
    
    # TODO - could combine the meds, items, and afflictions event funcntions
    def afflictions_button_event(self):
        print("Afflictions Button Pressed")
        if self.afflictions_window is None or not self.afflictions_window.winfo_exists():
            self.afflictions_window = AfflictionsWindow(self)  # create window if its None or destroyed
        else:
            self.afflictions_window.focus()

        afflictions_str = ""
        for affliction in self.dog.afflictions:
            afflictions_str += affliction + "\n"

        self.afflictions_window.afflictions_textbox.configure(state="normal")
        self.afflictions_window.afflictions_textbox.delete("0.0", tkinter.END)
        self.afflictions_window.afflictions_textbox.insert("0.0", afflictions_str)
        self.afflictions_window.afflictions_textbox.configure(state="disabled")
        self.afflictions_window.afflictions_textbox.insert("0.0", afflictions_str)
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
        self.event = controller.load_event(self.dog)
        event_name = self.event["name"]

        resistance = controller.check_resistance(self.dog, self.event)

        if resistance:
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", tkinter.END)
            self.textbox.insert("0.0", self.event["resist"]["message"])
            self.textbox.configure(state="disabled")
            
            if event_name in self.dog.medications:
                if self.dog.medications[event_name] == 0:
                    del self.dog.medications[event_name]

        elif len(self.event["options"])==0:
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", tkinter.END)
            self.textbox.insert("0.0", self.event["intro"])
            self.textbox.configure(state="disabled")
        
        else:
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", tkinter.END)
            self.textbox.insert("0.0", self.event["intro"] + "\n" 
                                + f'[Option 1]: {self.event["options"]["1"]["intro"]}' + "\n" 
                                + f'[Option 2]: {self.event["options"]["2"]["intro"]}')
            self.textbox.configure(state="disabled")
            self.dog, self.human, summary = controller.next_round(self.dog, self.human)
            self.push_splash_screen(summary)
            self.decision_options_frame.tkraise()
            return
            # return TODO <- This could prevent stat updates until an option is selected

        #TODO update dog and human stats
        self.dog, self.human, summary = controller.next_round(self.dog, self.human)
        self.push_splash_screen(summary)
        self.refresh_screen()
        return
    
    def option_button_event(self, button_number):
        print("Option Button Pressed")

        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", tkinter.END)
        self.textbox.insert("0.0", self.event["options"][button_number]["outro"])
        self.textbox.configure(state="disabled")

        self.continue_button_frame.tkraise()
        

        #TODO update dog and human stats
        #print("event = ", self.event)
        self.dog, self.human = controller.handle_event(self.event, button_number, self.dog, self.human)
        self.refresh_screen()
        print(self.dog)
        print(self.human)
        return

    def change_walk_option_event(self, choice: str):
        print(f"Walk Option Changed to {choice}")
        for key, value in walk_options.items():
            if value["display"] == choice:
                self.dog.walk_schedule = key
                return
        print("ERROR: No Value Found For Walk Option")
        return

    def change_food_option_event(self, choice: str):
        print(f"Food Option Changed to {choice}")
        for key, value in meal_options.items():
            if value["display"] == choice:
                self.dog.meal_plan = key
                return
        print("ERROR: No Value Found For Walk Option")
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
    
    def refresh_screen(self):
        print("Refreshing")
        self.balance_label.configure(text=f"Balance: ${self.human.balance}")
        self.time_invested_label.configure(text=f"Time Invested: {self.human.time_spent}")
        self.age_label.configure(text=f'Age: {self.dog.age}')

        # Happiness image based on dogs happiness
        happiness_value = self.dog.happiness
        if (80 <= happiness_value <= 100):
            self.happiness_image_label.configure(image=self.face1_image)
        elif (60 <= happiness_value <= 79):
            self.happiness_image_label.configure(image=self.face2_image)
        elif (40 <= happiness_value <= 59):
            self.happiness_image_label.configure(image=self.face3_image)
        elif (20 <= happiness_value <= 39):
            self.happiness_image_label.configure(image=self.face4_image)
        elif (0 <= happiness_value <= 79):
            self.happiness_image_label.configure(image=self.face5_image)

        return


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
