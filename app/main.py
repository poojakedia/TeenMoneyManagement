import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
import app.teen as teen
import app.dbConnect as dbConnect
import matplotlib.pyplot as plt
import matplotlib, numpy, sys
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
LARGEFONT =("Verdana", 20)
LABELFONT =("Times", 10)

class tkinterApp(tk.Tk):
  # __init__ function for class tkinterApp
  def __init__(self, *args, **kwargs):
    # __init__ function for class Tk
    tk.Tk.__init__(self, *args, **kwargs)
    
    # creating a container
    container = tk.Frame(self)
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    # initializing frames to an empty array
    self.frames = {}

    # iterating through a tuple consisting
    # of the different page layouts
    #for F in (SignUp, SignIn, StartPage):
    for F in(SignUp, StartPage, SignIn, StartPage, AddData, SavingsGoals):

      frame = F(container, self)

      # initializing frame of that object from
      # startpage, page1, page2 respectively with
      # for loop

      self.frames[F] = frame

      frame.grid(row = 0, column = 0, sticky ="nsew")

      self.show_frame(SignUp)
      #self.show_frame(StartPage)
  
  # to display the current frame passed as parameter
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

# first window frame startpage
class StartPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    frame1 = Frame(self, height = 30, width = 400)
    frame1.grid(row = 1, column = 0)
		# label of frame Layout 2
    frame2 = Frame(self, height = 500, width = 400)
    frame2.grid(row = 2, column =0)
    frame3 = Frame(frame2, width = 500, height = 500)
    frame3.grid(row = 2, column = 1)
    label = ttk.Label(frame2, text ="Welcome to Teen's Money Management App", font = LARGEFONT)
    
		# putting the grid in its place by using
		# grid
    label.grid(row = 1, column = 1, padx = 20, pady = 10)
    button1 = ttk.Button(frame1, text ="Logout",
                         command = lambda : controller.show_frame(SignIn))
    button1.grid(row = 1, column = 2, padx = 10, pady = 10)
    button2 = ttk.Button(frame1, text = "Add Data Page", command = lambda : controller.show_frame(AddData))
    button2.grid(row = 1, column = 0, padx = 10, pady = 0)
    button3 = ttk.Button(frame1, text = "Savings Goals Page", command = lambda : controller.show_frame(SavingsGoals))
    button3.grid(row = 1, column = 1, padx = 10, pady = 10)
    btn = tk.Label(frame3, text = "Item Category Graph")
    btn.grid(row = 0, column = 0)
    a = 50
    b = 70
    x = ['Need', 'Want']
    y = [a,b]
    fig = plt.figure(figsize=(2,3))
    plt.bar(x=x, height = y)
    plt.xticks(x, rotation = 90)
    graph_label = tk.Label(frame3, text = 'Budget Graph')
    graph_label.grid(row = 0, column =1)
    canvas = FigureCanvasTkAgg(fig, master = frame3)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 1, column = 0)
    canvas1 = tk.Canvas(frame3, width= 100, height = 200)
    canvas1.grid(column = 1, row = 1)
    figure1 = Figure(figsize = (2,1))
    subplot1 = figure1.add_subplot()
    total_budget = 100
    used_budget = 20
    labels = ['Remaining', 'Used']
    sizes = [(total_budget- used_budget), used_budget]
    subplot1.pie(sizes, labels = labels)
    subplot1.axis('equal')
    pie1 = FigureCanvasTkAgg(figure1, frame3)
    pie1.get_tk_widget().grid(column = 1, row = 1)
    frame4 = Frame(frame3, width = 150, height = 80)
    frame4.grid(column = 2, row = 1)

    

    
    #axes = figure.add_subplot()

        # create the barchart
    '''axes.bar(category, items)
    axes.set_title('Needs/Wants Purchases')
    axes.set_ylabel('Items')
    figure_canvas.get_tk_widget().grid(row =1, column = 1)'''
		## button to show frame 2 with text layout2
		
		# putting the button in its place by
		# using grid
		
