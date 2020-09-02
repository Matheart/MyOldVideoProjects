from manimlib.imports import *
import random
import pandas as pd

class Test(PhysicScene):
    def construct(self):
        self.set_gravity(9.81 * DOWN)
        r = np.sqrt(2)
        mass = 10
        w = 2
        h = 0.1
        
        C_moment = pymunk.moment_for_circle(mass, 0, r)
        C_body = pymunk.Body(mass, C_moment)
        C_body.position = 0, 4 - r
        C_body.velocity = 2, 1
        C_mob = Circle(radius = r).set_fill(RED, opacity = 0.8).shift(2*UP)
        C_shape = pymunk.Circle(C_body, C_mob.radius)

        Line_size = [w, h]
        Line_moment = pymunk.moment_for_box(mass, Line_size)
        Line_body = pymunk.Body(mass, Line_moment, 0)
        Line_body.angle = 0.5
        Line_body.position -2, 3
        Line_mob = Rectangle(width = w, height = h).set_color(BLUE)
        Line_shape = pymunk.Poly.create_box(Line_body, Line_size) #pymunk.Segment(Line_body, (-5, 3), (-1, 2), 0)

        ground_body = self.space.static_body
        ground_mob = Line(np.array([-7,-1,0]),np.array([7,-1,0])).set_color(GREEN)
        ground_shape = pymunk.Segment(ground_body,
                                          (-7, -1),
                                          ( 7, -1),
                                          0)

        C_shape.friction = ground_shape.friction = Line_shape.friction = 0.5
        C_shape.elasticity = ground_shape.elasticity = Line_shape.elasticity = 0.8

        C = PhysicMobject(C_body, C_shape, C_mob)
        Lne = PhysicMobject(Line_body, Line_shape, Line_mob)
        ground = PhysicMobject(ground_body, ground_shape, ground_mob)

        self.add(C_mob, Line_mob, ground_mob)
        self.add_physic_obj(C, Lne)
        self.add_static_obj(ground)
        self.simulate(10)

class RotateTest(Scene):
    def construct(self):
        rec = Rectangle(width = 2, height = 1)
        self.play(ShowCreation(rec))
        self.play(Rotating(rec, PI/2))

class RGBTest(Scene):
    def construct(self):
        rec = Rectangle(width = 3, height = 1).set_color(rgb_to_color((50, 50, 50)))
        self.add(rec)

def CSVTest():
        dt = pd.read_csv('D:\\Maths\\CaiDian\\Markers.csv', sep = '\t')
        print(dt["Name"][0][2:])
        for i in dt["Name"]:
            print(float(i[2:]))

if __name__ == "__main__":
    CSVTest()

