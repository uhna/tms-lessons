import pytest


@pytest.mark.wizard
@pytest.mark.parametrize("first_name", ["John", "Harry", "Ron"])
@pytest.mark.parametrize("last_name", ["Smith", "Potter", "Weasly"])
def test_fail_if_john_smith(random_age, before_test, first_name,
                            last_name, after_test):
    print(f"\nHello {first_name} {last_name}! Your age is {random_age}")
    full_name = f"{first_name} {last_name}"

    if full_name == "John Smith":
        pytest.xfail("We hate John Smith")
