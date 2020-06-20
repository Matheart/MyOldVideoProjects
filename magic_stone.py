from manimlib.imports import *
from manim_sandbox.utils.imports import *

class MyText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
    }
    
class Cover(Scene):
    def construct(self):
        title = Text("Magic Stone")
        title[:5].set_color(BLUE)
        title[5:].set_color(GREEN)
        tar = Text("Task 1524").next_to(title,DOWN)
        sol = Text("Solution By Artanis").scale(0.5).to_edge(RIGHT+DOWN)
        sol[12:].set_color(RED)

        self.play(FadeIn(title),FadeIn(tar))
        self.wait(1)
        self.play(Write(sol))
        self.wait(1.5)
        self.play(FadeOut(title),FadeOut(tar),FadeOut(sol))
        self.wait(1)

class BigGoal(Scene):
    def construct(self):
        title = Text("Big Goals").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)

        text1 = Text("Problem Description").scale(0.5)
        text2 = Text("Technique Introduction").scale(0.5)
        text3 = Text("Variables").scale(0.5)
        text4 = Text("Sample").scale(0.5)
        text5 = Text("Code").scale(0.5)
        text6 = Text("Reminder").scale(0.5)

        dot1 = Dot(color=YELLOW).move_to(np.array([-2,2,0]))
        dot2 = Dot(color=YELLOW).move_to(np.array([-2,1,0]))
        dot3 = Dot(color=YELLOW).move_to(np.array([-2,0,0]))
        dot4 = Dot(color=YELLOW).move_to(np.array([-2,-1,0]))
        dot5 = Dot(color=YELLOW).move_to(np.array([-2,-2,0]))
        dot6 = Dot(color=YELLOW).move_to(np.array([-2,-3,0]))

        text1.next_to(dot1,RIGHT)
        text2.next_to(dot2,RIGHT)
        text3.next_to(dot3,RIGHT)
        text4.next_to(dot4,RIGHT)
        text5.next_to(dot5,RIGHT)
        text6.next_to(dot6,RIGHT)
        
        def init():
            title.set_opacity(1)
            line.set_opacity(1)
            dot1.set_opacity(1)
            dot2.set_opacity(1)
            dot3.set_opacity(1)
            dot4.set_opacity(1)
            dot5.set_opacity(1)
            dot6.set_opacity(1)
            text1.set_opacity(1)
            text2.set_opacity(1)
            text3.set_opacity(1)
            text4.set_opacity(1)
            text5.set_opacity(1)
            text6.set_opacity(1)



        self.play(FadeIn(title),FadeIn(line),
                  FadeIn(dot1),FadeIn(dot2),FadeIn(dot3),FadeIn(dot4),FadeIn(dot5),FadeIn(dot6),
                  FadeIn(text1),FadeIn(text2),FadeIn(text3),FadeIn(text4),FadeIn(text5),FadeIn(text6))
        # 1
        self.wait(2)
        init()
        self.wait(1.5)
        self.play(ApplyMethod(title.set_opacity,0.5),ApplyMethod(line.set_opacity,0.5),
                  ApplyMethod(dot2.set_opacity,0.5),ApplyMethod(dot3.set_opacity,0.5),
                  ApplyMethod(dot4.set_opacity,0.5),ApplyMethod(dot5.set_opacity,0.5),ApplyMethod(dot6.set_opacity,0.5),
                  ApplyMethod(text2.set_opacity,0.5),ApplyMethod(text3.set_opacity,0.5),
                  ApplyMethod(text4.set_opacity,0.5),ApplyMethod(text5.set_opacity,0.5),ApplyMethod(text6.set_opacity,0.5),)
        # 2
        self.wait(2)
        init()
        self.wait(1.5)
        self.play(ApplyMethod(title.set_opacity,0.5),ApplyMethod(line.set_opacity,0.5),
                  ApplyMethod(dot1.set_opacity,0.5),ApplyMethod(dot3.set_opacity,0.5),
                  ApplyMethod(dot4.set_opacity,0.5),ApplyMethod(dot5.set_opacity,0.5),ApplyMethod(dot6.set_opacity,0.5),
                  ApplyMethod(text1.set_opacity,0.5),ApplyMethod(text3.set_opacity,0.5),
                  ApplyMethod(text4.set_opacity,0.5),ApplyMethod(text5.set_opacity,0.5),ApplyMethod(text6.set_opacity,0.5),)
        # 3
        self.wait(2)
        init()
        self.wait(1.5)
        self.play(ApplyMethod(title.set_opacity,0.5),ApplyMethod(line.set_opacity,0.5),
                  ApplyMethod(dot1.set_opacity,0.5),ApplyMethod(dot2.set_opacity,0.5),
                  ApplyMethod(dot4.set_opacity,0.5),ApplyMethod(dot5.set_opacity,0.5),ApplyMethod(dot6.set_opacity,0.5),
                  ApplyMethod(text1.set_opacity,0.5),ApplyMethod(text2.set_opacity,0.5),
                  ApplyMethod(text4.set_opacity,0.5),ApplyMethod(text5.set_opacity,0.5),ApplyMethod(text6.set_opacity,0.5),)
        # 4
        self.wait(2)
        init()
        self.wait(1.5)
        self.play(ApplyMethod(title.set_opacity,0.5),ApplyMethod(line.set_opacity,0.5),
                  ApplyMethod(dot1.set_opacity,0.5),ApplyMethod(dot2.set_opacity,0.5),ApplyMethod(dot3.set_opacity,0.5),
                  ApplyMethod(dot5.set_opacity,0.5),ApplyMethod(dot6.set_opacity,0.5),
                  ApplyMethod(text1.set_opacity,0.5),ApplyMethod(text2.set_opacity,0.5),ApplyMethod(text3.set_opacity,0.5),
                  ApplyMethod(text5.set_opacity,0.5),ApplyMethod(text6.set_opacity,0.5),)
        # 5
        self.wait(2)
        init()
        self.wait(1.5)
        self.play(ApplyMethod(title.set_opacity,0.5),ApplyMethod(line.set_opacity,0.5),
                  ApplyMethod(dot1.set_opacity,0.5),ApplyMethod(dot2.set_opacity,0.5),ApplyMethod(dot3.set_opacity,0.5),
                  ApplyMethod(dot4.set_opacity,0.5),ApplyMethod(dot6.set_opacity,0.5),
                  ApplyMethod(text1.set_opacity,0.5),ApplyMethod(text2.set_opacity,0.5),ApplyMethod(text3.set_opacity,0.5),
                  ApplyMethod(text4.set_opacity,0.5),ApplyMethod(text6.set_opacity,0.5),)
        # 6
        self.wait(2)
        init()
        self.wait(1.5)
        self.play(ApplyMethod(title.set_opacity,0.5),ApplyMethod(line.set_opacity,0.5),
                  ApplyMethod(dot1.set_opacity,0.5),ApplyMethod(dot2.set_opacity,0.5),ApplyMethod(dot3.set_opacity,0.5),
                  ApplyMethod(dot4.set_opacity,0.5),ApplyMethod(dot5.set_opacity,0.5),
                  ApplyMethod(text1.set_opacity,0.5),ApplyMethod(text2.set_opacity,0.5),ApplyMethod(text3.set_opacity,0.5),
                  ApplyMethod(text4.set_opacity,0.5),ApplyMethod(text5.set_opacity,0.5))
        self.wait(3)