# second window frame page1
class SignUp(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    name_var=tk.StringVar()
    doB_var=tk.StringVar()
    email_var=tk.StringVar()
    username_var=tk.StringVar()
    password_var=tk.StringVar()
    cnfPassword_var=tk.StringVar()


    label = ttk.Label(self, text ="Sign Up", font = LARGEFONT)
    label.grid(row = 0, column = 2, padx = 10, pady = 10)
    
    nameLbl = ttk.Label(self, text ="Name", font = LABELFONT)
    nameLbl.grid(row = 1, column = 1, padx = 10, pady = 10)

    nameEntry = ttk.Entry(self, font = LABELFONT)
    nameEntry.grid(row = 1, column = 2, padx = 10, pady = 10)
    name_var = nameEntry.get()
    

    doBLbl = ttk.Label(self, text ="Date of Birth", font = LABELFONT)
    doBLbl.grid(row = 2, column = 1, padx = 10, pady = 10)
    '''
    def handle_focus_in(_):
      doBEntry.delete(0, tk.END)
      doBEntry.config(fg='black')
    
    def handle_focus_out(_):
      doBEntry.delete(0, tk.END)
      doBEntry.config(fg='grey')
      doBEntry.insert(0, "dd/mm/yyyy")

    def handle_enter(txt):
      print(doBEntry.get())
      handle_focus_out('dummy')
    '''
    doBEntry = ttk.Entry(self,textvariable = doB_var, font = LABELFONT)
    doBEntry.grid(row = 2, column = 2, padx = 10, pady = 10)
    '''
    doBEntry.insert(0, "dd/mm/yyyy")

    doBEntry.bind("<FocusIn>", handle_focus_in)
    doBEntry.bind("<FocusOut>", handle_focus_out)
    doBEntry.bind("<Return>", handle_enter)
    '''
    errDoBLbl = ttk.Label(self, text="In dd/mm/yyyy format", font=LABELFONT)
    errDoBLbl.grid(row = 2, column = 3, padx = 10, pady = 10)
    
    emailLbl = ttk.Label(self, text ="Email Id", font = LABELFONT)
    emailLbl.grid(row = 3, column = 1, padx = 10, pady = 10)

    emailEntry = ttk.Entry(self, font = LABELFONT)
    emailEntry.grid(row = 3, column = 2, padx = 10, pady = 10)

    usernameLbl = ttk.Label(self, text ="Username", font = LABELFONT)
    usernameLbl.grid(row = 4, column = 1, padx = 10, pady = 10)

    usernameEntry = ttk.Entry(self, font = LABELFONT)
    usernameEntry.grid(row = 4, column = 2, padx = 10, pady = 10)

    # check availability button
    num = 5
    def my_command():
      if(num >10):
        checkUNABtn.config(image=available2)
        text.config(text="Username available") 
      else:
        checkUNABtn.config(image=notAvailable2)
        text.config(text="Select other Username") 

    #Import the image using PhotoImage function
    check_btn = Image.open('checkAvailability1.png')
    check_btn1 = check_btn.resize((30,30))
    check_btn2= ImageTk.PhotoImage(check_btn1)

    available = Image.open('available.jpg')
    available1 = available.resize((30,30))
    available2= ImageTk.PhotoImage(available1)

    notAvailable = Image.open('notAvailable.jpg')
    notAvailable1 = notAvailable.resize((30,30))
    notAvailable2= ImageTk.PhotoImage(notAvailable1)
    
    #Let us create a label for button event
    #img_label= tk.Label(win, text="Original")

    #Let us create a dummy button and pass the image
    checkUNABtn= ttk.Button(self, image=check_btn2, command= my_command)
    checkUNABtn.grid(row = 4, column = 2, padx = 10, pady = 10)

    text= ttk.Label(self, text= "Check Availability",  font = LABELFONT)
    text.grid(row = 4, column = 3, padx = 10, pady = 10)

    #Password checking

    def cnfPassword(*args):
      password_var = passwordEntry.get()
      cnfPassword_var = cnfPasswordEntry.get()
      
      if(password_var == cnfPassword_var):
        print("Password Matches")
        errPassLbl.config(text="Password Matches")        
      else:
        errPassLbl.config(text="Retype both the passwords")
        #passwordEntry.set("")
        #cnfPasswordEntry.set("")
        passwordEntry.delete(0,'end')
        cnfPasswordEntry.delete(0,'end')

    okayPassword = self.register(cnfPassword)

    passwordLbl = ttk.Label(self, text ="Password", font = LABELFONT)
    passwordLbl.grid(row = 5, column = 1, padx = 10, pady = 10)    

    passwordEntry = ttk.Entry(self, font = LABELFONT, show="*")
    passwordEntry.grid(row = 5, column = 2, padx = 10, pady = 10)

    cnfPasswordLbl = ttk.Label(self, text ="Confirm Password", font = LABELFONT)
    cnfPasswordLbl.grid(row = 6, column = 1, padx = 10, pady = 10)    

    cnfPasswordEntry = ttk.Entry(self, font = LABELFONT, show="*", validate='focusout', validatecommand=(okayPassword,'%W'))
    cnfPasswordEntry.grid(row = 6, column = 2, padx = 10, pady = 10)
    #cnfPasswordEntry.bind("<Key-Return>", cnfPassword)

    errPassLbl = ttk.Label(self, text="Check here")
    errPassLbl.grid(row = 6, column = 3, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2

    def sign_up():
      name = nameEntry.get()
      print(name,"printing" )
      #doB = doB_var.get()
      email = emailEntry.get()
      username= usernameEntry.get()
      password= passwordEntry.get()
      print(name,email,username, password, "printing")
      dbConnect.initDb()
      T1 = teen.Teen(name,email, username, password)
      print(teen.db.view(T1),"dbPart")
      dbConnect.log(T1)
      controller.show_frame(SignIn)
      
    sign_up_btn= ttk.Button(self, text= "Sign Up", command = sign_up)
    sign_up_btn.grid(row=7, column = 2)
         
        # putting the button in its place
        # by using grid

        # button to show frame 2 with text
        # layout2
    button2 = ttk.Button(self, text ="Sign In",
                  command = lambda : controller.show_frame(SignIn))
      
        # putting the button in its place by
        # using grid
    button2.grid(row = 8, column = 2, padx = 10, pady = 10)

   
    

# third window frame page2
class SignIn(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = ttk.Label(self, text ="Sign In", font = LARGEFONT)
    label.grid(row = 0, column = 3, padx = 10, pady = 10)
    username_var=tk.StringVar()
    password_var= tk.StringVar()
		# button to show frame 2 with text
		# layout2
    button1 = ttk.Button(self, text ="Sign up",
							command = lambda : controller.show_frame(SignUp))
	
		# putting the button in its place by
		# using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
    
    # putting the button in its place by
		# using grid
  
    usernameLbl = ttk.Label(self, text = "Username:", font = LABELFONT)
    usernameLbl.grid(row = 2, column= 2, padx = 10, pady = 10)
    
    usernameEntry = ttk.Entry(self, font = LABELFONT)
    usernameEntry.grid(row = 2, column = 3, padx = 10, pady = 10)

    passwordLbl = ttk.Label(self, text = "Password:", font = LABELFONT)
    passwordLbl.grid(row = 3, column = 2, padx = 10, pady =10)

    passwordEntry = ttk.Entry(self, show= "*", font = LABELFONT)
    passwordEntry.grid(row = 3, column = 3, padx = 10, pady = 10)
    errorLbl = ttk.Label(self, font = LABELFONT)
    errorLbl.grid(row = 5, column = 3, padx = 10, pady = 10)
    

    def sign_in():
      username_var = usernameEntry.get()
      password_var = passwordEntry.get()
      db_array= dbConnect.login(username_var, password_var) #fill with value that is fetched based on username from db
      if len(db_array)>0:
        print("continue next page")
        controller.show_frame(StartPage)
      else:
        errorLbl.config(text= "Enter valid username or password")   
    sign_in_button = ttk.Button(self, text = "Sign in", command= sign_in)
    sign_in_button.grid(row = 4, column = 3, padx = 10, pady = 10)

class AddData(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self,parent)
    
    self.columnconfigure(7, weight = 1, pad=7)
    left_side = Frame(self,width=300,height=800)
    left_side.grid(row = 1, column = 1, pady=10,padx=10)
    home_button = ttk.Button(left_side, text = "home", command = lambda: controller.show_frame(StartPage))
    home_button.grid(row = 1, column = 6)
    label = ttk.Label(left_side, text = "Add Data Page", font = LARGEFONT)
    label.grid(row = 1, column = 7, padx = 2, pady = 2)
    w = Scale(left_side, length = 200, from_= 0, to= 40000, orient=HORIZONTAL)
    w.grid(row = 2, column = 7, padx = 10, pady = 10)
    monthly_budget_lbl = ttk.Label(left_side, text = "Monthly Budget", font = LABELFONT)
    monthly_budget_lbl.grid(row = 2, column = 6, padx= 10, pady= 10)
    l = Scale(left_side, length = 200, from_=0, to = 40000, orient= HORIZONTAL)
    l.grid(row = 3, column = 7, padx= 10, pady=10)
    monthly_earning_lbl = ttk.Label(left_side, text = "Monthly Earning", font = LABELFONT)
    monthly_earning_lbl.grid(row = 3, column = 6, padx= 10, pady= 10)
    def show_values():
      print(w.get(), l.get())

    add_exp_label = ttk.Label(left_side, text= "Add Expenditure", font= ("Arial", 10))
    add_exp_label.grid(row =5, column = 6, pady= 10, padx=10)

    item_name_lbl = ttk.Label(left_side, text= "Item Name:", font = LABELFONT)
    item_name_lbl.grid(row = 6, column = 6, pady=10, padx=10)

    item_name_entry = ttk.Entry(left_side, width = 15)
    item_name_entry.grid(row = 6, column = 7, pady =10, padx= 10)
    item_value_lbl = ttk.Label(left_side, text= "Item Value:", font = LABELFONT)
    item_value_lbl.grid(row = 7, column = 6, pady=10, padx=10)

    item_value_entry = ttk.Entry(left_side, width = 15)
    item_value_entry.grid(row = 7, column = 7, pady =10, padx= 10)

    classify_var= StringVar()
    radiobutton_want = tk.Radiobutton(left_side, text= "Want", variable = classify_var, value= "Want")
    radiobutton_want.grid(row = 8, column = 6, pady=10, padx=20)
    radiobutton_need = ttk.Radiobutton(left_side, text= "Need", variable = classify_var, value= "Need")
    radiobutton_need.grid(row = 8, column = 7, pady=10, padx=20)
    self.columnconfigure(9, pad=7)
    side_bar = Frame(self,width=200,height=600)
    side_bar.grid(row = 1, column = 2, pady=10,padx=10)
    #add database values here to calculate costs
    overall_expenditures_label = Label(side_bar, text= "Overall Expenditure", font = LABELFONT)
    overall_expenditures_label.grid(row = 1, column = 1, padx= 10, pady = 10)
    budget_change_label = Label(side_bar, text= "", font = LABELFONT)
    budget_change_label.grid(row = 2, column = 1, padx= 10, pady = 10)
    cal = Calendar(side_bar, selectmode= 'day', year = 2022, month = 6)
    cal.grid(row= 4, column = 1, sticky = tk.NE, padx=10, pady=10)
    future_expenditure_label = Label(side_bar, text = "Upcoming Events:", font= LABELFONT)
    future_expenditure_label.grid(row = 3, column = 1)
    event_description_label = Label(side_bar, text = "Desc.", font = LABELFONT)
    event_description_label.grid(row = 5, column = 1)
    event_des_entry = Entry(side_bar, width = 10)
    event_des_entry.grid(row =5, column = 2, padx = 10, pady = 10)
    value_label = Label(side_bar, text = "$$", font = LABELFONT)
    value_label.grid(row = 6, column = 1)
    value_entry = Entry(side_bar, width = 10)
    value_entry.grid(row =6, column = 2, padx = 10, pady = 10)
    new_budget_value = 10000
    def budget_change():
      budget_change_label.configure(text = new_budget_value)
    def confirm_data():
      monthly_earning = int(l.get())
      monthly_budget = int(w.get())
      item_name = item_name_entry.get()
      item_value = float(item_value_entry.get())
      classify = classify_var.get()
      counter_need = 0
      counter_want = 0
      if classify == 'Need':
        counter_need+= 1
      elif classify == 'Want':
        counter_want+=1
      dbConnect.initDb()
      TD = teen.Data(monthly_budget, monthly_earning, item_name, item_value, classify)
      TD.display()
      dbConnect.DataLog(TD)
      
      '''dbConnect.initDb()
      T1 = teen.Teen(name,email, username, password)
      print(teen.db.view(T1),"dbPart")
      dbConnect.log(T1)
      controller.show_frame(SignIn)'''
    submit_button= ttk.Button(left_side, text= "Confirm", command = confirm_data)
    submit_button.grid(row =9, column = 7, padx =10, pady=10)
a = 20
b = 10
c= 50
d = 20
class SavingsGoals(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    new_frame = Frame(self,width=100,height=100)
    new_frame.grid(row = 1, column = 1, pady=10,padx=10)
    page_title = Label(new_frame, text = "Savings Page", font = LARGEFONT)
    page_title.grid(row = 1, column = 2)
    home_icon = PhotoImage(file = r'home_icon(1).png')
    resized_icon = home_icon.subsample(7, 7)
    
    home_button = Button(new_frame, text = "Home", command = lambda: controller.show_frame(StartPage))
    home_button.grid(row = 1, column = 1)
    slide_label = Label(new_frame, text = "Total Savings", font = LABELFONT)
    slide_label.grid(row =2 , column = 1, pady=5, padx = 10)
    
    l = Scale(new_frame, length = 300, from_=0, to = 10000, orient= HORIZONTAL)
    l.grid(row = 2, column = 2, pady =5, padx = 10)

    value_input_label = Label(new_frame, text = "Value Input", font = LABELFONT)
    value_input_label.grid(row = 3, column = 1, pady = 5, padx = 10)
    value_entry = ttk.Entry(new_frame, width = 30)
    value_entry.grid(row = 3, column = 2, pady =5, padx = 5)
    classify_var= StringVar()
    radiobutton_personal = tk.Radiobutton(new_frame, text= "Personal Savings", variable = classify_var, value= "Personal")
    radiobutton_personal.grid(row = 4, column = 1, pady=10, padx=20)
    radiobutton_investment = ttk.Radiobutton(new_frame, text= "Investment Savings", variable = classify_var, value= "Ivestment")
    radiobutton_investment.grid(row = 4, column = 2, pady=10, padx=20)
    enter_value_button = ttk.Button(new_frame, text = "Add Savings")
    enter_value_button.grid(row = 5, column = 2)
    labels = 'personal', 'investment', 'education', 'family'
    left_frame = Frame(self)
    left_frame.grid(row =1, column = 2)
    savings_sizes = [a, b, c, d]
    #ax1 = plt.subplot()
    canvas1 = tk.Canvas(left_frame, width= 300, height = 10)
    canvas1.grid(column = 1, row = 2)
    figure1 = Figure(figsize = (3,2))
    subplot1 = figure1.add_subplot()
    subplot1.pie(savings_sizes, labels = labels)
    subplot1.axis('equal')
    pie1 = FigureCanvasTkAgg(figure1, left_frame)
    pie1.get_tk_widget().grid(column = 1, row = 3)
    

    




# Driver Code
app = tkinterApp()
app.mainloop()
