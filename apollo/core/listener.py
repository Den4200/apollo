from frost.client.events import Messages


def listen(manager, *_) -> None:
    msgs = Messages.get_new_msgs()

    if msgs:
        msgs = msgs[1].values()

        for msg in msgs:
            manager.messages_screen.messages.message_history.update_chat_history(
                 f'[color=dd2020]{msg["from_user"]["username"]}[/color] > {msg["message"]}'
            )
