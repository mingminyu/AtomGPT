from nicegui import ui, app
# from nicegui.events import ValueChangeEventArguments
# from atomui import to_ref, effect
from atomui import webui

# from atomui.mock.markdown import markdown_content_example
from atomui.components import Router
from atomui.layout.header import chat_header
from atomui.layout.sidebar import chat_sidebar, chat_sidebar_card
from atomui.layout.footer import chat_footer
from atomui.layout.body import chat_greet

# from atomui import ref_computed, to_ref
from atomui.mock.chat_conversation import chat_conversation_example
from atomui.models.chat import ChatCard
from atomui.elements.drawer import DrawerBindableUi
from atomui.utils.parser import MarkdownParser
from atomui.layout.body import chat_messages_card
from atomui.models.chat import ChatMessage

md_parser = MarkdownParser()


app.add_static_files('/static', 'static')



def add_new_card(router: Router, left_sidebar: DrawerBindableUi):
    new_card = chat_sidebar_card(chat_card=ChatCard(**chat_conversation_example[0]), router=router)
    new_card.element.move(left_sidebar.element)



@ui.page("/")
@ui.page("/{_:path}")
def main():
    router = Router()

    @router.add('/')
    def index():
        # webui.button('Add new Chat', on_click=lambda: add_new_card(router, left_drawer))
        chat_messages_card(ChatCard(**chat_conversation_example[1]).conversation)
        # chat_conversation_msg(ChatCard(**chat_conversation_example[0]).conversation[1])

        # chat_message = ChatCard(**chat_conversation_example[1]).conversation[1]
        # if chat_message.role == "user":
        #     avatar = "img:/static/avatar/default.png"
        # else:
        #     avatar = "img:/static/avatar/logo.svg"
        #
        # with ui.row(wrap=True).classes(
        #         'w-full items-center self-center w-[900px] max-w-8xl landscape:mx-60 portrait:mx-40'):
        #     with webui.card(bordered=False).classes('w-full min-w-3xl max-w-4xl my-1 no-shadow'):
        #         with webui.card_section(horizontal=True):
        #             webui.avatar(avatar, color=None).props('dense flat')
        #
        #             with ui.column().classes('self-center pr-8'):
        #                 for message_token in md_parser.split_code_block_content(chat_message.value):
        #                     if message_token.type != 'fence':
        #                         ui.markdown(message_token.content).classes('w-full')
        #                     else:
        #                         ui.code(message_token.content).classes('w-full bg-gray-200')




            # with ui.row(wrap=False).classes('w-full'):
            #     with ui.column():
            #         webui.avatar(avatar, color=None).props('dense flat')
            #
            #     with ui.column():
            #         for message_token in md_parser.split_code_block_content(chat_message.value):
            #             if message_token.type != 'fence':
            #                 ui.markdown(message_token.content).classes('w-full')
            #             else:
            #                 ui.code(message_token.content).classes('w-full bg-gray-200')

    def var_index(uid: str):
        webui.label(f'uid: {uid}')

    left_drawer = chat_sidebar(router)
    chat_header(left_drawer)
    chat_box, send_disabled = chat_footer()
    chat_greet(show_ref=send_disabled)

    router.add_parameters_url('/c/c1', var_index)
    router.add_parameters_url('/c/c2', var_index)
    router.frame()



ui.run(language='zh-CN', port=8081, reload=True)
