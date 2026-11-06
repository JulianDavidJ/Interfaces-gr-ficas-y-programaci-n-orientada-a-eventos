# Contador interactivo con Flet

Aplicación mínima en Python que usa la biblioteca **Flet** para mostrar un contador que responde a clics del mouse y a pulsaciones del teclado.



## Biblioteca seleccionada: Flet

Flet es un framework para construir aplicaciones interactivas de escritorio, web y móviles usando solo Python. Sus controles están basados en widgets de Flutter, por lo que no hace falta saber HTML, CSS ni JavaScript.

## Instalación y ejecución

Requisitos: **Python 3.10 o superior** (macOS 12+, Windows 10/11 de 64 bits, o Debian/Ubuntu recientes).

```bash
git clone <https://github.com/JulianDavidJ/Interfaces-gr-ficas-y-programaci-n-orientada-a-eventos>
cd flet-contador

python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

flet run main.py          # ventana de escritorio
# flet run --web main.py  # alternativa: en el navegador
```

También funciona con `python main.py`.

## Cómo usar la aplicación

| Acción del usuario | Resultado |
|---|---|
| Clic en **Sumar 1** | El contador aumenta en 1 |
| Tecla **Enter** | El contador aumenta en 1 |
| Clic en **Reiniciar** o tecla **R** | El contador vuelve a 0 |

## Explicación del funcionamiento

1. **Ventana principal.** Flet llama a `main(page: ft.Page)` y le entrega un objeto `Page`, que representa la ventana. Se configura con `page.title` y las alineaciones. La app se inicia con `ft.run(main)`.
2. **Componentes gráficos.** Se crean `ft.Text` (el número y el mensaje de estado), `ft.Button` y `ft.OutlinedButton`. Los botones se agrupan en un `ft.Row`. Todo se muestra con `page.add(...)`.
3. **Eventos implementados.**
   * **Clic:** el parámetro `on_click` de cada botón recibe la función a ejecutar.
   * **Teclado:** se asigna una función a `page.on_keyboard_event`; Flet la invoca con un `KeyboardEvent` cuya propiedad `e.key` indica la tecla (por ejemplo `"Enter"`).
4. **Funciones que responden.** `incrementar(e)` y `reiniciar(e)` modifican la variable `contador`; `al_presionar_tecla(e)` decide cuál llamar según la tecla.
5. **Cómo cambia la interfaz.** `actualizar_vista()` asigna el nuevo valor a `texto_contador.value` y `texto_estado.value`, y luego llama a `page.update()`, que envía los cambios y redibuja la pantalla.

## Investigación

**1. ¿Qué es y para qué sirve?** Flet es una biblioteca de Python para crear interfaces gráficas interactivas multiplataforma sin conocimientos de tecnologías web. Su propósito es que un desarrollador Python construya aplicaciones modernas con poco código.

**2. ¿Qué aplicaciones permite desarrollar?** Aplicaciones de escritorio (Windows, macOS, Linux), web y móviles (iOS/Android). Un mismo código puede ejecutarse como ventana nativa (`flet run`) o en el navegador (`flet run --web`).

**3. Instalación y requisitos.** `pip install flet` (o `pip install 'flet[all]'`). Requiere Python 3.10 o superior. Se recomienda usar un entorno virtual y se puede verificar con `flet doctor`.

**4. Componentes principales.** `Page` (la ventana), controles de texto (`Text`, `TextField`), botones (`Button`, `OutlinedButton`, `TextButton`, `IconButton`), contenedores y diseño (`Container`, `Row`, `Column`) y muchos otros controles basados en Material Design.

**5. Manejo de eventos.** Cada control expone propiedades `on_*` (por ejemplo `on_click`, `on_hover`, `on_focus`, `on_long_press` en los botones) a las que se asigna una función. El teclado se captura globalmente con `page.on_keyboard_event`, que entrega `key`, `shift`, `ctrl`, `alt` y `meta`.

**6. Ventajas y limitaciones frente a Tkinter.**

| | Flet | Tkinter |
|---|---|---|
| Instalación | Requiere `pip install` | Viene con Python |
| Apariencia | Moderna (Material Design) | Clásica, más básica |
| Plataformas | Escritorio, web y móvil | Solo escritorio |
| Actualización de la UI | Hay que llamar a `page.update()` | Se actualiza al cambiar el widget |
| Estabilidad de la API | Joven: cambió entre versiones (p. ej. `ft.app`/`ft.icons` → `ft.run`/`ft.Icons`) | Muy estable |
| Tamaño y dependencias | Más pesado (ejecutable cliente basado en Flutter) | Ligero |
| Documentación y comunidad | Creciente, pero menor | Muy extensa |

## Fuentes consultadas

* Flet – Documentación oficial: https://docs.flet.dev
* Flet – Instalación: https://docs.flet.dev/getting-started/installation
* Flet – Control `Button` (clics): https://docs.flet.dev/controls/button
* Flet – Atajos de teclado: https://docs.flet.dev/cookbook/keyboard-shortcuts
* Flet – `KeyboardEvent`: https://docs.flet.dev/types/keyboardevent
* Flet en PyPI: https://pypi.org/project/flet
