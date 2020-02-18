import logging 


class HoneyPot(object):
    def __init__(self,ports,log_filepath):
        if len(ports)<1:
            raise Exception('No ports provided')
        logging.basicConfig(level = logging.DEBUG,
                           format ='%(asctime)s %(levelname)-8s %(message)s',
                           datefmt='%Y-%m-%d %H:%M:%s',
                           filename = log_filepath,
                           filemode = 'w')

        self.logger  = logging.getLogger(__name__)
        self.logger.info('Test!')
 