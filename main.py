# Automatic Birthday Wisher:

import smtplib as st
import datetime as dt
import pandas as pd


MY_EMAIL = 'anshsoni702@gmail.com'
PASSWORD = 'hnae syae ioqr rney'

# Checking Day and Month from brithday.csv
now = dt.datetime.now()
Month = now.month
Day = now.day


data_file = pd.read_csv('birthday.csv', encoding='utf-8')
dic = data_file.to_dict(orient='records')

for items in dic:
    if (items['month'] == Month and items['day'] == Day):
        name = items['name']
        email = items['email']
        
        with open('format.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            updated_content = content.replace('[Name]', name)
            message = f'Subject:HAPPY BIRTHDAY\n\n{updated_content}'
            
        with st.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            encoded_string = message.encode('utf-8')
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=email, msg=encoded_string)