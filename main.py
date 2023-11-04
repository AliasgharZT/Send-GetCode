from kivymd.app import MDApp 
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.properties import ObjectProperty
import random 
from kivymd.toast import toast
import time

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    mn=ObjectProperty()
    num=ObjectProperty()
    cd=ObjectProperty()

    def build_code(self):
        lc=[]
        for i in range(5):
            q=random.randint(0,9)
            lc.append(str(q))

        return lc

    def operation1(self):
        if self.num.text=='':
            toast('Number : 0912 345 67 89')
        elif len(self.num.text)==11 and self.num.text[0]=='0' and self.num.text[1]=='9':
            # number=self.num.text
            a=self.build_code()
            self.code=a[0]+a[1]+a[2]+a[3]+a[4]
            self.mn.current='fake'
            # /////////Client//////////
            print(self.code)
        else:
            toast('Number : 0912 345 67 89')
 
    def operation2(self):
        if self.cd.text==self.code:
            time.sleep(1.6)
            MainApp().stop()
        else:
            toast('Error') 

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()
    

MainApp().run()
