import requests
from constants import sms_get_post_url
import acquire_access_token
from json import loads
import prepare_payload

class RemoteDevice():
    '''
    Device class has two instant methods, needs serial number and iccid
    '''

    def __init__(self, number_id, iccid):
        self.number_id = number_id
        self.iccid = iccid
        
        
    
    def get_sms(self) -> list:
        '''
        GET list of the massages from the server for particular IccID 
        returns list of dicts
        '''

        url = sms_get_post_url.format(self.iccid)

        my_header = {
                      'Accept': 'application/json',
                      'Authorization': f'Bearer {acquire_access_token.acquire_access_token()}'
                    }
        my_reply = requests.request('GET', url, headers=my_header)
        
        return loads(my_reply.text)
    
    def send_sms(self) -> list:
        '''
        POST sends text massage
        returns 'Created'
        '''

        url = sms_get_post_url.format(self.iccid)

        # payload = "{\"source_address\":\"667\",\"payload\":\"API TEST 2\"}"



        my_header = {
                     "Accept": "application/json",
                     "Content-Type": "application/json;charset=UTF-8",
                     "Authorization": f"Bearer {acquire_access_token.acquire_access_token()}"

        }
        my_response = requests.request("POST", url, data=f'{prepare_payload.preparing_payload()}', headers=my_header)
        
        
        return 'Created'
        


