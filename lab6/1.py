class UserAccount:
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.__password = password

  def set_password(self, new_password) -> None:
    self.__password = new_password

  def check_password(self, check_password) -> bool:
      return True if check_password == self.__password else False
    

newAcc = UserAccount(
    "P1ecful",
    "awesome-email-template@yandex.ru",
    "awesome-password"
)

print(newAcc.check_password("awesome-password"))
newAcc.set_password("new-password")
print(newAcc.check_password("awesome-password"))