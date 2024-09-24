from CustomExc import *


class Car:
    model = None
    _vin = None
    _numbers = None

    def _is_valid_vin(self, vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber("Введенный vin-номер не является числом")
        if not (1000000 < vin_number and vin_number < 9999999):
            raise IncorrectVinNumber("Vin-номер не в диапозоне от 1000000 до 9999999")
        return True

    def _is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumber("Введенный Номер не является строкой")
        if not (len(numbers) == 6):
            raise IncorrectCarNumber("Длина номера недостаточна или избыточна, необходимая длина - 6")
        return True

    def __init__(self,model,Vin,LPlate):
        self.model = model
        if self._is_valid_vin(Vin):
            self._vin = Vin
        if self._is_valid_numbers(LPlate):
            self._numbers = LPlate
        print("Машина создана")