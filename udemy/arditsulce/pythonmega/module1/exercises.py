def coding_exercise_13_1(unit_test=False):
    def get_age(year_of_birth: int, current_year:int = 2024) -> int:
        """
        Calculate the age based on the year of birth and the current year.

        Args:
            year_of_birth (int): The year of birth.
            current_year (int): The current year. Default is 2024.

        Returns:
            int: The age of the person.
        """
        return current_year - year_of_birth

    # Test the function
    print(get_age(1990))

    if unit_test:
        # Unit tests
        assert get_age(1990) == 34
        assert get_age(2000) == 24
        assert get_age(2005) == 19


def coding_exercise_13_2(unit_test=False):
    def get_nr_items(string: str) -> int:
        """
        Count the number of items in a string separated by commas.

        Args:
            string (str): The string to be checked.

        Returns:
            int: The number of items in the string.
        """
        return len(string.split(","))

    # Test the function
    print(get_nr_items("apple,banana,orange"))

    if unit_test:
        # Unit tests
        assert get_nr_items("apple,banana,orange") == 3
        assert get_nr_items("apple") == 1
        assert get_nr_items("apple,banana,orange,kiwi") == 4


def coding_exercise_13_3(unit_test=False):
    def area_of_square(side_length: float) -> float:
        """
        Calculate the area of a square.

        Args:
            side_length (float): The side length of the square.

        Returns:
            int/float: The area of the square.
        """
        return side_length ** 2

    # Test the function
    print(area_of_square(5))

    if unit_test:
        # Unit tests
        assert area_of_square(5) == 25
        assert area_of_square(10) == 100
        assert area_of_square(15) == 225


def coding_exercise_13_4(unit_test=False):
    def weather_condition(temperature: float) -> str:
        """
        Determine the weather condition based on the temperature.

        Args:
            temperature (float): The temperature to be checked.

        Returns:
            str: The weather condition. "Warm" if temperature > 7, "Cold" otherwise.
        """
        return "Warm" if temperature > 7 else "Cold"

    # Test the function
    print(weather_condition(5))

    if unit_test:
        # Unit tests
        assert weather_condition(5) == "Cold"
        assert weather_condition(10) == "Warm"
        assert weather_condition(15) == "Warm" 


def coding_exercise_13_5(unit_test=False):
    def length_of_string(string: str) -> bool:
        """
        Check if the length of the string is greater than or equal to 8.

        Args:
            string (str): The string to be checked.

        Returns:
            bool: True if the length of the string is greater than or equal to 8, False otherwise.
        """
        return len(string) >= 8

    # Test the function
    print(length_of_string("hello"))

    if unit_test:
        # Unit tests
        assert length_of_string("hello") == False
        assert length_of_string("hello world") == True
        assert length_of_string("hello world!") == True
    


def coding_exercise_14_1(unit_test=False):
    def water_state(temperature: float) -> str:
        """
        Determine the state of water based on the temperature.

        Args:
            temperature (float): The temperature of the water (in Celsius).

        Returns:
            str: The state of the water. "Solid" if temperature <= 0, "Liquid" if temperature < 100, and "Gas" otherwise.
        """
        if temperature <= 0:
            return "Solid"
        elif temperature < 100:
            return "Liquid"
        else:
            return "Gas"
    
    # Test the function
    print(water_state(50))

    if unit_test:
        # Unit tests
        assert water_state(50) == "Liquid"
        assert water_state(0) == "Solid"
        assert water_state(100) == "Gas"


def coding_exercise_14_2(unit_test=False):
    def water_state(temperature: float) -> str:
        """
        Determine the state of water based on the temperature.

        Args:
            temperature (float): The temperature of the water (in Celsius).

        Returns:
            str: The state of the water. "Solid" if temperature <= 0, "Liquid" if temperature < 100, and "Gas" otherwise.
        """
        FREEZING_POINT = 0
        BOILING_POINT = 100

        if temperature <= FREEZING_POINT:
            return "Solid"
        
        elif temperature < BOILING_POINT:
            return "Liquid"
    
        else:
            return "Gas"

    
    # Test the function
    print(water_state(50))

    if unit_test:
        # Unit tests
        assert water_state(50) == "Liquid"
        assert water_state(0) == "Solid"
        assert water_state(100) == "Gas"


def coding_exercise_14_3(unit_test=False):
    def temperature_state(temperature: float) -> str:
        """
        Determine the state of the temperature.

        Args:
            temperature (float): The temperature to be checked.

        Returns:
            str: The state of the temperature. "Hot" if temperature > 25, "Warm" if temperature >= 15, and "Cold" otherwise.
        """
        if temperature > 25:
            return "Hot"
        elif temperature >= 15:
            return "Warm"
        else:
            return "Cold"
    
    # Test the function
    print(temperature_state(10))

    if unit_test:
        # Unit tests
        assert temperature_state(10) == "Cold"
        assert temperature_state(15) == "Warm"
        assert temperature_state(25) == "Warm"
        assert temperature_state(30) == "Hot"


def coding_exercise_15_1(unit_test=False):
    def random_number(lower_bound:int, upper_bound: int) -> int:
        """
        Generate a random number between lower_bound and upper_bound.

        Args:
            lower_bound (int): The lower bound of the random number.
            upper_bound (int): The upper bound of the random number.

        Returns:
            int: A random number between lower_bound and upper_bound.
        """
        import random
        return random.randint(lower_bound, upper_bound)
    
    # Test the function
    print(random_number(1, 10))

    if unit_test:
        # Unit tests
        for _ in range(10):
            assert 1 <= random_number(1, 10) <= 10
            assert 1 <= random_number(1, 100) <= 100
            assert 1 <= random_number(1, 1000) <= 1000



def coding_exercise_17_1(unit_test=False):
    def ounces2milimeters(ounces: float) -> float:
        """
        Convert ounces to milimeters.

        Args:
            ounces (float): The number of ounces to be converted.

        Returns:
            float: The number of milimeters after conversion. Precision is 4 decimal places.
        """
        return round((ounces * 29.57353), 4)
    
    # Test the function
    print(ounces2milimeters(5))

    if unit_test:
        # Unit tests
        assert ounces2milimeters(5) == 147.8675
        assert ounces2milimeters(10) == 295.735
        assert ounces2milimeters(15) == 443.6025



if __name__ == "__main__":
    input_day = int(input("Enter the day of the function: "))
    input_exercise = int(input("Enter the exercise number: "))
    input_unit_test = input("Do you want to run the unit tests? (y/n): ")

    unit_test = input_unit_test.lower() == "y"

    if input_day == 13:
        if input_exercise == 1:
            coding_exercise_13_1(unit_test)
        elif input_exercise == 2:
            coding_exercise_13_2(unit_test)
        elif input_exercise == 3:
            coding_exercise_13_3(unit_test)
        elif input_exercise == 4:
            coding_exercise_13_4(unit_test)
        elif input_exercise == 5:
            coding_exercise_13_5(unit_test)

    elif input_day == 14:
        if input_exercise == 1:
            coding_exercise_14_1(unit_test)
        elif input_exercise == 2:
            coding_exercise_14_2(unit_test)
        elif input_exercise == 3:
            coding_exercise_14_3(unit_test)

    elif input_day == 15:
        if input_exercise == 1:
            coding_exercise_15_1(unit_test)

    elif input_day == 17:
        if input_exercise == 1:
            coding_exercise_17_1(unit_test)