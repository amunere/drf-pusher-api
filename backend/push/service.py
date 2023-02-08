import os
import requests
import logging
from datetime import datetime
from django.utils.timezone import get_current_timezone
from api.models import Maillist, Message, Client
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
handler = logging.FileHandler('applog.log')
handler.setLevel(logging.DEBUG)
format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(format)
logger.addHandler(handler)

DATATIME_FORMAT = os.getenv('DATETIME_FORMAT')
API_TOKEN = os.getenv('API_TOKEN')

def push_message(message_id, phone, text):
    """
    Sending a message via external API.
    """
    if API_TOKEN is None:  
        logger.critical('Missing environment variables!')
        raise RuntimeError('Missing environment variables!')

    headers = {'Authorization': f'Bearer {API_TOKEN}', 'Content-type': 'application/json'}
    payload = {'id': message_id, 'phone': str(phone), 'text': text}
    try:
        response = requests.post(f'https://probe.fbrq.cloud/v1/send/{message_id}', json=payload, headers=headers)
        logger.info(f'Message sent for {phone}')
        if response.status_code == 200:
            logger.info('Statis code: 200')
            Message.objects.create(
                date = datetime.now(tz=get_current_timezone()).strftime(DATATIME_FORMAT),
                status = True,
                maillist = Maillist.objects.get(id=message_id),
                client = Client.objects.get(phone_number=phone)
            )
        else:
            return response.status_code
    except Exception as error:
        logger.error(f'Failed to send message: {error}')
        return False

def check_datetime(start, end):
    """
    Check Start and End dates.
    """
    current_datetime = datetime.now(tz=get_current_timezone()).strftime('%Y-%m-%d %H:%M')
    if (str(start) <= str(current_datetime) and str(end) >= str(current_datetime)):
        return True
    else:
        return False

def check_mailing_send(mailling_id):
    """
    Check sending maillist.
    """
    messages = Message.objects.filter(maillist=mailling_id)
    if not messages:
        return True
    else:
        for message in messages:
            if message.maillist.id != mailling_id:                
                return True
            else:
                return False

def set_message(message_id, phone):
    """
    Set status False if mailling don't send and not send anyway
    """
    try:
        if check_mailing_send(mailling_id=message_id):
            Message.objects.create(
                date = datetime.now(tz=get_current_timezone()).strftime(DATATIME_FORMAT),
                status = False,
                maillist = Maillist.objects.get(id=message_id),
                client = Client.objects.get(phone_number=phone)
            )
    except Exception as error:
        logger.error(f'Failed set message: {error}')
        return False