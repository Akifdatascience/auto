#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import smtplib
import streamlit as st

def send_email(sender_email, sender_password, receiver_email, subject, body):
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

def process_excel_file(file):
    data = pd.read_excel(file)

    # Sender's email and password
    sender_email = "akifdatascience@gmail.com"
    sender_password = "byvoviuolhuwdrcl"

    # Iterate over rows and send reminder emails for unpaid invoices
    for index, row in data.iterrows():
        recipient = row["Email"]
        paid = row["Paid"]
        amount = row["Amount"]
        invoice_number = row["Invoice Number"]

        if paid == "No":
            subject = "Payment Reminder"
            body = f"Dear {row['Name']},\n\nThis is a reminder that your invoice ({invoice_number}) with an amount of {amount} is still unpaid. Please submit your payment at your earliest convenience.\n\nThank you!\nSender"

            send_email(sender_email, sender_password, recipient, subject, body)
            st.write(f"Payment reminder sent to {recipient}")

# Streamlit web app code
def main():
    st.title("Invoice Reminder")

    # File uploader
    file = st.file_uploader("Upload your Excel file", type=["xlsx"])

    if file is not None:
        st.write("Processing file...")
        process_excel_file(file)
        st.success("Invoice reminder emails sent!")

if __name__ == "__main__":
    main()

