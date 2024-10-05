from .materials import materials_db


def production_time(product):
    """Розрахунок часу виробництва виробу.
    :param product: назва виробу
    :return: час виробництва в годинах
    """
    if product == "шафа":
        return 10  # години
    elif product == "стіл":
        return 5  # години
    elif product == "стілець":
        return 3  # години
    return 0


def labor_cost(product):
    """Розрахунок трудомісткості виробу.
    :param product: назва виробу
    :return: вартість праці в гривнях
    """
    return production_time(product) * 100  # 100 грн/година


def production_cost(product):
    """Розрахунок вартості виробництва.
    :param product: назва виробу
    :return: загальна вартість виробництва в гривнях
    """
    materials_cost = 0
    required_materials = {
        "шафа": {"дошка": 5, "фурнітура": 4},
        "стіл": {"плита": 1, "фурнітура": 2},
        "стілець": {"дошка": 2, "фурнітура": 1},
    }
    for material, amount in required_materials[product].items():
        if material in materials_db:
            materials_cost += materials_db[material]["ціна"] * amount
    return materials_cost + labor_cost(product)
