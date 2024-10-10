# File: 02_Data_Cleaning/scripts/db_utils.py

import pandas as pd
import yaml
from sqlalchemy import create_engine

def load_db_credentials(file_path='C:/Users/user/Documents/AiCore/Projects/Finance_Project/credentials.yaml'):
    """
    Load database credentials from a YAML file.
    
    Parameters:
        file_path (str): The file path of the credentials.yaml file.
        
    Returns:
        dict: A dictionary containing the database credentials.
    """
    try:
        with open(file_path, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    except FileNotFoundError:
        raise Exception(f"Credentials file not found at {file_path}. Please ensure the file exists.")
    except yaml.YAMLError as e:
        raise Exception(f"Error reading the YAML file: {e}")

class RDSDatabaseConnector:
    """
    A class to manage connection and data extraction from the RDS database.
    """

    def __init__(self, credentials):
        """
        Initialize the database connector with the given credentials.
        
        Parameters:
            credentials (dict): A dictionary containing the database credentials.
        """
        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT')

        # Validate that all required credentials are provided
        if not all([self.host, self.user, self.password, self.database, self.port]):
            raise ValueError("Missing one or more required database credentials.")
        
        # Placeholder for the database connection (will be set when connecting)
        self.connection = None

    def initialize_engine(self):
        """
        Initialize a SQLAlchemy engine using the provided database credentials.
        
        Returns:
            engine (sqlalchemy.engine.Engine): A SQLAlchemy engine for connecting to the RDS database.
        """
        try:
            # Create the connection string
            connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            # Initialize the SQLAlchemy engine
            engine = create_engine(connection_string)
            return engine
        except Exception as e:
            raise Exception(f"Failed to initialize SQLAlchemy engine: {e}")

    def extract_data_as_dataframe(self, table_name='loan_payments'):
        """
        Extract data from the specified table in the RDS database and return it as a Pandas DataFrame.
        
        Parameters:
            table_name (str): The name of the table to query. Defaults to 'loan_payments'.
        
        Returns:
            pd.DataFrame: A DataFrame containing the data from the specified table.
        """
        try:
            # Initialize the engine
            engine = self.initialize_engine()
            
            # Use Pandas to execute a SQL query and fetch the data
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, engine)
            
            # Close the engine connection
            engine.dispose()
            
            return df
        except Exception as e:
            raise Exception(f"Failed to extract data from the database: {e}")

    def save_data_to_csv(self, df, file_path):
        """
        Save the given DataFrame to a .csv file at the specified file path.
        
        Parameters:
            df (pd.DataFrame): The DataFrame to save.
            file_path (str): The path where the .csv file will be saved.
        """
        try:
            df.to_csv(file_path, index=False)
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            raise Exception(f"Failed to save data to CSV: {e}")