class Description(Scene):
    def construct(self):
        title = Text("Problem Description").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)
        self.play(FadeIn(title),FadeIn(line))
        self.wait(2)

        man = TextMobject("There are four types of events").scale(0.8).next_to(line,DOWN).to_edge(LEFT)
        txt1 = TextMobject("Type $T_i$ = 1: Buy $A_i$ magic stones.").scale(0.8).next_to(man,DOWN).to_edge(LEFT)
        txt2 = TextMobject("Type $T_i$ = 2: Given $A_i$ magic stones.").scale(0.8).next_to(txt1,DOWN).to_edge(LEFT)
        txt3 = TextMobject("Type $T_i$ = 3: Use $A_i$ magic stones.").scale(0.8).next_to(txt2,DOWN).to_edge(LEFT)
        txt4 = TextMobject("Type $T_i$ = 4: Query: Among the magic stones Dr. Jones currently has,").scale(0.8).next_to(txt3,DOWN).to_edge(LEFT)
        txt5 = TextMobject("                at most how many of them were bought,").scale(0.8).next_to(txt4,DOWN).to_edge(LEFT)
        txt6 = TextMobject("            and at least how many of them were bought?").scale(0.8).next_to(txt5,DOWN).to_edge(LEFT)

        nwtxt1 = TextMobject("For convenience, we use").scale(0.8).next_to(line,DOWN).to_edge(LEFT)
        nwtxt2 = TextMobject("BLUE color to denote the Bought magic stones.").scale(0.8).next_to(nwtxt1,DOWN).to_edge(LEFT)
        nwtxt3 = TextMobject("And GREEN color to denote the Given magic stones.").scale(0.8).next_to(nwtxt2,DOWN).to_edge(LEFT)

        blue_circle = Circle(radius = 1, color=BLUE).move_to(np.array([-4,-1,0])).set_opacity(0.5)
        blue_ex = TextMobject("Bought Magic Stone",color=BLUE).next_to(blue_circle,DOWN)

        green_circle = Circle(radius = 1, color=GREEN).move_to(np.array([4,-1,0])).set_opacity(0.5)
        green_ex = TextMobject("Given Magic Stone",color=GREEN).next_to(green_circle,DOWN)

        nwtxt2[0][0:4].set_color(BLUE)
        nwtxt2[0][20:21].set_color(BLUE)
        nwtxt3[0][3:8].set_color(GREEN)
        nwtxt3[0][24:25].set_color(GREEN)

        txt1[0][4:6].set_color(RED)
        txt2[0][4:6].set_color(RED)
        txt3[0][4:6].set_color(RED)
        txt4[0][4:6].set_color(RED)

        txt1[0][12:14].set_color(ORANGE)
        txt2[0][14:16].set_color(ORANGE)
        txt3[0][12:14].set_color(ORANGE)

        txt1[0][9:12].set_color(BLUE)
        txt2[0][9:14].set_color(GREEN)
        
        txt5[0][:6].set_color(PURPLE)
        txt6[0][3:10].set_color(PURPLE)

        txt5[0][-7:-1].set_color(BLUE)
        txt6[0][-7:-1].set_color(BLUE)

        self.play(FadeIn(man))
        self.wait(1)
        self.play(FadeIn(txt1))
        self.wait(1)
        self.play(FadeIn(txt2))
        self.wait(1)
        self.play(FadeIn(txt3))
        self.wait(1)
        self.play(FadeIn(txt4))
        self.wait(1)
        self.play(FadeIn(txt5))
        self.wait(1)
        self.play(FadeIn(txt6))
        self.wait(5)
        self.play(FadeOut(man),FadeOut(txt1),FadeOut(txt2),FadeOut(txt3),FadeOut(txt4),FadeOut(txt5),FadeOut(txt6))
        self.wait(1)
        self.play(FadeIn(nwtxt1))
        self.wait(1)
        self.play(FadeIn(nwtxt2))
        self.wait(1)
        self.play(FadeIn(nwtxt3))
        self.wait(1)
        self.play(FadeIn(blue_circle),FadeIn(blue_ex))
        self.wait(1)
        self.play(FadeIn(green_circle),FadeIn(green_ex))
        self.wait(2)
        self.play(FadeOut(nwtxt1),FadeOut(nwtxt2),FadeOut(nwtxt3),FadeOut(blue_circle),FadeOut(blue_ex),FadeOut(green_circle),FadeOut(green_ex),
                  FadeOut(title),FadeOut(line))

