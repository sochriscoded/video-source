from manim import *

#TODO: Construct Scene 1 (intro) and Scene 6 (conclusion)

class Scene1(Scene):
    def construc(self):
        text = MathTex("y = mx+b")

class Scene2(Scene):
    def construct(self):
        r = 2
        circle = Circle(radius=r, color=BLUE)
        self.play(Create(circle, run_time=1))

        n_values = [3, 4, 6, 12, 24, 48]
        inscribed = RegularPolygon(n_values[0], radius=r, color=YELLOW).set_fill(YELLOW, opacity=0.5)
        circumscribed = RegularPolygon(n_values[0], radius=r/np.cos(np.pi/n_values[0]), color=RED).set_fill(RED, opacity=0.3)

        self.play(Create(inscribed), Create(circumscribed))
        self.wait(0.5)

        for n in n_values[1:]:
            new_inscribed = RegularPolygon(n, radius=r, color=YELLOW).set_fill(YELLOW, opacity=0.5)
            new_circumscribed = RegularPolygon(n, radius=r/np.cos(np.pi/n), color=RED).set_fill(RED, opacity=0.3)

            label = MathTex(f"n = {n}").next_to(circle, DOWN)

            self.play(
                Transform(inscribed, new_inscribed, run_time=0.5),
                Transform(circumscribed, new_circumscribed, run_time=0.5),
                FadeIn(label, run_time=0.3)
            )
            self.wait(0.3)
            self.play(FadeOut(label, run_time=0.3))

        self.wait(1)

        formula = MathTex(r"A_n = \tfrac{1}{2} n r^2 \sin\!\big(\tfrac{2\pi}{n}\big)")
        formula.to_edge(UP)
        self.play(Write(formula), run_time=1)
        self.wait(1.5)

        limit = MathTex(r"\lim_{n \to \infty} A_n = \pi r^2")
        limit.next_to(formula, DOWN)
        self.play(Write(limit), run_time=1.5)

        circle_area = MathTex(r"A_c = \pi r^2")
        circle_area.to_edge(LEFT)
        self.play(Transform(limit, circle_area))
        self.wait(3)
        self.play(FadeOut(inscribed), FadeOut(circumscribed), FadeOut(circle_area))
        self.wait(0.5)

        circle = Circle(radius=r, color=BLUE)
        self.play(Create(circle, run_time=1))

        polygon = RegularPolygon(n_values[0], radius=r, color=GREEN)
        polygon.set_fill(GREEN, opacity=0.4)
        self.play(Create(polygon))

        perim_formula = MathTex(r"P_n = 2n r \sin\!\left(\tfrac{\pi}{n}\right)")
        perim_formula.to_edge(UP)
        self.play(Transform(formula, perim_formula))
        self.wait(0.5)

        for n in n_values[1:]:
            new_polygon = RegularPolygon(n, radius=r, color=GREEN).set_fill(GREEN, opacity=0.4)
            label = MathTex(f"n = {n}").next_to(circle, DOWN)

            self.play(
                Transform(polygon, new_polygon, run_time=0.5),
                FadeIn(label, run_time=0.3)
            )
            self.wait(0.3)
            self.play(FadeOut(label, run_time=0.3))

        circumference = MathTex(r"\lim_{n \to \infty} P_n = 2\pi r")
        circumference.next_to(perim_formula, DOWN)
        self.play(Write(circumference), run_time=1.5)

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        question = Text("Why does Algebra Exist at All? What is its purpose?", font_size=24)

        self.play(Write(question))
        self.wait(2)
        self.play(FadeOut(question))
        self.clear()

