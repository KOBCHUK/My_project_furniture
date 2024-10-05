from .materials import materials_db
from .production import labor_cost
from .products import required_materials


def calculate_budget(product):
    """Розрахунок загальної вартості виробництва.
    :param product: назва виробу
    :return: загальна вартість виробництва в гривнях
    """
    materials_cost = 0
    labor_cost_value = 0
    if product in ["шафа", "стіл", "стілець"]:
        labor_cost_value = labor_cost(product)
        required_materials_value = required_materials(product)
        for material, amount in required_materials_value.items():
            materials_cost += materials_db[material]["ціна"] * amount
    return materials_cost + labor_cost_value


def generate_report(product):
    """Формування звіту про вартість виробництва.
    :param product: назва виробу
    :return: звіт про вартість виробництва
    """
    total_cost = calculate_budget(product)
    return f"Вартість виробництва {product}: {total_cost} грн"
