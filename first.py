from manim import *
from pathlib import Path
import os
import random

FLAGS = "-pql"
SCENE = "Positioning"
#base class
class MyScene(Scene):
    def small_pause(self, n=0.5):
        self.wait(n)
    
    def pause(self, n=1.5):
        self.wait(n)

    def medium_pause(self, n=3):
        self.wait(n)

    def long_pause(self, n=5):
        self.wait(n)

class Positioning(MyScene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        for i in range(4):
            c = Circle()
            #c.next_to(s)
            #c.next_to(s,LEFT)
            if i==0:
                p = UP
            elif i==1:
                p = DOWN
            elif i==2:
                p = LEFT
            else:
                p = RIGHT

            c.next_to(s, p)
            self.small_pause()
            self.play(Create(c))
        #self.add(s,c)
        #self.play(Create(s), Create(c))
        
        


class Transformation(MyScene):
    def construct(self):
        square = Square()
        square.set_fill(RED,opacity=1)
        square.rotate(PI/3)
        circle = Circle()
        circle.set_fill(GREEN,opacity=1)
        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))



class RunExperiment(MyScene):
    def construct(self):
        self.play(Create(Circle(), run_time=1), Create(Triangle(), run_time=2),Create(Square(), run_time=3),Create(Ellipse(), run_time=4),Create(Rectangle(), run_time=5))
        self.small_pause()

class RateFuncExperiment(MyScene):
    def construct(self):
        self.play(Create(Circle(), rate_func=lingering, run_time=5))

class basic_animations(MyScene):
    def construct(self):
        shapes = [Circle(), Triangle(), Square(), Ellipse()]
        animations = [FadeOut, Create, FadeIn, GrowFromCenter, Uncreate]
        indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
        runtime = 1
        for shape in shapes:
            for a in animations:
                self.play(a(shape),remover=True, run_time=runtime)
        t = Text("Playing with numbers")
        for i in indications:
            self.play(i(t))
        self.clear()
        self.play(DrawBorderThenFill(Circle(fill_opacity=1, fill_color=ORANGE)),remover=True)
        self.play(Write(t),remover=True)
        self.play(AddTextLetterByLetter(t),remover=True)
        self.play(Unwrite(t))
        self.small_pause()

class Random_Numbers(Scene):
    def construct(self):
        c = Circle()
        t = Triangle()
        r = Rectangle()
        s = Square()
        e = Ellipse()
        text = Text("Manim experiment")
        '''
        self.add(c)
        self.wait()
        self.add(t)
        self.wait()
        self.add(r)
        self.wait()
        self.add(s)
        self.wait()
        self.add(e)
        self.wait()
        self.add(text)
        self.wait()'''
        #numbers moving on the screen at random position 
        b = 0.01
        for num in range(100):
            #print(str(num))
            t = Text(str(num), color= RED).scale(5)
            #t.to_edge(LEFT,buff=num)
            t.move_to([random.randint(-4,4),random.randint(-2,2),0])
            self.add(t)
            self.wait()
            self.remove(t)
            b += 0.01

class PauseExperiment(MyScene):
    def construct(self):
        self.small_pause()
        self.add(Circle())
        self.medium_pause()
        self.add(Ellipse())
        self.long_pause()
        self.add(Triangle())
        self.small_pause()

class Grow(Scene):
    def construct(self):
        # Define Mobjects
        #circle = Circle()
        # Animations
        self.play(GrowFromCenter(Circle()))
        #self.wait()
        #self.add(circle)
        #self.wait()

class Square_Uncreate(Scene):
    def construct(self):
        # Define Mobjects
        #circle = Ellipse()
        # Animations
        #self.play(GrowFromCenter(circle))
        #self.wait()
        #self.add(circle)
        #self.wait()
        self.play(Uncreate(Square()))

class Grouping(Scene):
    def construct(self):
        image = ImageMobject(np.uint8([list(range(1,2550))]))
        #print((np.uint8([list(range(1,255))])))
        grp = Group(image, Circle())
        self.add(grp)

if __name__ == '__main__':
    script_name = f"{Path(__file__).resolve()}"
    print(__name__)
    print(__file__)
    print(".........................................................",script_name)
    os.system(f"manim {script_name} {SCENE} {FLAGS}")