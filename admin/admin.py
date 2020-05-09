# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:56:47 2020

@author: SahilHP
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    client = MongoClient()
    db = client.silverpos
    # users = 

class AdminApp(App):
    def build(self):
        return AdminWindow()
    
if __name__ == '__main__':
    AdminApp().run()