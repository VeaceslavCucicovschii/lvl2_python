from datetime import datetime
import random


def id():
    # date + time
    time_now = datetime.now()
    time = time_now.strftime("%Y-%m-%d-%H-%M-%S-")

    # rand number
    random_nr = random.randint(0, 999999)
    return f"{time}-{random_nr:06d}"
