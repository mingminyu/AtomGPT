from tortoise import Tortoise, run_async
from typing import Dict, Any
from atomui.models.chat import ChatInfo, ChatMessageInfo


async def init():
    await Tortoise.init(
        db_url='sqlite://../db.sqlite3',
        modules={'models': ['orm.chat']}
    )
    await Tortoise.generate_schemas()


chat_infos = [
    {
        "uid": 100001,
        "username": "draven",
        "cid": "164334f0-bc9f-4e4a-9b12-038a201f7387",
        "ts": "2024-01-15 14:25:00",
        "date": "2024-01-15",
        "title": "Greet",
        "status": True,
        "create_time": "2024-01-15 14:25:00",
        "modify_time": "2021-01-15 14:25:01"
    },
    {
        "uid": 100001,
        "username": "draven",
        "cid": "b4cba9bc-e26b-4d28-b206-4c26aee5e64f",
        "ts": "2024-01-14 14:25:00",
        "date": "2024-01-14",
        "title": "Chat Markdown",
        "status": True,
        "create_time": "2024-01-14 14:25:00",
        "modify_time": "2024-01-14 14:25:01"
    },
    {
        "uid": 100001,
        "username": "draven",
        "cid": "ab132efb-fac4-46d9-82ec-ae4c283f180b",
        "ts": "2024-01-11 14:25:00",
        "date": "2024-01-11",
        "title": "Chat Pyecharts",
        "status": True,
        "create_time": "2024-01-11 14:25:00",
        "modify_time": "2024-01-11 14:25:01"
    },
    {
        "uid": 100002,
        "username": "chen",
        "cid": "9e1c9190-e8f1-46b8-a6b8-750645dc243a",
        "ts": "2024-01-11 14:25:00",
        "date": "2024-01-11",
        "title": "Hello chen",
        "status": True,
        "create_time": "2024-01-11 14:25:00",
        "modify_time": "2024-01-11 14:25:01"
    },
]


chat_messages = [
    {
        "cid": "164334f0-bc9f-4e4a-9b12-038a201f7387",
        "index": 1,
        "role": "user",
        "content": "Hello, Atom",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:00"
    },
    {
        "cid": "164334f0-bc9f-4e4a-9b12-038a201f7387",
        "index": 2,
        "role": "assistant",
        "content": "I'm AtomGPT, Can I help you?",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:00"
    },
]


class ChatDBTool:

    @staticmethod
    async def add_chat_info(chat_info_: Dict[str, Any]):
        await ChatInfo.create(**chat_info_)



if __name__ == "__main__":
    run_async(init())

    for chat_info in chat_infos:
        run_async(ChatDBTool.add_chat_info(chat_info))
