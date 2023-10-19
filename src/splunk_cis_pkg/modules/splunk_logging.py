class SplunkLogger():
    def __init__(self) -> None:
        pass
    def send_log_to_splunk(self,log_data):
        """
        The function `send_log_to_splunk` sends log data to Splunk for storage in a specified index.
        
        :param log_data: The `log_data` parameter is the actual log message or data that you want to
        send to Splunk. It can be a string or any other data type that represents the log information
        you want to store
        """
        try:
            log_msg = "THis is a log meaasge"
            # Choose the index where you want to store the log data
            index_name = 'my_index'

            # Create an event and write the log data to it
            index = service.indexes[index_name]
            print('Index created')
            event = index.attach(host=self.HOST, source='/Users/blackhat/programs/python-project/demo/logs.log/', sourcetype='app-logs')
            print('event created')
            event.write(log_data)
            print('Message written')
            event.close()
        except Exception as e:
            print("Error in sending log to splunk")
            print(e)
    def search_indexes(self):
        if not self.SERVICE:
            print('services is None')
            self.connnect_to_splunk()
        # Define the search query
        search_query = "search index='my_index'"

        # Execute the search
        try:
            service_job = service.jobs.create(search_query)
            return service_job
        except Exception as e:
            print('Error  searching in index:',e)

        # Retrieve the search results
        return None