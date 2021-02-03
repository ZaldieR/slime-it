from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Slime-it",
    version = "0.1",
    description = "un rolit revisité ^^",
    executables = [Executable("D:/Users/Mathis/Desktop/Rolit/main.py")],
)