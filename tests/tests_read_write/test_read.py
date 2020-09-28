from hamcrest import assert_that, equal_to, has_entries
import pytest
import random
import string
from tests.api.data import GetData, PostData
import time


def parametrize_letters_numbers():
    numbers = [''.join(random.choice(string.digits) for _ in range(6)) for _ in range(5)]
    letters = [''.join(random.choice(string.ascii_lowercase) for _ in range(6)) for _ in range(5)]
    letters_and_numbers = [''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits)
                                   for _ in range(3)) for _ in range(5)]
    numbers.extend(letters)
    letters_and_numbers.extend(numbers)
    return letters_and_numbers


@pytest.mark.parametrize('_', range(1, 6), ids=lambda x: f'iteration {x}')
def test_that_input_buffer_is_empty_after_opening_port(_):
    response = GetData().send()
    assert_that(response.status_code, equal_to(200))
    assert_that(response.json(), has_entries({'string': equal_to(''), 'in_waiting': equal_to(0)}), response.text)


@pytest.mark.parametrize('test_string', parametrize_letters_numbers(), ids=lambda x: f'writing string {x}')
def test_that_input_buffer_is_empty_after_opening_port(test_string):
    post_response = PostData(test_string).send()
    assert_that(post_response.status_code, equal_to(201), post_response.text)
    time.sleep(0.5)
    get_response = GetData().send()
    assert_that(get_response.status_code, equal_to(200), get_response.text)
    assert_that(get_response.json(),
                has_entries({'string': equal_to(test_string), 'in_waiting': equal_to(len(test_string))}),
                get_response.text)