class SegmentAppendTest(PhysicScene):
    def construct(self):
        self.set_gravity(9.81*DOWN)
        def SegmentAppend(A, B, col): # return essential information for appending segment
            xA = A.get_center()[0]
            yA = A.get_center()[1]
            xB = B.get_center()[0]
            yB = B.get_center()[1]

            center = ((xA+xB)/2, (yA+yB)/2)

            if xB == xA:
                theta = 0
            elif yB == yA:
                theta = PI/2
            else:
                theta = PI/2 + np.arctan((yB-yA)/(xB-xA))
            w = 0.1
            h = np.sqrt((xB-xA)**2 + (yB-yA)**2)
            mass = 10

            Ln_size = [w, h]
            Ln_moment = pymunk.moment_for_box(mass, Ln_size)
            Ln_body = pymunk.Body(mass, Ln_moment, 0)
            Ln_body.angle = theta 
            Ln_body.position = center
            Ln_mob = Rectangle(height = h, width = w).set_color(col).set_fill(col, opacity = 0.6)
            Ln_mob.move_to(np.array([(A.get_center()[0]+B.get_center()[0])/2,(A.get_center()[1]+B.get_center()[1])/2,0]))
            Ln_shape = pymunk.Poly.create_box(Ln_body, Ln_size)
            Ln_shape.friction = 0.1
            Ln_shape.elasticity = 0.8

            Ln_mob.rotate(theta, about_point = np.array([(A.get_center()[0]+B.get_center()[0])/2,(A.get_center()[1]+B.get_center()[1])/2,0]))
            zero_one_avg = (Ln_mob.get_vertices()[0] + Ln_mob.get_vertices()[1]) / 2
            two_three_avg = (Ln_mob.get_vertices()[2] + Ln_mob.get_vertices()[3]) / 2
            Ln_mob.rotate(-theta, about_point = np.array([(A.get_center()[0]+B.get_center()[0])/2,(A.get_center()[1]+B.get_center()[1])/2,0]))
            
            if abs(A.get_center()[0] - zero_one_avg[0]) < 0.01 and abs(A.get_center()[1] - zero_one_avg[1]) < 0.01:
                A.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[0] + Ln_mob.get_vertices()[1]) / 2))
                B.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[2] + Ln_mob.get_vertices()[3]) / 2))
            elif abs(A.get_center()[0] - two_three_avg[0]) < 0.01 and abs(A.get_center()[1] - two_three_avg[1]) < 0.01:
                B.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[0] + Ln_mob.get_vertices()[1]) / 2))
                A.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[2] + Ln_mob.get_vertices()[3]) / 2))
            
            Ln = PhysicMobject(Ln_body, Ln_shape, Ln_mob) 
            return Ln

        L_wall = pymunk.Body(body_type = pymunk.Body.STATIC)
        L_mob = Line(7*LEFT+4*UP, 7*LEFT+4*DOWN).set_color("#7CFC00")
        L_shape = pymunk.Segment(L_wall, (-7, 4), (-7, -4), 0)

        R_wall = pymunk.Body(body_type = pymunk.Body.STATIC)
        R_mob = Line(7*RIGHT+4*UP, 7*RIGHT+4*DOWN).set_color("#7CFC00")
        R_shape = pymunk.Segment(R_wall, (7, 4), (7, -4), 0)

        D_wall = self.space.static_body
        D_mob = Line(7*LEFT+4*DOWN, 7*RIGHT+4*DOWN).set_color("#7CFC00")
        D_shape = pymunk.Segment(D_wall, (-7, -4), (7, -4), 0)


        L_shape.friction = R_shape.friction = D_shape.friction = 0.1
        L_shape.elasticity = R_shape.elasticity = D_shape.elasticity = 0.8

        L = PhysicMobject(L_wall, L_shape, L_mob)
        R = PhysicMobject(R_wall, R_shape, R_mob)
        D = PhysicMobject(D_wall, D_shape, D_mob)
        self.add_static_obj(L, R, D)

        col_choice = ["#800000","#8B0000","#A52A2A","#B22222","#DC143C","#FF0000","#FF6347","#FF7F50","#CD5C5C","#F08080","#E9967A","#FA8072","#FFA07A","#FF4500",
               "#FF8C00","#FFA500","#FFD700","#B8860B","#DAA520","#FFFF00","#9ACD32",
               "#556B2F","#6B8E23","#7CFC00","#7FFF00","#ADFF2F","#006400","#008000","#228B22","#00FF00","#32CD32","#90EE90","#98FB98","#00FA9A","#00FF7F","#2E8B57",
               "#20B2AA","#008080","#008B8B","#00FFFF","#00CED1","#40E0D0","#7FFFD4","#4682B4","#6495ED","#00BFFF","#1E90FF","#191970","#000080","#00008B","#0000FF",
               "#8A2BE2","#4B0082","#483D8B","#6A5ACD","#7B68EE","#9400D3","#9932CC","#BA55D3","#EE82EE","#FF00FF","#FF1493","#FF69B4"]
        dt = pd.read_csv('D:\\Maths\\CaiDian\\Markers.csv', sep = '\t')
        tme = dt['Name']

        for i in range(len(tme)):
            X_cor = np.array([random.randint(-6,6), random.randint(2,4),0])
            Y_cor = np.array([random.randint(-5,5), random.randint(2,4),0])

            while (X_cor == Y_cor).all():
                Y_cor = np.array([random.randint(-4,4), random.randint(-3,3),0]) 

            col = col_choice[random.randint(0, len(col_choice)-1)]
            X = Dot(X_cor).set_color(col)
            Y = Dot(Y_cor).set_color(col)
            Ln = SegmentAppend(X, Y, col)

            Ln.set_add_time(float(tme[i][2:]))
            #self.add(X,Y)
            self.add_physic_obj(Ln)
        self.simulate(50)

