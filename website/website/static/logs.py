from datetime import datetime


def write_log(message):

    with open(
        "logs/system.log",
        "a"
    ) as file:

        file.write(
            str(datetime.now())
            + " - "
            + message
            + "\n"
        )
