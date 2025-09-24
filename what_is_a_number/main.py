from manim import *

class HelloText(Scene):
    def construct(self):
        text = Text("Hello, Manim!", font_size=72)
        self.play(Write(text))
        self.play(text.animate.scale(0.5).set_color(BLUE))