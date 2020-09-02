from manimlib.imports import *

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


class Green1(Scene): # Blue
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "4. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[4].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[4], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[1][11:].set_color("#00EE00")
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[4][3:5].set_color("#D2691E")
        cap_text[4][8:10].set_color("#00EE00")
        cap_text[6][8:10].set_color("#00EE00")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")

        BluePerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, DOWN).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, DOWN).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(Task)
        self.add(GroundLine)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-6.0568,-2.5,0]))
        B = Dot(np.array([-6.0212,-1.4576,0]))
        C = Dot(np.array([-5.9857,-0.3718,0]))
        D = Dot(np.array([-5.2025,-2.5,0]))
        E = Dot(np.array([-5.2025,-1.4042,0]))
        F = Dot(np.array([-4.3126,-2.5,0]))
        G = Dot(np.array([-4.2948,-1.3508,0]))
        H = Dot(np.array([-4.2414,-0.3184,0]))
        I = Dot(np.array([-4.2770,1.070,0]))
        J = Dot(np.array([-3.2090,-2.5,0]))
        K = Dot(np.array([-3.2980,-1.3686,0]))
        L = Dot(np.array([-2.9598,-0.4430,0]))
        M = Dot(np.array([-2.2835,0.4647,0]))
        N = Dot(np.array([-1.6071,0.9097,0]))
        O = Dot(np.array([-0.7350,1.1055,0]))
        P = Dot(np.array([-1.4469,-2.5,0]))
        Q = Dot(np.array([-1.5003,-1.3864,0]))

        AB = AppendSegment(A, B).set_color("#00EE00")
        BC = AppendSegment(B, C).set_color("#00EE00")
        DE = AppendSegment(D, E).set_color("#00EE00")
        FG = AppendSegment(F, G).set_color("#00EE00")
        GH = AppendSegment(G, H).set_color("#00EE00")
        HI = AppendSegment(H, I).set_color("#00EE00")
        JK = AppendSegment(J, K).set_color("#00EE00")
        KL = AppendSegment(K, L).set_color("#00EE00")
        LM = AppendSegment(L, M).set_color("#00EE00")
        MN = AppendSegment(M, N).set_color("#00EE00")
        NO = AppendSegment(N, O).set_color("#00EE00")
        PQ = AppendSegment(P, Q).set_color("#00EE00")

        self.play(FadeIn(VGroup(
            A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q,
            AB, BC, DE, FG, GH, HI, JK, KL, LM, MN, NO, PQ
        )))
        self.wait(7)

class Green2(Scene): # Red
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "4. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[4].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[4], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[1][11:].set_color("#00EE00")
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[4][3:5].set_color("#D2691E")
        cap_text[4][8:10].set_color("#00EE00")
        cap_text[6][8:10].set_color("#00EE00")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, DOWN).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, DOWN).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-6.1598,-2.5,0]))
        B = Dot(np.array([-5.1708,-2.5,0]))
        C = Dot(np.array([-4.1058,-2.5,0]))
        D = Dot(np.array([-3.3450,-2.5,0]))
        E = Dot(np.array([-2.0191,-2.5,0]))
        F = Dot(np.array([-0.8454,-2.5,0]))
        G = Dot(np.array([-6.1598,-1.413,0]))
        H = Dot(np.array([-5.2034,-1.4022,0]))
        I = Dot(np.array([-4.1710,-1.369,0]))
        J = Dot(np.array([-3.06,-1.62,0]))
        K = Dot(np.array([-1.85,-1.7,0]))
        L = Dot(np.array([-1.21,-1.61,0]))
        M = Dot(np.array([-5.26,-0.837,0]))
        N = Dot(np.array([-3.986,-0.641,0]))
        O = Dot(np.array([-5.366,0,0]))
        P = Dot(np.array([-6.453,-0.402,0]))

        AG = AppendSegment(A, G).set_color("#00EE00")
        BH = AppendSegment(B, H).set_color("#00EE00")
        HM = AppendSegment(H, M).set_color("#00EE00")
        HN = AppendSegment(H, N).set_color("#00EE00")
        MP = AppendSegment(M, P).set_color("#00EE00")
        MO = AppendSegment(M, O).set_color("#00EE00")
        CI = AppendSegment(C, I).set_color("#00EE00")
        DJ = AppendSegment(D, J).set_color("#00EE00")
        EK = AppendSegment(E, K).set_color("#00EE00")
        FL = AppendSegment(F, L).set_color("#00EE00")

        self.play(FadeIn(VGroup(
            A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,
            AG,BH,HM,HN,MP,MO,CI,DJ,EK,FL
        )))
        self.wait(7)

