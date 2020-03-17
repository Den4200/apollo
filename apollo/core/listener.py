from frost.client.events import messages


def listen(updater, *_) -> None:
    msgs = messages.get_new_msgs().values()

    if msgs:
        for msg in msgs:
            updater(
                 f'[color=dd2020]{msg["from_user"]["username"]}[/color] > {msg["message"]}'
            )
