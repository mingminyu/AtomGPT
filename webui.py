from nicegui import ui, app
from nicegui.events import ValueChangeEventArguments
from atomui import to_ref
from atomui import webui
from atomui.utils.parser import MarkdownParser
from atomui.mock.markdown import md_message_example
from atomui.components import Router
from atomui.layout.header import chat_header
from atomui.layout.sidebar import chat_sidebar
from atomui.layout.footer import chat_footer
from atomui.layout.body import chat_greet


app.add_static_files('/static', 'static')
md_parser = MarkdownParser()


@ui.page("/")
@ui.page("/{_:path}")
def main():
    router = Router()

    @router.add('/')
    def index():
        ui.label('abc')
        ui.label('abc')
        ui.label('abc')
        ui.label('abc')

    left_drawer = chat_sidebar()
    chat_header(left_drawer)
    chat_box, send_disabled = chat_footer()
    chat_greet(show=send_disabled)

    with ui.row():
        ui.button('One', on_click=lambda: router.open(index)).classes('w-32')

    router.frame()



# @ui.page('/')
# def atom_chat():
#     left_drawer = chat_sidebar()
#     chat_header(left_drawer)
#     chat_box, send_disabled = chat_footer()
#     chat_greet(show=send_disabled)


ui.run(language='zh-CN', port=8082, reload=True)
