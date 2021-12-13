# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:16:17 2021

@author: Akash
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

Window.size=(500,700)


Builder.load_file("calc.kv")
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text='0'
        
    def button_press(self,button):
        prior = self.ids.calc_input.text
        
        if "Error" in prior:
            prior=""
        
        if prior =="0":
           self.ids.calc_input.text=''
           self.ids.calc_input.text=f'{button}'
           
        else:
           self.ids.calc_input.text=f'{prior}{button}'
           
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
   
        if "+" in prior and "." not in num_list [-1]:
             prior=f'{prior}.'
             self.ids.calc_input.text=prior
        elif "."in prior:
            pass
        else:
        
            prior=f'{prior}.'
            self.ids.calc_input.text=prior
            
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text=prior
        
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
             self.ids.calc_input.text=f'{prior.replace("-","")}'
        else:
             self.ids.calc_input.text=f'-{prior}'
   
           
    def add(self):
         prior = self.ids.calc_input.text
         self.ids.calc_input.text = f'{prior}+'
         
    def subtraction(self):
         prior = self.ids.calc_input.text
         self.ids.calc_input.text = f'{prior}-'
         
    def multiply(self):
         prior = self.ids.calc_input.text
         self.ids.calc_input.text = f'{prior}*'  
         
    def divide(self):
         prior = self.ids.calc_input.text
         self.ids.calc_input.text = f'{prior}/'
         
    def percent(self):
         prior = self.ids.calc_input.text
         self.ids.calc_input.text = f'{prior}%'
         
    def equals(self):
         prior = self.ids.calc_input.text
         try:
             answer = eval(prior)
             self.ids.calc_input.text=str(answer)
         except:
             self.ids.calc_input.text="Error"
             
         #addition
         '''if "+" in prior:
             num_list = prior.split("+")
             answer = 0.0
             for number in num_list:
                 answer=answer+float(number)
                 
             #print answer 
             self.ids.calc_input.text =str( answer)'''

         
  

class CalculatorApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()
if __name__=='__main__':
    CalculatorApp().run()