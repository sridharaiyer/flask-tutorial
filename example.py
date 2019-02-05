from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
password = 'mypassword'
hashed_password = bcrypt.generate_password_hash(password=password)
print(hashed_password)
check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')
print(f'Check wrong password: {check}')
check = bcrypt.check_password_hash(hashed_password, password)
print(f'Check right password: {check}')
