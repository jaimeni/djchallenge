# Useful functions
def get_or_none(model, *args, **kwargs):
    try:
        return model.current.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
