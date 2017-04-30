import logging
import settings 

def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename="HDV_database.log", level=logging.INFO)
    logging.info("Program started")
    
 
if __name__ == "__main__":
    main()
