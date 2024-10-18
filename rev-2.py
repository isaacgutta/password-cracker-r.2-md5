import hashlib


# permision error? ive tried C:\Users\Isaac\10-million-password-list-top-1000.txt and  10-million-password-list-top-1000.txt
pass_filename = "10-million-password-list-top-1000.txt"

password = "booomer"


enc_password = password.encode("utf-8")
password_hash = hashlib.md5(enc_password.strip()).hexdigest()
print(password_hash)

# line 15 has error
pass_file = open(pass_filename, "r")

# The hash format can be swaped 
for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()


    if password_hash == enc_hash:
        print("this three-letter agency has been hacked. the pasword was" + word)
        quit()


print("the three-letter agency has a strong password.")