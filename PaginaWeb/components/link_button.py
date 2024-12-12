import reflex as rx


def link_button(texto,url) -> rx.Component:
    return rx.button(
            rx.link(
                texto,
                href=url,
                is_external=True,
                color_scheme="blue"
            ),
            color_scheme="red"
            
        )