class HackenBushTest(PhysicScene):
    CONFIG = {
        "camera_config": {"use_plot_depth": True}
    }
    def construct(self):
        def AppendSegment(A, B, col):
            xA = A.get_center()[0]
            yA = A.get_center()[1]
            xB = B.get_center()[0]
            yB = B.get_center()[1]
            w = 0.1
            h = np.sqrt((xB-xA)**2 + (yB-yA)**2)

            if xB == xA:
                theta = 0
            elif yB == yA:
                theta = PI/2
            else:
                theta = PI/2 + np.arctan((yB-yA)/(xB-xA))

            Ln_mob = Rectangle(height = h, width = w).set_color(col).set_fill(col, opacity = 0.6)
            Ln_mob.move_to(np.array([(A.get_center()[0]+B.get_center()[0])/2,(A.get_center()[1]+B.get_center()[1])/2,0]))
            Ln_mob.rotate(theta, about_point = np.array([(A.get_center()[0]+B.get_center()[0])/2,(A.get_center()[1]+B.get_center()[1])/2,0]))
            return Ln_mob

        def ApplyFreeFall(A, B, Ln_mob): # Append Segment
            xA = A.get_center()[0]
            yA = A.get_center()[1]
            xB = B.get_center()[0]
            yB = B.get_center()[1]

            center = ((xA+xB)/2, (yA+yB)/2)

            if xB == xA:
                theta = 0
            elif yB == yA:
                theta = PI/2
            else:
                theta = PI/2 + np.arctan((yB-yA)/(xB-xA))
            w = 0.1
            h = np.sqrt((xB-xA)**2 + (yB-yA)**2)
            mass = 10

            Ln_size = [w, h]
            Ln_moment = pymunk.moment_for_box(mass, Ln_size)
            Ln_body = pymunk.Body(mass, Ln_moment, 0)
            Ln_body.angle = theta 
            Ln_body.position = center
            Ln_shape = pymunk.Poly.create_box(Ln_body, Ln_size)
            Ln_shape.friction = 0.1
            Ln_shape.elasticity = 0.8
            
            zero_one_avg = (Ln_mob.get_vertices()[0] + Ln_mob.get_vertices()[1]) / 2
            two_three_avg = (Ln_mob.get_vertices()[2] + Ln_mob.get_vertices()[3]) / 2
            Ln_mob.rotate(-theta, about_point = np.array([(A.get_center()[0]+B.get_center()[0])/2,(A.get_center()[1]+B.get_center()[1])/2,0]))
            
            if abs(A.get_center()[0] - zero_one_avg[0]) < 0.01 and abs(A.get_center()[1] - zero_one_avg[1]) < 0.01:
                A.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[0] + Ln_mob.get_vertices()[1]) / 2))
                B.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[2] + Ln_mob.get_vertices()[3]) / 2))
            elif abs(A.get_center()[0] - two_three_avg[0]) < 0.01 and abs(A.get_center()[1] - two_three_avg[1]) < 0.01:
                B.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[0] + Ln_mob.get_vertices()[1]) / 2))
                A.add_updater(lambda obj: obj.move_to((Ln_mob.get_vertices()[2] + Ln_mob.get_vertices()[3]) / 2))
            
            Ln = PhysicMobject(Ln_body, Ln_shape, Ln_mob) 
            return Ln

        GroundBody = self.space.static_body
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#00FF7F")
        GroundShape = pymunk.Segment(GroundBody, (-7, -2.5), (1, -2.5), 0)
        GroundShape.friction = 0.8
        GroundShape.elasticity = 0.8
        Ground = PhysicMobject(GroundBody, GroundShape, GroundLine)
        self.add_static_obj(Ground)

        A = Dot(np.array([-7+8.0/3,-2.5,0])).set_plot_depth(100)
        B = Dot(np.array([-7+8.0/3,0,0])).set_plot_depth(100)
        C = Dot(np.array([-7+8.0/3*2,-2.5,0])).set_plot_depth(100)
        D = Dot(np.array([-7+8.0/3*2,0,0])).set_plot_depth(100)
        E = Dot(np.array([-7+8.0/3*2,2.5,0])).set_plot_depth(100)
        F = Dot(np.array([-7+8.0/3+1, 3.5, 0])).set_plot_depth(100)

        L1 = AppendSegment(A, B, "#00EE00")
        L2 = AppendSegment(C, D, "#00EE00")
        L3 = AppendSegment(D, E, "#00EE00")
        L4 = AppendSegment(E, F, "#00EE00")

        BluePerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(BLUE).shift((-7+4.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).shift((-3+8.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)

        self.play(ShowCreation(GroundLine))
        self.play(ShowCreation(VGroup(A,B,L1,L2,C,D)))
        self.play(ShowCreation(VGroup(L3,E)))
        self.play(ShowCreation(VGroup(L4,F)))
        self.wait()
        self.play(FadeIn(BluePerson, direction = UP),FadeIn(RedPerson, direction = UP))
        self.wait()
        
        EF = ApplyFreeFall(E, F, L4)
        self.add_physic_obj(EF)
        self.simulate(3)