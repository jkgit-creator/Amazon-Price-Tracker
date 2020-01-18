import smtplib

def send_mail(URL, title):
    """
    Sends an email stating that the product is below target price. Provides a link to the page.

    Parameters: 
        URL: a url link
        title(string): the title of the product  
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #make sure to insert email addresses and create a gmail app password
    server.login('sender@gmail.com', 'sender gmail app password')
    subject = f"Your desired {title} is below your target price!"
    body = 'Check the amazon link ' + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender@gmail.com',
        'reciever@gmail.com',
        msg
    )
    print('Email Sent')
    server.quit()