from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alison", "Daniel", "Charlie", "Mona", "Micheal"]

    def build(self):
        self.title = "Dynamic Labels"
        root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            temp_label = Label(text=name)
            root.ids.main.add_widget(temp_label)

        return root


DynamicLabelsApp().run()