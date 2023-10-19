import dotenv
import requests
from splunklib import client as client
import os
from typing import List, Dict, Optional
dotenv.load_dotenv()
class SplunkConnection:
    HOST=''
    PORT=''
    USERNAME=''
    PASSWORD=''
    BEARER_TOKEN=''
    
    def __init__(self) -> None:
       
        self.HOST=os.getenv('HOST','')
        self.PORT=os.getenv('PORT','')
        self.USERNAME=os.getenv('USERNAME','')
        self.PASSWORD=os.getenv('PASSWORD','')
        self.BEARER_TOKEN=os.getenv('BEARER_TOKEN','')

    def create_bearer_token(self,username,password):
        url=''
    def create_session_key(self):
        pass
    def get_bearer_token(self):
        pass
    def get_session_key(self):
        pass
    def connect(self, username: str, password: str, host: Optional[str | None]=None,
                port: Optional[int | None]=None, token_authentication: bool=False,
                session_authentication: bool=False):
        # Create a Service instance and log in 
        """Method to make connection to splunk

        Args:
            username (str): Username required parameter
            password (str): Password required parameter
            host (Optional[str  |  None], optional): host of splunk Defaults to None.
            port (Optional[int  |  None], optional): port on which to make connection. Defaults to None.
            token_authentication (bool, optional): if true use brearer token for authentication. Defaults to False.
            session_authentication (bool, optional): if true use session key for authentication. Defaults to False.

        return:
          service:service 
        """        
        if token_authentication:
            bearer_token=self.get_bearer_token()
            service = client.connect(
                        host=host,
                        port=port,
                        splunkToken=self.BEARER_TOKEN)
        elif session_authentication:
            session_key=self.get_session_key()
            service = client.connect(
                        host=host,
                        port=port,
                        token=session_key)
        else:                
            service = client.connect(
                host=host,
                port=port,
                username=username,
                password=password)

sc = SplunkConnection()
sc.connect(username='admin', password='admin123', token_authentication=True)

