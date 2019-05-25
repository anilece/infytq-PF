
def validate_name(name):
    if name.isalpha():
        if len(name)<=15:
            return(True)
        else:
            return(False)
    else:
        return(False)
def validate_phone_no(phno):
    if phno.isdigit():
        if len(str(phno))<=10:
            set_phno=set(phno)
            if len(set_phno)>1:
                return(True)
            else:
                return(False)
        else:
            return(False)        
    else:
        return(False)
def validate_email_id(email_id):
    w=email_id.find("@")
    e=email_id.find(".")
    domain_name=email_id[w+1:e]
    if email_id[-4:]==".com" and (domain_name=="gmail" or domain_name=="yahoo" or domain_name=="hotmail"):
        return(True)
    else:
        return(False)
        
def validate_all(name,phone_no,email_id):
    flag=0
    if (validate_name(name)!=True):
        print("Invalid Name")
        flag=1
    if (validate_phone_no(phone_no)!=True):
            print("Invalid phone number")
            flag=1
    if (validate_email_id(email_id)!=True):
        print("Invalid email id")
        flag=1
    if(flag==0):
        print("All the details are valid")
        
   
validate_all("Tina", "9994599998", "tina@yahoo.com")
