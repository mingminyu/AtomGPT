from nicegui import ui, app
# from nicegui.events import ValueChangeEventArguments
# from atomui import to_ref, effect
from atomui import webui
from atomui.components import Router
from atomui.layout.header import chat_header
from atomui.layout.sidebar import chat_sidebar, chat_sidebar_card
from atomui.layout.footer import chat_footer
from atomui.layout.body import chat_greet

from atomui.mock.chat_conversation import chat_conversations_example
from atomui.models.chat import ChatCard
from atomui.elements.drawer import DrawerBindableUi
from atomui.utils.parser import MarkdownParser
from atomui.layout.body import chat_messages_card
from atomui.models.chat import ChatMessage

md_parser = MarkdownParser()


app.add_static_files('/static', 'static')



def add_new_card(router: Router, left_sidebar: DrawerBindableUi):
    new_card = chat_sidebar_card(chat_card=ChatCard(**chat_conversations_example[0]), router=router)
    new_card.element.move(left_sidebar.element)



@ui.page("/")
@ui.page("/{_:path}")
def main():
    router = Router()

    @router.add('/')
    def index():
        # webui.button('Add new Chat', on_click=lambda: add_new_card(router, left_drawer))
        chat_messages_card(ChatCard(**chat_conversations_example[1]).conversation)

    def var_index(uid: str):
        webui.label(f'uid: {uid}')

    left_drawer = chat_sidebar(router)
    chat_header(left_drawer)
    chat_box, send_disabled = chat_footer()
    chat_greet(show_ref=send_disabled)

    ui.add_head_html(
        """
        <style>
            .chat-card .q-input 
                .q-field__control{height:32px}
            
            .chat-card .q-input .q-field__control
                .q-field__marginal{height:32px; font-size:small}
        </style>
        """
    )

    # router.add_parameters_url('/c/c1', var_index)
    # router.add_parameters_url('/c/c2', var_index)
    router.frame().classes('w-full')



ui.run(language='zh-CN', port=8081, reload=True)
