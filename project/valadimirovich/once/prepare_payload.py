

def preparing_payload()-> str:

    source_address = input('Please input source address:')
    payload = input('Please input the content body of the SMS massage: ')

    payload111 = "{\"source_address\":\"%s\",\"payload\":\"%s\"}"
    
    part1 = '"{\"source_address\":\"'
    part2 = '\",\"payload\":\"'
    part3 = '\"}"'


    ready_string = part1 + source_address + part2 + payload + part3


    return payload111 % (source_address, payload)

