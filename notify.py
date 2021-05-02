import os
import json
import requests
from os.path import join, dirname
from dotenv import load_dotenv
import smtplib

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Notification:
    ''' Method will be used to send the notification on the Slack,
        Google Chat, email or all three
    '''

    slack_url = os.getenv('SLACK_WEBHOOK')
    gchat_url = os.getenv('GCHAT_WEBHOOK')

    def trigger_notification(self, url, message):
        """Method is used to trigger the webhook based notification"""
        # Trigger the webhook
        response = requests.post(
            url,
            data=json.dumps(message),
            headers={'Content-Type': 'application/json'}
        )

    def _post_slack_message(self, text):
        """Slack Webhook"""
        message = {
            'text': text,
            'mrkdwn': True
        }

        self.trigger_notification(self.slack_url, message)

    def _post_gchat_message(self, text):
        """Hangouts Chat incoming webhook"""
        message = {
            'text': text
        }
        self.trigger_notification(self.gchat_url, message)

    def _send_email(self, message):
        """ Method to send email """
        # Email of the receiver
        TO = os.getenv('EMAIL')
        # Subject of the Email
        SUBJECT = os.getenv('SUBJECT')
        # Message need to be sent
        TEXT = message

        # Env's needed for sending email
        SENDER_EMAIL = os.getenv('SENDER_EMAIL')
        SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')
        SMTP_SERVER = os.getenv('SMTP_SERVER')
        SMTP_PORT = os.getenv('SMTP_PORT')

        # Server configuration for sending email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % SENDER_EMAIL,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])

        try:
            server.sendmail(SENDER_EMAIL, [TO], BODY)
            print ('email sent')
        except Exception as e:
            print ('error sending mail', str(e))
        server.quit()

    def get_notification_channel_and_send(self, message):
        """ Method to check the notification channel and trigger
            notifications
        """
        notification_channel = os.getenv('NOTIFICATION_CHANNEL')
        if notification_channel:
            channels = notification_channel.lower().split(',')
            try:
                if 'slack' in channels:
                    self._post_slack_message(message)
                if 'gchat' in channels:
                    self._post_gchat_message(message)
                if 'email' in channels and os.getenv('SMTP_SERVER'):
                    self._send_email(message)
            except:
                pass

