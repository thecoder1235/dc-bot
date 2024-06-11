import  random



ZOR="!'^+%&/()=?*\_1234567890*-q@we€rtyuıopğü,;àsdfghjklşízxcvbmöç.:<>QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ¨₺$"

def sifre(a,value):
    password = ''
    for i in range(value):
        password += random.choice(a)
    return password
