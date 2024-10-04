# База даних матеріалів
materials_db = {
    "дошка": {"розмір": "200x20 см", "ціна": 50, "щільність": 0.7},
    "плита": {"розмір": "250x120 см", "ціна": 150, "щільність": 0.9},
    "фурнітура": {"ціна": 10},
}


def calculate_materials_needed(product, material_requirements):
    """Розрахунок необхідної кількості матеріалів для виробу.
    :param product: назва виробу
    :param material_requirements: словник з вимогами до матеріалів
    :return: словник з необхідними матеріалами
    """
    required_materials = {}
    for material, amount in material_requirements.items():
        if material in materials_db:
            required_materials[material] = amount
    return required_materials


def optimize_cutting(material_size, required_size):
    """Оптимізація розкрою матеріалів.
    :param material_size: розмір матеріалу
    :param required_size: розмір необхідного вирізу
    :return: кількість вирізів
    """
    return material_size // required_size
