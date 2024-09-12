from user_data import UserData


if __name__ == "__main__":
    user_1 = UserData(
        "Иван",
        "Иванов",
        "Ivanov",
        "********",
        "ул. Первомайская д. 3",
        "362819203",
        "Ivanov@gmail.com",
        39,
    )
    user_1

    print("===" * 30)

    user_2 = user_1.clone()
    user_2.name = "София"
    user_2.surname = "Смирнова"
    user_2.login = "Smirnova"
    user_2.password = "#########"
    user_2.address = "ул.Красноармейская д. 7"
    user_2.phone = "264839201"
    user_2.email = "Smirnova@mail.ru"
    user_2.age = 27
    user_2.__post_init__()
