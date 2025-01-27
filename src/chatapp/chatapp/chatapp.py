import os
import reflex as rx
from reflex_chat import chat, api


from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")


@rx.page()
def index() -> rx.Component:
    return rx.container(
        rx.box(
            chat(process=api.openai(model="gpt-3.5-turbo")),
            height="100vh",
        ),
        size="2",
    )


# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accent_color="violet",
    ),
)
