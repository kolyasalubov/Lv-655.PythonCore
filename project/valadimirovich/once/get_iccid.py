import re

def getting_iccid(number_id:int) -> int:
    '''
    Excpects for int serial number
    Looks up IccID in the CSV file and returns int IccID
    '''
    try:
        with open(r"C:\Hank\Python\HomeWork_GIT\Lv-655.PythonCore\project\valadimirovich\once\iccid.csv") as file_csv:

            pre_sorted = file_csv.read()

            list_of_id_iccid = re.split(',', pre_sorted)

            iccid_dict = {}

            for item in range(0, len(list_of_id_iccid), 2):

                iccid_dict.update({int(list_of_id_iccid[item]): list_of_id_iccid[item+1]})
            
            return iccid_dict[number_id]            
            
    except Exception as ex:
            print('Error loading IccID from the file ', ex)


