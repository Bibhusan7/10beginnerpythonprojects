email = input("Email Address: ")
email.strip()
name = email[:email.index("@")] #takes out whats before the @ in email.
domain_name = email[email.index("@")+1:] #takes out whats after the @ in email not including the @ itself.
detail = ("Username: {}\nDomain: {}").format(name, domain_name)
print(detail)