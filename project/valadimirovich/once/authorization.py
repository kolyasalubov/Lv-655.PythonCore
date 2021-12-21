import base64


def authorization() -> str:
    '''
    Promting user's ID and password from console 
    combining them 'ID:pass' and encoding into base64
    Returns str with base64 encoded user credentials
    '''

    user_id = input('Please input your user id: ')
    user_pass = input('Please input your password: ')

    user_credentials = f'{user_id}:{user_pass}'

    user_credentials_bytes = user_credentials.encode('ascii')

    user_credentials_bytes_base64 = base64.standard_b64encode(user_credentials_bytes)

    user_credentials_base64 = user_credentials_bytes_base64.decode('ascii')

    return user_credentials_base64

