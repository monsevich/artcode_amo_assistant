def extract_lead_id(data):
    """
    Извлекает ID сделки из webhook amoCRM.
    Структура может отличаться в зависимости от типа события.
    """
    # Пример для webhook "leads" → "add" или "update"
    try:
        if "leads" in data and "add" in data["leads"]:
            return data["leads"]["add"][0]["id"]
        if "leads" in data and "update" in data["leads"]:
            return data["leads"]["update"][0]["id"]
        # Добавить другие варианты, если потребуется
    except Exception as e:
        print(f"Ошибка при извлечении lead_id: {e}")
    return None

def extract_fields(data):
    """
    Извлекает все основные поля сделки (примерно для MVP).
    """
    try:
        # Структура webhook может отличаться!
        if "leads" in data and "add" in data["leads"]:
            return data["leads"]["add"][0]
        if "leads" in data and "update" in data["leads"]:
            return data["leads"]["update"][0]
        # Добавить другие варианты, если потребуется
    except Exception as e:
        print(f"Ошибка при извлечении полей сделки: {e}")
    return {}
