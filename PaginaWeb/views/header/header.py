import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="RRC", variant="solid"),
            rx.text("@rubenruizcastano", font_size="xl",font_weight="bold",color = "yellow"),
        ),
        rx.text("Hola sigueme, soy Auri",font_size="md",font_weight="bold",color = "red"),
        bg = "green",
        padding_x = "500px",
        padding_y = "16px",
    )