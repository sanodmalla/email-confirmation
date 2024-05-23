email = input("Enter your email: ") # e@e.in
a,b,c = 0, 0, 0
if len(email) > 6:
    if "@" in email and email.count("@") == 1:
        if email[0].isalpha():
            if email[-3] == "." or email[-4] == ".":
                for x in email:
                    if x == " ":
                        a = 1
                    elif x.isalpha():
                        if x == x.upper():
                            b = 1
                    elif x == "_" or x == "." or x == "a":
                        continue
                    elif x == x.isdigit():
                        continue

                if a == 1 or b == 1:
                    print("Wrong email.")
                else:
                    print("CORRECT EMAIL.")
            else:
                print("Wrong email. --> '.' positioning.")
        else:
            print("Wrong email. First letter has to be alphabet.")
    else:
        print("Wrong email. --> @")
else:
    print("Wrong email. --> Length")

# email = "g@@g .in"
# # # # print(email.count("@"))
# # # # print(email[1])
# # # print(email[-3])
# # if " " in email:
# #     print("True")
# # else:
# #     print("no space")
# for x in email:
#     if x.isalpha():
#         print(x.upper())