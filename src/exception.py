import sys # maniulate different path of python environment 
import logger
from logger import logging

def error_message_detail(error, error_details:sys): #error details will be present under sys
    _,_,exc_tb = error_details.exc_info() # give details about where the exception has occured 
    file_name = exc_tb.tb_frame.f_code.co_filename #  from exception handeling db, custome exception handeling ## search custom exception handeling
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #inhereting the error from exception class 
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
    
    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a =1/0
#         print(1)
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e, sys)