class Technique(Scene):
    def construct(self):
        title = Text("Greedy Technique").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)

        text1 = TextMobject("We can apply the greedy technique to solve the problem").scale(0.8).next_to(line,DOWN)
        text2 = TextMobject("As in the query there are two questions to answer").scale(0.8).next_to(line,DOWN)
        text3 = TextMobject("We could handle them separately").scale(0.8).next_to(line,DOWN)
        text4 = TextMobject("Task I : Answer at most how many of the existing stones are Bought.").scale(0.8).next_to(line,DOWN)
        text5 = TextMobject("Task II: Answer at least how many of the existing stones are Bought.").scale(0.8).next_to(line,DOWN)

        ans1_1 = TextMobject("As we want to retain as many Bought stones as possible").scale(0.8).next_to(text4,DOWN)
        ans1_2 = TextMobject("Therefore, We can use as many Given stones as possible.").scale(0.8).next_to(text4,DOWN)
        ans1_3 = TextMobject("In this case, we should use those two Given stones.").scale(0.8).next_to(text4,DOWN)
        ans1_4 = TextMobject("So the maximum number is 1.").scale(0.8).next_to(text4,DOWN)

        ans2_1 = TextMobject("Similarly, we can use as many Bought stones as possible").scale(0.8).next_to(text5,DOWN)
        ans2_2 = TextMobject("Therefore, the minimum number of Bought stones is 0.").scale(0.8).next_to(text5,DOWN)

        text4[0][12:18].set_color(PURPLE)
        text4[0][-7:-1].set_color(BLUE)
        text5[0][13:20].set_color(PURPLE)
        text5[0][-7:-1].set_color(BLUE)
        ans1_1[0][22:28].set_color(BLUE)
        ans1_2[0][24:29].set_color(GREEN)
        ans1_3[0][30:35].set_color(GREEN)
        ans2_1[0][24:30].set_color(BLUE)
        ans2_2[0][28:34].set_color(BLUE)

        circle1 = Circle(radius=1,color=GREEN).move_to(np.array([-4,-2,0])).set_opacity(0.5)
        circle2 = Circle(radius=1,color=BLUE).move_to(np.array([-3,-2+np.sqrt(3),0])).set_opacity(0.5)
        circle3 = Circle(radius=1,color=GREEN).move_to(np.array([-2,-2,0])).set_opacity(0.5)
        ex = TextMobject("For Example:").scale(0.8).next_to(circle2,LEFT)
        use = TextMobject("Use two stones").scale(0.8).move_to(np.array([-3,-3.5,0]))

        self.play(FadeIn(title),FadeIn(line))
        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3))
        self.wait(2)
        self.play(FadeOut(text3))
        self.play(FadeIn(text4))
        self.wait(1)
        self.play(FadeIn(ans1_1))
        self.wait(2)
        self.play(ReplacementTransform(ans1_1,ans1_2))
        self.wait(2)
        self.play(FadeIn(ex))
        self.play(FadeIn(circle1),FadeIn(circle2),FadeIn(circle3))
        self.play(FadeIn(use))
        self.wait(3)
        self.play(ReplacementTransform(ans1_2,ans1_3))
        self.wait(3)
        self.play(FadeOut(circle1),FadeOut(circle3))
        self.wait(2)
        self.play(ReplacementTransform(ans1_3,ans1_4))
        self.wait(3)
        self.play(FadeOut(text4),FadeOut(ans1_4))
        self.play(FadeIn(text5),FadeIn(circle1),FadeIn(circle3))
        self.wait(3.5)
        self.play(FadeIn(ans2_1))
        self.wait(2)
        self.play(FadeOut(circle1),FadeOut(circle2))
        self.wait(2)
        self.play(ReplacementTransform(ans2_1,ans2_2))
        self.wait(3)
        self.play(FadeOut(circle3),FadeOut(text5),FadeOut(ex),FadeOut(use),FadeOut(title),FadeOut(line),FadeOut(ans2_2))

