from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_registration_email_to_Student(email, password):
    EMAIL_HOST_USER = "singhnischal355@gmail.com"
    send_mail(
        "Welcome!",
        f"Thank you, you have been successfully registered!\n\nUsername: {email}\nPassword: {password}",
        EMAIL_HOST_USER,  # This is the 'from_email'
        [email],  # This is the 'recipient_list'
          # Optional argument, set to False if you want to raise errors
    )
