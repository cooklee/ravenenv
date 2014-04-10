import os
from raven.base import DummyClient
import pytest


@pytest.fixture
def raven_client():
    return DummyClient(processors=('ravenenv.processors.AddEnviromentContext',))


def test_check_if_message_is_dict(raven_client):
    message = raven_client.build_msg('raven.events.Exception', tags=None, exc_info=None)
    assert isinstance(message, dict)


def test_check_if_message_contains_all_standard_data(raven_client):
    message = raven_client.build_msg('raven.events.Exception', tags=None, exc_info=None)
    standard_message = DummyClient().build_msg('raven.events.Exception', tags=None, exc_info=None)
    for var in standard_message:
        assert var in message
        if var == 'event_id' or var == 'timestamp' or var == 'extra':
            continue
        assert standard_message[var] == message[var]


def test_check_if_message_extra_contains_all_env_var(raven_client):
    message = raven_client.build_msg('raven.events.Exception', tags=None, exc_info=None)
    for env_var in os.environ:
        assert env_var in message['extra']
        message['extra'][env_var] = message['extra'][env_var][1:-1]
        assert os.environ[env_var][:len(message['extra'][env_var])] == message['extra'][env_var]
