import customtkinter as ctk
from PIL import Image
import pywinstyles  # Ensure you have run: pip install pywinstyles
from dashboard import Dashboard

def center_window(window, width, height):
    # 1. Get the user's screen resolution
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 2. Calculate the X and Y coordinates to center the window
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    # 3. Apply the geometry
    window.geometry(f"{width}x{height}+{x}+{y}")

# Initialize the main application window
app = ctk.CTk()
app.title("Library Management System")
center_window(app, 1100, 900)

# -- Functions for App Configuration --



def changeText():
    if labelDesc1.my_custom_tag == "LogIn":
        labelDesc1.configure(text="Don't have an account?")
        labelDesc1.my_custom_tag = "SignUp"
        labelDesc2.configure(text="Please sign up to continue...")
        signUpButton.configure(text="Sign Up from here")
        confirmPasswordEntry.grid_remove()  # Hide confirm password on login
        frameUpperConfirmPasswordLabel.grid_remove()  # Hide confirm password label on login
        loginButton.configure(text="Log In")
        frameUpperSubTitle.configure(text="Log in to your account")

    else:
        labelDesc1.configure(text="Have an account?")
        labelDesc1.my_custom_tag = "LogIn"
        labelDesc2.configure(text="Please log in to continue...")
        signUpButton.configure(text="Log In from here")
        confirmPasswordEntry.grid()  #  Show confirm password on sign up
        frameUpperConfirmPasswordLabel.grid()  # Show confirm password label on sign up
        loginButton.configure(text="Sign Up")
        frameUpperSubTitle.configure(text="Sign Up to your account")



def open_dashboard():
    # Fix: Create the window logic
    window = Dashboard(app)
    window.focus() # Bring to front

def login():
    # --- BUG FIX: Do not use app.destroy() ---
    print("Logging in...")
    app.withdraw() # Hide the login window
    open_dashboard() # Open the new window














# -- END of Functions for App Configuration --

# --- Grid Configuration ---
app.grid_columnconfigure(0, weight=1)  # Left column
app.grid_rowconfigure(0, weight=0)  # Top label row 1
app.grid_rowconfigure(1, weight=0)  # Top label row 2
app.grid_rowconfigure(2, weight=1)  # Main content row
app.grid_rowconfigure(3, weight=1)

# --- Top Labels ---
label = ctk.CTkLabel(app, text="Hello!", fg_color="transparent", font=("Arial", 40, "bold"))
label2 = ctk.CTkLabel(app, text="Welcome...", fg_color="transparent", font=("Arial", 40, "bold"))
label.grid(row=0, column=0, pady=(40, 0), sticky="n")
label2.grid(row=1, column=0, pady=10, sticky="n")

# --- Image Loading (With Safety Check) ---
# This ensures the app doesn't crash if the image path is wrong
try:
    pil_image = Image.open("assets/backgroundOption.jpg")
    my_image = ctk.CTkImage(light_image=pil_image,
                            dark_image=pil_image,
                            size=(1000, 700))
except Exception as e:
    print(f"Image not found: {e}. Using a placeholder.")
    my_image = None

# --- Frame 1: Description Frame ---
frameLower = ctk.CTkFrame(master=app,
                          width=1000,
                          height=700,
                          corner_radius=20,
                          fg_color="white") 
frameLower.grid(row=2, column=0, pady=10, sticky="n")
frameLower.grid_propagate(False)  # Fix size

# --- Background Image inside Frame ---
if my_image:
    bg_label = ctk.CTkLabel(master=frameLower,
                            image=my_image,
                            text="")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    # Fallback if image fails
    bg_label = ctk.CTkLabel(master=frameLower, text="Image Missing", fg_color="gray")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# --- Transparent Text Label (The Fix) ---

# 1. Pick a unique color for the background (Chroma Key)
# We use a distinct color that is NOT in your text or image generally.
chroma_color = "#000001" 

labelDesc1 = ctk.CTkLabel(master=frameLower,
                         text="Have an account?",
                         font=("Arial", 35, "bold"),
                         text_color="Black",  # Make sure text contrasts with your image
                         fg_color=chroma_color,
                         width=500,   # <--- FIX
                         height=50,   # <--- FIX
                         anchor="center") # Set the background to our key color

labelDesc1.my_custom_tag = "LogIn"  # Custom tag for identification

labelDesc2 = ctk.CTkLabel(master=frameLower,
                         text="Please log in to continue...",
                         font=("Arial", 25),
                         text_color="#000000",  # Make sure text contrasts with your image
                         fg_color=chroma_color,
                         width=500,   # <--- FIX
                         height=50,   # <--- FIX
                         anchor="center")

signUpButton = ctk.CTkButton(master=frameLower,
                             text="Log In from here", bg_color=chroma_color,
                             width=150, height=50,
                             font=("Arial", 20, "bold"), command=changeText,)


labelDesc1.grid(row=0, column=0, pady=(100,0), padx=0, sticky="n")
labelDesc2.grid(row=1, column=0, pady=20, padx=0, sticky="n", )
signUpButton.grid(row=2, column=0, pady=20, padx=0, sticky="n")

# 2. Force the label to the top layer
labelDesc1.lift()
labelDesc2.lift()

