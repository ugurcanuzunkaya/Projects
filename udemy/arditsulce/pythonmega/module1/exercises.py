def coding_exercise_13_1(unit_test=False):
    def get_age(year_of_birth, current_year = 2024):
        return current_year - year_of_birth

    # Test the function
    print(get_age(1990))

    if unit_test:
        # Unit tests
        assert get_age(1990) == 34
        assert get_age(2000) == 24
        assert get_age(2005) == 19


def coding_exercise_13_2(unit_test=False):
    def get_nr_items(string):
        return len(string.split(","))

    # Test the function
    print(get_nr_items("apple,banana,orange"))

    if unit_test:
        # Unit tests
        assert get_nr_items("apple,banana,orange") == 3
        assert get_nr_items("apple") == 1
        assert get_nr_items("apple,banana,orange,kiwi") == 4


def coding_exercise_13_3(unit_test=False):
    def area_of_square(side_length):
        return side_length ** 2

    # Test the function
    print(area_of_square(5))

    if unit_test:
        # Unit tests
        assert area_of_square(5) == 25
        assert area_of_square(10) == 100
        assert area_of_square(15) == 225


def coding_exercise_13_4(unit_test=False):
    def weather_condition(temperature):
        return "Warm" if temperature > 7 else "Cold"

    # Test the function
    print(weather_condition(5))

    if unit_test:
        # Unit tests
        assert weather_condition(5) == "Cold"
        assert weather_condition(10) == "Warm"
        assert weather_condition(15) == "Warm" 


def coding_exercise_13_5(unit_test=False):
    def length_of_string(string):
        if len(string) < 8:
            return False

        return True
    
    # Test the function
    print(length_of_string("hello"))

    if unit_test:
        # Unit tests
        assert length_of_string("hello") == False
        assert length_of_string("hello world") == True
        assert length_of_string("hello world!") == True
    


def coding_exercise_14_1(unit_test=False):
    def water_state(temperature):
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
    def water_state(temperature):
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
    def temperature_state(temperature):
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
    def random_number(lower_bound, upper_bound):
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



