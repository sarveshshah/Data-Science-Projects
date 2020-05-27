import pyodbc
import logging
import pandas as pd
import os
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_format = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

file_handler = logging.FileHandler('OT_process.log')
file_handler.setFormatter(log_format)

logger.addHandler(file_handler)

def get_data_from_database(database, query):
    """
        database: str, query: str\n
        Get data from CPM,CPMS. Accepts database name as CPM, CPMS and query for the database. Returns the output as a dataframe.
    """
    cpm_conn_string = get_query('./CPM Conn String.txt')
    cpms_conn_string = get_query('./CPMS Conn String.txt')

    if database == 'CPM':
        conn = pyodbc.connect(cpm_conn_string
                )

    elif database == 'CPMS':
        conn = pyodbc.connect(
            
        )

    logger.info('Processing {} Query'.format(database))

    try:
        df = pd.read_sql(query,conn)
        logger.info('{} Query Processed'.format(database))

        return df

    except Exception as e:
        logger.exception('Something went wrong with the query execution. Exception: {}'.format(e))
        logger.error("Error Occured")


def export_data(data_frame,filename,output_format='CSV',path='./'):
    """
        data_frame: pandas.data_frame, filename: str
        Pass the dataframe that you want to export. Accepts 'CSV', and 'XLS' as the output format. WARNING: Existing file will be overwritter. 
        By default outputs a CSV in the same directory. Default filename 'file'.<extension>
        \nFormat Codes:
            \n\tCSV: Comma Separated Value File: overtime.csv
            \n\tXLS: Excel File: overtime.xlsx
        Default filename: "overtime", unless specified in path argument
    """
    if isinstance(data_frame, pd.DataFrame):
        print("WARNING: Existing file will be overwritter")

        if output_format == 'CSV':
            logger.info('Output Format Recognized as {}. Outputting Data'.format(output_format))
            data_frame.to_csv('{}-{}.csv'.format(path+filename,datetime.now().strftime('%c')))
            logger.info('Ouput Complete')

        elif output_format == 'XLS':
            logger.info('Output Format Recognized as {}. Outputting Data'.format(output_format))
            data_frame.to_excel('{}-{}.xlsx'.format(path+filename,datetime.now().strftime('%c')))
            logger.info('Ouput Complete')

        else:
            logger.error('Unknown Output Format provided. Outputting Data as CSV')
            logger.info('Output Format Recognized as {}. Outputting Data'.format(output_format))
            data_frame.to_csv('{}-{}.csv'.format(path+filename,datetime.now().strftime('%c')))
            logger.info('Ouput Complete')

    else:
        logger.error("Unknown format provided, please provide a pandas dataframe")
        logger.error("Error Occured")


def get_query(filepath):
    """Returns the query as a str from filesystem"""
    with open(filepath ,'r') as myfile:
        return myfile.read()

def get_data_from_file(filename,filepath='./'):
    """ 
        Retreive a file from file system. Default path is set to filepath of data_functions.
        Use 'filepath' to retrieve a file. Accepts <file_name>.<extenstion> as input. Supports reading from CSV, Excel files.
        Returns a pandas dataframe object.
    """
    try:
        if filename.split('.')[-1].lower() == 'csv':
            logger.info('Data successfully loaded.')
            return pd.read_csv(filepath+filename)

        elif filename.split('.')[-1].lower() == 'xlsx':
            logger.info('Data successfully loaded.')
            return pd.read_excel(filepath+filename)

        else:
            logger.error("Unknown format provided, please provide a .csv or .xlsx")
    
    except Exception as e:
            logger.exception("Something went wrong. Exception: {}".format(e))
            logger.error("Error Occured")


