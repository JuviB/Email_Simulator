### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Email class is created with constructor and methods to create a new Email object.
class Email:
    
    # Constructor function is created with 'email_address', 'subject_line' and 'email_content' as parameters/ attributes
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content    
        self.has_been_read = False

    # Method is created to call upon when 'self.has_been_read' changed from false ('Unread') to true ('Read')
    def mark_as_read(self):
        self.has_been_read = True

    # Method is created to display an email with the approprotate titles for its inserted attributes 
    def display_email_details(self):
        print(f"From: {self.email_address}")
        print(f"Subject: {self.subject_line}")
        print(f"Content: {self.email_content}")
        
        # 'if and else' statement in order to insert the appropriate email status depending on the 'self.has_been_read' boolean
        print(f"Status: {'Read' if self.has_been_read else 'Unread'}")

# --- Lists --- #
# An empty list is initialised in order to store the email objects.
inbox_list = []

# --- Functions --- #
# Function created to populate inbox with 3 emails and their given attributes
def populate_inbox():
    email1 = Email("jbechoo19@gmail.com", "Shoes", "Tie your shoe laces")
    email2 = Email("nizam@hype.co.za", "Stop", "Stop drinking during the week")
    email3 = Email("pathy@gmail.com", "Hat", "Lend me your hat")
    
    # Append emails and their attributes to the empty inbox list 
    inbox_list.append(email1)
    inbox_list.append(email2)
    inbox_list.append(email3)

# Function created to add an index to each email listed with the corresponding subject line
def list_emails():
    
    for index, email in enumerate(inbox_list):
        subject_line = email.subject_line
        print(f"{index} {subject_line}")


def read_email(index):
    if 0 <= index < len(inbox_list):
        email = inbox_list[index]
        
        # Display email details
        email.display_email_details()
        
        # Set 'has_been_read' to True
        email.mark_as_read()  
        
    else:
        print("You have entered an invalid email index, please try again!")    

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# 'while' loop used to loop through the menu options requesting user input 
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    # 'if, elif, else' statements used to distinguish the various menu options
    # Menu option 1 displays a list of all emails available for the user to choose and read from
    if user_choice == 1:
        print("\nList of emails:")
        
        # 'list_emails()' function used to display the various emails 
        list_emails()
        
        # Requests user to choose email index they wish to read
        index = int(input("Enter the index of the email you want to read: "))
        
        # 'read_email(index)' function is called to display specific email and mark it as read
        read_email(index)

    # Menu option 2 displays a list of unread emails
    elif user_choice == 2:
        
        # Stores unread emails from inbox list in 'unread_emails' list
        unread_emails = [email for email in inbox_list if not email.has_been_read]
        
        # 'if, else' statement used to distinguish 'unread' emails from 'read' emails and prints them
        if not unread_emails:
            print("You have no unread emails.")
            
        else:
            print("\nUnread Emails:")
            
            # Loops through all emails, indexes each unread email and displays the emails subject line
            for index, email in enumerate(unread_emails):
                print(f"{index}: {email.subject_line}")

    # Menu option 3 quits the email application
    elif user_choice == 3:
        print("Exiting email application, goodbye...")
        break
    
    # Error message displayed for invalid menu option
    else:
        print("Oops - incorrect input.")

