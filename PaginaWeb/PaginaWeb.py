import reflex as rx
from PaginaWeb.views.navbar.navbar import navbar
from PaginaWeb.views.header.header import header
from PaginaWeb.views.links.links import links
from PaginaWeb.views.footer.footer import footer

class State (rx.State):
    pass

def index () -> rx.Component:
    return rx.vstack(
        navbar(), 
        header(),
        links(),
        footer(),
        align="center"
    )

app = rx.App()
app.add_page(index)
app._compile()