class Variable(Scene):
    def construct(self):
        title = Text("Variables").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)   

        self.play(FadeIn(title),FadeIn(line))
        self.wait(1.5)
        text1 = TextMobject("We can use four variables for computing the result.").scale(0.8).next_to(line,DOWN)
        text2 = TextMobject("These two indicate the number of Bought and Given stones in the Maximisation Scenario").scale(0.8).to_edge(DOWN)
        text3 = TextMobject("And these two indicate the number of Bought and Given stones in the Minimisation Scenario").scale(0.8).to_edge(DOWN)
        
        var1 = Text(r"MX_B      MX_G").shift(0.5*UP)
        var2 = Text(r"MN_B      MN_G").next_to(var1,DOWN)

        var1[0:4].set_color(BLUE)
        var2[0:4].set_color(BLUE)
        var1[4:].set_color(GREEN)
        var2[4:].set_color(GREEN)
        text2[0][27:33].set_color(BLUE)
        text2[0][36:41].set_color(GREEN)
        text3[0][30:36].set_color(BLUE)
        text3[0][39:44].set_color(GREEN)      

        self.play(Write(text1))
        self.wait(2)
        self.play(FadeIn(var1))
        self.wait(2.5)
        self.play(Write(text2))
        self.wait(3)
        self.play(FadeIn(var2))
        self.wait(2.5)
        self.play(ReplacementTransform(text2,text3))
        self.wait(3.5)

