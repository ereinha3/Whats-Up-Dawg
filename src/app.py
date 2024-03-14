"""
Graphical User Interface Module
CS422, Group 7, Project 2 - What's Up Dawg!?

Created on 3/2/2024

Contributors:
Darby W. (daw)
Ethan R. (ear)

- Created main screen and shop window - (daw) 3/3/2024
- Added welcome and stat/info screens - (daw) 3/4/2024
- Refined look of all menus and changed the arangement - (daw) 3/4/2024
- Implemented continue and options buttons - (daw) 3/5/2024
- Added happiness indicator and fixed meds/items/afflictions lists - (daw) 3/6/2024
- Made shop dynamically load based on items and meds lists - (daw) 3/7/2024
- Added screen refresh + bug fixes - (daw) 3/8/2024
- Reforamtted splash screen, added docstrings and comments - (daw) 3/10/2024

"""

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


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# This code to create the tool tip object was directly copied from this link : https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# All credit for the code for the ToolTip object is directed to user squareRoot17 at the following URL.
class ToolTip(object):
    '''Tool tip pop up window - shows cost of food and time investment for walk options'''
    def __init__(self, widget: tkinter.Widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text: str) -> None:
        '''Display text in tooltip window'''
        self.text = text
        if self.tipwindow or not self.text:
            return
        
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx()
        y = y + cy + self.widget.winfo_rooty()
        self.tipwindow = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tkinter.Label(
            tw,
            text=self.text,
            justify="left",
            background="#ffffe0",
            relief="solid",
            borderwidth=1,
            font=("tahoma", "12", "normal"))
        label.pack(ipadx=1)

    def hidetip(self) -> None:
        '''Hide tooltip window'''
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
def CreateToolTip(widget, text: str) -> None:
    '''Function for creating the tooltip widget'''
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

class MedicationsWindow(customtkinter.CTkToplevel):
    '''Medication list pop up window containing list of current medications
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Medications")
        self.geometry(f"{380}x{625}")

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
    def close_button_event(self) -> None:
        '''Destroys the medications window when close button is pressed'''
        self.destroy()
        return

class ItemsWindow(customtkinter.CTkToplevel):
    '''Items list pop up window containing list of current items
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Items")
        self.geometry(f"{380}x{625}")

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
    def close_button_event(self) -> None:
        '''Destroys the items window when close button is pressed'''
        self.destroy()
        return

