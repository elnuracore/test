import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")

    greeting_history = []

    history_text = ft.Text("История приветствий:")

    def on_button_click(_):
        name = name_input.value.strip()
        now = datetime.now()

        timestamp = now.strftime("%y:%m:%d - %H:%M:%S")
        hour = now.hour

        if name:
            greeting_text.value = f"{timestamp} Hello {name}"
            greeting_text.color = None

            greeting_history.append({
                "timestamp": timestamp,
                "hour": hour,
                "name": name
            })

            history_text.value = "История приветствий:\n" + \
                "\n".join(f"{item['timestamp']} - {item['name']}" for item in greeting_history)

            name_input.value = ""
        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click, expand=True)

    send_button = ft.ElevatedButton("send", on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)

    def show_morning(_):
        filtered = []
        for item in greeting_history:
            if item["hour"] < 12:
                filtered.append(f"{item['timestamp']} - {item['name']}")

        if filtered:
            history_text.value = "Утренние приветствия:\n" + "\n".join(filtered)
        else:
            history_text.value = "Нет утренних приветствий"

        page.update()

    morning_button = ft.TextButton("Показать утренние", on_click=show_morning)

    def show_evening(_):
        filtered = []
        for item in greeting_history:
            if item["hour"] >= 12:
                filtered.append(f"{item['timestamp']} - {item['name']}")

        if filtered:
            history_text.value = "Вечерние приветствия:\n" + "\n".join(filtered)
        else:
            history_text.value = "Нет вечерних приветствий"

        page.update()

    evening_button = ft.TextButton("Показать вечерние", on_click=show_evening)

    page.add(
        ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([name_input, send_button], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([morning_button, evening_button, clear_button],
               alignment=ft.MainAxisAlignment.CENTER),

        history_text
    )

ft.app(target=main)
