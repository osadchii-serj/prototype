from interfaces.interface_prototype import IPrototype
from interfaces.interface_user_date import IForm
from dataclasses import dataclass
import copy


@dataclass
class UserData(IForm, IPrototype):

    name: str = None
    surname: str = None
    login: str = None
    password: str = None
    address: str = None
    phone: str = None
    email: str = None
    age: int = 0

    def create_form(self):
        return f"{self.name}\n{self.surname}\n{self.age}\n{self.login}\n{self.password}\n{self.email}\n{self.phone}\n{self.address}"

    def clone(self):
        return copy.deepcopy(self)

    def __post_init__(self):
        print(self.create_form())