class Green3(Scene): # Blue
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "4. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[4].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[4], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[1][11:].set_color("#00EE00")
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[4][3:5].set_color("#D2691E")
        cap_text[4][8:10].set_color("#00EE00")
        cap_text[6][8:10].set_color("#00EE00")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, DOWN).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, DOWN).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-5.7,-2.5,0]))
        B = Dot(np.array([-5.3,-1.5,0]))
        C = Dot(np.array([-4.3,-1.1,0]))
        D = Dot(np.array([-3.4,-1.2,0]))
        E = Dot(np.array([-2.5,-1.7,0]))
        F = Dot(np.array([-2,-2.5,0]))
        
        AB = AppendSegment(A, B).set_color("#00EE00")
        BC = AppendSegment(B, C).set_color("#00EE00")
        CD = AppendSegment(C, D).set_color("#00EE00")
        DE = AppendSegment(D, E).set_color("#00EE00")
        EF = AppendSegment(E, F).set_color("#00EE00")

        self.play(FadeIn(VGroup(
            A,B,C,D,E,F,
            AB,BC,CD,DE,EF
        )))
        self.wait(7)

class RedBlue1(Scene):
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 沧蓝只能砍蓝色的树枝",
            "绯樱只能砍红色的树枝",
            "4. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "5. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[6].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[6], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[3][2:5].set_color(BLUE)
        cap_text[3][8:].set_color(BLUE)
        cap_text[4][:2].set_color(RED)
        cap_text[4][5:].set_color(RED)
        cap_text[6][3:5].set_color("#D2691E")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, DOWN).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, DOWN).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-5,-2.5,0]))
        B = Dot(np.array([-5,-1.6,0]))
        C = Dot(np.array([-5.5,-1,0]))
        D = Dot(np.array([-5.5,-0.1,0]))
        E = Dot(np.array([-4.5,-1,0]))
        F = Dot(np.array([-4.4,-0.1,0]))
        G = Dot(np.array([-3.7,-1,0]))
        H = Dot(np.array([-2.7,-2.5,0]))
        I = Dot(np.array([-2,-1.6,0]))
        J = Dot(np.array([-1.4,-2.5,0]))
        K = Dot(np.array([-2.1,-0.7,0]))
        L = Dot(np.array([-3.1,-1.6,0]))
        M = Dot(np.array([-0.9,-1.5,0]))

        AB = AppendSegment(A, B).set_color(BLUE)
        BC = AppendSegment(B, C).set_color(BLUE)
        CD = AppendSegment(C, D).set_color(BLUE)
        BE = AppendSegment(B, E).set_color(BLUE)
        EF = AppendSegment(E, F).set_color(BLUE)
        EG = AppendSegment(E, G).set_color(BLUE)

        HI = AppendSegment(H, I).set_color(RED)
        JI = AppendSegment(J, I).set_color(RED)
        IL = AppendSegment(I, L).set_color(RED)
        IK = AppendSegment(I, K).set_color(RED)
        IM = AppendSegment(I, M).set_color(RED)

        self.play(FadeIn(VGroup(
            A, B, C, D, E, F, G, H, I, J, K, L, M,
            AB, BC, CD, BE, EF, EG, HI, JI, IL, IK, IM
        )))
        self.wait(7)

