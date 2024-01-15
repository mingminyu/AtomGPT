import asyncio
from nicegui import ui, app, run
# from nicegui.elements.chat_message import ChatMessage
from tortoise import Tortoise

# from nicegui.events import ValueChangeEventArguments
# from atomui import to_ref, effect
from atomui import webui
from atomui.components import Router
from atomui.layout.header import chat_header
from atomui.layout.sidebar import chat_sidebar_card
from atomui.layout.footer import chat_footer
from atomui.elements.chatgpt import chat_greet

from atomui.mock.chat_conversation import chat_conversations_example
from atomui.models.chat import ChatCardModel, ChatInfo
from atomui.elements.drawer import DrawerBindableUi
from atomui.utils.parser import MarkdownParser
from atomui.layout.body import chat_messages_card
from atomui.models.chat import ChatMessageModel
from atomui.elements.chatgpt import ChatFooter, ChatSidebar, ChatHeader
from orm.chat import ChatInfo

md_parser = MarkdownParser()
app.add_static_files('/static', 'static')

# chat_cards = [ChatCardModel(**chat_conversation) for chat_conversation in chat_conversations_example]


async def init_db() -> None:
    await Tortoise.init(db_url='sqlite://db.sqlite3', modules={'models': ['orm.chat']})
    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()


app.on_startup(init_db)
app.on_shutdown(close_db)



# def get_chat_card(chat_id: str):
#     for chat_card in chat_cards:
#         if chat_card.cid == chat_id:
#             return chat_card



async def get_chat_infos(username: str):
    return await ChatInfo.filter(username=username).order_by('ts')


@ui.page("/")
@ui.page("/{_:path}")
async def main():
    router = Router()

    @router.add('/')
    def index():
        chat_greet()
        with ui.row().classes("w-full flex justify-center self-center items-center pt-[260px] portrait:pt-[1350px]"):
            with ui.grid(rows=2, columns=2).classes("max-w-6xl self-center items-center"):
                with webui.card(bordered=True).tight().classes('max-w-3xl justify-center self-center items-center'):
                    with webui.card_section().classes('w-3xl'):
                        webui.label("Make a content strategy").classes('text-bold text-blue-10')
                        webui.label("for a newsletter featuring free weekend events").classes('text-grey-6')

                with webui.card(bordered=True).tight().classes('max-w-3xl self-center items-center'):
                    with webui.card_section().classes('w-3xl'):
                        webui.label("Make a content strategy").classes('text-bold text-blue-10')
                        webui.label("for a newsletter featuring free weekend events").classes('text-grey-6')

                with webui.card(bordered=True).tight().classes('max-w-3xl flex justify-center self-center items-center'):
                    with webui.card_section().classes('w-3xl'):
                        webui.label("Make a content strategy").classes('text-bold text-blue-10')
                        webui.label("for a newsletter featuring free weekend events").classes('text-grey-6')

                with webui.card(bordered=True).tight().classes('max-w-3xl flex justify-center self-center items-center'):
                    with webui.card_section().classes('w-3xl'):
                        webui.label("Make a content strategy").classes('text-bold text-blue-10')
                        webui.label("for a newsletter featuring free weekend events").classes('text-grey-6')

        # webui.button('Add new Chat', on_click=lambda: add_new_card(router, chat_sidebar))
        # chat_messages_card(ChatCard(**chat_conversations_example[1]).conversation)

    @router.add('/chat')
    async def chat_home(chat_id: str = None):
        # chat_message = get_chat_card(chat_id)
        # chat_messages_card(chat_message.conversation)
        ...

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
    # for chat_info in await get_chat_infos(username):
    #     print(chat_info)


    # left_drawer = chat_sidebar(router)
    chat_sidebar = ChatSidebar(router=router, chat_infos=chat_infos)
    chat_header = ChatHeader(chat_sidebar)
    # chat_box, send_disabled = chat_footer()
    # ChatFooter(router=router, chat_sidebar=chat_sidebar)

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
