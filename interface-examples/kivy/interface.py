import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MyScreenManager(ScreenManager):
    def __init__(self,**kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
class MainLayout(BoxLayout):
	def __init__(self,**kwargs):
		super(MainLayout, self).__init__(**kwargs)
		
class ButtonsScreen(Screen):
	def __init__(self,**kwargs):
        	super(ButtonsScreen, self).__init__(**kwargs)
	def add_node(self,*args):
		print("add node")
	def del_node(self,*args):
		pass
	def add_edge(self,*args):
		pass
	def del_edge(self,*args):
		pass
	def save(self,*args):
		pass
class NodeMgmntScreen(Screen):
	def __init__(self,**kwargs):
        	super(NodeMgmntScreen, self).__init__(**kwargs)
	DEL_ACTION = 0
	ADD_ACTION = 1

class EdgeMgmntScreen(Screen):
	def __init__(self,**kwargs):
        	super(EdgeMgmntScreen, self).__init__(**kwargs)
	DEL_ACTION = 0
	ADD_ACTION = 1
	
class DesignApp(App):
	def build(self):
		return MainLayout()

if __name__ == "__main__":
	DesignApp().run()
