from collections import Counter

class Coin:
    def __init__(self, denomination: float):
        """
        Инициализация монеты.

        :param denomination: Номинал монеты.
        """
        self.denomination = denomination

    def __repr__(self):
        return f"Coin({self.denomination})"


class PiggyBank:
    def __init__(self):
        """
        Инициализация копилки.
        """
        self.coins = []
        self.is_broken = False

    def add_coin(self, coin: Coin):
        """
        Добавляет монету в копилку.

        :param coin: Объект Coin для добавления.
        """
        # TODO реализуйте метод как в описании

        if not (self.is_broken):
            self.coins.append(coin)
        else:
            raise ValueError("Копилка разбита. Нельзя добавить монеты.")



    def break_piggy_bank(self):
        """
        Разбивает копилку и возвращает информацию о монетах.

        :return: Словарь, где ключ - номинал монеты, значение - количество монет этого номинала.
        """
        # TODO реализуйте метод как в описании

        if(self.is_broken):
            raise ValueError("Копилка уже разбита.")


        #print(self.coins)
        # print(len(self.coins)) # cумма монет
        total_sum = sum(coin.denomination for coin in self.coins)
        print(total_sum)

        # result = dict(Counter(self.coins))
        result ={}
        for coin in self.coins:
            if coin.denomination in result:
                result[coin.denomination] += 1
            else:
                result[coin.denomination] = 1


        self.coins = []
        # self.coins.clear()
        self.is_broken = True

        return result



# piggy_bank = PiggyBank()
# coin1 = Coin(1.0)
# coin2 = Coin(0.5)
#
# piggy_bank.add_coin(coin1)
# piggy_bank.add_coin(coin2)
# piggy_bank.add_coin(coin1)
#
# piggy_bank.break_piggy_bank()

if __name__ == "__main__":
    # Создаем копилку
    piggy_bank = PiggyBank()

    # Создаем несколько монет
    coin1 = Coin(1.0)
    coin2 = Coin(0.5)
    coin3 = Coin(0.25)
    coin4 = Coin(1.0)
    coin5 = Coin(0.5)

    # Добавляем монеты в копилку
    piggy_bank.add_coin(coin1)
    piggy_bank.add_coin(coin2)
    piggy_bank.add_coin(coin3)
    piggy_bank.add_coin(coin4)
    piggy_bank.add_coin(coin5)

    # Печатаем состояние копилки
    print(piggy_bank.coins)

    # Разбиваем копилку
    coins_info = piggy_bank.break_piggy_bank()
    print("Монеты в копилке:", coins_info)

    # Пытаемся добавить монету в разбитую копилку (должна быть ошибка)
    try:
        piggy_bank.add_coin(Coin(2.0))
    except ValueError as e:
        print(e)

    # Пытаемся снова разбить копилку (должна быть ошибка)
    try:
        piggy_bank.break_piggy_bank()
    except ValueError as e:
        print(e)
