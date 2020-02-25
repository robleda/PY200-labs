class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # кол-во дней в месяцах обычного года
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # у високосного

    def __init__(self, day: int, month: int, year: int):
        """
        Принимает значения int для даты. Формат ДД, ММ, ГГГГ
        Либо принимает строку в формате "ДД.ММ.ГГГГ"

        Начало ВСЕХ времён - 01 января 0000 года, оно же 1.1.0

        :param day: день
        :param month: месяц
        :param year: год
        """
        self.__is_valid_date(day, month, year)
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Проверка на високосность года
        :param year: int
        :return: True - високосный, иначе False
        """
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            return False
        else:
            return True

    @classmethod
    def get_max_day(cls, year: int, month: int) -> int:  # берет макс. значение дня из кортежа
        """
        Возвращает значение максимального кол-ва дней в месяце, в зависимости от високосности года
        :param year: int
        :param month: int
        :return: int
        """
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @classmethod
    def __is_valid_date(cls, day, month, year):  # проверка корректности
        """
        Проверка корректности даты
        :param day: int
        :param month: int
        :param year: int
        :return: nothing
        """
        if not isinstance(day, int):
            raise TypeError('day must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(year, int):
            raise TypeError('year must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        """
        Сеттер даты, преобразует str значение в int для day, month, year
        :param value: str - строка с датой в формате '06.02.2020'
        :return: nothing
        """
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.__is_valid_date(day, month, year)

        except ValueError:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return f'{self.__day}'

    @property
    def month(self):
        return f'{self.__month}'

    @property
    def year(self):
        return f'{self.__year}'

    @day.setter
    def day(self, value):
        """
        Сеттер дня. Принимает int значение и устанавливает его для экземпляра
        Также проводится проверка на корректность получившейся даты, чтобы не задавать, к примеру, 29 февраля
        для невисокосного года

        Аналогично работают сеттеры месяца и года

        :param value:
        :return:
        """
        if not isinstance(value, int):
            raise TypeError('Day must be int')
        if 1 <= value <= 31:
            self.__day = value
            self.__is_valid_date(value, self.__month, self.__year)
        else:
            raise ValueError('Invalid day value')

    @month.setter
    def month(self, value):
        if not isinstance(value, int):
            raise TypeError('Month must be int')
        if 0 < value <= 12:
            self.__month = value
            self.__is_valid_date(self.__day, value, self.__year)
        else:
            raise ValueError('Invalid month value')

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise TypeError('Year must be int')
        if value >= 0:
            self.__year = value
            self.__is_valid_date(self.__day, self.__month, value)
        else:
            raise ValueError('Invalid year value')

    def add_day(self, day: int):
        """
        Увеличивает дату на day
        :param day: int
        :return: новая дата
        """
        if isinstance(day, int):
            our_days = self.date_to_int()
            result = our_days + day
            return self.int_to_date(result)
        else:
            raise TypeError('days to add must be int')

    def add_month(self, month: int):  # пока не понятно, но не дико сложно
        pass

    def add_year(self, year: int):
        """
        Увеличивает дату на year кол-во лет
        :param year: int
        :return: новая дата
        """
        if isinstance(year, int):
            self.year = int(self.year) + year
            return self.date
        else:
            raise TypeError('years to add must be int')

    def date_to_int(self):
        """
        Пересчитывает заданную дату в число дней с начала времен
        :return: int -> количество дней
        """
        if isinstance(self, Date):
            days_count = 0
            for i in range(self.__year):  # счетчик дней из
                if self.is_leap_year(i):
                    days_count += 366
                else:
                    days_count += 365

            for i in range(1, self.__month):  # счетчик дней из месяцев
                days_count += self.get_max_day(self.__year, i)

            days_count += self.__day  # соответственно

            return days_count

        else:
            raise TypeError('Can calculate only Date object')

    # def int_to_date(self, days_count):  - ЧЕРЕЗ ЭТУ РЕАЛИЗАЦЮ КОПИТСЯ ОШИБКА
    #     """
    #     Преобразует число (дней) в дату
    #     :param days_count: int - количество дней, которые мы хотим преобразовать в дату, минимум 1
    #     """
    #     years_gone = days_count // 365
    #     for i in range(years_gone):
    #         if self.is_leap_year(i):
    #             days_count -= 366
    #         else:
    #             days_count -= 365
    #
    #     self.__year = years_gone
    #     if days_count == 0:
    #         self.__month = 12
    #         self.__day = 31
    #
    #     else:
    #         months_gone = days_count // 30
    #         for i in range(months_gone):
    #             days_count -= self.get_max_day(years_gone, i)
    #
    #     self.__month = months_gone + 1
    #     self.__day = days_count
    #
    #     return self.date

    def int_to_date(self, days_count: int):
        """
        Преобразует число (дней) в дату
        :param days_count: int - количество дней, которые мы хотим преобразовать в дату, минимум 1
        """
        if isinstance(days_count, int):
            if days_count < 0:
                raise ValueError('Number must be >= 1')
            year_counter = 0
            while days_count > 366:
                if self.is_leap_year(year_counter):
                    days_count -= 366
                    year_counter += 1
                else:
                    days_count -= 365
                    year_counter += 1

            month_count = 1
            while days_count >= 31:
                days_count -= self.get_max_day(year_counter, month_count)
                if days_count == 0:
                    days_count = self.get_max_day(year_counter, month_count)
                    break
                month_count += 1

            self.year = year_counter
            self.month = month_count
            self.day = days_count
            return self.date

    # погнали перегрузку
    def __lt__(self, other):
        if self.date_to_int() < other.date_to_int():
            return True
        else:
            return False

    def __le__(self, other):
        if self.date_to_int() <= other.date_to_int():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.date_to_int() == other.date_to_int():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.date_to_int() != other.date_to_int():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.date_to_int() > other.date_to_int():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.date_to_int() >= other.date_to_int():
            return True
        else:
            return False

    def __add__(self, other):
        res = self.date_to_int() + other.date_to_int()
        date_refresh = Date('01.01.0000')
        return date_refresh.int_to_date(res)

    def __radd__(self, other):
        res = self.date_to_int() + other.date_to_int()
        date_refresh = Date('01.01.0000')
        return date_refresh.int_to_date(res)

    def __sub__(self, other):
        res = self.date_to_int() - other.date_to_int()
        if res < 0:
            raise ValueError('Работает только с начала времен - 01.01.0000')
        date_refresh = Date('01.01.0000')
        return date_refresh.int_to_date(res)

    def __rsub__(self, other):
        res = self.date_to_int() - other.date_to_int()
        if res < 0:
            raise ValueError('Работает только с начала времен - 01.01.0000')
        date_refresh = Date('01.01.0000')
        return date_refresh.int_to_date(res)

    def __iadd__(self, other):
        res = self.date_to_int() + other.date_to_int()
        return self.int_to_date(res)

    def __isub__(self, other):
        res = self.date_to_int() - other.date_to_int()
        if res < 0:
            raise ValueError('Работает только с начала времен - 01.01.0000')
        return self.int_to_date(res)


if __name__ == '__main__':
    date1 = Date(28, 2, 1999)
    print(date1)
    date1.date = '31.12.2020'
    # print(date1)
    # date1.day = 28
    # date1.month = 2
    # date1.year = 5

    print(date1.date_to_int())
    print(date1.int_to_date(738156))

# 737831
