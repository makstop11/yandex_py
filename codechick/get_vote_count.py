# https://codechick.io/challenges/111


def get_vote_count(votes):
    keys = ['лайки', 'дизлайки']

    # for key in keys:
    #     if key not in votes:
    #         raise ValueError(
    #             "Некорректные входные данные, "
    #             f"ключ '{key}' не существует"
    #         )

    # if 'лайки' not in votes or 'дизлайки' not in votes:
    #     raise ValueError("Некорректные входные данные")

    return votes[keys[0]] - votes[keys[1]]


print(get_vote_count({"лайки": 13, "дизлайки": 0}))
print(get_vote_count({"лайки1": 2, "дизлайки2": 33}))
print(get_vote_count({"лайки": 132, "дизлайки": 132}))
