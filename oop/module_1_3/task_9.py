class Figure:
    type_fig: str = 'ellipse'
    color: str = 'red'


fig_1 = Figure()

setattr(fig_1, 'start_pt', (10, 5))
setattr(fig_1, 'end_pt', (100, 20))
setattr(fig_1, 'color', 'blue')
delattr(fig_1, 'color')

attrs: dict = fig_1.__dict__

for key in attrs.keys():
    print(key, end=" ")
print()

for key in attrs:
    print(key, end=" ")
print()

# print(attrs.items())
# dict_items([
#     ('start_pt', (10, 5)),
#     ('end_pt', (100, 20)),
# ])

# print(attrs.keys())
# dict_keys(["start_pt", "end_pt"])

# print(attrs.values())
# dict_values([(10, 5), (100, 20)])
