class LimitExceedException(Exception):
    def __init__(self,arg):
        self.msg=arg
class InvalidMinimumException(Exception):
    def __init__(self,arg):
        self.msg=arg
class InsufficientFundException(Exception):
    def __init__(self,arg):
        self.msg=arg
balance=1000
amount=int(input("Enter amount==>"))
if amount>10000:
    raise LimitExceedException("Limit Exceeded")
elif amount<100:
    raise InvalidMinimumException("Invalid Mnimum Amount")
else: # Amount is less than the balance
    raise InsufficientFundException("Insufficient Funds")


