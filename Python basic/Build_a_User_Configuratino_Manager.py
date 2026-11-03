def add_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available"

    formatted_settings = "\n".join(
        f"{key.capitalize()}: {value}" for key, value in settings.items()
    )
    return f"Current User Settings:\n{formatted_settings}\n"


test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
}


print(view_settings(test_settings))
print(add_setting(test_settings, ("language", "indonesian")))
print(update_setting(test_settings, ("volume", "low")))
print(delete_setting(test_settings, "notifications"))
print(view_settings(test_settings))

