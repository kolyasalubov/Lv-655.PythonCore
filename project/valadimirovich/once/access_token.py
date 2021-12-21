import requests, json, time
from authorization import authorization as author
from urls import url_access_token as url

def getting_access_token() -> str:

    '''
    Function checking if old access token is still valid 
    if it is valid, it will return old token int string format from file.
    It is isn't valid, it gets authorization credentials base64 encoded
    and obtain fresh access token for the 1NCE API and returns it in string format

    '''

    time_stemp = 0

    time_stamp_file = open('time_stemp.txt')

    time_stemp = int(time_stamp_file.read())

    if int(time.time()) - 3600 >= time_stemp:
        
        credentials = author()
        
        my_payload = {'grant_type': credentials}

        my_headers = {'Accept': 'application/json',
                      'Content-Type': 'application/json',
                      'Authorization': f'Basic {credentials}'
                      }

        my_response = requests.request('POST', url, json=my_payload, headers=my_headers)
        
        response_dict = json.loads(my_response.text)

        access_token = response_dict['access_token']

        my_file = open('token_cache.bin', 'wb')
        my_file.write(access_token.encode('ascii'))
        my_file.close()

        time_stamp_file = open('time_stemp.txt', 'w')
        time_stamp_file.write(str(int(time.time())))
        time_stamp_file.close()

        print('Fresh token')

        return access_token

    else:

        my_file = open('token_cache.bin', 'rb')

        access_token_bytes = my_file.read()

        my_file.close()

        access_token_from_file = access_token_bytes.decode('ascii')
        
        print('Old token')

        return access_token_from_file

getting_access_token()