import requests
from json import loads as converts_json_to_dict
from time import time
from coding_credanials import coding_credanials as author
from constants import url_access_token as url

def acquire_access_token() -> str:

    '''
    Function checking if old access token is still valid 
    if it is valid, it will return old token int string format from file.
    It is isn't valid, it gets authorization credentials base64 encoded
    and obtain fresh access token for the 1NCE API and returns it in string format

    '''

    time_stemp = 0

    try:
        with open('time_stemp.txt') as time_stamp_file:
            time_stemp = int(time_stamp_file.read())
    except Exception as ex:
        print(ex)


    if int(time()) - 3600 >= time_stemp:
        
        credentials = author()
        
        my_payload = {'grant_type': credentials}

        my_headers = {'Accept': 'application/json',
                      'Content-Type': 'application/json',
                      'Authorization': f'Basic {credentials}'
                      }

        my_response = requests.request('POST', url, json=my_payload, headers=my_headers)
        
        response_dict = converts_json_to_dict(my_response.text)

        access_token = response_dict['access_token']

        try:
            with open('token_cache.bin', 'wb') as my_token:
                my_token.write(access_token.encode('ascii'))
        except Exception as ex:
            print('Exception with token file ', ex)
        
        try:
            with open('time_stemp.txt', 'w') as time_stamp_file:
                time_stamp_file.write(str(int(time())))
        except Exception as ex:
            print('Exception with time stamp file ', ex)

        print('Fresh token')

        return access_token

    else:

        try:
            with open('token_cache.bin', 'rb') as my_token_file:
                access_token_bytes = my_token_file.read()
        except Exception as ex:
            print('Error loading token from the file ', ex)

        access_token_from_file = access_token_bytes.decode('ascii')
        
        print('Old token')
        
        return access_token_from_file




