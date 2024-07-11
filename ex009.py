
def reverse_words_str(strdata):
    words = strdata.split(' ')
    nw_words = [ word[-1::-1] for word in words]
    nw_strdata = " ".join(nw_words)
    return nw_strdata

usr_str=input("Enter sentance to reverse ")
print(reverse_words_str(usr_str))