class Sample(Scene):
    def construct(self):
        title = Text("Sample").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)
        self.play(FadeIn(title),FadeIn(line))
        self.wait(1)       

        txt1 = TextMobject("We use sample as an example").scale(0.8).next_to(line,DOWN).to_edge(LEFT)
        txt2 = TextMobject("There are six events").scale(0.8).next_to(line,DOWN)
        txt3 = TextMobject("Buy three magic stones",color=BLUE).scale(0.8).next_to(line,DOWN)
        txt4 = TextMobject("Given four magic stones",color=GREEN).scale(0.8).next_to(line,DOWN)
        txt5 = TextMobject("Use five magic stones.").scale(0.8).next_to(line,DOWN)
        txt6 = TextMobject("Query").scale(0.8).next_to(line,DOWN)
        txt7 = TextMobject("Use one magic stone.").scale(0.8).next_to(line,DOWN)
        txt8 = TextMobject("Query").scale(0.8).next_to(line,DOWN)

        txt3[0][0:3].set_color(BLUE)
        txt4[0][0:5].set_color(GREEN)

        sample1 = TextMobject("6").scale(0.8).next_to(line,DOWN).to_edge(LEFT)
        sample2 = TextMobject("1 3").scale(0.8).next_to(sample1,DOWN).to_edge(LEFT)
        sample3 = TextMobject("2 4").scale(0.8).next_to(sample2,DOWN).to_edge(LEFT)
        sample4 = TextMobject("3 5").scale(0.8).next_to(sample3,DOWN).to_edge(LEFT)
        sample5 = TextMobject("4").scale(0.8).next_to(sample4,DOWN).to_edge(LEFT)
        sample6 = TextMobject("3 1").scale(0.8).next_to(sample5,DOWN).to_edge(LEFT)
        sample7 = TextMobject("4").scale(0.8).next_to(sample6,DOWN).to_edge(LEFT)
        
        sample1_bg = SurroundingRectangle(sample1, fill_opacity = .2)
        sample2_bg = SurroundingRectangle(sample2, fill_opacity = .2)       
        sample3_bg = SurroundingRectangle(sample3, fill_opacity = .2)
        sample4_bg = SurroundingRectangle(sample4, fill_opacity = .2)
        sample5_bg = SurroundingRectangle(sample5, fill_opacity = .2)
        sample6_bg = SurroundingRectangle(sample6, fill_opacity = .2)
        sample7_bg = SurroundingRectangle(sample7, fill_opacity = .2)

        exp1 = TextMobject("In the maximisation scenario, we use as many Given stones as possible").scale(0.8).next_to(line,DOWN)
        exp2 = TextMobject("If it is in the minimisation scenario, we use as many Bought stones as possible").scale(0.8).next_to(line,DOWN)
        exp3 = TextMobject("We could directly output MX\_B and MN\_B").scale(0.8).next_to(line,DOWN)
        exp4 = TextMobject("2 0").scale(0.8).next_to(line,DOWN)
        exp5 = TextMobject("In the maximisation scenario").scale(0.8).next_to(line,DOWN)
        exp6 = TextMobject("In the minimisation scenario").scale(0.8).next_to(line,DOWN)
        exp7 = TextMobject("We can output 1 0").scale(0.8).next_to(line,DOWN)

        exp1[0][37:42].set_color(GREEN)
        exp2[0][43:49].set_color(BLUE)
        exp3[0][21:25].set_color(BLUE)
        exp3[0][28:32].set_color(BLUE)

        var1 = Text(r"MX_B      MX_G").scale(0.3).shift(0.5*UP).to_edge(RIGHT)
        var_eq1 = Text(r"0         0").scale(0.3).next_to(var1,DOWN)
        var2 = Text(r"MN_B      MN_G").scale(0.3).next_to(var_eq1,DOWN)
        var_eq2 = Text(r"0         0").scale(0.3).next_to(var2,DOWN)

        var1_eq1 = Text(r"3         0").scale(0.3).next_to(var1,DOWN)
        var1_eq2 = Text(r"3         0").scale(0.3).next_to(var2,DOWN)

        var2_eq1 = Text(r"3         4").scale(0.3).next_to(var1,DOWN)
        var2_eq2 = Text(r"3         4").scale(0.3).next_to(var2,DOWN)

        var3_eq1 = Text(r"2         0").scale(0.3).next_to(var1,DOWN)
        var3_eq2 = Text(r"0         2").scale(0.3).next_to(var2,DOWN) 

        var4_eq1 = Text(r"1         0").scale(0.3).next_to(var1,DOWN)
        var4_eq2 = Text(r"0         1").scale(0.3).next_to(var2,DOWN) 

        var_eq1_bg = SurroundingRectangle(var_eq1, fill_opacity = .2)     
        var_eq2_bg = SurroundingRectangle(var_eq2, fill_opacity = .2)    

        var1[0:4].set_color(BLUE)
        var2[0:4].set_color(BLUE)
        var1[4:].set_color(GREEN)
        var2[4:].set_color(GREEN)
    
        blue_circle1 = Circle(radius=1,color=BLUE).move_to(np.array([-4,-2,0])).set_opacity(0.5)
        blue_circle2 = Circle(radius=1,color=BLUE).move_to(np.array([-3,-2+np.sqrt(3),0])).set_opacity(0.5)
        blue_circle3 = Circle(radius=1,color=BLUE).move_to(np.array([-2,-2,0])).set_opacity(0.5)

        green_circle1 = Circle(radius=1,color=GREEN).move_to(np.array([0.5,-2,0])).set_opacity(0.5)
        green_circle2 = Circle(radius=1,color=GREEN).move_to(np.array([0.5,0,0])).set_opacity(0.5)
        green_circle3 = Circle(radius=1,color=GREEN).move_to(np.array([2.5,-2,0])).set_opacity(0.5)
        green_circle4 = Circle(radius=1,color=GREEN).move_to(np.array([2.5,0,0])).set_opacity(0.5)

        self.play(FadeIn(txt1))
        self.wait(0.5)
        self.play(FadeIn(var1),FadeIn(var_eq1),FadeIn(var2),FadeIn(var_eq2))
        self.play(FadeOut(txt1))
        self.play(FadeIn(sample1),FadeIn(sample2),FadeIn(sample3),FadeIn(sample4),FadeIn(sample5),FadeIn(sample6),FadeIn(sample7))
        
        self.wait(0.5)
        self.play(FadeIn(sample1_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample1,sample1_bg), txt2))
        self.wait(1)
        self.play(FadeOut(txt2))

        self.wait(0.5)
        self.play(FadeIn(sample2_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample2,sample2_bg), txt3))
        self.wait(1)
        self.play(FadeIn(blue_circle1),FadeIn(blue_circle2),FadeIn(blue_circle3))
        self.play(Write(var_eq1_bg),Write(var_eq2_bg))
        self.wait(1)
        self.play(ReplacementTransform(var_eq1,var1_eq1),ReplacementTransform(var_eq2,var1_eq2))
        self.play(FadeOut(var_eq1_bg),FadeOut(var_eq2_bg))        
        self.play(FadeOut(txt3))

        self.wait(0.5)
        self.play(FadeIn(sample3_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample3,sample3_bg), txt4))
        self.wait(1)
        self.play(FadeIn(green_circle1),FadeIn(green_circle2),FadeIn(green_circle3),FadeIn(green_circle4))
        self.play(Write(var_eq1_bg),Write(var_eq2_bg))
        self.wait(1)
        self.play(ReplacementTransform(var1_eq1,var2_eq1),ReplacementTransform(var1_eq2,var2_eq2))
        self.play(FadeOut(var_eq1_bg),FadeOut(var_eq2_bg))
        self.play(FadeOut(txt4))

        self.wait(0.5)
        self.play(FadeIn(sample4_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample4,sample4_bg), txt5))
        self.wait(1.5)
        self.play(ReplacementTransform(txt5, exp1))
        self.wait(2.5)
        self.play(FadeOut(green_circle1),FadeOut(green_circle2),FadeOut(green_circle3),FadeOut(green_circle4),FadeOut(blue_circle2))
        self.wait(2)
        self.play(Write(var_eq1_bg))
        self.wait(1)
        self.play(ReplacementTransform(var2_eq1,var3_eq1))
        self.wait(1)
        self.play(FadeOut(var_eq1_bg))
        self.wait(2.5)
        self.play(FadeIn(green_circle1),FadeIn(green_circle2),FadeIn(green_circle3),FadeIn(green_circle4),FadeIn(blue_circle2))
        self.play(ReplacementTransform(exp1, exp2))
        self.wait(2.5)
        self.play(FadeOut(green_circle1),FadeOut(green_circle3),FadeOut(blue_circle1),FadeOut(blue_circle2),FadeOut(blue_circle3))
        self.wait(2)
        self.play(Write(var_eq2_bg))
        self.wait(1)
        self.play(ReplacementTransform(var2_eq2,var3_eq2))
        self.wait(1)
        self.play(FadeOut(var_eq2_bg))
        self.wait(2.5)
        self.play(FadeOut(exp2))

        self.wait(0.5)
        self.play(FadeIn(sample5_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample5,sample5_bg), txt6))
        self.wait(1) # Query
        self.play(ReplacementTransform(txt6,exp3))
        self.wait(2.5)
        self.play(ReplacementTransform(exp3,exp4))
        self.wait(2)
        self.play(FadeOut(exp4))
        self.wait(0.5)
        self.play(FadeIn(green_circle1),FadeIn(green_circle3),FadeIn(blue_circle1),FadeIn(blue_circle2),FadeIn(blue_circle3))
        self.play(FadeIn(sample6_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample6,sample6_bg), txt7))
        self.wait(1.5)
        self.play(ReplacementTransform(txt7, exp5))
        self.play(FadeOut(green_circle1),FadeOut(green_circle2),FadeOut(green_circle3),FadeOut(green_circle4),FadeOut(blue_circle2))
        self.wait(1.5)
        self.play(FadeOut(blue_circle3))
        self.play(Write(var_eq1_bg))
        self.wait(1)
        self.play(ReplacementTransform(var3_eq1,var4_eq1))
        self.wait(1)
        self.play(FadeOut(var_eq1_bg))

        self.wait(3)
        self.play(FadeIn(green_circle1),FadeIn(green_circle2),FadeIn(green_circle3),FadeIn(green_circle4),FadeIn(blue_circle2),FadeIn(blue_circle3))
        self.play(ReplacementTransform(exp5,exp6))
        self.wait(1.5)
        self.play(FadeOut(green_circle1),FadeOut(green_circle3),FadeOut(blue_circle1),FadeOut(blue_circle2),FadeOut(blue_circle3))
        self.wait(2.5)
        self.play(FadeOut(green_circle4))
        self.play(Write(var_eq2_bg))
        self.wait(1)
        self.play(ReplacementTransform(var3_eq2,var4_eq2))
        self.wait(1)
        self.play(FadeOut(var_eq2_bg))
        self.wait(0.5)
        self.play(FadeOut(exp6))

        self.wait(0.5)
        self.play(FadeIn(green_circle1),FadeIn(green_circle3),FadeIn(green_circle4),
                  FadeIn(blue_circle1),FadeIn(blue_circle2),FadeIn(blue_circle3))
        self.play(FadeIn(sample7_bg))
        self.wait(0.5)
        self.play(ReplacementTransform(VGroup(sample7,sample7_bg), txt8))
        self.wait(1)
        self.play(ReplacementTransform(txt8, exp7))
        self.wait(2)
        self.play(FadeOut(exp7))
        self.wait(2)
        self.play(FadeOut(title),FadeOut(line),FadeOut(var1),FadeOut(var2),FadeOut(var4_eq1),FadeOut(var4_eq2),
                  FadeOut(blue_circle1),FadeOut(blue_circle2),FadeOut(blue_circle3),
                  FadeOut(green_circle1),FadeOut(green_circle2),FadeOut(green_circle3),FadeOut(green_circle4))

