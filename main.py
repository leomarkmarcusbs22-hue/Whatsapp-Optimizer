from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class OptimizerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.status_label = Label(text="Ready to Optimize", font_size='20sp')
        btn = Button(text="Select Video/Image", size_hint=(1, 0.2), background_color=(0, 0.7, 0.3, 1))
        
        # We'll link the compression logic to this button later
        btn.bind(on_press=self.start_optimization)
        
        layout.add_widget(self.status_label)
        layout.add_widget(btn)
        return layout

    def start_optimization(self, instance):
        self.status_label.text = "Optimizing... (Simulated)"
        print("Compression logic will run here!")

if __name__ == '__main__':
    OptimizerApp().run()