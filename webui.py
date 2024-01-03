from markdown_it import MarkdownIt
from typing import List
from nicegui import ui, app
from nicegui.events import ValueChangeEventArguments
from atomui import to_ref
from atomui import webui


app.add_static_files('/static', 'static')

messages = '''
在 ECharts 中，如果你希望自动排列节点坐标，你可以使用布局算法。ECharts 提供了一些布局算法，其中之一是力导向图（Force-directed Graph）布局，它可以自动调整节点的位置，使得图形更加美观。

以下是一个简单的力导向图布局的示例：

```javascript
option = {
    series: [{
        type: 'graph',
        layout: 'force',
        force: {
            repulsion: 100,  // 节点之间的斥力
            edgeLength: 150,  // 连接线的默认长度
        },
        data: [{
            name: 'Node 1',
        }, {
            name: 'Node 2',
        }, {
            name: 'Node 3',
        }],
        links: [{
            source: 'Node 1',
            target: 'Node 2',
        }, {
            source: 'Node 2',
            target: 'Node 3',
        }],
    }],
};
```

在这个例子中，通过将 `layout` 设置为 `'force'`，并调整 `repulsion` 参数来调整节点之间的斥力，可以实现自动排列节点坐标。布局算法会根据节点之间的关系和斥力，自动计算节点的位置。

```python
import os

print(123)
```

你可以根据实际需求调整 `repulsion` 和其他参数，以便获得满足你设计需求的图形布局。此外，ECharts 还提供其他布局算法，如环形布局、树状布局等，你可以根据具体情况选择合适的布局算法。
'''

md_parser = MarkdownIt()


def split_code_block_from_markdown(md_text: str) -> List:
    """split markdown content into code and non-code content list"""
    tokens = [md_token for md_token in md_parser.parse(md_text) if md_token.content != '']
    return tokens





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

        with ui.row().classes("items-center justify-center self-end bg-white"):
            with webui.chip(color="stone-50").classes('text-white-10'):
                webui.avatar(icon="img:static/avatar/default.png", color='blue-2')
                ui.label('draven').classes('font-bold')
                webui.badge('3', color='red', floating=True).props('dense')

                with webui.menu().style('width: 150px'):
                    webui.button(
                        "Settings", icon="settings", color="zinc-50", flat=True, align='left', dense=True
                    ).classes('w-full font-normal')
                    ui.separator()
                    webui.button(
                        "Logout", icon="logout", color="zinc-50", flat=True, align='left', dense=True
                    ).classes('w-full font-normal')

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
                shape="square", align="between", no_caps=True, flat=True, dense=True
            ).classes(
                'flex-grow w-full text-white'
            ).style(
                'width: 220px; background: #777E90; border-radius: 0.5rem'
            )

    send_disabled = to_ref(True)

    def update_send_btn_disabled(e: ValueChangeEventArguments):
        if len(e.value.strip()) == 0:
            send_disabled.value = True
        else:
            send_disabled.value = False

    with ui.column().classes('items-center self-center gap-0 mt-60 mb-0').style('padding-top: 120px') as home_greet:
        ui.avatar(
            icon="img:static/images/site_logo.svg", size="100px", color="white"
            )
        ui.markdown("**How can I help you today?**").classes('text-xl gap-0 mt-0')
    home_greet.bind_visibility_from(send_disabled, 'value')

    with ui.card().classes('w-full max-w-4xl mx-auto my-0 no-shadow border-[0px]'):
        with ui.row().classes('w-full'):
            webui.avatar('img:static/images/site_logo.svg', color=None)
            ui.markdown(
                'This is **good**\n\nThis is **good** This is **good**'
            )
    with ui.card().classes('w-full max-w-4xl mx-auto my-0 no-shadow border-[0px]'):
        with ui.row(wrap=False).classes('w-full'):
            with ui.column():
                webui.avatar('img:static/avatar/default.png', color=None)

            with ui.column():
                for message_token in split_code_block_from_markdown(messages):
                    if message_token.type != 'fence':
                        ui.markdown(message_token.content).classes('w-full')
                    else:
                        ui.code(message_token.content).classes('w-full bg-gray-200')

    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-4xl mx-auto my-6'):
        with ui.row().classes('w-full items-end content-end'):
            chat_box = webui.input(
                placeholder="Message AtomGPT", outlined=True, input_class='mx-3', autogrow=True, item_aligned=True,
                on_change=lambda e: update_send_btn_disabled(e)
            ).classes('flex-grow self-end')

            with chat_box.add_slot('append'):
                # 通过设定 `absolute md:bottom-3 md:right-3` 来使图标沉底固定
                webui.button(
                    icon='send', shape='rounded', flat=True, size='xm', dense=True, disabled=send_disabled
                ).classes('self-center absolute md:bottom-3 md:right-3').style('border-radius: 0.5rem')

        ui.markdown(
            'AtomGPT can make mistakes. Consider checking important information.'
        ).classes('text-xs self-center mr-8 m-[-1em] text-grey')


ui.run(language='zh-CN', port=8082, reload=True)
