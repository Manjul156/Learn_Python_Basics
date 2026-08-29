password = 'Manjul'

if len(password) < 6:
    print("weak password")
elif 6 < len(password) < 10:
    print("medium password")
else:
    print("Strong password")
