from ravenenv.processors import AddEnviromentContext
import os


def test_check_if_get_env_info_return_dict():
    assert isinstance(AddEnviromentContext(None).get_env_info(), dict)


def test_process_return_dict_with_extra_key_empty():
    data = {}
    assert 'extra' in AddEnviromentContext(None).process(data)


def test_process_return_dict_with_extra_key_with_extra():
    data = {'extra': {}}
    assert 'extra' in AddEnviromentContext(None).process(data)


def test_process_return_non_empty_dict():
    data = {}
    assert len(AddEnviromentContext(None).process(data)['extra']) > 0


def test_env_variable_are_in_dict_returned_by_get_env_info():
    env = os.environ
    assert env == AddEnviromentContext(None).get_env_info()
