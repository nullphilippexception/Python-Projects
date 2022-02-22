from tkinter import *
import smtplib
import ssl
from email.message import EmailMessage

# set tkinter window up
window = Tk()
window.title("E-Mail Sender")
window.geometry("700x240")

# create all the labels needed to describe the entryboxes
lbl_sender_name = Label(text="Sender Address:")
lbl_sender_pw = Label(text="Password:")
lbl_receiver_name = Label(text="Receiver Address:")
lbl_mail_subject = Label(text="Subject of E-Mail:")
lbl_mail_text = Label(text="Text of E-Mail:")
lbl_server_name = Label(text="Server:")
lbl_port = Label(text="Port:")

# place all labels on the window
lbl_sender_name.place(x=50, y=20, width=100, height=25)
lbl_sender_pw.place(x=50, y=50, width=100, height=25)
lbl_receiver_name.place(x=50, y=80, width=100, height=25)
lbl_mail_subject.place(x=50, y=110, width=100, height=25)
lbl_mail_text.place(x=50, y=140, width=100, height=25)
lbl_server_name.place(x=160, y=170, width=50, height=25)
lbl_port.place(x=400, y=170, width=50, height=25)

# create the entry boxes that will be filled with the user's data
eb_sender_name = Entry()
eb_sender_pw = Entry(show="*")  # to avoid showing password on screen
eb_receiver_name = Entry()
eb_mail_subject = Entry()
eb_mail_text = Entry()
eb_server_name = Entry()  # e.g. smtp.gmail.com
eb_port = Entry()  # e.g. 465

# place entry boxes on screen
eb_sender_name.place(x=160, y=20, width=500, height=25)
eb_sender_pw.place(x=160, y=50, width=500, height=25)
eb_receiver_name.place(x=160, y=80, width=500, height=25)
eb_mail_subject.place(x=160, y=110, width=500, height=25)
eb_mail_text.place(x=160, y=140, width=500, height=25)
eb_server_name.place(x=220, y=170, width=150, height=25)
eb_port.place(x=460, y=170, width=50, height=25)

# method that contains the actual functionality
# is called when "Send" button is pressed
# fetches data from entry boxes, connects to email server via smtp and sends email
def send_mail():
    # fetch core mail data and create message object
    message = EmailMessage()
    sender_name = eb_sender_name.get()
    message["From"] = sender_name
    receiver_name = eb_receiver_name.get()
    message["To"] = receiver_name
    message["Subject"] = eb_mail_subject.get()
    message.set_content(eb_mail_text.get())

    # fetch additional required data for transmission, establish connection and send mail
    context = ssl.create_default_context()
    server_name = eb_server_name.get()
    port = eb_port.get()
    with smtplib.SMTP_SSL(server_name, int(port), context=context) as server:
        sender_pw = eb_sender_pw.get()
        server.login(sender_name, sender_pw)
        server.sendmail(sender_name, receiver_name, message.as_string())

# button that initiates the sending functionality if pressed
btn_send_mail = Button(text="Send", command=send_mail)
btn_send_mail.place(x=160, y=200, width=500, height=25)

# execute tkinter window
window.mainloop()