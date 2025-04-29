import flet as ft

class MyApp:

    def main(self, page: ft.Page):
        page.window.width = 375  # Adjusted for mobile width
        page.window.height = 667  # Adjusted for mobile height
        page.add(
            ft.Container(
                content=ft.Text("Hello world 375", width=375, color=ft.colors.RED),
                bgcolor=ft.colors.YELLOW,
                padding=10,
            ),
            ft.Container(
                content=ft.Text("Hello world 512", width=512, color=ft.colors.RED),
                bgcolor=ft.colors.GREEN,
                padding=10, 
            ),
        )

    def run(self):
        ft.app(target=self.main)

if __name__ == "__main__":
    app = MyApp()
    app.run()