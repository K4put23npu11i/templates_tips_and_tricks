import pandas as pd
import json
import requests

# Configure logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(funcName)s: %(message)s")

# Measure running time:
start_time = datetime.now()
logger.info('Script started successfully!')


def send_request(url):
    api_call_start_time = datetime.now()
    header = {"Accept": "application/json"}
    r = requests.get(base_url, header)
    if r.status_code == 200:
        content_bytes = r.content
        content_json = json.loads(content_bytes.decode('utf8'))
        
        api_call_end_time = datetime.now()
        logging.debug("API call duration: {}".format(api_call_end_time - api_call_start_time))
        return content_json
    else:
        logging.error("Status Code != 200. Request failed")
        return None


amount = 1
loop = 1
base_url = f"https://my.api.mockaroo.com/sample_data/{amount}.json?key=51144890"

response = send_request(base_url)

if response is not None:
    logging.debug("Create DataFrame")
    keys = list(response[0].keys())
    df = pd.DataFrame(columns=keys)
    
    logging.debug("Fill DataFrame with rows")
    for i in range(0, len(response)):
        df = df.append(response[i], ignore_index=True)

    if 1 < loop < 150:
        logging.info("More than one call is needed. Start looping")
        for call_counter in range(1, loop):
            m = f"{call_counter} of {loop} calls to mockaroo are done. {loop-call_counter} are pending"
            logging.debug(f"{call_counter} of {loop} calls to mockaroo are done. {loop-call_counter} are pending")
            
            response = send_request(base_url)

            if response is not None:
                for i in range(0, len(response)):
                    df = df.append(response[i], ignore_index=True)

else:
    logging.error("Request failed. Script will break here")
    df = pd.DataFrame()

# Measure running time:
end_time = datetime.now()
logger.info('End of Script!')
logger.debug('Runtime of script: {}'.format(end_time - start_time))
