# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:52:10 2020

@author: SahilHP
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        info = self.ids.info
        
        uname = self.ids.username_field.text
        pwd = self.ids.pwd_field.text
        
        if uname == '' or pwd == '':
            info.text = '[color=#FF0000]Username and/or password required![/color]'
        else:
            if uname == 'admin' and pwd == 'admin':
                info.text = '[color=#00FF00]Logged in successfully![/color]'
            else:
                info.text = '[color=#FF0000]Username and/or password incorrect![/color]'
                uname = ''
                pwd = ''
                


class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == '__main__':
    sa = SigninApp()
    sa.run()