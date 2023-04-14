from manim import *
import math
import numpy
class evolute(Scene):
    def construct(self):
        a = NumberPlane()
        self.play(Create(a), run_time=2, lag_ratio=0.1)
        ecc = Line(ORIGIN, a.c2p(1,0,0)).get_length()
        parabola = ImplicitFunction(lambda x, y: y**2 - 4*ecc*x, color=RED)
        l1 = ImplicitFunction(lambda x, y: 0, color=YELLOW)
        l2 = ImplicitFunction(lambda x, y: 0, color=YELLOW)
        l3 = ImplicitFunction(lambda x, y: 0, color=YELLOW)
        
        evolute = ImplicitFunction(lambda x, y: 6.75*ecc*y**2 - (x-2*ecc)**3, color=PURPLE)
        
        
        self.play(Create(parabola))
        self.play(Create(evolute))
        
        def get_roots(x, y):
            roots = np.roots([ecc, 0, 2*ecc - x, -y])
            return roots
        
        
        h = ValueTracker(-4)
        k = ValueTracker(2)
        
        p = Dot(a.c2p(h.get_value(), k.get_value(), 0), color=GREEN)
        self.play(Create(p), Create(l1), Create(l2), Create(l3))
        p.add_updater(
            lambda x: x.move_to(a.c2p(h.get_value(),k.get_value(),0))
        )
        
        l1.add_updater(
            lambda x: x.become(ImplicitFunction(lambda x,y: ecc*get_roots(h.get_value(), k.get_value())[0]**3*(np.isreal(get_roots(h.get_value(), k.get_value())[0])) + 2*ecc*get_roots(h.get_value(), k.get_value())[0]*(np.isreal(get_roots(h.get_value(), k.get_value())[0])) -get_roots(h.get_value(), k.get_value())[0]*x*(np.isreal(get_roots(h.get_value(), k.get_value())[0])) - y*(np.isreal(get_roots(h.get_value(), k.get_value())[0])), color=YELLOW))
        )
        l2.add_updater(
            lambda x: x.become(ImplicitFunction(lambda x,y: ecc*get_roots(h.get_value(), k.get_value())[1]**3*(np.isreal(get_roots(h.get_value(), k.get_value())[1])) + 2*ecc*get_roots(h.get_value(), k.get_value())[1]*(np.isreal(get_roots(h.get_value(), k.get_value())[1])) -get_roots(h.get_value(), k.get_value())[1]*x*(np.isreal(get_roots(h.get_value(), k.get_value())[1])) - y*(np.isreal(get_roots(h.get_value(), k.get_value())[1])), color=YELLOW))
        )
        l3.add_updater(
            lambda x: x.become(ImplicitFunction(lambda x,y: ecc*get_roots(h.get_value(), k.get_value())[2]**3*(np.isreal(get_roots(h.get_value(), k.get_value())[2])) + 2*ecc*get_roots(h.get_value(), k.get_value())[2]*(np.isreal(get_roots(h.get_value(), k.get_value())[2])) -get_roots(h.get_value(), k.get_value())[2]*x*(np.isreal(get_roots(h.get_value(), k.get_value())[2])) - y*(np.isreal(get_roots(h.get_value(), k.get_value())[2])), color=YELLOW))
        )
        
        
        self.play(h.animate.set_value(4), k.animate.set_value(2), run_time=3)
        self.wait(1)
        self.play(h.animate.set_value(4), k.animate.set_value(math.sqrt(32/27)), run_time=1)
        self.wait(1)
        self.play(h.animate.set_value(4), k.animate.set_value(-2), run_time=3)
        self.wait(1)
        self.play(h.animate.set_value(4), k.animate.set_value(0), run_time=1)
        self.play(h.animate.set_value(2*ecc), k.animate.set_value(0), run_time=3)
        self.wait(1)

