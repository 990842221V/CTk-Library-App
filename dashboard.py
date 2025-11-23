# dashboard.py
import customtkinter as ctk

def center_window(window, width, height):
    # 1. Get the user's screen resolution
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 2. Calculate the X and Y coordinates to center the window
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    # 3. Apply the geometry
    window.geometry(f"{width}x{height}+{x}+{y}")

class Dashboard(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        center_window(self, 1100, 900)
        self.title("Library Dashboard")

        # content Begining
        
        # --- Main Layout Configuration (2 Columns) ---
        # Column 0: Navigation (Fixed width)
        # Column 1: Main Content (Expands)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ================= LEFT SIDE: NAVIGATION FRAME =================
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0, width=200, fg_color="gray20")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configure row weights to push logout button to the bottom
        self.navigation_frame.grid_rowconfigure(7, weight=1) 

        # --- Navigation Title ---
        self.nav_label = ctk.CTkLabel(self.navigation_frame, text="  Library System", 
                                      font=ctk.CTkFont(size=20, weight="bold"))
        self.nav_label.grid(row=0, column=0, padx=20, pady=20)

        # --- Navigation Buttons ---
        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                         text="Home",
                                         fg_color="transparent", text_color=("gray10", "gray90"), 
                                         hover_color=("gray70", "gray30"),
                                         anchor="w", command=lambda: self.select_frame("home"))
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.books_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                          text="Manage Books",
                                          fg_color="transparent", text_color=("gray10", "gray90"), 
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=lambda: self.select_frame("books"))
        self.books_button.grid(row=2, column=0, sticky="ew")

        self.users_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                          text="Manage Users",
                                          fg_color="transparent", text_color=("gray10", "gray90"), 
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=lambda: self.select_frame("users"))
        self.users_button.grid(row=3, column=0, sticky="ew")

        self.issue_returns_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                          text="Issue & Returns ",
                                          fg_color="transparent", text_color=("gray10", "gray90"), 
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=lambda: self.select_frame("issue_returns"))
        self.issue_returns_button.grid(row=4, column=0, sticky="ew")

        self.reports_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                          text="Reports",
                                          fg_color="transparent", text_color=("gray10", "gray90"), 
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=lambda: self.select_frame("reports"))
        self.reports_button.grid(row=5, column=0, sticky="ew")

        self.settings_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                          text="Settings",
                                          fg_color="transparent", text_color=("gray10", "gray90"), 
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=lambda: self.select_frame("settings"))
        self.settings_button.grid(row=6, column=0, sticky="ew")
        
        # --- Logout Button (Bottom) ---
        self.logout_btn = ctk.CTkButton(self.navigation_frame, text="Log Out", 
                                        fg_color="transparent", border_width=2,
                                        text_color=("gray10", "gray90"), 
                                        command=lambda: [self.destroy(), parent.deiconify()])
        self.logout_btn.grid(row=8, column=0, padx=20, pady=20, sticky="s")


        # ================= RIGHT SIDE: MAIN CONTENT CONTAINER =================
        self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_content.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        
        # Make the frames inside expandable
        self.main_content.grid_columnconfigure(0, weight=1)
        self.main_content.grid_rowconfigure(0, weight=1)

        # --- CREATE THE DIFFERENT PAGE FRAMES ---
        # We create them all now, but we only show one at a time.
        
        # 1. Home Frame
        self.home_frame = ctk.CTkFrame(self.main_content, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.home_frame, text="Dashboard Home", font=("Arial", 30)).pack(pady=20)
        ctk.CTkLabel(self.home_frame, text="Overview of library stats...").pack()

        # 2. Books Frame
        self.books_frame = ctk.CTkFrame(self.main_content, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.books_frame, text="Book Inventory", font=("Arial", 30)).pack(pady=20)
        ctk.CTkButton(self.books_frame, text="+ Add New Book").pack(pady=10)

        # 3. Users Frame
        self.users_frame = ctk.CTkFrame(self.main_content, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.users_frame, text="User Management", font=("Arial", 30)).pack(pady=20)
        ctk.CTkCheckBox(self.users_frame, text="Show Active Users Only").pack()

        # 4. Issue & Returns Frame
        self.issue_returns_frame = ctk.CTkFrame(self.main_content, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.issue_returns_frame, text="Issue & Returns", font=("Arial", 30)).pack(pady=20)
        ctk.CTkButton(self.issue_returns_frame, text="Issue New Book").pack(pady=10)

        # 5. Reports Frame
        self.reports_frame = ctk.CTkFrame(self.main_content, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.reports_frame, text="Reports", font=("Arial", 30)).pack(pady=20)
        ctk.CTkButton(self.reports_frame, text="Generate Report").pack(pady=10)

        # 6. Settings Frame
        self.settings_frame = ctk.CTkFrame(self.main_content, corner_radius=0, fg_color="transparent")
        ctk.CTkLabel(self.settings_frame, text="Settings", font=("Arial", 30)).pack(pady=20)
        ctk.CTkCheckBox(self.settings_frame, text="Enable Notifications").pack()

        # Select default frame
        self.select_frame("home")

        # content Ending
        
        # When Dashboard closes, end the whole app
        self.protocol("WM_DELETE_WINDOW", lambda: parent.destroy())

    # --- FUNCTION TO SWITCH TABS ---
    def select_frame(self, name):
        # 1. Reset all buttons to transparent (inactive look)
        self.home_button.configure(fg_color="transparent")
        self.books_button.configure(fg_color="transparent")
        self.users_button.configure(fg_color="transparent")
        self.issue_returns_button.configure(fg_color="transparent")
        self.reports_button.configure(fg_color="transparent")
        self.settings_button.configure(fg_color="transparent")

        # 2. Hide all frames
        self.home_frame.grid_forget()
        self.books_frame.grid_forget()
        self.users_frame.grid_forget()
        self.issue_returns_frame.grid_forget()
        self.reports_frame.grid_forget()
        self.settings_frame.grid_forget()

        # 3. Show the selected frame and highlight button
        if name == "home":
            self.home_frame.grid(row=0, column=0, sticky="nsew")
            self.home_button.configure(fg_color=("gray75", "gray25"))
        elif name == "books":
            self.books_frame.grid(row=0, column=0, sticky="nsew")
            self.books_button.configure(fg_color=("gray75", "gray25"))
        elif name == "users":
            self.users_frame.grid(row=0, column=0, sticky="nsew")
            self.users_button.configure(fg_color=("gray75", "gray25"))
        elif name == "issue_returns":
            self.issue_returns_frame.grid(row=0, column=0, sticky="nsew")
            self.issue_returns_button.configure(fg_color=("gray75", "gray25"))
        elif name == "reports":
            self.reports_frame.grid(row=0, column=0, sticky="nsew")
            self.reports_button.configure(fg_color=("gray75", "gray25"))
        elif name == "settings":
            self.settings_frame.grid(row=0, column=0, sticky="nsew")
            self.settings_button.configure(fg_color=("gray75", "gray25"))