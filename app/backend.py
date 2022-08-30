import eel


@eel.expose  # Expose function to JavaScript
def get_text(x):
    return "Message from python! " + x