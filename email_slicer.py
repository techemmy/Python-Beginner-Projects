mail = input("Enter you mail:")

name, domain = mail[:mail.index("@")], mail[mail.index("@"):]
print(f"You name is {name} and you use a {domain} domain")