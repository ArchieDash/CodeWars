def validate_pin(pin):
    if pin.isdigit() and len(pin) in (4,6):
        return True
    else:
        return False