# 3. Apply the transparency hack to the key color
pywinstyles.set_opacity(labelDesc1, color=chroma_color)
pywinstyles.set_opacity(labelDesc2, color=chroma_color)
pywinstyles.set_opacity(signUpButton, color=chroma_color)


# --- Frame 2: User Detail Input Frame (Right Side Overlay) ---
frameUpper = ctk.CTkFrame(master=frameLower, width=500, height=700, corner_radius=20, fg_color="white")
# Note: I changed sticky to "ne" (North East) and added padx to position it
frameUpper.grid(row=0, column=1, pady=0, sticky="ne", rowspan=3) 
frameUpper.grid_propagate(False)

# --- Frame Internal Grid Config ---
frameLower.grid_columnconfigure(0, weight=1)
frameLower.grid_columnconfigure(1, weight=1)
frameLower.grid_rowconfigure(0, weight=0)
frameLower.grid_rowconfigure(1, weight=1)
frameLower.grid_rowconfigure(2, weight=1)

# --- frameUpper grid making ---
frameUpper.grid_columnconfigure(0, weight=1)
frameUpper.grid_rowconfigure(0, weight=0)
frameUpper.grid_rowconfigure(1, weight=0)
frameUpper.grid_rowconfigure(2, weight=0)
frameUpper.grid_rowconfigure(3, weight=0)
frameUpper.grid_rowconfigure(4, weight=0)
frameUpper.grid_rowconfigure(5, weight=0)
frameUpper.grid_rowconfigure(6, weight=0)
frameUpper.grid_rowconfigure(7, weight=0)
frameUpper.grid_rowconfigure(8, weight=0)
frameUpper.grid_rowconfigure(9, weight=0)
frameUpper.grid_rowconfigure(10, weight=0)


# --- frameUpper Content ---
frameUpperTitle = ctk.CTkLabel(master=frameUpper, 
                          text="Let's Get Started", 
                          font=("Arial", 30, "bold"),
                          text_color="#1B7383",
                          fg_color="transparent")
frameUpperTitle.grid(row=0, column=0, pady=(50, 0), sticky="nw", padx=40)

frameUpperSubTitle = ctk.CTkLabel(master=frameUpper, 
                          text="Sign Up to your account", 
                          font=("Arial", 15, "bold"),
                          text_color="#7C8586",
                          fg_color="transparent")
frameUpperSubTitle.grid(row=1, column=0, pady=(0, 0), sticky="nw", padx=40)

frameUpperUsernameLabel = ctk.CTkLabel(master=frameUpper, 
                          text="Enter Username", 
                          font=("Arial", 15, "bold"),
                          text_color="#1B7383",
                          fg_color="transparent")
frameUpperUsernameLabel.grid(row=2, column=0, pady=(150, 0), sticky="nw", padx=40)

usernameEntry = ctk.CTkEntry(master=frameUpper,
                             width=400,
                             height=40,
                             font=("Arial", 15),
                             fg_color="transparent",
                             corner_radius=10,
                             border_width=2,
                             border_color="#1B7383")
usernameEntry.grid(row=3, column=0, pady=0, sticky="nw", padx=40)

frameUpperPasswordLabel = ctk.CTkLabel(master=frameUpper, 
                          text="Enter Password", 
                          font=("Arial", 15, "bold"),
                          text_color="#1B7383",
                          fg_color="transparent")
frameUpperPasswordLabel.grid(row=4, column=0, pady=(30, 0), sticky="nw", padx=40)

passwordEntry = ctk.CTkEntry(master=frameUpper,
                             width=400,
                             height=40,
                             font=("Arial", 15),
                             fg_color="transparent",
                             corner_radius=10,
                             border_width=2,
                             border_color="#1B7383")
passwordEntry.grid(row=5, column=0, pady=0, sticky="nw", padx=40)

frameUpperConfirmPasswordLabel = ctk.CTkLabel(master=frameUpper, 
                          text="Confirm Password", 
                          font=("Arial", 15, "bold"),
                          text_color="#1B7383",
                          fg_color="transparent")
frameUpperConfirmPasswordLabel.grid(row=6, column=0, pady=(30, 0), sticky="nw", padx=40)

confirmPasswordEntry = ctk.CTkEntry(master=frameUpper,
                             width=400,
                             height=40,
                             font=("Arial", 15),
                             fg_color="transparent",
                             corner_radius=10,
                             border_width=2,
                             border_color="#1B7383")
confirmPasswordEntry.grid(row=7, column=0, pady=0, sticky="nw", padx=40)

loginButton = ctk.CTkButton(master=frameUpper,
                             text="Sign Up",
                             width=300, height=40,
                             font=("Arial", 20, "bold"), command=login)
loginButton.grid(row=8, column=0, pady=(50,0), sticky="n", padx=40)

# -- change the application theme to light --
switch_theme = ctk.StringVar(value="dark")
switch_theme_button = ctk.CTkSwitch(master=app,
                                    text="Change the Theme",
                                    command=lambda: ctk.set_appearance_mode(switch_theme.get()),
                                    variable=switch_theme,
                                    onvalue="dark",
                                    offvalue="light")
switch_theme_button.grid(row=3, column=0, pady=(20,0), sticky="e", padx=40)



# Run the app
app.mainloop()