from manim import *
class inversePythagorasTheorem(Scene):
    def construct(self):
        self.camera.background_color = "#002B48"
        a = Axes(
            x_range=[-10, 10, PI/4],
            y_range=[-3, 3, PI/4], 
            y_length=3,
            axis_config={"include_tip":False, "include_ticks":False},
            color=WHITE
        ).move_to(UP*1.5)
        sin_g = a.plot(lambda x: np.sin(x), x_range=[-10*PI, -PI], color="#0E94ED") # Left wave
        cos_g = a.plot(lambda x: 0.5*np.sin(2*x), x_range=[PI, 10*PI], color="#ED2726") # Right wave
        
        
        
        self.play(Create(a))
        # self.play(Create(sin_g)) <-- Uncomment these lines to also show the underylying graphs
        # self.play(Create(cos_g))
        self.wait(1)
        
        tracker = ValueTracker(0)
        
        def get_sin_value(x): # Function to return the value of the left wave at an x coord. Returns 0 if input is outside the x_range of the wave.
            if x>=((-10*PI)+(PI*tracker.get_value())) and x<=(-PI+(PI*tracker.get_value())):
                return np.sin(x - PI*tracker.get_value())
            else:
                return 0
                
        def get_cos_value(x):
            if x>=(PI - (PI*tracker.get_value())) and x<=(10*PI - (PI*tracker.get_value())):
                return np.sin(2*x + 2*PI*tracker.get_value())/2
            else:
                return 0
    
        a2 = Axes(
            axis_config={"include_tip": False, "include_ticks":False},
            x_range=[0, 15],
            y_range=[-3, 3], 
            y_length=3,
        ).move_to(DOWN*1.5)
        
        self.play(Create(a2))
        
        tracer = Dot(a2.c2p(0, 0), color=GREEN)
        
        trace = TracedPath(tracer.get_center, stroke_color="#ED2726", stroke_width=5)
        self.play(Create(trace))
        self.play(Create(tracer))
        
        combination_g = a.plot(lambda x: get_sin_value(x) + get_cos_value(x), color="#0E94ED") # This is the visible graph in the upper graph. Its just the sum of values of the waves at all points.
        self.play(Create(combination_g))
        # sin_g.add_updater(
        #     lambda x: x.become(a.plot(lambda x: np.sin(x - PI*tracker.get_value()), x_range=[(-10*PI)+(PI*tracker.get_value()), -PI+(PI*tracker.get_value())], color="#0E94ED"))
        # )
        # cos_g.add_updater(
        #     lambda x: x.become(a.plot(lambda x: np.sin(2*x +2*PI*tracker.get_value()), x_range=[PI-(PI*tracker.get_value()), 10*PI-(PI*tracker.get_value())], color="#ED2726"))
        # )
        combination_g.add_updater(
            lambda x: x.become(a.plot(lambda x: get_sin_value(x) + get_cos_value(x), color="#0E94ED"))
        )
        
        tracer.add_updater(
            lambda x: x.move_to(a2.c2p(tracker.get_value(), get_sin_value(0) + get_cos_value(0)))
        )
        
        
        self.add(tracker)
        tracker.add_updater(lambda x, dt: x.increment_value(dt))
        
        self.wait(12)
        
        
        tracker.clear_updaters()
        self.wait(1)
        

    