class RedBlue2(Scene):
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 沧蓝只能砍蓝色的树枝",
            "绯樱只能砍红色的树枝",
            "4. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "5. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[6].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[6], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[3][2:5].set_color(BLUE)
        cap_text[3][8:].set_color(BLUE)
        cap_text[4][:2].set_color(RED)
        cap_text[4][5:].set_color(RED)
        cap_text[6][3:5].set_color("#D2691E")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, DOWN).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, DOWN).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array(np.array([-5,-2.5,0])))
        B = Dot(np.array(np.array([-5,-2,0])))
        C = Dot(np.array(np.array([-5.4,-1.5,0])))
        D = Dot(np.array(np.array([-4.5,-1.5,0])))
        E = Dot(np.array(np.array([-5.8,-0.8,0])))
        F = Dot(np.array(np.array([-5.9,-1.8,0])))
        G = Dot(np.array(np.array([-4,-1,0])))
        H = Dot(np.array(np.array([-4,-2,0])))

        A2 = A.copy().shift(3*RIGHT)
        B2 = B.copy().shift(3*RIGHT)
        C2 = C.copy().shift(3*RIGHT)
        D2 = D.copy().shift(3*RIGHT)
        E2 = E.copy().shift(3*RIGHT)
        F2 = F.copy().shift(3*RIGHT)
        G2 = G.copy().shift(3*RIGHT)
        H2 = H.copy().shift(3*RIGHT)

        AB = AppendSegment(A, B).set_color(RED)
        BC = AppendSegment(B, C).set_color(RED)
        BD = AppendSegment(B, D).set_color(RED)
        CD = AppendSegment(C, D).set_color(BLUE)
        CE = AppendSegment(C, E).set_color(BLUE)
        CF = AppendSegment(C, F).set_color(BLUE)
        DG = AppendSegment(D, G).set_color(BLUE)
        DH = AppendSegment(D, H).set_color(BLUE)

        A2B2 = AppendSegment(A2, B2).set_color(BLUE)
        B2C2 = AppendSegment(B2, C2).set_color(BLUE)
        B2D2 = AppendSegment(B2, D2).set_color(BLUE)
        C2D2 = AppendSegment(C2, D2).set_color(RED)
        C2E2 = AppendSegment(C2, E2).set_color(RED)
        C2F2 = AppendSegment(C2, F2).set_color(RED)
        D2G2 = AppendSegment(D2, G2).set_color(RED)
        D2H2 = AppendSegment(D2, H2).set_color(RED)

        self.play(FadeIn(VGroup(
            A,B,C,D,E,F,G,H,
            A2,B2,C2,D2,E2,F2,G2,H2,
            AB,BC,BD,CD,CE,CF,DG,DH,
            A2B2,B2C2,B2D2,C2D2,C2E2,C2F2,D2G2,D2H2
        )))
        self.wait(7)

class RedBlue3(Scene):
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 沧蓝只能砍蓝色的树枝",
            "绯樱只能砍红色的树枝",
            "4. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "5. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[6].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[6], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[3][2:5].set_color(BLUE)
        cap_text[3][8:].set_color(BLUE)
        cap_text[4][:2].set_color(RED)
        cap_text[4][5:].set_color(RED)
        cap_text[6][3:5].set_color("#D2691E")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, DOWN).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, DOWN).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-5.6,-2.5,0])) 
        B = Dot(np.array([-5.6,-1.6,0])) 
        C = Dot(np.array([-4.9,-1.3,0])) 
        D = Dot(np.array([-4.3,-1.3,0])) 
        E = Dot(np.array([-3.9,-1.7,0])) 
        F = Dot(np.array([-3.9,-2.5,0])) 
        G = Dot(np.array([-2.8,-2.5,0])) 
        H = Dot(np.array([-2.8,-1.6,0])) 
        I = Dot(np.array([-3.2,-1,0])) 
        J = Dot(np.array([-2.2,-1,0])) 
        K = Dot(np.array([-1.5,-2.5,0]))
        L = Dot(np.array([-1.5,-1.8,0]))
        M = Dot(np.array([-1.5,-1,0])) 
        N = Dot(np.array([-1.5,-0.3,0])) 
        O = Dot(np.array([-1.4,0.4,0])) 

        AB = AppendSegment(A, B).set_color(BLUE)
        BC = AppendSegment(B, C).set_color(RED)
        CD = AppendSegment(C, D).set_color(RED)
        DE = AppendSegment(D, E).set_color(RED)
        EF = AppendSegment(E, F).set_color(BLUE)
        GH = AppendSegment(G, H).set_color(RED)
        HI = AppendSegment(H, I).set_color(BLUE)
        HJ = AppendSegment(H, J).set_color(BLUE)
        KL = AppendSegment(K, L).set_color(RED)
        LM = AppendSegment(L, M).set_color(BLUE)
        MN = AppendSegment(M, N).set_color(BLUE)
        NO = AppendSegment(N, O).set_color(BLUE)

        self.play(FadeIn(
            VGroup(
                A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,
                AB,BC,CD,DE,EF,GH,HI,HJ,KL,LM,MN,NO
            )
        ))
        self.wait(7)

