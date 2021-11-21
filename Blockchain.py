from SHA256 import *
import os

class blocks:
    def components(self, previoushash, data, date):
        return('{}{}{}'.format(previoushash, data, date))

b = blocks()

class Chain:
    def mine(self,previous, data, date):
        from Hashbank import Bank
        self.Bank = Bank
        next = me.hash(b.components(previous, data, date))
        self.Bank.append(next)
        path = r"C:\Users\gsbaw\PycharmProjects\Accounting_Cycle_V2\Hashbank.py"
        assert os.path.isfile(path)
        with open(path, "w") as bank:
            bank.write(f'Bank = {self.Bank}')
            bank.close()

C = Chain()
