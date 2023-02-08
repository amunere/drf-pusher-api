from api.models import Maillist
from celery import shared_task
from .service import check_datetime, check_mailing_send, push_message, logger, set_message
@shared_task()
def pusher():
    """
    Pusher 
    """
    logger.info('-----------------')    
    while True:
        if Maillist.objects.count() > 0:
            try:
                logger.info('Start sending')  
                for maillist in Maillist.objects.all(): 
                    if (check_datetime(maillist.start, maillist.end) and check_mailing_send(maillist.id)):                     
                        push_message(maillist.id, maillist.phone, maillist.text)
                        logger.info(f'Send message for maillist: {maillist.id}, for client: {maillist.phone}, with text: {maillist.text}')  
                    else:
                        set_message(maillist.id, maillist.phone)
                        logger.info(f'This maillist ID: {maillist.id} Done! OR already late date')            
                logger.info('End of sending')
                logger.info('-----------------')
                return False
            except Exception as error:
                logger.error(f'Program crash: {error}')
                logger.info('-----------------')
                return False
        else:
            logger.info('Maillist is empty')
            return False