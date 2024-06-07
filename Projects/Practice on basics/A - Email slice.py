# first project

# ---------------------------
# -- Practical Slice Email --
# ---------------------------

name = input("enter your user name : ").strip().capitalize()
Email = input("enter your email : ").strip()

username = Email[ :Email.index("@")]
website = Email[Email.index("@") + 1 : ]

print(f"Hello, {name}")
print(f"your email is : {Email}")
print(f"your username is : {username}")
print(f"your wesite is : {website}")