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

    # print(dict_of_sms['payload'], "\n", dict_of_sms['status']['description'])

    # for keys, items in dict_of_sms.items():
    #     print(f'Here your key: "{keys}", and it value is: "{items}"')



    



  
