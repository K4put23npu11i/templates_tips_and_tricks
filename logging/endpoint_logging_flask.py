from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)

# Global Variables for endpoint logging
LOGGING_DIC = {}
LOGGING_LEVEL = "DEBUG"
assert LOGGING_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], "LOGGING_LEVEL not in defined list"


@app.route('/logging')
def root():
    """
    Creates output html string from global variable LOGGING_DIC when endpoint is called

    Returns
    -------
    output: str,
        html string which is diplayed at the endpoint
    """
    output = ""
    ordered_dic = sorted(LOGGING_DIC)
    for key in ordered_dic:
        value = LOGGING_DIC[key]
        line = "<p>" + str(key) + ":  " + str(value) + "</p>"
        output += line
    return output


# test endpoint to create some logging messages
@app.route('/test')
def test():
    for index in range(0, 3):
        time.sleep(2)
        log_to_endpoint("DEBUG", "TEST " + str(index))
        time.sleep(2)
        log_to_endpoint("INFO", "TEST " + str(index))
        time.sleep(2)
        log_to_endpoint("WARNING", "TEST " + str(index))
        time.sleep(2)
        log_to_endpoint("ERROR", "TEST " + str(index))
        time.sleep(2)
        log_to_endpoint("CRITICAL", "TEST " + str(index))
        time.sleep(2)
        log_to_endpoint("blablabla", "TEST " + str(index))
        print(LOGGING_DIC)

    return "DONE"


def log_to_endpoint(level: str, message: str):
    """
    Function to include the incoming message in the global variable LOGGING_DIC when level is over global level.
    Checks the length and pops the oldest entry when dictionary gets too long

    Parameters
    ----------
    level: str,
        indicates the level of the message, should all be uppercase
    message: str,
        log messages
    """
    timestamp = datetime.now().strftime("%D, %H:%M:%S")

    # Include message when level is valid
    if check_level(level.upper()) is True:
        LOGGING_DIC[timestamp] = level.upper() + ' - ' + message

    # Pops oldest entry when dictionary gets too long
    keys = sorted(LOGGING_DIC)
    if len(keys) > 1000:
        LOGGING_DIC.pop(keys[0])

    return 1


def check_level(level: str) -> bool:
    """
    Checks the given level and decides if the message will be included in log endpoint or not due to the global variable
    LOGGING_LEVEL

    Parameters
    ----------
    level: str,
        string which indicates the level of the log message

    Returns
    -------
    valid: bool,
        true/false to indicate if the message should be included in existing log

    """
    lookup = {
        "DEBUG": 10,
        "INFO": 20,
        "WARNING": 30,
        "ERROR": 40,
        "CRITICAL": 50
    }
    level_value = lookup.get(level)

    assert LOGGING_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], "LOGGING_LEVEL not in defined list"
    logging_value = lookup.get(LOGGING_LEVEL)

    if str(type(level_value)) == "<class 'NoneType'>":
        valid = False
    elif level_value >= logging_value:
        valid = True
    else:
        valid = False

    return valid


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