class Code(Scene):
    def construct(self):
        title = Text("Code").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)

        text1 = TextMobject("The Variable Declaration and Input Part").next_to(line,DOWN).scale(0.75).to_edge(RIGHT)
        text2 = TextMobject("As $1 \leq N \leq 100000$, we should use $longint$",t2c={"longint":BLUE}).scale(0.75).next_to(text1,DOWN).align_to(text1,LEFT)
        text3 = TextMobject("when Type is 4, we directly output the result.").next_to(line,DOWN)
        text4 = TextMobject("when Type is 1, both scenarios receive $k$ Bought stones").next_to(line,DOWN)
        text5 = TextMobject("when Type is 2, both scenarios receive $k$ Given stones").next_to(line,DOWN)
        text6 = TextMobject("In the maximisation scenario, we use Given stones first").next_to(line,DOWN)
        text7 = TextMobject("Only when all of them have been used can we use Bought stones.").next_to(line,DOWN)
        text8 = TextMobject("In the minimisation scenario, we use Bought stones first").next_to(line,DOWN)
        text9 = TextMobject("Only when all of them have been used can we use Given stones.").next_to(line,DOWN)

        text4[0][33:39].set_color(BLUE)
        text5[0][33:38].set_color(GREEN)
        text6[0][31:36].set_color(GREEN)
        text7[0][37:43].set_color(BLUE)
        text8[0][31:37].set_color(BLUE)
        text9[0][37:42].set_color(GREEN)

        self.play(FadeIn(title),FadeIn(line))
        self.wait(0.5)

        code_init = Text("program task_1524;\nvar\n    i:longint;\n    n,t,k:longint;\n    mx_b,mx_g:longint;\n    mn_b,mn_g:longint;\nbegin\n    readln(n);\n\n    mx_b:=0;\n    mn_b:=0;\n    mn_g:=0;\n    mx_g:=0;",
                         font="consolas",
                         t2c = {
                             "var" : BLUE,
                             "longint" : BLUE,
                             "begin" : BLUE,
                             "0" : GREEN,
                          }).scale(0.4).next_to(line,DOWN).to_edge(LEFT)

        code_f = Text("for i:=1 to n do\n begin\n    read(t);\n    if (t=4) then writeln(mx_b,' ',mn_b)\n    else\n    begin\n        readln(k);\n        if (t=1) then\n        begin\n            mn_b:=mn_b+k;\n            mx_b:=mx_b+k;\n        end\n        else if (t=2) then\n        begin\n            mn_g:=mn_g+k; \n            mx_g:=mx_g+k; \n        end",
                     font = "consolas",
                     t2c = {
                        "if" : BLUE,
                        "else" : BLUE,
                        "then" : BLUE,
                        "begin" : BLUE,
                        "to" : BLUE,
                        "end" : BLUE,
                        "for" : PURPLE,
                        "do" : PURPLE,
                        "4" : GREEN,
                        "2" : GREEN,
                        "1" : GREEN,
                     }).scale(0.3).next_to(line,DOWN).to_edge(LEFT+DOWN)

        code_l = Text("else if (t=3) then\nbegin\n    if (mx_g>=k) then mx_g:=mx_g-k\n    else\n    begin\n        mx_b:=mx_b-(k-mx_g);\n        mx_g:=0;\n    end;\n\n    if (mn_b>=k) then mn_b:=mn_b-k\n    else\n    begin\n        mn_g:=mn_g-(k-mn_b);\n        mn_b:=0;\n    end;\nend;",
                     font = "consolas",
                     t2c = {
                        "if" : BLUE,
                        "else" : BLUE,
                        "then" : BLUE,
                        "begin" : BLUE,
                        "end" : BLUE,
                        "0" : GREEN,
                     }).scale(0.3).next_to(line,DOWN).to_edge(LEFT+DOWN) 


        self.play(FadeIn(code_init))
        self.wait(0.5)
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(code_init))
        self.wait(1)
        self.play(FadeIn(code_f))
        self.wait(1)
        self.play(FadeIn(text3))
        self.wait(3)
        self.play(ReplacementTransform(text3,text4))
        self.wait(3)
        self.play(ReplacementTransform(text4,text5))
        self.wait(3)
        self.play(FadeOut(text5),FadeOut(code_f))
        self.wait(1)
        self.play(FadeIn(code_l))
        self.wait(1)
        self.play(FadeIn(text6))
        self.wait(4.5)
        self.play(ReplacementTransform(text6,text7))
        self.wait(4.5)
        self.play(ReplacementTransform(text7,text8))
        self.wait(4.5)
        self.play(ReplacementTransform(text8,text9))
        self.wait(2)
        self.play(FadeOut(text9),FadeOut(code_l),FadeOut(title),FadeOut(line))
        self.wait(1.5)


class End(Scene):
    def construct(self):
        title = Text("Other Problems About Greedy Technique").scale(0.7).to_edge(UP)
        line = Line(np.array([-10,2.75,0]),np.array([10,2.75,0]),color=ORANGE)
        text1 = TextMobject("PCOJ 1205 Currency Exchange")

        self.play(FadeIn(title),FadeIn(line),FadeIn(text1))

        self.wait(3)
        self.play(FadeOut(title),FadeOut(line),FadeOut(text1))

        text2 = TextMobject("Remember to attend PCOI summer training in summer holiday!")
        text3 = TextMobject("I am Artanis, see you next time!")
        text3[0][3:10].set_color(RED)

        self.play(Write(text2))
        self.wait(3)
        self.play(ReplacementTransform(text2,text3))
        self.wait(2)