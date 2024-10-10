##
#  Questo programma illustra vari metodi che verificano proprietà di sottostringhe.
#

# Chiede all’utente una stringa e una sottostringa.
the_string = input("Enter a string: ")
the_sub_string = input("Enter a substring: ")

if the_sub_string in the_string:
    print("The string does contain the substring.")

    how_many = the_string.count(the_sub_string)
    print("   It contains", how_many, "instance(s)")

    where = the_string.find(the_sub_string)
    print("   The first occurrence starts at position", where)

    if the_string.startswith(the_sub_string):
        print("   The string starts with the substring.")
    else:
        print("   The string does not start with the substring.")

    if the_string.endswith(the_sub_string):
        print("   The string ends with the substring.")
    else:
        print("   The string does not end with the substring.")

else:
    print("The string does not contain the substring.")
