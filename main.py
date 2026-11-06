"""Contador interactivo con Flet.

Demuestra:
  * Creación de la ventana principal (ft.Page).
  * Componentes gráficos: Text y Button.
  * Eventos del usuario: clic del mouse (on_click) y teclado (on_keyboard_event).
  * Una función que procesa la interacción y actualiza la interfaz.
"""

import flet as ft


def main(page: ft.Page):
    # --- 1. Configuración de la ventana principal -------------------------
    page.title = "Contador interactivo con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Estado de la aplicación
    contador = 0

    # --- 2. Componentes gráficos ------------------------------------------
    texto_contador = ft.Text(value="0", size=80, weight=ft.FontWeight.BOLD)
    texto_estado = ft.Text(
        value="Presiona el botón o la tecla Enter para sumar.",
        size=16,
    )

    # --- 3. Funciones que responden a los eventos -------------------------
    def actualizar_vista(mensaje: str):
        """Refleja el valor actual del contador en la interfaz."""
        texto_contador.value = str(contador)
        texto_estado.value = mensaje
        page.update()  # le indica a Flet que redibuje los cambios

    def incrementar(e):
        """Evento: clic en el botón 'Sumar 1'."""
        nonlocal contador
        contador += 1
        actualizar_vista(f"Contador incrementado a {contador}")

    def reiniciar(e):
        """Evento: clic en el botón 'Reiniciar'."""
        nonlocal contador
        contador = 0
        actualizar_vista("Contador reiniciado")

    def al_presionar_tecla(e: ft.KeyboardEvent):
        """Evento de teclado: Enter suma 1, R reinicia."""
        if e.key == "Enter":
            incrementar(e)
        elif e.key.upper() == "R":
            reiniciar(e)

    # --- 4. Conexión de eventos y armado de la pantalla -------------------
    page.on_keyboard_event = al_presionar_tecla

    page.add(
        texto_contador,
        texto_estado,
        ft.Row(
            controls=[
                ft.Button(content="Sumar 1", on_click=incrementar),
                ft.OutlinedButton(content="Reiniciar", on_click=reiniciar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


if __name__ == "__main__":
    ft.run(main)