class AfflictionsWindow(customtkinter.CTkToplevel):
    '''Afflictions list pop up window containing list of current afflictions
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Afflictions")
        self.geometry(f"{380}x{625}")

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
    def close_button_event(self) -> None:
        '''Destroys the afflictions window when close button is pressed'''
        self.destroy()
        return

class InstructionsWindow(customtkinter.CTkToplevel):
    '''Instructions pop up window contiaing rules and instructions on how to play the game.
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Game Instructions")
        self.geometry(f"{380}x{625}")

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
        
        instructions = "How To Play\n- To start a new game, press the 'Start New Game' button on the main menu.\n- Enter your name and monthly income (on average), and pick a name and breed for your dog.\nThen press the 'Lets Begin!' button to start the game!\n\n"
        instructions += "- Once the game begins, press the 'Continue' button to begin the next round.\n- You will be presented with two options which you must pick from.\n- Between rounds, you can select a new walk schedule and food quality, as well as purchase items and medications from the shop.\n"
        instructions += "- At any time, you can see your current list of items, medications, or afflictions by pressing the cooresponding buttons in the lower left corner of the main window.\n\n- The game ends when either your dog passes away or you become too financially burdoned to continue.\n"
        instructions += "Gameplay:\nThis game is designed to follow the simulated ownership of the life of a dog. \
The goal of the game is to educate prospective dog owners about the responsibilites, consequences, costs, and good practices of owning a dog. \
The gameplay starts with selection of breed and input of Player Statistics such as Monthly Income, Dog Name, and Player Name. \
The game follows the life of your selected dog, prompting the Player with a single event prompt for every 6-month interval of time. \
This is implemented such that the Player starts the game and is prompted with an event. The Player should first consider all potential ways of modifying the default care system: ie Change Walk/Meal Plan Options or Purchase Items from the Shop. These will affect the Dog during the course of the next round. \
The Player should the respond to the event by choosing one of the two options. The selection will affect the dog and Player in different ways and result in distinct outro messages. \
The Player will then be presented with a summarizing pop-up screen, detailing what has occured over the period of the previous 6-months. The Player should interpret this information and reavulate their dog care regiment to improve the output of this Pop-Up screen. \
\n\nPurpose:\n\
This game is designed to be enjoyed but also educate prospective dog owners about the responsibilities and costs of owning a dog. Approximately 3.1 million dogs are surrendered each year in the US alone, most commonly due to negiligence or unpreparedness when adopting or purchasing a dog. This game hopes to enlighten Players about the things you need to consider when owning a dog such as feeding, walking, and taking it to the vet. It follows the simulation of a dog owner who is prompted with events that occur that the player must respond to. These events vary from rudimentary day-to-day interactions, such as you're dog has made a new friend at the dog park, to more severe diseases such as heartworm. This game is designed to mimic the randomness of daily life, showing users that money needs to always be saved in the event that your dog needs medical attention which proves costly. This game also serves to educate players to proper care for thier dog. It encourages players to walk their dog frequently, feed them high-quality food, and take them to the vet when they are exhibiting any symptoms. While this game should not serve as medical or life advice, it functions as a good guideline for how to responsibly take care of a dog while providing a stimulating player experience. This game has no true objective other than to assist your dog in living their best life, just as true dog ownership does. Our hope is this game will be able to make some impact on the number of dogs being surrended to shelters every year."

        self.instructions_textbox = customtkinter.CTkTextbox(
            self,
            wrap="word")
        self.instructions_textbox.grid(
            row=1,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew")
        
        self.instructions_textbox.insert("0.0", instructions)
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
    def close_button_event(self) -> None:
        '''Destroys the Instructions window when close button is pressed'''
        self.destroy()
        return

class ShopWindow(customtkinter.CTkToplevel):
    '''Shop pop up window containing both the medications and items shops.
    This window is a child (top level) of the main CTk window'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ye Olde Shoppe")
        self.geometry(f"{380}x{625}")

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
    def item_selected(self) -> None:
        '''Command function for items/meds checkboxes.
        Called whenever an item is selected or unselected'''
        # print("Item Selected")
        self.pay_button.configure(state="enabled")
        self.total = 0
        # To update the running total we iterate through all meds/items and check which are switched on.
        for med_checkbox in self.meds_checkboxes:
            key = med_checkbox.cget("text")
            med_price = medications[key]["cost"]
            if med_checkbox.get(): # Check if the textbox is selected. If so, increment total
                self.total += med_price

        for item_checkbox in self.items_checkboxes:
            key = item_checkbox.cget("text")
            item_price = care_items[key]["cost"]
            if item_checkbox.get():
                self.total += item_price

        # Update screen with new total every time an item is selected or un-selected
        self.cost_label.configure(text=f'Cost: $ {str(self.total)}.00')

        return
    
    def pay_button_event(self) -> None:
        '''Command function for shop 'Pay' button'''
        # print("Pay Button Pressed")
        # Add all selected meds/items to appropriate dog attribute dictionaries
        for med_checkbox in self.meds_checkboxes:
            if med_checkbox.get():
                med_key = med_checkbox.cget("text")
                self.master.dog.medications[med_key] = dict(medications[med_key])

        for item_checkbox in self.items_checkboxes:
            if item_checkbox.get():
                item_key = item_checkbox.cget("text")
                self.master.dog.items[item_key] = dict(care_items[item_key])

        # Update main window human balance and screen
        self.master.human.balance = round(int(self.master.human.balance) - int(self.total), 2)
        self.master.balance_label.configure(text=f'Balance: ${str(self.master.human.balance)}')
    
        self.destroy()
        return

class MainWindow(customtkinter.CTk):
    '''The main window of the application. Contains high level frames,
    each containing various subframes with human and dog attributes and
    buttons for game loop iteration'''
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("What's Up Dawg?")
        self.geometry(f"{1000}x{625}")

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

        # Number of iterations through the game loop
        self.num_rounds = 0
        
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
        # Dog Side Bar (Right Side) - Contains dog name, age, image, and meds/items/afflictions lists
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
        self.dog_stats_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.dog_name_label = customtkinter.CTkLabel(
            self.dog_stats_frame,
            text="Dog Name",
            font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.dog_name_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5))

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
        
        self.health_frame = customtkinter.CTkFrame(self.dog_stats_frame)
        self.health_frame.grid(
            row=2,
            column=0,
            padx=5,
            pady=(0, 5))
        
        self.health_label = customtkinter.CTkLabel(
            self.health_frame,
            text=f"Health: 100",
            font=customtkinter.CTkFont(size=18, weight="normal"))
        self.health_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5)
        
        self.happiness_frame = customtkinter.CTkFrame(self.dog_stats_frame)
        self.happiness_frame.grid(
            row=3,
            column=0,
            padx=20,
            pady=(5, 10))
        
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
        # Human Side Bar (Left Side) - Contains human stats, walk/food options, and shop/menu/dark-mode buttons
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
            pady=(10, 5))

        #------------------------------
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
        food_text = ""
        for val in meal_options.values():
            food_text += f'{val["display"]} : ${val["cost"]}/lb\n'
        CreateToolTip(self.food_option_label, text = food_text)

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
        # Bottom Bar Frame (Inside Human Side Bar)
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
        # TextBox and Decision Selection Frame
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
        self.start_string = "It's time to begin your adventure with your new furry friend! Make sure to take good care of them!\n\nPress 'Continue' to begin."
        self.textbox.insert("0.0", self.start_string)
        self.textbox.configure(state="disabled")

        #------------------------------
        # Decisions Options Frame (Inside Text and Decisions Frame)
        self.decision_options_frame = customtkinter.CTkFrame(self.text_and_decision_frame)
        self.decision_options_frame.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="ew")
        self.decision_options_frame.grid_columnconfigure((0, 1), weight=1)

        self.option1_button = customtkinter.CTkButton(
            self.decision_options_frame,
            text="Option 1",
            command=lambda: self.option_button_event(1))
        self.option1_button.grid(
            row=0,
            column=0,
            padx=(20, 5),
            pady=10)
        
        self.option2_button = customtkinter.CTkButton(
            self.decision_options_frame,
            text="Option 2",
            command=lambda: self.option_button_event(2))
        self.option2_button.grid(
            row=0,
            column=1,
            padx=(5, 20),
            pady=10)
        
        #------------------------------
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
        # Welcome / Main Menu Screen
        self.main_menu_screen_frame = customtkinter.CTkFrame(self)
        self.main_menu_screen_frame.grid(
            row=0,
            column=0,
            rowspan=3,
            columnspan=3,
            sticky="news")
        self.main_menu_screen_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_menu_screen_frame.grid_rowconfigure(1, weight=1)
        
        self.welcome_label = customtkinter.CTkLabel(
            self.main_menu_screen_frame,
            text="Welcome!",
            font=customtkinter.CTkFont(size=40, weight="bold"))
        self.welcome_label.grid(
            row=0,
            column=0,
            columnspan=3,
            padx=20,
            pady=20)
        
        self.instructions_button = customtkinter.CTkButton(
            self.main_menu_screen_frame,
            text="How to Play",
            command=self.instructions_button_event,
            font=customtkinter.CTkFont(size=20))
        self.instructions_button.grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="e")
        
        # Resume Button added once a game is started...

        self.start_button = customtkinter.CTkButton(
            self.main_menu_screen_frame,
            text="Start New Game",
            command=self.start_button_event,
            font=customtkinter.CTkFont(size=20))
        self.start_button.grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="w")
        
        self.exit_button = customtkinter.CTkButton(
            self.main_menu_screen_frame,
            text="Exit",
            command=self.exit_button_event)
        self.exit_button.grid(
            row=2,
            column=1,
            padx=20,
            pady=20)
        
        self.resume_button = None

    #--------------------------------------------------------------------------
    # Main Window Methods
    def splash_continue_button_event(self, frame: customtkinter.CTkFrame) -> None:
        """Called when the 'Continue' button on the splash screen is pressed.
        Acts as an end game check.
        
        Inputs:
            frame: the splash screen frame to be destroyed
        """
        frame.destroy() # Remove splash screen
        # Check if the dog is not alive or if it has been surrendered
        if not self.dog.alive or self.human.dog.surrendered:
            self.resume_button.destroy()
            self.main_menu_button_event()
    
    def push_splash_screen(self, text: str) -> None:
        """Add's a splash screen to the main window containing a summary of events.
        
        Inputs:
            text: The text to be displayed on the splash screen
            """
    #--------------------------------------------------------------------------
        # Splash Screen Frame
        self.splash_frame = customtkinter.CTkFrame(self)
        self.splash_frame.grid(
            row=0,
            column=0,
            sticky="news")
        self.splash_frame.grid_columnconfigure(0, weight=1)

        # List of summary lines to be displayed - list length might be different each round
        summary_lines: list[customtkinter.CTkLabel] = []
        for index, line in enumerate(text.split("\n")):
            self.line_label = customtkinter.CTkLabel(
                self.splash_frame,
                text=line,
                font=customtkinter.CTkFont(size=15, weight="normal"))
            self.line_label.grid(
                row=index,
                column=0,
                padx=10,
                pady=10)
            summary_lines.append(self.line_label)

        # Make the title bold
        summary_lines[0].configure(font=customtkinter.CTkFont(size=20, weight="bold"))
        length = len(summary_lines)
        self.splash_frame.grid_rowconfigure((length, length + 1), weight=1)
        
        self.splash_continue_button = customtkinter.CTkButton(
            self.splash_frame,
            width=250,
            text="Continue",
            command=lambda: self.splash_continue_button_event(self.splash_frame))
        self.splash_continue_button.grid(
            row=len(summary_lines) + 1,
            column=0,
            padx = 20,
            pady = 20)
        
        self.splash_frame.tkraise()
    
    def instructions_button_event(self) -> None:
        """Called when the "How to Play' Button is pressed.
        Opens up a toplevel child window containing a set of instructions."""
        # print("How to Button Pressed")
        if self.instructions_window is None or not self.instructions_window.winfo_exists():
            self.instructions_window = InstructionsWindow(self)  # create window if its None or destroyed
        else:
            self.instructions_window.focus()
        return

    def start_button_event(self) -> None:
        """Called every time the 'Start' Button is pressed.
        This initiates the process of gathering required input from the user."""
        # print("Start Button Pressed")
        # Reset the entry boxes in case they contiain any values
        self.human_name_variable.set("")
        self.dog_name_variable.set("")
        self.income_variable.set("")

        self.stat_screen_frame.tkraise()
        return

    def back_button_event(self) -> None:
        """Called every time the 'Back' button is pressed.
        This happens from within the stat selection frame.
        Allows a user to go back to the main menu from the stat selection screen."""
        # print("Back Button Pressed")
        # Reset the entry boxes if the user started filling them out
        self.human_name_variable.set("")
        self.dog_name_variable.set("")
        self.income_variable.set("")

        self.main_menu_screen_frame.tkraise()
        return
    
    def begin_button_event(self) -> None:
        """Called every time the 'Begin' buttton is pressed.
        Resets the dog and human objects, resets the screen, and adds a resume button to the main menu."""
        # print("Begin Button Pressed")
        human_name = self.human_name_variable.get().strip()
        dog_name = self.dog_name_variable.get().strip()
        income = self.income_variable.get().strip().strip("$").strip() # strip white space, then $ symbol, then whitespace again

        # If there are current dog or human objects, clear them out
        if self.dog or self.human:
            print("Deleting Old Dog/Human")
            self.dog = None
            self.human = None

        self.dog = model.Dog(name=dog_name, breed = self.dog_type_combobox.get().lower()) #option: breed
        self.human = model.Human(income, self.dog, name=human_name)
        self.num_rounds = 0

        # Update screen
        self.human_name_label.configure(text=human_name)
        self.dog_name_label.configure(text=dog_name)
        self.balance_label.configure(text=f'Balance: ${self.human.revenue}')
        self.age_label.configure(text=f'Age: {self.dog.age}')
        self.health_label.configure(text=f"Health: {self.dog.health}")
        self.time_invested_label.configure(text=f'Time Invested: {self.human.time_spent}')

        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", tkinter.END)
        self.textbox.insert("0.0", self.start_string)
        self.textbox.configure(state="disabled")
        self.continue_button_frame.tkraise()

        # Set Dog Image
        dog_string = self.dog_type_combobox.get().lower().strip().replace(" ", "_") + ".jpg"
        
        self.dog_image = customtkinter.CTkImage(
            Image.open(os.path.join(self.dog_image_path, dog_string)),
            size=(250, 250))
        
        self.dog_image_label.configure(image=self.dog_image)
    
        # Add resume button to main menu once a game is started
        self.resume_button = customtkinter.CTkButton(
            self.main_menu_screen_frame,
            text="Resume",
            command=self.resume_button_event)
        self.resume_button.grid(
            row=1,
            column=1,
            padx=5,
            pady=5)

        self.main_window_frame.tkraise()
        return

    def meds_button_event(self):
        """Called when the 'Medications' button is pressed.
        Opens up a new window containing a list of current medications"""
        # print("Meds Button Pressed")
        if self.meds_window is None or not self.meds_window.winfo_exists():
            self.meds_window = MedicationsWindow(self)  # create window if its None or destroyed
        else:
            self.meds_window.focus()

        # Iterate through meds and add a newline after each one (for formatting)
        meds_str = ""
        for med in self.dog.medications:
            meds_str += med + "\n"

        # Then add our meds to the medications textbox within the meds window
        self.meds_window.meds_textbox.configure(state="normal")
        self.meds_window.meds_textbox.delete("0.0", tkinter.END)
        self.meds_window.meds_textbox.insert("0.0", meds_str)
        self.meds_window.meds_textbox.configure(state="disabled")
        self.meds_window.meds_textbox.insert("0.0", meds_str)
        return
    
    def items_button_event(self):
        """Called when the 'Items' button is pressed.
        Opens up a new window containing a list of current items"""
        # print("Items Button Pressed")
        if self.items_window is None or not self.items_window.winfo_exists():
            self.items_window = ItemsWindow(self)  # create window if its None or destroyed
        else:
            self.items_window.focus()
    
        # Iterate through items and add a newline after each one (for formatting)
        items_str = ""
        for item in self.dog.items:
            items_str += item + "\n"

        # Then add our items to the items textbox within the items window
        self.items_window.items_textbox.configure(state="normal")
        self.items_window.items_textbox.delete("0.0", tkinter.END)
        self.items_window.items_textbox.insert("0.0", items_str)
        self.items_window.items_textbox.configure(state="disabled")
        self.items_window.items_textbox.insert("0.0", items_str)
        return
    
    def afflictions_button_event(self):
        """Called when the 'Afflictions' button is pressed.
        Opens up a new window containing a list of current afflictions"""
        # print("Afflictions Button Pressed")
        if self.afflictions_window is None or not self.afflictions_window.winfo_exists():
            self.afflictions_window = AfflictionsWindow(self)  # create window if its None or destroyed
        else:
            self.afflictions_window.focus()

        # Iterate through afflictions and add a newline after each one (for formatting)
        afflictions_str = ""
        for affliction in self.dog.afflictions.keys():
            afflictions_str += affliction.replace("_", " ").capitalize() + "\n"

        # Then add our afflictions to the afflictions textbox within the afflictions window
        self.afflictions_window.afflictions_textbox.configure(state="normal")
        self.afflictions_window.afflictions_textbox.delete("0.0", tkinter.END)
        self.afflictions_window.afflictions_textbox.insert("0.0", afflictions_str)
        self.afflictions_window.afflictions_textbox.configure(state="disabled")
        self.afflictions_window.afflictions_textbox.insert("0.0", afflictions_str)
        return
    
    def shop_button_event(self):
        """Called when the 'Shop' button is pressed.
        Opens up a new shop window, which is a toplevel child of the main window"""
        # print("Shop Button Pressed")
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = ShopWindow(self)  # create window if its None or destroyed
        else:
            self.shop_window.focus()
        return
    
    def main_menu_button_event(self):
        """Called when the Main Menu button is pressed.
        Raises the main menu screen frame to the top of the screen"""
        # print("Main Menu Button Pressed")
        self.main_menu_screen_frame.tkraise()
        return
    
    def resume_button_event(self):
        """Called when the resume button is pressed.
        Raises the main window frame to the top of the screen."""
        # print("Resume Button Pressed")
        self.main_window_frame.tkraise()
        return
    
    def exit_button_event(self):
        """Called when the exit button is pressed.
        Destroys the main window, closing the application"""
        # print("Exit Button Pressed")
        self.destroy()
        return
    
    def change_appearance_mode_event(self):
        """Called when the Light/Dark mode switch is interacted with.
        Swaps the mode to the opposite of the current."""
        mode = customtkinter.get_appearance_mode()
        if mode == "Dark":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")
    
    def continue_button_event(self):
        """Called every time the 'Continue' button on the main window is pressed.
        Acts as the main driver of the game loop. Updates the player and human objects
        as well as the screen."""
        # print("Continue Button Pressed")
        # Prevent screen update on initial continue press
        if self.num_rounds != 0:
            self.dog, self.human, summary = controller.next_round(self.dog, self.human, self.event["name"])
            self.push_splash_screen(summary)
            self.refresh_screen()
        self.num_rounds += 1

        # Load a semi random event
        self.event = controller.load_event(self.dog)

        # Check if the dog has resistance to the event
        resistance = controller.check_resistance(self.dog, self.event)
        if resistance:
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", tkinter.END)
            self.textbox.insert("0.0", self.event["resist"]["message"])
            self.textbox.configure(state="disabled")
            
        elif len(self.event["options"])==0:
            # If there are no options for the event loaded, just print the intro
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", tkinter.END)
            self.textbox.insert("0.0", self.event["intro"])
            self.textbox.configure(state="disabled")
        else:
            # Otherwise display both options and raise the options buttons
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", tkinter.END)
            self.textbox.insert("0.0", self.event["intro"] + "\n" 
                                + f'[Option 1]: {self.event["options"][1]["intro"]}' + "\n" 
                                + f'[Option 2]: {self.event["options"][2]["intro"]}')
            self.textbox.configure(state="disabled")
            
            self.decision_options_frame.tkraise()
        
        return
    
    def option_button_event(self, button_number: str) -> None:
        """Called every time one of the option buttons is pressed.
        
        Inputs:
            button_number: a string representing the button pressed, either '1' or '2'
        """
        # print("Option Button Pressed")
        # Handle the event and update the textbox
        self.dog, self.human = controller.handle_event(self.event, button_number, self.dog, self.human)
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", tkinter.END)
        self.textbox.insert("0.0", self.event["options"][button_number]["outro"])
        self.textbox.configure(state="disabled")
        
        self.continue_button_frame.tkraise()
        return

    def change_walk_option_event(self, choice: str) -> None:
        """Called every time the walk option changes. Updates the dog walk_schedule attribute.
        
        Inputs:
            choice: The new walk option choice - choices are derived from walk_options in shop.py
        """
        # print(f"Walk Option Changed to {choice}")
        for key, value in walk_options.items():
            if value["display"] == choice:
                self.dog.walk_schedule = key
                break
        return

    def change_food_option_event(self, choice: str) -> None:
        """Called every time the food option changes. Updates the dog meal_plan attribute.
        
        Inputs:
            choice: The new meal plan choice - choices are derived from meal_options in shop.py
        """
        # print(f"Food Option Changed to {choice}")
        for key, value in meal_options.items():
            if value["display"] == choice:
                self.dog.meal_plan = key
                break
        return

    def trace_function(self, *args) -> None:
        '''Trace function called every time the human and dog stats change.
        Used primarily to ensure that all required entries (dog name, human name, human income)
        are filled appropriately
        
        Inputs:
            args: Included when a trace function is assigned to a tkinter widget. Not used in our case
        '''
        # print("Trace Function Called")
        # Make sure all fields contain at least 1 character
        if (len(self.human_name_variable.get()) > 0 and len(self.dog_name_variable.get()) > 0 and len(self.income_variable.get()) > 0):
            # Strip the supplied income value of any spaces and '$' signs
            income_value = self.income_variable.get().strip()
            if len(income_value) > 0 and income_value[0] == '$':
                income_value = income_value[1:]

            try:
                int(income_value) # income needs to be an integer
            except:
                print("Income Value Invalid - Not a Number")
                self.begin_button.configure(state="disabled") # Dont let the user proceed until income is an int
                return
             
            # If all entries are filled out with appropriate data, enable the begin button
            self.begin_button.configure(state="enabled")
        else:
            self.begin_button.configure(state="disabled") # otherwise disable and wait for proper entries

        return
    
    def refresh_screen(self) -> None:
        '''Updates the screen labels and images with current values'''
        # print("Refreshing")
        self.balance_label.configure(text=f"Balance: ${self.human.balance}")
        self.time_invested_label.configure(text=f"Time Invested: {self.human.time_spent}")
        self.age_label.configure(text=f'Age: {self.dog.age}')
        self.health_label.configure(text=f"Health: {self.dog.health}")

        # Happiness image based on dogs happiness
        happiness_value = self.dog.happiness
        # print(f"Happiness Value: {happiness_value}")
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
