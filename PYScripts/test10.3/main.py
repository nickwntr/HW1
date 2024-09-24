import threading

import economy
jpm = economy.Bank()


th1 = threading.Thread(target=economy.Bank.deposit,args=(jpm,))
th2 = threading.Thread(target=economy.Bank.take,args=(jpm,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {jpm.balance}')
