import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_format = logging.Formatter('%(levelname)s: %(name)s: %(asctime)s: %(message)s')

file_handler = logging.FileHandler('OT_process.log')

file_handler.setFormatter(log_format)

logger.addHandler(file_handler)
logger.info('Running {}'.format(__name__))

def merge_data(cpm_data_frame, cpms_data_frame):
    """
        Pass CPM and CPMS processed dataframe to stich the overtime data together. Note this method can be used to append any two dataframes as long as the columns match
    """
    if not (isinstance(cpm_data_frame, pd.DataFrame) and isinstance(cpms_data_frame, pd.DataFrame)):
        logger.info('One or more of the arguments are not valid Data Frame objects. Please provide pandas dataframe objects')
    
    else:
        df1 = cpm_data_frame
        df2 = cpms_data_frame

        if list(df1).sort() == list(df2.sort):
            logger.info('Data columns match. Proceeding to compile data together')
            
            try:
                df = pd.concat([df1,df2])
                logger.info('Data successfully reconciled')

                return df

            except Exception as e:
                logger.exception('Something went wrong during re-concilation. Exception; {}'.format(e))
        
        else:
            logger.info('Columns: {} are mismatched'.format(list(set(list(df1)) - set(list(df2)))))
            return None

