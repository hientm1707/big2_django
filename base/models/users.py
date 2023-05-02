# from datetime import datetime
# from datetime import date
# from accounts import Account
#
#
# class UserDetail:
#
#     def __init__(self, account: Account, first_name, last_name, birthday: datetime):
#         self.username = account.username
#         self.password = account.password
#         self.name = first_name + ' ' + last_name
#         self.birthday = birthday
#         self.years_of_age = self.compute_years_of_age()
#
#     def compute_years_of_age(self):
#         today = date.today()
#         age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#         return age
