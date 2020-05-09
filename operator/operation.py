# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:58:46 2020

@author: SahilHP
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

import re

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cart = []
        self.qty = []
        self.total = 0.00
        
    def update_purchases(self):
        pcode= self.ids.code_inp.text
        products_container = self.ids.products_container
        
        if pcode == '1234' or '2345':
            
            details = BoxLayout(size_hint_y=None, height=30,
                               pos_hint={'top': 1})
            products_container.add_widget(details)
            
            code = Label(text=pcode, size_hint_x=0.2,color=(0.06, 0.45, 0.45, 1))
            name = Label(text='Product One', size_hint_x=0.3, color=(0.06, 0.45, 0.45, 1))
            qty = Label(text='1', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            disc = Label(text='0.00', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            price = Label(text='0.00', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            total = Label(text='0.00', size_hint_x=0.2, color=(0.06, 0.45, 0.45, 1))
            
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)
            
            #Update preview
            pname = 'Product One'
            if pcode == '2345':
                pname = 'Product Two'
            pprice = 1.00
            pqty = str(1)
            self.total += pprice
            purchase_total = '`\n\nTotal\t\t\t\t\t\t\t\t'+str(self.total)
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            
            self.ids.curr_product.text = pname
            self.ids.curr_price.text = str(pprice)
            
            
            if _prev > 0:
                prev_text = prev_text[:_prev]
                
            ptarget = -1
            for i, c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i
                    
            if ptarget >= 0:
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\t\tx\d\t' % (pname)
                rexpr = pname + '\t\tx' + str(pqty) + '\t'
                nu_text = re.sub(expr, rexpr, prev_text)
                preview.text = nu_text + purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                nu_preview = '\n'.join([prev_text, pname+'\t\tx' + pqty +
                                        '\t\t'+str(pprice), purchase_total])
                preview.text = nu_preview
                
        

class OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()
    