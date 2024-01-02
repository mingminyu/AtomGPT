from nicegui import ui, app
from nicegui.events import ValueChangeEventArguments
from atomui import to_ref
from atomui import webui


app.add_static_files('/static', 'static')


@ui.page('/')
def atom_chat():
    toggle_icon = to_ref("format_indent_decrease")

    with (
        ui.header(elevated=True, add_scroll_padding=True)
        .classes("self-center items-center justify-between")
        .style("background: white; height: 55px")
    ):
        def _change_toggle_icon():
            """改变侧滑按钮的图标"""
            if toggle_icon.value == "format_indent_decrease":
                toggle_icon.value = "format_indent_increase"
            else:
                toggle_icon.value = "format_indent_decrease"

            left_drawer.toggle()

        webui.button(
            icon=toggle_icon, color="primary", flat=True, dense=True,
            on_click=_change_toggle_icon
        )

        with ui.row().classes("items-center justify-center self-end").style("background: white"):
            with webui.button(
                    icon='img:static/avatar/default.png',
                    color='blue-2', size="10px",
                    shape="round"
            ):
                webui.badge('3', color='red').props('dense floating')

                with webui.menu().style('width: 150px') as user_menu:
                    webui.button(
                        "Settings", icon="settings", color=None, flat=True, align='left').classes('w-full')
                    ui.separator()
                    # logout_menu = webui.menu_item("Logout")
                    webui.button(
                        "Logout", icon="logout", color=None, flat=True, align='left').classes('w-full')


    with webui.drawer(
            side="left",
            value=True,
            top_corner=True,
            bottom_corner=True,
            fixed=True,
            bordered=True,
            elevated=True,
            overlay=False,
            show_if_above=False,
            width="260",
    ).style('background: #777E90') as left_drawer:
        with ui.row().classes('items-center justify-center'):
            webui.button(
                "New Chat", icon="img:static/images/site_logo.svg", icon_right="edit", color="#777E90",
                shape="square", align="between", no_caps=True, flat=True
            ).classes(
                'flex-grow w-full text-white'
            ).style(
                'width: 220px; background: #777E90; border-radius: 0.5rem'
            )

    send_disabled = to_ref(True)

    def update_send_btn_disabled(e: ValueChangeEventArguments):
        if len(e.value) == 0:
            send_disabled.value = True
        else:
            send_disabled.value = False

    with ui.column().classes('items-center self-center').style('padding-top: 120px; gap: 0') as home_greet:
        ui.avatar(
            icon="img:static/images/site_logo.svg", size="100px", color="white"
            ).style('height: 80px')
        ui.markdown("**How can I help you today?**").classes('text-xl')
    home_greet.bind_visibility_from(send_disabled, 'value')

    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-4xl mx-auto my-6'):
        with ui.row().classes('w-full items-center'):
            chat_box = webui.input(
                placeholder="Message AtomGPT", outlined=True, input_class='mx-3',
                on_change=lambda e: update_send_btn_disabled(e)
            ).classes('flex-grow')

            with chat_box.add_slot('append'):
                webui.button(
                    icon='send', shape='square', flat=True, size='xm', dense=True, disabled=send_disabled
                ).style('border-radius: 0.5rem')

        ui.markdown(
            'AtomGPT can make mistakes. Consider checking important information.'
        ).classes('text-xs self-center mr-8 m-[-1em] text-grey')


ui.run(language='zh-CN', port=8082, reload=True)
