class TravelBlog:
    total_blogs: int = 0


print(f"Количество блогов: {TravelBlog.total_blogs}\n")

# -------------------------

tb_1 = TravelBlog()
# tb_1.name = "Франция"
setattr(tb_1, "name", "Франция")
setattr(tb_1, "days", "6")
# TravelBlog.total_blogs += 1
TravelBlog.total_blogs = TravelBlog.total_blogs + 1

print(f"Страна: {tb_1.name}, день {tb_1.days}")
print(f"Количество блогов: {TravelBlog.total_blogs}\n")

# -------------------------

tb_2 = TravelBlog()
setattr(tb_2, "name", "Италия")
setattr(tb_2, "days", "5")
TravelBlog.total_blogs = TravelBlog.total_blogs + 1

print(f"Страна: {tb_2.name}, день {tb_2.days}")
print(f"Количество блогов: {TravelBlog.total_blogs}")
