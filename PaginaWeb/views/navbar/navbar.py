import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Home", height="40px",color = "green"),
        rx.text("About", height="40px", color="red"),
        position = "sticky",
        bg = "black",
        padding_x = "500px",
        padding_y = "16px",
        z_index = 999,
    )