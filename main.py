# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import kivy
import libusb
import nfc


kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

with nfc.ContactlessFrontend('udp') as clf:
    print(clf)
# clf.nfc.ContactlessFrontend("usb")
# class MyRoot(BoxLayout):
#     def __init__(self):
#         super(MyRoot, self).__init__()
#
#     def generate_number(self):
#         self.random_label.text = str(random.randint(0, 1000))
#
#
# class NeuralRandom(App):
#     def build(self):
#         return MyRoot()

class LoginWindow(Screen):
    pass


class SignUpWindow(Screen):
    pass


class ScanItemWindow(Screen):
    pass

class CartWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass



# # Inner window to hopefully display different pages without changing window
# class InnerWindowManager(ScreenManager):
#     pass
#
#     # Page for displaying the button to use the NFC
#
#
# class ButtonDisplayPage(Screen):
#     pass
#
#     # Page for displaying the item that has been scanned
#
#
# class ItemDisplayPage(Screen):
#     pass


# class AppLogin(BoxLayout):
#     pass

kv = Builder.load_file("nfspeed.kv")


class NFSpeed(App):
    def build(self):
        Window.size = (360, 640)
        return kv
    # neuralRandom = NeuralRandom()


# # neuralRandom.run()

NFSpeed().run()