class RGB1(Scene):
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 双方都能砍绿色的根茎",
            "4. 沧蓝只能砍蓝色的树枝",
            "绯樱只能砍红色的树枝",
            "5. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "6. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[7].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[7], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[3][8:].set_color("#00EE00")
        cap_text[4][2:5].set_color(BLUE)
        cap_text[4][8:].set_color(BLUE)
        cap_text[5][:2].set_color(RED)
        cap_text[6][5:].set_color(RED)
        cap_text[7][3:5].set_color("#D2691E")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, RIGHT).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, RIGHT).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-4.4015,-2.5,0]))
        B = Dot(np.array([-4.4015,-0.7124,0]))
        C = Dot(np.array([-1.9103,-2.5,0]))
        D = Dot(np.array([-1.6441,-0.6982,0]))
        
        FuncA_1 = ParametricFunction(lambda t: np.array([-4.9498725962 + 0.5763200046 * np.cos(t) - 0.0035856237 * np.sin(t), -0.7253854661 + 0.00113439428 * np.cos(t) + 0.1821647471 * np.sin(t),0]), t_min = -PI, t_max = PI)
        FuncA_2 = ParametricFunction(lambda t: np.array([-3.902214 + 0.528856 * np.cos(t) + 0.00107848 * np.sin(t),-0.743395 - 0.032857 * np.cos(t) + 0.1734935 * np.sin(t),0]), t_min = -PI, t_max = PI)
        FuncB_1 = ParametricFunction(lambda t: np.array([-1.922033 + 0.310691 * np.cos(t) + 0.0245166 * np.sin(t),-0.64909986 - 0.0548804022 * np.cos(t) + 0.1387943 * np.sin(t),0]), t_min = -PI, t_max = PI)
        FuncB_2 = ParametricFunction(lambda t: np.array([-1.350123 + 0.3164432 * np.cos(t) + 0.0018442906 * np.sin(t),-0.70282574 - 0.004980 * np.cos(t) + 0.1171887052 * np.sin(t),0]), t_min = -PI, t_max = PI)
        FuncB_3 = ParametricFunction(lambda t: np.array([-1.58353336 + 0.0646896412 * np.cos(t) -0.0928553603 * np.sin(t),-0.4517945133 + 0.2633204123 * np.cos(t) + 0.022811676 * np.sin(t),0]), t_min = -PI, t_max = PI)

        FuncA_1.set_color(BLUE)
        FuncA_2.set_color(BLUE)
        FuncB_1.set_color(RED)
        FuncB_2.set_color(RED)
        FuncB_3.set_color(BLUE)

        AB = AppendSegment(A, B).set_color("#00EE00")
        CD = AppendSegment(C, D).set_color("#00EE00")

        self.play(FadeIn(VGroup(
            AB, CD,
            FuncA_1,FuncA_2,FuncB_1,FuncB_2,FuncB_3,
            A,B,C,D
        )))
        self.wait(7)

