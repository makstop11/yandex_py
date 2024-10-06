class Figure:
    type_fig: str = 'ellipse'
    color: str = 'red'


# TODO: На доработку (пример уже был в задаче №8)

fig_1 = Figure()

setattr(fig_1, "start_pt", "10, 5")
setattr(fig_1, "end_pt", "100, 20")
setattr(fig_1, "color", "blue")
delattr(fig_1, 'color')

print(fig_1.__dict__)  # Подсказка ко второй части