class Scene3 (Scene):
    def construct(self):
        # Triangle
        tri = Triangle()
        tri.stretch_to_fit_height(4)
        tri.stretch_to_fit_width(6)
        self.play(Create(tri))
        self.wait(2)

        rec = Rectangle()
        rec.stretch_to_fit_width(6)
        rec.stretch_to_fit_height(4)
        rec.move_to(tri.get_center())
        self.play(Create(rec))
        self.wait(2)

        line_center = Line(UP, DOWN, color=RED)
        tri_height = tri.height
        line_center.stretch_to_fit_height(tri_height)
        line_center.move_to(tri.get_center())
        self.play(Create(line_center))
        self.wait(2)

        v0, v1, v2 = tri.get_vertices()
        line_diag1 = Line(v0,v1, color=YELLOW)
        line_diag2 = Line(v0,v2, color=YELLOW)
        self.play(Create(line_diag1))
        self.play(Create(line_diag2))
        self.wait(2)

        rec_left = Rectangle(color=YELLOW)
        rec_right = Rectangle(color=YELLOW)
        rec_left.stretch_to_fit_width(3)
        rec_right.stretch_to_fit_width(3)
        rec_left.stretch_to_fit_height(4)
        rec_right.stretch_to_fit_height(4)
        rec_left.set_fill(color=YELLOW, opacity=0.2)
        rec_right.set_fill(color=YELLOW, opacity=0.2)
        rec_left.move_to(tri.get_center())
        rec_right.move_to(tri.get_center())
        rec_left.shift(LEFT*1.5)
        rec_right.shift(RIGHT*1.5)
        self.play(Create(rec_left))
        self.play(Create(rec_right))
        self.wait(2)

        self.play(rec_left.animate.move_to(LEFT*5))
        self.play(rec_right.animate.move_to(RIGHT*5))
        self.wait(2)

        self.play(line_diag1.animate.move_to(LEFT*5))
        self.play(line_diag2.animate.move_to(RIGHT*5))
        self.wait(2)

        self.play(FadeOut(line_diag1, run_time=0.3))
        self.play(FadeOut(rec_left, run_time=0.3))
        self.play(FadeOut(line_diag2, run_time=0.3))
        self.play(FadeOut(rec_right, run_time=0.3))
        self.wait(2)

        rec_area = MathTex("A_{r}=bh")
        tri_area = MathTex("A_{t}=\\frac{1}{2}bh")
        brace1 = Brace(rec)
        labelw = brace1.get_text("base")
        brace2 = Brace(rec, direction=LEFT)
        labelh = brace2.get_text("height")
        self.play(Create(brace1), Write(labelw))
        self.play(Create(brace2), Write(labelh))
        self.wait(4)

        rec_area.to_edge(UP)
        self.play(Write(rec_area))
        self.wait(4)

        tri_area.to_edge(UP)
        self.play(Transform(rec_area, tri_area))
        self.wait(4)

        self.play(FadeOut(Group(*self.mobjects)))
        self.clear()

class Scene4 (Scene):
  def construct(self):
      
      square = Square()
      length = Brace(square)
      label1 = MathTex("l", tex_to_color_map={"l": BLUE})
      length.put_at_tip(label1)
      width = Brace(square, direction=LEFT)
      label2 = MathTex("w", tex_to_color_map={"w": BLUE})
      width.put_at_tip(label2)
      self.play(Create(square))
      self.wait(1)

      self.play(Create(length), Write(label1))
      self.wait(1)
      self.play(Create(width), Write(label2))
      self.wait(2)

      area = MathTex("A = l\\cdotw", tex_to_color_map={"l" : BLUE, "w" : BLUE})
      labelw = MathTex("x", tex_to_color_map={"x": BLUE})
      width.put_at_tip(labelw)
      labelh = MathTex("x", tex_to_color_map={"x": BLUE})
      length.put_at_tip(labelh)
      area.to_corner(LEFT)
      self.play(Write(area))
      self.wait(2)

      self.play(Transform(label1, labelh))
      self.play(Transform(label2, labelw))
      self.wait(2)

      areax = MathTex(
            "A = x\\cdotx",
            tex_to_color_map={"x": BLUE}
        ).to_corner(LEFT)
      self.play(TransformMatchingTex(area, areax))
      self.wait(2)

      areax2 = MathTex(
            "A = x^2",
            tex_to_color_map={"x": BLUE}
        ).to_corner(LEFT)
      self.play(TransformMatchingTex(areax, areax2))
      self.wait(2)

      fade_group = VGroup(square, labelh, labelw, label1, label2, width, length, areax2)
      self.play(FadeOut(fade_group))
      self.wait(2)
      self.clear()

