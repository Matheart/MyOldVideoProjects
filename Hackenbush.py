from manimlib.imports import *
from manim_sandbox.utils.imports import *

class HText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Regular',
        'size' : 0.75,
    }

class SmallHText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Regular',
        'size' : 0.65,
    }

def Create_Axe(Lne, col): # Coordinate
    return SVGMobject("D:\\Maths\\Hackenbush\\Axe.svg").scale(0.3).move_to((Lne.get_start()+Lne.get_end())/2).set_color(col)

def AppendSegment(A, B, col = "#00EE00"):
    if A.get_center()[1] > B.get_center()[1]:
        A, B = B, A

    x1 = A.get_center()[0]
    y1 = A.get_center()[1]
    x2 = B.get_center()[0]
    y2 = B.get_center()[1]
    r = 0.08

    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        return Line(np.array([x1,y1+r,0]), np.array([x2,y2-r,0])).set_color(col)
    elif y1 == y2:
        x1, x2 = min(x1,x2), max(x1, x2)
        return Line(np.array([x1+r,y1,0]), np.array([x2-r,y2,0])).set_color(col)
    else:
        theta = np.arctan((y2 - y1) / (x2 - x1))
        if x1 > x2:
            return Line(A.get_center() - r * np.array([np.cos(theta), np.sin(theta), 0]),
                        B.get_center() + r * np.array([np.cos(theta), np.sin(theta), 0]))
        else:
            return Line(A.get_center() + r * np.array([np.cos(theta), np.sin(theta), 0]),
                        B.get_center() - r * np.array([np.cos(theta), np.sin(theta), 0]))      

class GreenIntro(Scene):
    def construct(self):
        captions = [
            "在數心花园里",
            "沧蓝和绯樱过着幸福快乐的生活",
            "在里面生长着绿树",
            "所有树枝都是绿色的",
        ]
        cap_text = [HText(caption) for caption in captions]

        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        
        Tree1 = [
            Line(np.array([-4.1361,-2.5,0]),np.array([-4.3964,-1.5843,0])), # CD 0
            Line(np.array([-4.3964,-1.5843,0]),np.array([-5.2015,-1.1216,0])), # DG 1
            Line(np.array([-5.2015,-1.1216,0]),np.array([-6.2960,-0.7859,0])), # GI 2
            Line(np.array([-5.2015,-1.1216,0]),np.array([-5.3912,-0.2022,0])), # GH 3
            Line(np.array([-4.3964,-1.5843,0]),np.array([-4.2804,-0.4514,0])), # DE 4
            Line(np.array([-4.2804,-0.4514,0]),np.array([-4.4856,0.3337,0])), # EF 5
            Line(np.array([-4.4856,0.3337,0]),np.array([-5.2599,1.0382,0])), # FJ 6
            Line(np.array([-4.2804,-0.4514,0]),np.array([-3.4649,0.2648,0])), # EK 7
            Line(np.array([-3.4649,0.2648,0]),np.array([-3.3482,0.9069,0])), # KL 8 
            Line(np.array([-4.3964,-1.5843,0]),np.array([-2.6769,-1.0778,0])), # DN 9
            Line(np.array([-2.6769,-1.0778,0]),np.array([-2.035,-0.3190,0])), # NO 10
            Line(np.array([-2.6769,-1.0778,0]),np.array([-1.6261,-0.7421,0])), # NP 11
        ]
        # 0;
        # 1,4,9;
        # 2,3,5,7,10,11;
        # 6,8;
        for i in Tree1:
            i.set_color("#00EE00")
        Tree2 = Line(np.array([-1.3197,-2.5,0]),np.array([-1.3051,-2.5,0])).set_color("#00EE00")
        Tree3 = [
            Line(np.array([-0.4441,-2.5,0]),np.array([-0.4149,-1.6032,0])).set_color("#00EE00"),
            Line(np.array([-0.4149,-1.6032,0]),np.array([-0.9402,-0.6692,0])).set_color("#00EE00"),
            Line(np.array([-0.4149,-1.6032,0]),np.array([-0.3419,-0.3919,0])).set_color("#00EE00"),
            Line(np.array([-0.4149,-1.6032,0]),np.array([0.5483,-0.7567,0])).set_color("#00EE00")
        ]
        Tree4 = Line(np.array([0.3294,-2.5,0]),np.array([0.3002,-1.9388,0])).set_color("#00EE00")
        
        BluePerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(BLUE).shift(5.2015*LEFT).rotate(PI).scale(0.3).shift(2.2*DOWN)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).shift(2.6769*LEFT).rotate(PI).scale(0.3).shift(2.2*DOWN)

        cap_text[0].to_edge(UP).shift(2.5*RIGHT+0.5*DOWN)
        for i in range(1,4):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        cap_text[0][1:5].set_color("#00EE00")
        cap_text[1][:2].set_color(BLUE)
        cap_text[1][3:5].set_color(RED)
        cap_text[2][6:].set_color("#00EE00")
        cap_text[3][2:4].set_color("#00EE00")
        cap_text[3][6:8].set_color("#00EE00")

        self.play(Write(cap_text[0]),ShowCreation(GroundLine))
        self.play(ShowCreation(VGroup(Tree1[0],Tree2,Tree4,Tree3[0])),run_time = 0.75)
        self.play(ShowCreation(VGroup(Tree1[1],Tree1[4],Tree1[9],Tree3[1],Tree3[2],Tree3[3])), run_time = 0.65)
        self.play(ShowCreation(VGroup(Tree1[2],Tree1[3],Tree1[5],Tree1[7],Tree1[10],Tree1[11])),run_time = 0.55)
        self.play(ShowCreation(VGroup(Tree1[6],Tree1[8])), run_time = 0.45)   
        self.wait(.5)
        self.play(Write(cap_text[1]),FadeIn(BluePerson),FadeIn(RedPerson))
        self.wait()
        self.play(Write(cap_text[2]))
        self.play(Write(cap_text[3]))
        self.wait(1)
        rec = FullScreenFadeRectangle().set_opacity(1)
        self.play(FadeIn(rec))

