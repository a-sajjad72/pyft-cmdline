import re
from datetime import datetime

def get_version():
    today = datetime.now()
    return today.strftime('%Y.%m.%d')


