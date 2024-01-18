# encoding: utf-8
from typing import Dict, Any
from tortoise import Tortoise, run_async
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
        "create_time": "2024-01-15 14:25:01"
    },
    {
        "cid": "164334f0-bc9f-4e4a-9b12-038a201f7387",
        "index": 2,
        "role": "assistant",
        "content": "I'm AtomGPT, Can I help you?",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:02"
    },
    {
        "cid": "b4cba9bc-e26b-4d28-b206-4c26aee5e64f",
        "index": 1,
        "role": "user",
        "content": "在ECharts关系图中实现自动布局",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:01"
    },
    {
        "cid": "b4cba9bc-e26b-4d28-b206-4c26aee5e64f",
        "index": 2,
        "role": "assistant",
        "content": "在 ECharts 中，如果你希望自动排列节点坐标，你可以使用布局算法。ECharts 提供了一些布局算法，其中之一是力导向图（Force-directed Graph）布局，它可以自动调整节点的位置，使得图形更加美观。\n\n以下是一个简单的力导向图布局的示例：\n\n```javascript\noption = {\n    series: [{\n        type: 'graph',\n        layout: 'force',\n        force: {\n            repulsion: 100,  // 节点之间的斥力\n            edgeLength: 150,  // 连接线的默认长度\n        },\n        data: [{\n            name: 'Node 1',\n        }, {\n            name: 'Node 2',\n        }, {\n            name: 'Node 3',\n        }],\n        links: [{\n            source: 'Node 1',\n            target: 'Node 2',\n        }, {\n            source: 'Node 2',\n            target: 'Node 3',\n        }],\n    }],\n};\n```\n\n在这个例子中，通过将 `layout` 设置为 `'force'`，并调整 `repulsion` 参数来调整节点之间的斥力，可以实现自动排列节点坐标。布局算法会根据节点之间的关系和斥力，自动计算节点的位置。\n\n你可以根据实际需求调整 `repulsion` 和其他参数，以便获得满足你设计需求的图形布局。此外，ECharts 还提供其他布局算法，如环形布局、树状布局等，你可以根据具体情况选择合适的布局算法。",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:01"
    },
    {
        "cid": "ab132efb-fac4-46d9-82ec-ae4c283f180b",
        "index": 1,
        "role": "user",
        "content": "Plotting a graph for atom documents.",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:01"
    },
    {
        "cid": "6b101588-755f-48ec-bd40-25e1fa3abf1c",
        "index": 1,
        "role": "user",
        "content": "Hello Atom, what day is it today?",
        "func_call": None,
        "func_call_params": None,
        "create_time": "2024-01-15 14:25:01"
    },
]


class ChatDBTool:

    @staticmethod
    async def add_chat_info(chat_info_: Dict[str, Any]):
        await ChatInfo.create(**chat_info_)

    @staticmethod
    async def add_chat_message(chat_message_: Dict[str, Any]):
        await ChatMessageInfo.create(**chat_message_)



if __name__ == "__main__":
    run_async(init())

    # for chat_info in chat_infos:
    #     run_async(ChatDBTool.add_chat_info(chat_info))

    for chat_message in chat_messages:
        run_async(ChatDBTool.add_chat_message(chat_message))
