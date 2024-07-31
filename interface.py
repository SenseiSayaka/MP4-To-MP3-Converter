import flet as ft
import threading
from converter import convert_mp4_to_mp3

def main(page: ft.Page):
    page.title = "Converter Mp4 to Mp3"
    page.update()
    def selected_file(e: ft.FilePickerResultEvent):
        if e.files:
            selected_path = e.files[0].path

            def convert_and_update():
                result_message = convert_mp4_to_mp3(selected_path)
                page.snack_bar = ft.SnackBar(ft.Text(result_message))
                page.snack_bar.open = True
                page.update()

            threading.Thread(target=convert_and_update).start()

    # Создаем file_picker здесь
    file_picker = ft.FilePicker(on_result=selected_file)  
    page.overlay.append(file_picker)

    def pick_file(e):
        file_picker.pick_files()
        page.update()
    page.add(
    ft.Row(
        [
            ft.ElevatedButton(text="Pick File", on_click=pick_file, color=ft.colors.WHITE),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update() 

ft.app(target=main)