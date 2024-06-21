from pyshortcuts import make_shortcut

# Параметры скрипта и ярлыка
script = "C:/Users/User/Desktop/Calculations/FilterCalculationApp.py"
icon = "C:/Users/User/Desktop/Calculations/App_icon_1.3_Update.png.ico"
name = "Filter Calculation App"
description = "Shortcut for Filter Calculation Application"

# Создание ярлыка
shortcut = make_shortcut(
    script=script,
    name=name,
    description=description,
    icon=icon
)

# Сохранение ярлыка на рабочем столе
shortcut.save()
