

class keyevent(PyKeyboardEvent):
    def __init__(self):
        super(keyevent, self).__init__()

    def tap(self, keycode, character, press):
        print('event: tab, keycode: {}, character: {}'.format(keycode, character))

if __name__ == "__main__":
    k = keyevent()
    k.daemon = False
    k.start()
    print("Capturing keyboard")
    k.stop()