class GreenRules(Scene):
    def construct(self):
        captions = [
            "有一天他们一起玩砍树枝游戏 其中规定：", # Right
            "他们轮流砍树枝 沧蓝先砍而绯樱后砍",
            "每人每次只能砍一根",
            "砍完后没有和地面连接的树枝将会消失", # Bottom 
            "如果轮到其中一方时那一方已经没有能砍的树枝则可判负",
            "在接下来的游戏中,试分析哪一方有必胜策略"
        ]
        cap_text = [HText(caption) for caption in captions]

        cap_text[0].to_edge(UP+RIGHT)
        cap_text[1].next_to(cap_text[0], DOWN, aligned_edge = LEFT)
        cap_text[2].next_to(cap_text[1], DOWN, aligned_edge = LEFT)

        cap_text[0][8:11].set_color("#00EE00")
        cap_text[1][5:7].set_color("#00EE00")
        cap_text[1][8:10].set_color(BLUE)
        cap_text[1][13:15].set_color(RED)
        cap_text[3][6:8].set_color("#D2691E")

        cap_text[3].to_edge(DOWN)
        cap_text[4].to_edge(DOWN)
        cap_text[5].to_edge(DOWN)

        cap_text[3][11:13].set_color("#00EE00")
        cap_text[4][19:21].set_color("#00EE00")

        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        A = Dot(np.array([-7+8.0/3,-2.5,0]))
        B = Dot(np.array([-7+8.0/3,0,0]))
        C = Dot(np.array([-7+8.0/3*2,-2.5,0]))
        D = Dot(np.array([-7+8.0/3*2,0,0]))
        E = Dot(np.array([-7+8.0/3*2,2.5,0]))
        F = Dot(np.array([-7+8.0/3+1, 3.5, 0]))
        theta = 2*PI-np.arctan((3.5-2.5)/(-7+8.0/3+1-(-7+8.0/3*2)))
        L1 = Line(np.array([-7+8.0/3, -2.5 + 0.08, 0]), np.array([-7+8.0/3, - 0.08, 0])).set_color("#00EE00")
        L2 = Line(np.array([-7+8.0/3*2, -2.5 + 0.08, 0]), np.array([-7+8.0/3*2, 0 - 0.08, 0])).set_color("#00EE00")
        L3 = Line(np.array([-7+8.0/3*2, 0.08, 0]), np.array([-7+8.0/3*2, 2.5 - 0.08, 0])).set_color("#00EE00")
        L4 = Line(E.get_center() + 0.08 * np.array([-np.cos(theta),  np.sin(theta), 0]),
                  F.get_center() + 0.08 * np.array([ np.cos(theta), -np.sin(theta), 0])).set_color("#00EE00")

        BluePerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(BLUE).shift((-7+4.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).shift((-3+8.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)
        L1_Axe = Create_Axe(L1, BLUE)
        L2_Axe = Create_Axe(L2, RED)

        win = TextMobject("Win").set_color(RED).next_to(RedPerson, UP)
        lose = TextMobject("Lose").set_color(BLUE).next_to(BluePerson, UP)

        BlueTurn = HText("轮到沧蓝").to_edge(UP+LEFT)
        RedTurn = HText("轮到绯樱").to_edge(UP+LEFT)
        BlueTurn[2:].set_color(BLUE)
        RedTurn[2:].set_color(RED)
        Turn = HText("#").to_edge(UP+LEFT).set_color(BLACK)

        self.play(ShowCreation(GroundLine))
        self.play(ShowCreation(VGroup(A,B,L1,L2,C,D)))
        self.play(ShowCreation(VGroup(L3,E)))
        self.play(ShowCreation(VGroup(L4,F)))
        self.play(FadeIn(BluePerson, direction = UP),FadeIn(RedPerson, direction = UP))
        self.play(Write(cap_text[0]), Write(Turn))
        self.wait()
        self.play(Write(cap_text[1]))
        self.wait()
        self.play(Write(cap_text[2]))
        self.wait()
        self.play(Transform(Turn, BlueTurn))
        self.play(FadeIn(L1_Axe))
        self.wait()
        self.play(FadeOut(L1), FadeOut(L1_Axe),FadeOut(A),FadeOut(B))
        self.play(Transform(Turn, RedTurn))
        self.play(FadeIn(L2_Axe))
        self.wait()
        self.play(FadeOut(L2_Axe), FadeOut(L2), FadeOut(C))
        self.wait()
        self.play(Write(cap_text[3])) 
        self.wait()
        self.play(FadeOut(VGroup(L3, L4, D, E, F)))
        self.wait()
        self.play(Transform(Turn, BlueTurn))
        self.wait(1.5)
        # DE, EF
        self.play(ReplacementTransform(cap_text[3],cap_text[4])) # Continue
        self.play(Write(win),Write(lose))
        self.wait()
        self.play(ReplacementTransform(cap_text[4],cap_text[5]))      
        self.wait(2)
        

class RedBlueIntro(Scene):
    def construct(self):              
        captions = [
            "过了几天",
            "沧蓝和绯樱一起去另一个花园游玩",
            "发现树只有红色和蓝色两种树枝",
            "于是他们又玩起了砍树枝游戏",
            "规则和上述相同",
            "但沧蓝只能砍蓝色的树枝",
            "绯樱只能砍红色的树枝",
            "在接下来的游戏中,试分析哪一方有必胜策略"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[2].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[2], LEFT).to_edge(UP)
        for i in range(1, len(cap_text)-1):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        cap_text[1][0:2].set_color(BLUE)
        cap_text[1][3:5].set_color(RED)
        cap_text[1][11:13].set_color("#00EE00")
        cap_text[2][5:7].set_color(RED)
        cap_text[2][8:10].set_color(BLUE)
        cap_text[5][1:3].set_color(BLUE)
        cap_text[5][6:].set_color(BLUE)
        cap_text[6][0:2].set_color(RED)
        cap_text[6][5:].set_color(RED)
        cap_text[7].to_edge(DOWN)

        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")

        A = Dot(np.array([-4.8213,-2.5,0]))
        B = Dot(np.array([-4.8123,-1.3644,0]))
        C = Dot(np.array([-5.7183,-0.5773,0]))
        D = Dot(np.array([-4.2638,-0.4201,0]))
        E = Dot(np.array([-4.3031,0.6216,0]))
        F = Dot(np.array([-4.1262,-1.1167,0]))
        G = Dot(np.array([-3.3007,-0.6560,0]))
        H = Dot(np.array([-2.6324,-2.5,0]))
        I = Dot(np.array([-2.6324,-1.4029,0]))
        J = Dot(np.array([-2,-1,0]))
        K = Dot(np.array([-1.1976,-1.029,0]))
        L = Dot(np.array([-0.6473,-1.7566,0]))

        AB = AppendSegment(A, B).set_color(RED)
        BC = AppendSegment(B, C).set_color(BLUE)
        BD = AppendSegment(B, D).set_color(BLUE)
        DE = AppendSegment(D, E).set_color(BLUE)
        BF = AppendSegment(B, F).set_color(BLUE)
        FG = AppendSegment(F, G).set_color(BLUE)
        HI = AppendSegment(H, I).set_color(RED)
        IJ = AppendSegment(I, J).set_color(BLUE)
        JK = AppendSegment(J, K).set_color(BLUE)
        KL = AppendSegment(K, L).set_color(RED)

        BD_Axe = Create_Axe(BD, BLUE)
        AB_Axe = Create_Axe(AB, RED)
        IJ_Axe = Create_Axe(IJ, BLUE)
        HI_Axe = Create_Axe(HI, RED)

        BluePerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(BLUE).shift((-7+4.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).shift((-3+8.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)

        win = TextMobject("Win").set_color(RED).next_to(RedPerson, UP)
        lose = TextMobject("Lose").set_color(BLUE).next_to(BluePerson, UP)

        BlueTurn = HText("轮到沧蓝").to_edge(UP+LEFT)
        RedTurn = HText("轮到绯樱").to_edge(UP+LEFT)
        BlueTurn[2:].set_color(BLUE)
        RedTurn[2:].set_color(RED)
        Turn = HText("#").to_edge(UP+LEFT).set_color(BLACK)

        self.play(ShowCreation(GroundLine))
        self.play(Write(cap_text[0]))
        self.play(Write(cap_text[1]))
        self.play(FadeIn(BluePerson), FadeIn(RedPerson))
        self.play(Write(cap_text[2]))
        self.wait()
        # Show Tree
        self.play(FadeIn(VGroup(A, AB, B)), FadeIn(VGroup(H, HI, I)))
        self.play(FadeIn(VGroup(BC, BD, BF, C, D, F)), FadeIn(VGroup(IJ, J)))
        self.play(FadeIn(VGroup(DE, FG, E, G)), FadeIn(VGroup(JK, K)))
        self.play(FadeIn(VGroup(KL, L)))
        self.wait()
        self.play(Write(cap_text[3]))
        self.play(Write(cap_text[4]))
        self.play(Write(cap_text[5]))
        self.play(Write(cap_text[6]))
        self.wait()
        # Show Cut
        self.play(Transform(Turn, BlueTurn))
        self.play(FadeIn(BD_Axe))
        self.play(FadeOut(VGroup(BD_Axe,BD,DE,D,E)))
        self.play(Transform(Turn, RedTurn))
        self.play(FadeIn(AB_Axe))
        self.play(FadeOut(VGroup(AB_Axe,A,B,C,G,F,AB,BC,BF,FG)))
        self.play(Transform(Turn, BlueTurn))
        self.play(FadeIn(IJ_Axe))
        self.play(FadeOut(VGroup(IJ_Axe,J,K,L,IJ,JK,KL)))
        self.play(Transform(Turn, RedTurn))
        self.play(FadeIn(HI_Axe))
        self.play(FadeOut(VGroup(H,I,HI,HI_Axe)))
        self.play(Transform(Turn, BlueTurn))
        self.wait(1)
        self.play(Write(win), Write(lose))
        self.wait()
        self.play(Write(cap_text[7]))


class RGBIntro(Scene):
    def construct(self):
        captions = [
            "又过了几天 他们看见了几朵花",
            "玩起了砍花小游戏",
            "规则与砍树枝游戏相似",
            "两人轮流砍",
            "每次只能砍一条根茎或一片花瓣",
            "双方都能砍绿色的根茎",
            "但蓝色的花瓣只能被沧蓝砍掉",
            "红色的花瓣只能被绯樱砍掉",
            "在接下来的游戏中,试分析哪一方有必胜策略"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[4].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[4], LEFT).to_edge(UP)
        for i in range(1, len(cap_text)-1):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        cap_text[8].to_edge(DOWN)
        cap_text[1][3:8].set_color(PURPLE)
        cap_text[4][7:9].set_color("#00EE00")
        cap_text[4][12:].set_color(PURPLE)
        cap_text[5][5:].set_color("#00EE00")
        cap_text[6][1:3].set_color(BLUE)
        cap_text[6][4:6].set_color(PURPLE)
        cap_text[6][9:11].set_color(BLUE)
        cap_text[7][:2].set_color(RED)
        cap_text[7][3:5].set_color(PURPLE)
        cap_text[7][8:10].set_color(RED)

        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")

        A = Dot(np.array([-4.4031,-2.5,0]))
        B = Dot(np.array([-4.4031,-0.7146,0]))
        C = Dot(np.array([-3.0521,-2.5,0]))
        D = Dot(np.array([-3.0521,-0.7146,0]))
        E = Dot(np.array([-1.5608,-2.5,0]))
        F = Dot(np.array([-1.5608,-0.6764,0]))
        func1 = ParametricFunction(lambda t: np.array([-4.7408588005 + 0.3460315312 * np.cos(t) + 0.0042571594 * np.sin(t), -0.6955046599 - 0.0195866904 * np.cos(t) + 0.0752098157 * np.sin(t), 0]), t_min = -PI, t_max = PI)
        func2 = ParametricFunction(lambda t: np.array([-4.0637288361 + 0.3460315312 * np.cos(t) + 0.0042571594 * np.sin(t), -0.7314771892 - 0.0195866904 * np.cos(t) + 0.0752098157 * np.sin(t), 0]), t_min = -PI, t_max = PI)
        func1.set_color(RED)
        func2.set_color(BLUE)
        AB = AppendSegment(A, B)
        CD = AppendSegment(C, D)
        EF = AppendSegment(E, F)

        func2Axe = SVGMobject("D:\\Maths\\Hackenbush\\Axe.svg").scale(0.3).move_to(np.array([-4.0799, -0.7214, 0])).set_color(BLUE)
        CDAxe = Create_Axe(CD, RED)
        EFAxe = Create_Axe(EF, BLUE)
        ABAxe = Create_Axe(AB, RED)

        BluePerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(BLUE).shift((-7+4.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).shift((-3+8.0/3)*RIGHT).rotate(PI).scale(0.3).shift(2.2*DOWN)

        win = TextMobject("Win").set_color(RED).next_to(RedPerson, UP)
        lose = TextMobject("Lose").set_color(BLUE).next_to(BluePerson, UP)

        BlueTurn = HText("轮到沧蓝").to_edge(UP+LEFT)
        RedTurn = HText("轮到绯樱").to_edge(UP+LEFT)
        BlueTurn[2:].set_color(BLUE)
        RedTurn[2:].set_color(RED)
        Turn = HText("#").to_edge(UP+LEFT).set_color(BLACK)

        self.play(ShowCreation(GroundLine), FadeIn(BluePerson), FadeIn(RedPerson))
        self.play(Write(Turn), ShowCreation(VGroup(A,C,E,AB,CD,EF,func1,func2)))
        self.play(ShowCreation(VGroup(B,D,F)))
        self.play(Write(cap_text[0]))
        self.wait()
        self.play(Write(cap_text[1]), Write(cap_text[2]))
        self.wait(1)
        self.play(Write(cap_text[3]), Write(cap_text[4]))
        self.wait(1)
        self.play(Write(cap_text[5]), Write(cap_text[6]), Write(cap_text[7]))
        self.wait(2)
        # Show Cut
        self.play(Transform(Turn, BlueTurn))
        self.play(FadeIn(func2Axe))
        self.wait()
        self.play(FadeOut(func2Axe), FadeOut(func2))
        self.play(Transform(Turn, RedTurn))
        self.play(FadeIn(CDAxe))
        self.wait()
        self.play(FadeOut(CDAxe), FadeOut(CD), FadeOut(C), FadeOut(D))
        self.play(Transform(Turn, BlueTurn))
        self.play(FadeIn(EFAxe))
        self.wait()
        self.play(FadeOut(EFAxe), FadeOut(EF), FadeOut(E), FadeOut(F))
        self.play(Transform(Turn, RedTurn))
        self.play(FadeIn(ABAxe))
        self.wait()
        self.play(FadeOut(ABAxe), FadeOut(AB), FadeOut(func1), FadeOut(A), FadeOut(B))
        self.play(Transform(Turn, BlueTurn))
        self.wait(1)
        self.play(Write(win), Write(lose))
        self.wait()
        self.play(Write(cap_text[8]))