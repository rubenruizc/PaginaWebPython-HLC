import reflex as rx
from PaginaWeb.componentes.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://www.twitch.tv/auri_981"),
        link_button("Amaro", "https://books.apple.com/ca/book/recibido/id6443753669"),
        link_button("Betis", "https://www.realbetisbalompie.es/"),
        align="center" 
    )