import logging
import os
import time
logger = logging.getLogger()


def await_user_input(message: str, allowed_answers: list = None) -> str:
    """
    Print message and wait for user input. Checks the input if allowed answers are specified.

    Parameters
    ----------
    message: str
        string that will be printed as question for user input
    allowed_answers: list
        list of allowed answers. Input will not be checked if not specified

    Returns
    ------
    user_input: str
        string of users input
    """
    allowed_answers_str_list = []
    if allowed_answers is not None:
        for element in allowed_answers:
            allowed_answers_str_list.append(str(element))
    logger.debug(f"Ask for approval for message: {message}")
    logger.debug(f"Allowed answers for user are: {allowed_answers_str_list}")
    user_input = ""
    good_to_go = False
    while not good_to_go:
        inp = str(input(message + "\n"))

        if allowed_answers is not None:
            if inp in allowed_answers_str_list:
                user_input = inp
                good_to_go = True
            else:
                print("\nGiven input is not in allowed answers. Try again please.")
                print("Allowed answers are: " + str(allowed_answers_str_list))
                logger.warning(f"Given input ({inp}) is not valid. Ask user again.")
        else:
            user_input = inp
            good_to_go = True

    logger.debug(f"User input of approval: {user_input}")

    return user_input


def await_user_input_from_list_decision(list_to_decide: list, header_message: str = "", lang: str = "de") -> str:
    """
    Print message and wait for user input. Let the user choose from a given list of choices.
    !! Calls the function >await_user_input()< !!

    Parameters
    ----------
    list_to_decide: list
        list of allowed answers.
    header_message: str
        string that will be printed as question for user input
    lang: str
        indicator for language that should be used

    Returns
    ------
    user_decision: str
        string of users input
    """
    language = {
        "de": "Nummer eingeben um Wert auszuwählen:",
        "eng": "Select a number to choose a value:"
    }

    user_decision = None

    if type(list_to_decide) is not list or len(list_to_decide) == 0:
        return user_decision

    if len(list_to_decide) == 1:
        user_decision = list_to_decide[0]

    else:
        indexes = list(range(0, len(list_to_decide)))
        sorted_list = sorted(list_to_decide)
        message_str = header_message + "\n"
        for idx in range(0, len(list_to_decide)):
            number_str = f"{idx}\t: {sorted_list[idx]}\n"
            message_str += number_str

        message_str += f"\n{language[lang]}\n"
        user_input = await_user_input(message=message_str, allowed_answers=indexes)
        user_decision = sorted_list[int(user_input)]

    return user_decision


def wait_for_shutdown(waittime: int):
    print(f"Script is finished. Will shutdown PC in {waittime} seconds! Press CTRL + C to prevent that.")
    waiting_list = [waittime, int(waittime * 0.5), int(waittime * 0.75), int(waittime * 0.9), int(waittime * 0.95),
                    int(waittime * 0.99), waittime]

    try:
        for idx, wait in enumerate(waiting_list):
            # Print message
            if wait == waittime and idx == 0:
                print(f"\n\t{wait} seconds till shutdown...  Press CTRL + C to prevent that")
            else:
                print(f"\n\t{waittime - wait} seconds till shutdown...  Press CTRL + C to prevent that")

            # Sleep
            if idx < len(waiting_list) - 1:
                time.sleep(waittime - waiting_list[idx + 1])
            else:
                time.sleep(2)

        print("\nWill shutdown now!")
        print("Uncomment the following line to shut down the PC!")
        # os.system("shutdown /s /t 20")
    except KeyboardInterrupt:
        print("  Continue processing...")


if __name__ == "__main__":
    user_inp1 = await_user_input(message="Test 1: Enter something")
    print(user_inp1)

    user_inp2 = await_user_input_from_list_decision(list_to_decide=["One", "Two"], header_message="Choose from list",
                                                    lang="eng")
    print(user_inp2)
    wait_for_shutdown(waittime=30)
    print("End")
