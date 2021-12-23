import my_classes
import get_iccid
from pprint import pprint
from prepare_payload import preparing_payload


if __name__ == '__main__':
    
    tds1 = my_classes.RemoteDevice(1, get_iccid.getting_iccid(1))

    tds1.send_sms()

    reply = tds1.get_sms()
    
    for dicts in reply:
        pprint(reply)

