"""
Khai báo lớp Hash có các hàm băm
"""


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    # Hàm băm mật khẩu
    def bcript(password: str):
        return pwd_context.hash(password)

    # Hàm xác minh mật khẩu thường với mật khẩu đã băm
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)