class RGB2(Scene):
    def construct(self):
        captions = [
            "规则：",
            "1. 沧蓝和绯樱轮流砍树枝",
            "2. 沧蓝先砍 绯樱后砍",
            "3. 双方都能砍绿色的根茎",
            "4. 沧蓝只能砍蓝色的树枝",
            "绯樱只能砍红色的树枝",
            "5. 每次只能砍一根，砍完后",
            "没有和地面连接的树枝将消失",
            "6. 如果轮到其中一方时",
            "他已经没有能砍的树枝则可判负"
        ]
        cap_text = [HText(caption) for caption in captions]
        cap_text[7].to_edge(RIGHT)
        cap_text[0].align_to(cap_text[7], LEFT).to_edge(UP)
        cap_text[1][3:5].set_color(BLUE)
        cap_text[1][6:8].set_color(RED)
        cap_text[2][3:5].set_color(BLUE)
        cap_text[2][8:10].set_color(RED)
        cap_text[3][8:].set_color("#00EE00")
        cap_text[4][2:5].set_color(BLUE)
        cap_text[4][8:].set_color(BLUE)
        cap_text[5][:2].set_color(RED)
        cap_text[6][5:].set_color(RED)
        cap_text[7][3:5].set_color("#D2691E")

        for i in range(1, len(cap_text)):
            cap_text[i].next_to(cap_text[i-1], DOWN, aligned_edge = LEFT)
        GroundLine = Line(np.array([-7,-2.5,0]),np.array([1,-2.5,0])).set_color("#D2691E")
        Task = HText("任务：试分析哪一方有必胜策略").to_edge(UP+LEFT).set_color(ORANGE)

        BluePerson = SVGMobject("D:\\Maths\\Hackenbush\\Person.svg").set_color(BLUE).rotate(PI).scale(0.3)
        RedPerson = SVGMobject("D:\\Maths\Hackenbush\\Person.svg").set_color(RED).rotate(PI).scale(0.3)

        BluePerson.next_to(Task, DOWN, aligned_edge = LEFT)
        RedPerson.next_to(Task, DOWN, aligned_edge = RIGHT).shift(0.5*LEFT)

        BlueText = HText("沧蓝").next_to(BluePerson, RIGHT).set_color(BLUE)
        RedText = HText("绯樱").next_to(RedPerson, RIGHT).set_color(RED)

        for i in cap_text:
            self.add(i)
        self.add(GroundLine, Task)
        self.add(BluePerson, RedPerson)
        self.add(BlueText, RedText)

        A = Dot(np.array([-4.4015,-2.5,0]))
        B = Dot(np.array([-4.4015,-0.7124,0]))
        C = Dot(np.array([-1.9103,-2.5,0]))
        D = Dot(np.array([-1.6441,-0.6982,0]))
        E = Dot(np.array([-5.5,-0.3,0]))
        F = Dot(np.array([-4.4,0.2,0]))
        G = Dot(np.array([-5.2,0.6,0]))
        H = Dot(np.array([-4.5,0.9,0]))
        I = Dot(np.array([-3.7,0.9,0]))
        
        FuncB_1 = ParametricFunction(lambda t: np.array([-1.922033 + 0.310691 * np.cos(t) + 0.0245166 * np.sin(t),-0.64909986 - 0.0548804022 * np.cos(t) + 0.1387943 * np.sin(t),0]), t_min = -PI, t_max = PI)
        FuncB_2 = ParametricFunction(lambda t: np.array([-1.350123 + 0.3164432 * np.cos(t) + 0.0018442906 * np.sin(t),-0.70282574 - 0.004980 * np.cos(t) + 0.1171887052 * np.sin(t),0]), t_min = -PI, t_max = PI)
        FuncB_3 = ParametricFunction(lambda t: np.array([-1.58353336 + 0.0646896412 * np.cos(t) -0.0928553603 * np.sin(t),-0.4517945133 + 0.2633204123 * np.cos(t) + 0.022811676 * np.sin(t),0]), t_min = -PI, t_max = PI)

        FuncB_1.set_color(BLUE)
        FuncB_2.set_color(BLUE)
        FuncB_3.set_color(BLUE)

        AB = AppendSegment(A, B).set_color("#00EE00")
        CD = AppendSegment(C, D).set_color("#00EE00")
        BE = AppendSegment(B, E).set_color("#00EE00")
        BF = AppendSegment(B, F).set_color("#00EE00")
        FG = AppendSegment(F, G).set_color("#00EE00")
        FH = AppendSegment(F, H).set_color("#00EE00")
        FI  = AppendSegment(F, I).set_color("#00EE00")

        self.play(FadeIn(VGroup(
            AB, CD, BE, BF, FG, FH, FI,
            FuncB_1,FuncB_2,FuncB_3,
            A,B,C,D,E,F,G,H,I
        )))
        self.wait(7)

class AnswerCorrect(Scene):
    def construct(self):
        text = HText("恭喜你 答案正确！").set_color(GREEN).scale(4.5)
        self.add(text)
        self.wait(3)

class AnswerWrong(Scene):
    def construct(self):
        text = HText("答案错误").set_color(RED).scale(5)
        self.add(text)
        self.wait(3)

class CorrectZero(Scene):
    def construct(self):
        text = HText("恭喜你一共答对零题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)       

class CorrectOne(Scene):
    def construct(self):
        text = HText("恭喜你一共答对一题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)       

class CorrectTwo(Scene):
    def construct(self):
        text = HText("恭喜你一共答对两题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)       

class CorrectThree(Scene):
    def construct(self):
        text = HText("恭喜你一共答对三题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)       

class CorrectFour(Scene):
    def construct(self):
        text = HText("恭喜你一共答对四题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)   

class CorrectFive(Scene):
    def construct(self):
        text = HText("恭喜你一共答对五题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)     

class CorrectSix(Scene):
    def construct(self):
        text = HText("恭喜你一共答对六题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)   

class CorrectSeven(Scene):
    def construct(self):
        text = HText("恭喜你一共答对七题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)       

class CorrectEight(Scene):
    def construct(self):
        text = HText("恭喜你一共答对八题！").set_color(GREEN).scale(4)
        self.add(text)
        self.wait(3)       

class SeeResult(Scene):
    def construct(self):
        text = HText("快来查看结果吧！").scale(4)
        self.add(text)
        self.wait(3)     

class Girl(Scene):         
    def construct(self):
        text = HText("少女祈祷中...").scale(4).set_color("#FF1493")
        self.add(text)
        self.wait(3)    