class Scene5 (Scene):
  def construct(self):
      
      def func(x):
          return x**2

      x_tracker = ValueTracker(1)

      area_3 = MathTex(
          "A = x^2", 
          tex_to_color_map={"x": BLUE, "A": YELLOW}).move_to(UP*3 + LEFT*6)
      self.play(Write(area_3))

      ax = Axes(
          x_range=[-10,10,1],
          y_range=[0,100,10],
          axis_config={"include_numbers": True, "color": RED},
          tips=True
      )

      labels = ax.get_axis_labels(x_label="x", y_label="A")
      sqrarea = ax.plot(lambda x:x**2)
      ax.scale(0.75)
      sqrarea.scale(.75)
      ax.to_edge(RIGHT)
      sqrarea.to_edge(RIGHT)

      new_square = Square(side_length=2.75).next_to(area_3, DOWN+RIGHT*.01, buff=0.5)
      area_label = MathTex("1").move_to(new_square.get_center()).set_color(YELLOW)
      x_label = MathTex("x=1").next_to(new_square, DOWN).set_color(BLUE)

      dots = VGroup()

      self.play(Create(ax), Write(labels), run_speed=.5)
      self.wait(1)
      self.play(Create(new_square))
      self.wait(1)
      self.play(Write(x_label), Write(area_label))
      self.wait(1)

      for x in range(1, 10):
          # Animate tracker
          self.play(x_tracker.animate.set_value(x), run_time=1)

          # Jump the labels instantly after animation
          area_label.become(MathTex(f"{x**2}").move_to(new_square.get_center())).set_color(YELLOW)
          x_label.become(MathTex(f"x={x}").next_to(new_square, DOWN)).set_color(BLUE)

          # Add the dot on the curve
          y = x**2
          dot = Dot(ax.c2p(x, y), color=GREEN)
          dots.add(dot)
          self.play(FadeIn(dot, scale=0.5))

      for x in range(-1, -10, -1):
          # Animate tracker
          self.play(x_tracker.animate.set_value(x), run_time=1)

          # Jump the labels instantly after animation
          area_label.become(MathTex(f"{x**2}").move_to(new_square.get_center())).set_color(YELLOW)
          x_label.become(MathTex(f"x={x}").next_to(new_square, DOWN)).set_color(BLUE)

          # Add the dot on the curve
          y = x**2
          dot = Dot(ax.c2p(x, y), color=GREEN)
          dots.add(dot)
          self.play(FadeIn(dot, scale=0.5))

      # Finally draw the full curve
      self.play(Create(sqrarea))
      self.play(FadeOut(dots))
      self.wait(2)

      # Put a dot on the curve and as it slides around, update the values of A and X
      t = ValueTracker(-10)

      new_area_label = MathTex("100").move_to(new_square.get_center()).set_color(YELLOW)

      new_area_label.add_updater(
            lambda m: m.become(
                MathTex(f"{int(round(func(t.get_value())))}").set_color(YELLOW).move_to(new_square.get_center())))
    
      new_x_label = MathTex("x=-10").next_to(new_square, DOWN).set_color(BLUE)

      new_x_label.add_updater(
          lambda m: m.become(
                MathTex(f"x={int(round(t.get_value()))}").next_to(new_square, DOWN).set_color(BLUE)
      ))

      initial_point = ax.coords_to_point(t.get_value(), func(t.get_value()))
      new_dot = Dot(point=initial_point).add_updater(
          lambda m: m.move_to(ax.c2p(t.get_value(), func(t.get_value())))
      ).set_color(GREEN_E)

      self.play(FadeOut(area_label, x_label))
      self.play(Write(new_area_label), Write(new_x_label))
      self.add(new_dot)
      self.wait(1)
      self.play(t.animate.set_value(10), run_time=10, rate_func=linear)
      self.wait(2)