import asyncio
from nicegui import ui, app, run
from tortoise import Tortoise
from typing import List

from atomui import webui
from atomui.components import Router
from atomui.elements.chatgpt import chat_greet

from atomui.utils.parser import MarkdownParser
from atomui.elements.chatgpt import ChatFooter, ChatSidebar, ChatHeader, ChatMessageCard1, ChatSampleCard
from orm.chat import ChatInfo, ChatMessageInfo

# from atomui.layout.header import chat_header
# from atomui.layout.footer import chat_footer
# from atomui.layout.body import chat_messages_card
# from atomui.layout.sidebar import chat_sidebar_card
# from atomui.elements.drawer import DrawerBindableUi
# from atomui.mock.chat_conversation import chat_conversations_example
# from atomui.models.chat import ChatMessageModel
# from atomui.models.chat import ChatCardModel, ChatInfo

md_parser = MarkdownParser()
app.add_static_files('/static', 'static')


async def init_db() -> None:
    await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['orm.chat']})
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()


app.on_startup(init_db)
app.on_shutdown(close_db)


async def get_chat_infos(username: str) -> List[ChatInfo]:
    from datetime import datetime, timedelta
    thirty_days_ago = datetime.now() - timedelta(days=30)
    return await ChatInfo.filter(username=username, status=True, ts__gte=thirty_days_ago).order_by('ts')


async def get_chat_messages(chat_id: str) -> List[ChatMessageInfo]:
    return await ChatMessageInfo.filter(cid=chat_id).order_by('index')


chat_sample_cards = [
    {
        "title": "Make a content strategy",
        "description": "for a newsletter featuring free weekend events",
        "user_input": "Make a content strategy for a newsletter featuring free weekend events"
    },
    {
        "title": "Create a personal webpage",
        "description": "for a newsletter featuring free weekend events",
        "user_input": "Create a personal webpage for me, all in a single file. Ask me 3 questions first on whatever you need to know."
    },
    {
        "title": "Plan a trip",
        "description": "to see the best of New York in 3 days",
        "user_input": "I'll be in New York for 3 days. Can you recommend what I should do to see the best of the city?"
    },
    {
        "title": "Show me a code snippet",
        "description": "of a website's sticky header",
        "user_input": "Show me a code snippet of a website's sticky header in CSS and JavaScript."
    },
]


@ui.page("/")
@ui.page("/{_:path}")
async def main():
    router = Router()

    @router.add('/')
    def index():
        # ui.label("下面试试 tw css 的")
        # ui.label("随屏幕大小，颜色变化").classes("max-[2800px]:pt-[60px] min-[1800px]:pt-[360px]")

        chat_greet()
        sample_cards_grid_css = (
            "w-full flex justify-center self-center items-center portrait:pt-[1350px] "
            "max-[2800px]:pt-[260px] min-[1800px]:pt-[360px]"
        )
        with ui.row().classes(sample_cards_grid_css):
            with ui.grid(rows=2, columns=2).classes("max-w-6xl self-center items-center"):
                for sample_card_info in chat_sample_cards:
                    ChatSampleCard(
                        title=sample_card_info['title'],
                        description=sample_card_info['description'],
                        user_input=sample_card_info['user_input']
                    )

    @router.add('/chat')
    async def chat_home(chat_id: str = None):
        chat_messages = await get_chat_messages(chat_id)
        for message in chat_messages:
            ChatMessageCard1(message)


    @router.add('/echarts_graph')
    def example_npm_graph():
        import json

        with open('static/data/les-miserables.json', 'r') as f:
            graph = json.loads(f.read())

        legend_cates = [cate['name'] for cate in graph['categories']]

        with webui.row().classes('w-full justify-center self-center items-self'):
            ui.echart({
                "title": {
                    "text": "Less Miserables",
                    "top": 'bottom',
                    "left": 'right',
                },
                "tooltip": {},
                'legend': {
                    'data': legend_cates
                },
                "animationDuration": 1500,
                "animationEasingUpdate": "quinticInOut",
                'series': [
                    {
                        "name": "Less Miserables",
                        "type": "graph",
                        "layout": "none",
                        "data": graph['nodes'],
                        "links": graph['links'],
                        "categories": graph['categories'],
                        "roam": True,
                        "label": {
                            "position": "right",
                        },
                        "lineStyle": {
                            "color": "source",
                            "curveness": 0.3,
                        },
                        "emphasis": {
                            "focus": "adjacency",
                            "lineStyle": {
                                "width": 10
                            }
                        }
                    }
                ],
            }).classes('w-full max-w-3xl h-[700px] flex justify-center self-center items-self')


    app.storage.user.update({"username": "draven"})
    username = app.storage.user.get("username")
    chat_infos = await get_chat_infos(username)

    chat_sidebar = ChatSidebar(router=router, chat_infos=chat_infos)
    chat_header = ChatHeader(chat_sidebar)
    ChatFooter(router=router, chat_sidebar=chat_sidebar)

    router.frame().classes('w-full')

    ui.add_head_html(
        """
        <style>
            .chat-card .q-input 
                .q-field__control{height:32px}

            .chat-card .q-input .q-field__control
                .q-field__marginal{height: 32px; font-size: small}

            .user-setting .q-btn .q-icon{font-size: 1.3em}
        </style>
        """
    )


ui.run(language='zh-CN', port=8081, reload=True, storage_secret="test")
