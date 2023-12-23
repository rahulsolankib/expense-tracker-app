class Expense:
    """This class will hold expense information."""
    """Will use builder pattern to validate data and then only create object if valid."""
    _name = ""
    _amount = 0.0
    _date = ""

    def __new__(cls) -> None:
        raise "Cannot create instance directly of Expense class."
    def __init__(self, name, amount, date) -> None:
        self._name = name
        self._amount = amount
        self._date = date

    # static factory method
    @classmethod
    def _create_instance(cls, *args, **kwargs):
        # return cls(name, amount, date) won't work
        instance = super(Expense, cls).__new__(cls)
        instance.__init__(*args, **kwargs)
        return instance

    # static factory method
    @classmethod
    def builder(cls):
        return cls.Builder()

    # static builder class implement
    class Builder:
        def __init__(self):
            self._name = None
            self._amount = None
            self._date = None

        def with_name(self, name):
            self._name = name
            return self

        def with_amount(self, amount):
            self._amount = amount
            return self

        def with_date(self, date):
            self._date = date
            return self

        def validate(self):
            if self._name is None:
                raise ValueError("Name is required")
            if self._amount is None or self._amount <= 0:
                raise ValueError("Amount is invalid")
            if self._date is None:
                raise ValueError("Date is required")
            return True

        def build(self):
            if self.validate() is False:
                raise ValueError("Provided expense data is invalid.")
            return Expense._create_instance(self._name, self._amount, self._date)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    def __str__(self):
        return f"{self._name} {self._amount} {self._date}"
    
# Testing 
    
# if __name__ == '__main__':
#     ice_cream = Expense.builder() \
#                     .with_name("Ice Cream") \
#                     .with_amount(100) \
#                     .with_date("2022-01-01") \
#                     .build()
#     print(ice_cream)
