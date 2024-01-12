from nicegui import ui, app
# from nicegui.events import ValueChangeEventArguments
# from atomui import to_ref, effect
from atomui import webui
from atomui.components import Router
from atomui.layout.header import chat_header
from atomui.layout.sidebar import chat_sidebar_card
from atomui.layout.footer import chat_footer
from atomui.elements.chatgpt import chat_greet

from atomui.mock.chat_conversation import chat_conversations_example
from atomui.models.chat import ChatCardModel
from atomui.elements.drawer import DrawerBindableUi
from atomui.utils.parser import MarkdownParser
from atomui.layout.body import chat_messages_card
from atomui.models.chat import ChatMessage
from atomui.elements.chatgpt import ChatFooter, ChatSidebar, ChatHeader

md_parser = MarkdownParser()
app.add_static_files('/static', 'static')



chat_cards = [ChatCardModel(**chat_conversation) for chat_conversation in chat_conversations_example]


# def add_new_card(router: Router, left_sidebar: DrawerBindableUi):
#     new_card = chat_sidebar_card(chat_card=ChatCard(**chat_conversations_example[1]), router=router)
#     # 将新卡片加入到 left_sidebar 的 default_slot 中，默认追加到 Today 标签下
#     new_card.element.move(
#         left_sidebar.element.default_slot.children[1], target_index=1
#     )


@ui.page("/")
@ui.page("/{_:path}")
def main():
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
    def chat_home(chat_id: str = None):
        ui.label(chat_id)


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


    # left_drawer = chat_sidebar(router)
    chat_sidebar = ChatSidebar(router=router, chat_cards=chat_cards)
    chat_header = ChatHeader(chat_sidebar)
    # chat_box, send_disabled = chat_footer()
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


ui.run(language='zh-CN', port=8081, reload=True)
