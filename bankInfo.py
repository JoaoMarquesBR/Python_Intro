from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Branch:
    branch_number : str
    branch_gross  : str

@dataclass
class UserBank:
    user_firstName : str
    user_lastname : str
    user_gross : Decimal
    user_returns : Decimal
    user_net : Decimal
