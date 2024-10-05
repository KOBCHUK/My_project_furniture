# Структури даних для опису виробів
products_db = {
    "шафа": {"об'єм": 0.5, "вага": 30, "площа": 1.5},
    "стіл": {"об'єм": 0.25, "вага": 20, "площа": 0.8},
    "стілець": {"об'єм": 0.1, "вага": 10, "площа": 0.4},
}


def calculate_volume(product):
    """Розрахунок об'єму виробу.
    :param product: назва виробу
    :return: об'єм виробу
    """
    return products_db[product]["об'єм"]


def calculate_weight(product):
    """Розрахунок ваги виробу.
    :param product: назва виробу
    :return: вага виробу
    """
    return products_db[product]["вага"]


def calculate_surface_area(product):
    """Розрахунок площі поверхні виробу.
    :param product: назва виробу
    :return: площа поверхні виробу
    """
    return products_db[product]["площа"]


def required_materials(product):
    """Визначення необхідних матеріалів для виробу.
    :param product: назва виробу
    :return: словник з необхідними матеріалами
    """
    if product == "шафа":
        return {"дошка": 5, "фурнітура": 4}
    elif product == "стіл":
        return {"плита": 1, "фурнітура": 2}
    elif product == "стілець":
        return {"дошка": 2, "фурнітура": 1}
    return {}
