from frost.client.events import EventStatus


def get_status(event_name):
    status = None
    while status is None:
        status = EventStatus.get_status(event_name)

    return status
