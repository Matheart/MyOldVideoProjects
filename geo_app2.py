from manimlib.imports import *
from manim_sandbox.utils.imports import *
from test_present_style import *
# 5min = 300s
class HText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Regular',
        'size' : 0.5,
    }

class Quote(Scene): #名言
    def construct(self): #火柴人movealongpath
        quote = HText("几何是人类进步的阶梯").scale(2).to_edge(UP)
        author = HText("--高尔几").next_to(quote,DOWN).align_to(quote,RIGHT).shift(RIGHT)

        quote[:2].set_color("#FFD700")
        author[4].set_color("#FFD700")

        # -4, -2.625, -1.25, 0.125, 1.5
        lad1 = Line(np.array([-7,-4,0]),np.array([-4.2,-4,0])).set_color("#FFD700")
        lad2 = Line(np.array([-4.2,-4,0]),np.array([-4.2,-2.625,0])).set_color("#FFD700")
        lad3 = Line(np.array([-4.2,-2.625,0]),np.array([-1.4,-2.625,0])).set_color("#FFD700")
        lad4 = Line(np.array([-1.4,-2.625,0]),np.array([-1.4,-1.25,0])).set_color("#FFD700")
        lad5 = Line(np.array([-1.4,-1.25,0]),np.array([1.4,-1.25,0])).set_color("#FFD700")
        lad6 = Line(np.array([1.4,-1.25,0]),np.array([1.4,0.125,0])).set_color("#FFD700")
        lad7 = Line(np.array([1.4,0.125,0]),np.array([4.2,0.125,0])).set_color("#FFD700")
        lad8 = Line(np.array([4.2,0.125,0]),np.array([4.2,1.5,0])).set_color("#FFD700")
        lad9 = Line(np.array([4.2,1.5,0]),np.array([7,1.5,0])).set_color("#FFD700")

        im1 = ImageMobject(r"geo_1.png").scale(0.6).next_to(lad3,DOWN).shift(0.2*UP)
        im2 = ImageMobject(r"geo_2.png").next_to(lad5,DOWN)
        im3 = ImageMobject(r"geo_3.png").scale(0.8).next_to(lad7,DOWN)
        im4 = ImageMobject(r"geo_4.png").next_to(lad9,DOWN)
        rec = Polygon(np.array([-7,-3.9,0]),np.array([-4.3,-3.9,0]),np.array([-4.3,-1.25,0]),np.array([-7,-1.25,0]), fill_opacity = 1).set_color(BLACK)
        cat = Emote_new(color="#FF69B4").next_to(lad1,UP).shift(0.2*UP)

        self.play(FadeIn(quote))
        self.wait(0.5)
        self.play(FadeIn(author))
        self.wait(1.5)
        self.play(FadeOut(author))
        self.play(Write(lad1),run_time = 0.1)
        self.play(Write(lad2),run_time = 0.1)
        self.play(Write(lad3),run_time = 0.1)
        self.play(Write(lad4),run_time = 0.1)
        self.play(Write(lad5),run_time = 0.1)
        self.play(Write(lad6),run_time = 0.1)
        self.play(Write(lad7),run_time = 0.1)
        self.play(Write(lad8),run_time = 0.1)
        self.play(Write(lad9),run_time = 0.1)
        self.wait(.5)
        self.add(cat, rec)
        self.play(FadeOut(rec))
        self.play(ApplyMethod(cat.shift,1.375*UP),run_time = 0.5)
        self.play(ApplyMethod(cat.shift,2.8*RIGHT),run_time = 0.5)
        self.play(FadeIn(im1))
        self.play(ApplyMethod(cat.shift,1.375*UP),run_time = 0.5)
        self.play(ApplyMethod(cat.shift,2.8*RIGHT),run_time = 0.5)
        self.play(FadeIn(im2))
        self.play(ApplyMethod(cat.shift,1.375*UP),run_time = 0.5)
        self.play(ApplyMethod(cat.shift,2.8*RIGHT),run_time = 0.5)
        self.play(FadeIn(im3))
        self.play(FadeOut(quote))
        self.play(ApplyMethod(cat.shift,1.375*UP),run_time = 0.5)
        self.play(ApplyMethod(cat.shift,2.8*RIGHT),run_time = 0.5)
        self.play(FadeIn(im4))
        self.wait(2)

class GergonneAndNagel(Scene): #热尔岗点&奈格尔点
    def construct(self):
        name1 = HText("奈格尔点").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng1 = HText("Nagel Point").set_color("#FFD700").scale(1.3).next_to(name1,DOWN).to_edge(RIGHT)
        name2 = HText("热尔岗点").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng2 = HText("Gergonne Point").set_color("#FFD700").scale(1.3).next_to(name2,DOWN).to_edge(RIGHT)   

        A_cor = np.array([0.5606852334-3.5,1.8437002954,0])
        B_cor = np.array([-2.0260885572-3.5,-0.6542572277,0])
        C_cor = np.array([2.2518538421-3.5,-0.6651468182,0])
        T_A_cor = np.array([-0.1723056696-3.5,-0.6589760702,0])
        T_B_cor = np.array([1.5968601838-3.5,0.3065356862,0])
        T_C_cor = np.array([-1.1831352878-3.5,0.1597534401,0])
        N_cor = np.array([-0.0146957788-3.5,-0.1208431314,0])
        D_cor = np.array([0.3980708731-3.5,-0.6604279754,0])
        E_cor = np.array([1.2156788916-3.5,0.872017791,0])
        F_cor = np.array([-0.282268036-3.5,1.0296896275,0])
        G_cor = np.array([0.4749381594-3.5,0.5232654228,0])
        
        Tri = MyTriangle(A_cor, B_cor, C_cor)
        A = Dot(A_cor).set_color(BLUE)
        B = Dot(B_cor).set_color(BLUE)
        C = Dot(C_cor).set_color(BLUE)
        T_A = Dot(T_A_cor) # Three tangent points
        T_B = Dot(T_B_cor)
        T_C = Dot(T_C_cor)
        N = Dot(N_cor).set_color(PURPLE) # Nagel Point
        AT_A = Line(A_cor, T_A_cor).set_color("#FF1493")
        BT_B = Line(B_cor, T_B_cor).set_color(ORANGE)
        CT_C = Line(C_cor, T_C_cor).set_color(RED)
        D = Dot(D_cor).set_color(RED)
        E = Dot(E_cor).set_color(YELLOW)
        F = Dot(F_cor).set_color(ORANGE)
        G = Dot(G_cor).set_color(PURPLE)
        AD = Line(A_cor, D_cor).set_color(RED)
        BE = Line(B_cor, E_cor).set_color(YELLOW)
        CF = Line(C_cor, F_cor).set_color(ORANGE)

        A_label = TextMobject("A").next_to(A,UP).set_color(BLUE)
        B_label = TextMobject("B").next_to(B,1.55*LEFT+0.17*DOWN).set_color(BLUE)
        C_label = TextMobject("C").next_to(C,1.2*RIGHT+0.4*DOWN).set_color(BLUE)
        T_A_label = TexMobject("T_A").next_to(T_A,DOWN).set_color("#FF1493")
        T_B_label = TexMobject("T_B").next_to(T_B,RIGHT).set_color(ORANGE)
        T_C_label = TexMobject("T_C").next_to(T_C,LEFT).set_color(RED)
        N_label = TextMobject("N").next_to(N,LEFT*0.5+UP*0.5).set_color(PURPLE)
        D_label = TextMobject("D").next_to(D, DOWN).set_color(RED)
        E_label = TextMobject("E").next_to(E, RIGHT).set_color(YELLOW)
        F_label = TextMobject("F").next_to(F, LEFT).set_color(ORANGE)
        G_label = TextMobject("G").next_to(G, RIGHT).set_color(PURPLE)

        Circ_A = Circle(radius = 4.5716080752).move_to(np.array([-0.1839426729-3.5,-5.2305693345,0])).set_color("#FF1493")
        Circ_B = Circle(radius = 2.2098902532).move_to(np.array([3.4293045091-3.5,1.5417533698,0])).set_color(ORANGE)
        Circ_C = Circle(radius = 2.8898346714).move_to(np.array([-3.1905578114-3.5,2.2385509867,0])).set_color(RED)

        l_A = Line(np.array([-3.1979139212-3.5,-0.6512743221,0]),np.array([3.4236792062-3.5,-0.6681297237,0])).set_color(BLUE)
        l_B = Line(np.array([-0.7943025508-3.5,3.8538234573,0]),np.array([3.6068416886-3.5,-2.6752700725,0])).set_color(BLUE)
        l_C = Line(np.array([1.8942051095-3.5,3.1314340813,0]),np.array([-3.3596084333-3.5,-1.9419910137,0])).set_color(BLUE)

        Incir = Tri.get_incircle().set_color("#FFD700")

        captionsN = [
            HText("构造三角形ABC和旁切圆").scale(0.8),
            HText("分别连接三角形顶点及对边切点").scale(0.8),
            HText("可以发现三条直线共点").scale(0.8),
            HText("这个点被称为奈格尔点").scale(0.8),
        ]
        captionsN[0].next_to(name_eng1,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captionsN[i].next_to(captionsN[i-1],DOWN).to_edge(RIGHT)

        captionsN[0][5:8].set_color("#00BFFF")
        captionsN[0][-3:].set_color(RED)
        captionsN[1][7:9].set_color(BLUE)
        captionsN[1][-2:].set_color(RED)
        captionsN[2][-2:].set_color(PURPLE)
        captionsN[3][-4:].set_color(PURPLE)

        captionsG = [
            HText("构造内切圆").scale(0.8),
            HText("分别连接三角形顶点及对边切点").scale(0.8),
            HText("可以发现三条直线共点").scale(0.8),
            HText("这个点被称为热尔岗点").scale(0.8),
        ]
        captionsG[0].next_to(name_eng2,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captionsG[i].next_to(captionsG[i-1],DOWN).to_edge(RIGHT)
        captionsG[0][-3:].set_color("#FFD700")
        captionsG[1][7:9].set_color(BLUE)
        captionsG[1][-2:].set_color(RED)
        captionsG[2][-2:].set_color(PURPLE)
        captionsG[3][-4:].set_color(PURPLE)

        self.play(Write(name1),Write(name_eng1))
        self.play(Write(captionsN[0]))
        self.wait(0.5)
        self.play(Write(VGroup(A,B,C)),ShowCreation(Tri))
        self.play(Write(VGroup(A_label,B_label,C_label)))
        self.wait(0.5)
        self.play(Write(VGroup(l_A,l_B,l_C)))
        self.play(ShowCreation(VGroup(Circ_A,Circ_B,Circ_C)))
        self.wait(1)
        self.play(Write(captionsN[1]))
        self.wait(0.5)
        self.play(Write(VGroup(T_A,T_B,T_C,T_A_label,T_B_label,T_C_label)))
        self.wait(1)
        self.play(Write(VGroup(AT_A,BT_B,CT_C)))
        self.wait(1)
        self.play(Write(captionsN[2]))
        self.wait(0.5)
        self.play(Write(N),Write(N_label))
        self.wait(1)
        self.play(Write(captionsN[3]))
        self.wait(2)
        self.play(FadeOut(VGroup(l_A,l_B,l_C,T_A,T_B,T_C,AT_A,BT_B,CT_C,Circ_A,Circ_B,Circ_C,N,N_label,T_A_label,T_B_label,T_C_label,
                                 captionsN[0],captionsN[1],captionsN[2],captionsN[3],name1,name_eng1)))
        self.play(Write(VGroup(name2,name_eng2)))
        self.play(Write(captionsG[0]))
        self.wait(0.5)
        self.play(ShowCreation(Incir))
        self.wait(1)
        self.play(Write(captionsG[1]))
        self.wait(0.5)
        self.play(Write(VGroup(D,E,F,D_label,E_label,F_label)))
        self.wait(1)
        self.play(Write(VGroup(AD,BE,CF)))
        self.play(Write(captionsG[2]))
        self.wait(0.5)
        self.play(Write(VGroup(G,G_label)))
        self.play(Write(captionsG[3]))
        self.wait(2)

class Steiner(Scene): #史坦纳定理
    def construct(self):
        def intersec(a,b,p,q): # y = ax+b, y = px+q
            return np.array([(q-b)/(a-p),(q-b)/(a-p)*p+q,0])

        name1 = HText("西姆松定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng1 = HText("Simson's theorem").set_color("#FFD700").scale(1.3).next_to(name1,DOWN).to_edge(RIGHT)
        name2 = HText("史坦纳定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng2 = HText("Steiner's theorem").set_color("#FFD700").scale(1.3).next_to(name2,DOWN).to_edge(RIGHT)
        
        captions = [
            HText("过三角形外接圆上").scale(0.8),
            HText("在异于三角形顶点的任意一点").scale(0.8),
            HText("作三边或其延长线上的垂线").scale(0.8),
            HText("则三垂足共线 此线被称为西姆松线").scale(0.8),
            HText("同时若垂心为H").scale(0.8),
            HText("则DH中点在西姆松线上").scale(0.8),
        ]
        captions[0].next_to(name_eng1,2*DOWN).to_edge(RIGHT)
        for i in range(1,6):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][4:7].set_color("#7CFC00")
        captions[1][9:].set_color(PURPLE)
        captions[2][-2:].set_color("#FF1493")
        captions[3][-4:].set_color("#FF00FF")
        captions[4][3:5].set_color("#00CED1")
        captions[4][-1:].set_color("#00CED1")
        captions[5][1:3].set_color(RED)
        captions[5][-5:-1].set_color("#FF00FF")

        A_cor = np.array([-4.162696696,2.7003599322,0])
        B_cor = np.array([-5.74221,-1.0038,0])
        C_cor = np.array([0,-1,0])
        D_cor = np.array([1.2672965913-2,2.1046258626,0])
        E_cor = np.array([1.8101634475-2,-1.0001256274,0])
        F_cor = np.array([0.7160559887-2,0.1413406464,0])
        G_cor = np.array([-2.0315611874-2,3.0078894068,0])  
        H_A_cor = np.array([-2.1602461012-2,-1.0027531099,0])
        H_B_cor = np.array([-1.2056887602-2,1.8496436589,0])
        H_C_cor = np.array([-2.8573706954-2,1.0712609003,0])

        k_AB = -1.0/-0.42641606542
        b_AB = 7.7721592176+2*-1.0/-0.42641606542
        k_AC = -1.0/1.12494372771
        b_AC = 0.7778667064+2*-1.0/1.12494372771

        tri = MyTriangle(A_cor, B_cor, C_cor)
        circ = tri.get_circumcircle().set_color("#7CFC00")
        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        D = Dot(D_cor,color=PURPLE)
        E = Dot(E_cor)
        F = Dot(F_cor)
        G = Dot(G_cor)
        H = Dot(tri.get_orthocenter()).set_color("#00CED1")
        H_label = TextMobject("H").set_color("#00CED1").next_to(H,DOWN+0.2*RIGHT)

        A_label = TextMobject("A").next_to(A,LEFT)
        B_label = TextMobject("B").next_to(B,LEFT)
        C_label = TextMobject("C").next_to(C,DOWN+0.4*RIGHT)
        D_label = TextMobject("D",color=PURPLE).next_to(D,RIGHT+0.3*UP)
        E_label = TextMobject("E").next_to(E,DOWN+LEFT)
        F_label = TextMobject("F").next_to(F,RIGHT)
        G_label = TextMobject("G").next_to(G,LEFT)

        DE = Line(D_cor,E_cor).set_color(ORANGE)
        DF = Line(D_cor,F_cor).set_color("#FF1493")
        DG = Line(D_cor,G_cor).set_color("#8470FF")
        AG = Line(A_cor,G_cor)
        GE = Line(G_cor,E_cor).set_color("#FF00FF")

        E.add_updater(lambda obj: obj.become(Dot(np.array([D.get_center()[0],-1,0]))))

        def update_F(obj):
            k_DF = 1.12494372771
            b_DF = D.get_center()[1]-k_DF*D.get_center()[0]
            dt = intersec(k_DF,b_DF,k_AC,b_AC)
            obj.become(Dot(dt))

        def update_G(obj):
            k_DG = -0.42641606542
            b_DG = D.get_center()[1]-k_DG*D.get_center()[0]
            dt = intersec(k_DG,b_DG,k_AB,b_AB)
            obj.become(Dot(dt))

        F.add_updater(update_F)
        G.add_updater(update_G)

        DE.add_updater(lambda obj: obj.put_start_and_end_on(D.get_center(),E.get_center()))
        DF.add_updater(lambda obj: obj.put_start_and_end_on(D.get_center(),F.get_center()))
        DG.add_updater(lambda obj: obj.put_start_and_end_on(D.get_center(),G.get_center()))
        AG.add_updater(lambda obj: obj.put_start_and_end_on(A.get_center(),G.get_center()))
        GE.add_updater(lambda obj: obj.put_start_and_end_on(G.get_center(),E.get_center()))
        
        D_label.add_updater(lambda obj: obj.next_to(D,RIGHT+0.3*UP))
        E_label.add_updater(lambda obj: obj.next_to(E,DOWN))
        F_label.add_updater(lambda obj: obj.next_to(F,RIGHT))
        G_label.add_updater(lambda obj: obj.next_to(G,LEFT))

        AH_A = Line(A_cor, H_A_cor).set_color("#FFC125")
        BH_B = Line(B_cor, H_B_cor).set_color(ORANGE)
        CH_C = Line(C_cor, H_C_cor).set_color(YELLOW)
        
        DH = Line(D_cor, tri.get_orthocenter()).set_color(RED)
        M = Dot(np.array([(D_cor[0] + tri.get_orthocenter()[0])/2.0,(D_cor[1] + tri.get_orthocenter()[1])/2.0,0])).set_color(RED)

        DH.add_updater(lambda obj: obj.put_start_and_end_on(D.get_center(),tri.get_orthocenter()))
        M.add_updater(lambda obj: obj.become(Dot(np.array([(D.get_center()[0] + tri.get_orthocenter()[0])/2.0,(D.get_center()[1] + tri.get_orthocenter()[1])/2.0,0])).set_color(RED)))

        self.play(ShowCreation(tri),ShowCreation(VGroup(A,B,C)),Write(name1),Write(name_eng1))
        self.play(Write(A_label),Write(B_label),Write(C_label))
        self.wait(1)
        self.play(Write(captions[0]))
        self.wait(.5)
        self.play(ShowCreation(circ))
        self.play(Write(captions[1]))
        self.wait(.5)
        self.play(Write(D),Write(D_label))
        self.wait(1)
        self.play(Write(captions[2]))
        self.wait(.5)
        self.play(Write(VGroup(DE,DF,DG,AG)))
        self.wait(0.5)
        self.play(FadeIn(VGroup(E,F,G,E_label,F_label,G_label)))
        self.wait(1)
        self.play(Write(captions[3]))
        self.wait(.5)
        self.play(Write(GE))
        self.wait(1.5)
        self.play(Rotating(D,about_point=np.array([-0.8717422353-2,-0.0389686799,0]),radians=PI/3),run_time=0.7)
        self.play(Rotating(D,about_point=np.array([-0.8717422353-2,-0.0389686799,0]),radians=-PI/3),run_time=0.7)
        self.wait(1.5)
        self.play(ReplacementTransform(name1,name2),ReplacementTransform(name_eng1,name_eng2))
        self.play(Write(captions[4]))
        self.wait(.5)
        self.play(Write(VGroup(AH_A,BH_B,CH_C)))
        self.wait(0.5)
        self.play(Write(H),Write(H_label))
        self.wait(1)
        self.play(Write(captions[5]))
        self.wait(.5)
        self.play(Write(DH))
        self.play(Write(M))
        self.wait(1.5)
        self.play(Rotating(D,about_point=np.array([-0.8717422353-2,-0.0389686799,0]),radians=PI/3),run_time=0.7)
        self.play(Rotating(D,about_point=np.array([-0.8717422353-2,-0.0389686799,0]),radians=-PI/3),run_time=0.7)
        self.wait(2)

class Thebault(Scene): #泰博第三定理
    def construct(self):
        name = HText("泰博第三定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng = HText("Thébault's Theorem III").set_color("#FFD700").scale(1.3).next_to(name,DOWN).to_edge(RIGHT)

        A_cor = np.array([-0.7521549075-4,1.5269722014,0])
        B_cor = np.array([-2.4870090841-4,-1.696851308,0])
        C_cor = np.array([2.6492521003-4,-0.426446281,0])
        M_cor = np.array([1.0735461546-4,-.8161820601,0])

        Tri = MyTriangle(A_cor, B_cor, C_cor)
        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        M = Dot(M_cor).set_color(GREEN)
        A_label = TextMobject("A").next_to(A, UP)
        B_label = TextMobject("B").next_to(B, LEFT)
        C_label = TextMobject("C").next_to(C, RIGHT)
        M_label = TextMobject("M").next_to(M, DOWN).set_color(GREEN)

        AM = Line(A_cor, M_cor).set_color(GREEN)
        in_centr = Dot(Tri.get_incenter()).set_color("#FF00FF")
        incircle = Tri.get_incircle().set_color("#FF00FF")
        circumcircle = Tri.get_circumcircle().set_color(RED)
        L_circle = Circle(radius = 1.2200502959).move_to(np.array([-1.0411934056-4,-0.0860167972,0])).set_color(YELLOW)
        R_circle = Circle(radius = 0.8741786228).move_to(np.array([1.4076777249-4,0.164891622,0])).set_color(ORANGE)
        L_centr = Dot(np.array([-1.0411934056-4,-0.0860167972,0])).set_color(YELLOW)
        R_centr = Dot(np.array([1.4076777249-4,0.164891622,0])).set_color(ORANGE)
        LR = Line(L_centr, R_centr).set_color("#FFD700")

        in_centr_label = TextMobject("I").next_to(in_centr, UP)

        captions = [
            HText("给定任意的三角形ABC").scale(0.8),
            HText("构建三角形ABC的内切圆和外接圆").scale(0.8),
            HText("并在BC上取任意一点M").scale(0.8),
            HText("然后构造另外两个圆").scale(0.8),
            HText("使得与AM，BC和外接圆都相切").scale(0.8),
            HText("可以发现这两个圆的圆心和内切圆圆心共线").scale(0.8),
        ]
        captions[0].next_to(name_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,6):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][-3:].set_color("#00BFFF")
        captions[1][5:8].set_color("#00BFFF")
        captions[1][9:12].set_color("#FF00FF")
        captions[1][-3:].set_color(RED)
        captions[2][-1].set_color(GREEN)
        captions[2][2:4].set_color("#00BFFF")
        captions[4][3:5].set_color(GREEN)
        captions[4][6:8].set_color("#00BFFF")
        captions[4][9:12].set_color(RED)
        captions[5][12:17].set_color("#FF00FF")

        self.play(Write(name),Write(name_eng))
        self.play(Write(captions[0]))
        self.play(ShowCreation(VGroup(Tri,A,B,C)))
        self.play(Write(A_label),Write(B_label),Write(C_label))
        self.wait(.5)
        self.play(Write(captions[1]))
        self.wait(.5)
        self.play(ShowCreation(VGroup(incircle,circumcircle)))
        self.play(Write(in_centr),Write(in_centr_label))
        self.wait(1)
        self.play(Write(captions[2]))
        self.wait(.5)
        self.play(Write(M),Write(M_label))
        self.wait(.5)
        self.play(Write(AM))
        self.wait(1)
        self.play(Write(captions[3]))
        self.wait(.5)
        self.play(Write(captions[4]))
        self.wait(.5)       
        self.play(ShowCreation(VGroup(L_circle,R_circle)))
        self.play(Write(VGroup(L_centr,R_centr)))
        self.wait(1)
        self.play(Write(captions[5]))
        self.wait(.5)
        self.play(Write(LR))
        self.wait(2)

#索迪线：内心，热尔岗点
class Soddy(Scene): #索迪圆
    def construct(self):
        name = HText("索迪圆").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng = HText("Soddy Circles").set_color("#FFD700").scale(1.3).next_to(name,DOWN).to_edge(RIGHT)
        name2 = HText("索迪线").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name2_eng = HText("Soddy Line").set_color("#FFD700").scale(1.3).next_to(name,DOWN).to_edge(RIGHT)

        A_cor = np.array([-1.6543209374-3,1.6679886694,0])
        B_cor = np.array([1.4429030129-3,-0.4641628538,0])
        C_cor = np.array([-2.167122111-3,-1.1173534133,0])
        D_cor = np.array([-0.818702898-3,-0.8733731999,0])
        E_cor = np.array([-1.9190075284-3,0.230311186,0])
        F_cor = np.array([-0.4502139123-3,0.8390726243,0])
        G_cor = np.array([-1.1278662703-3,0.0668841528,0])

        Tri = MyTriangle(A_cor, B_cor, C_cor)
        A = Dot(A_cor).set_color(ORANGE)
        B = Dot(B_cor).set_color(RED)
        C = Dot(C_cor).set_color("#FF69B4")

        AD = Line(A_cor, D_cor)
        BE = Line(B_cor, E_cor)
        CF = Line(C_cor, F_cor)
        
        A_label = TextMobject("A").next_to(A,UP).set_color(ORANGE)
        B_label = TextMobject("B").next_to(B,RIGHT).set_color(RED)
        C_label = TextMobject("C").next_to(C,LEFT).set_color("#FF69B4")
        Cir_A = Circle(radius = 1.4621750745).move_to(A_cor).set_color(ORANGE)
        Cir_B = Circle(radius = 2.2986744628).move_to(B_cor).set_color(RED)
        Cir_C = Circle(radius = 1.3732153543).move_to(C_cor).set_color("#FF69B4")
        insoddy = Circle(radius = 0.2518015476).move_to(np.array([-1.0515713604-3,0.0642567314,0])).set_color(PURPLE)
        otsoddy = Circle(radius = 3.8113987957).move_to(np.array([-3,0,0])).set_color(PURPLE)

        insoddyO = Dot(np.array([-1.0515713604-3,0.0642567314,0])).set_color(PURPLE)
        otsoddyO = Dot(np.array([-3,0,0])).set_color(PURPLE)
        incentr = Dot(Tri.get_incenter()).set_color(YELLOW)
        G = Dot(G_cor).set_color(GREEN)

        G_otsoddyO = Line(G_cor,np.array([-3,0,0])).set_color("#FFA500")

        incirc = Tri.get_incircle().set_color(YELLOW)

        captions = [
            HText("给定三角形ABC").scale(0.8),
            HText("以它们为圆心").scale(0.8),
            HText("做三个两两相切的圆").scale(0.8),
            HText("能做出与它们三个都外切的圆").scale(0.8),
            HText("这个圆被称为外索迪圆").scale(0.8),
            HText("也能做出与它们三个都内切的圆").scale(0.8),
            HText("这个圆被称为内索迪圆").scale(0.8),
        ]
        captions[0].next_to(name_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,7):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][-3:].set_color("#00BFFF")
        captions[4][-4:].set_color(PURPLE)
        captions[6][-4:].set_color(PURPLE)

        captions2 = [
            HText("如果将外内索迪圆圆心").scale(0.8),
            HText("内心，热尔岗点都画出来").scale(0.8),
            HText("能发现它们在同一条直线上").scale(0.8),
            HText("被叫做索迪线").scale(0.8),
        ]
        captions2[0].next_to(name2_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captions2[i].next_to(captions2[i-1],DOWN).to_edge(RIGHT)
        captions2[0][3:10].set_color(PURPLE)
        captions2[1][:2].set_color(YELLOW)
        captions2[1][3:7].set_color(GREEN)
        captions2[2][9:11].set_color("#FFA500")
        captions2[3][-3:].set_color("#FFA500")

        self.play(Write(name),Write(name_eng))
        self.play(Write(captions[0]))
        self.play(ShowCreation(VGroup(Tri,A,B,C)))
        self.play(Write(A_label),Write(B_label),Write(C_label))
        self.wait(1)      
        self.play(Write(captions[1]))
        self.play(Write(captions[2]))       
        self.wait(0.5)        
        self.play(ShowCreation(Cir_A),ShowCreation(Cir_B),ShowCreation(Cir_C))
        self.wait(1)
        self.play(Write(captions[3]))
        self.wait(0.5)       
        self.play(ShowCreation(otsoddy))
        self.play(Write(captions[4]))
        self.wait(1)
        self.play(Write(captions[5]))
        self.wait(0.5)       
        self.play(ShowCreation(insoddy))
        self.play(Write(captions[6]))     
        self.wait(1.5)
        self.play(FadeOut(VGroup(name,name_eng,captions[0],captions[1],captions[2],
                                 captions[3],captions[4],captions[5],captions[6])))
        self.play(Write(name2),Write(name2_eng))
        self.play(Write(captions2[0]))
        self.wait(0.5)
        self.play(Write(insoddyO),Write(otsoddyO))
        self.play(Write(captions2[1]))
        self.wait(0.5)
        self.play(ShowCreation(incirc),Write(incentr))
        self.play(Write(AD),Write(BE),Write(CF))
        self.play(Write(G))
        self.play(FadeOut(VGroup(AD,BE,CF)))
        self.wait(1)
        self.play(Write(captions2[2]))
        self.wait(0.5)
        self.play(Write(G_otsoddyO))
        self.wait(0.5)
        self.play(Write(captions2[3]))
        self.wait(2)

class Desargue(Scene): #笛沙格定理
    def construct(self):
        name = HText("笛沙格定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng = HText("Desargue's Theorem").set_color("#FFD700").scale(1.3).next_to(name,DOWN).to_edge(RIGHT)
        
        A_cor = np.array([-1.1984023031-1,-0.3688952897,0])
        B_cor = np.array([-3.1142190608-1,-1.836888208,0])
        C_cor = np.array([1.1602429491-1,-1.6792537632,0])
        D_cor = np.array([-1.3276750495-1,2.1202435797,0])
        E_cor = np.array([-2.3000337919-1,0.7992034412,0])
        F_cor = np.array([0.2934419338-1,0.1303791342,0])
        M_cor = np.array([-1.4089091871-1,3.6844019567,0])
        I_cor = np.array([6.5411179145-1,-1.4808168052,0])
        J_cor = np.array([2.270012857-1,-2.2957926008,0])
        K_cor = np.array([-5.697083614-1,-3.8160059175,0])

        A = Dot(A_cor)
        B = Dot(B_cor)
        C = Dot(C_cor)
        D = Dot(D_cor)
        E = Dot(E_cor)
        F = Dot(F_cor)
        M = Dot(M_cor)
        I = Dot(I_cor).set_color("#FF1493")
        J = Dot(J_cor).set_color("#FF1493")
        K = Dot(K_cor).set_color("#FF1493")
        Tri1 = MyTriangle(A_cor, B_cor, C_cor)
        Tri2 = MyTriangle(D_cor, E_cor, F_cor)
        FI = Line(F_cor, I_cor).set_color("#FFD700")
        CI = Line(C_cor, I_cor).set_color("#FFD700")
        FJ = Line(F_cor, J_cor).set_color(ORANGE)
        CJ = Line(C_cor, J_cor).set_color(ORANGE)
        BK = Line(B_cor, K_cor).set_color(PURPLE)
        EK = Line(E_cor, K_cor).set_color(PURPLE)
        IK = Line(I_cor, K_cor).set_color("#FF1493")
        AM = Line(A_cor, M_cor).set_color(RED)
        BM = Line(B_cor, M_cor).set_color(RED)
        CM = Line(C_cor, M_cor).set_color(RED)

        A_label = TextMobject("A").next_to(A,RIGHT)
        B_label = TextMobject("B").next_to(B,LEFT)
        C_label = TextMobject("C").next_to(C,RIGHT)
        D_label = TextMobject("D").next_to(D,RIGHT)
        E_label = TextMobject("E").next_to(E,LEFT)
        F_label = TextMobject("F").next_to(F,RIGHT)

        captions = [
            HText("平面上有两个三角形ABC、DEF").scale(0.8),
            HText("设它们的对应顶点的连线交于一点").scale(0.8),
            HText("这时如果对应边相交").scale(0.8),
            HText("则这三个交点共线").scale(0.8),
        ]
        captions[0].next_to(name_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][9:12].set_color("#00BFFF")
        captions[0][-3:].set_color("#00BFFF")
        captions[1][-2:].set_color(RED)
        captions[2][4:7].set_color("#00BFFF")
        captions[3][-2:].set_color("#FFD700")

        self.play(Write(name),Write(name_eng))
        self.play(Write(captions[0]))
        self.wait(.5)
        self.play(Write(Tri1),Write(Tri2))
        self.play(Write(VGroup(A,B,C,D,E,F,A_label,B_label,C_label,D_label,E_label,F_label)))
        self.wait(1)
        self.play(Write(captions[1]))
        self.wait(.5)
        self.play(Write(VGroup(AM,BM,CM)))
        self.wait(.5)
        self.play(Write(M))
        self.wait(1)
        self.play(Write(captions[2]))
        self.wait(.5)
        self.play(Write(VGroup(FI,CI,FJ,CJ,BK,EK)))
        self.wait(.5)
        self.play(Write(VGroup(I,J,K)))
        self.play(Write(captions[3]))
        self.wait(1)
        self.play(Write(IK))
        self.wait(2)

class Poncelet(Scene): #彭赛列闭合定理
    def construct(self):
        name = HText("彭赛列闭合定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng = HText("Poncelet's closure theorem").set_color("#FFD700").scale(0.9).next_to(name,DOWN).to_edge(RIGHT)

        small_func = ParametricFunction(lambda t: np.array([-0.66-3.2+2.36*np.cos(t)-0.18*np.sin(t),-0.21+0.22*np.cos(t)+1.97*np.sin(t),0]), t_min = -PI, t_max = PI).set_color(BLUE)
        big_func = ParametricFunction(lambda t: np.array([-0.03-3.2-3.43*np.cos(t)+1.07*np.sin(t),-0.1-1.43*np.cos(t)-2.58*np.sin(t),0]), t_min = -PI, t_max = PI).set_color(PURPLE)

        A1_cor = np.array([0.59445-3.2,2.85216,0])
        A2_cor = np.array([2.50533-3.2,-1.7301,0])
        A3_cor = np.array([-2.62594-3.2,-2.52393,0])
        A4_cor = np.array([-3.22746-3.2,0.70312,0])
        B1_cor = np.array([1.39663-3.2,2.78936,0])
        B2_cor = np.array([1.93687-3.2,-2.19451,0])
        B3_cor = np.array([-3.0197-3.2,-2.19414,0])
        B4_cor = np.array([-3.02573-3.2,1.01258,0])
        C1_cor = np.array([-1.78063-3.2,2.1426,0])
        C2_cor = np.array([3.52969-3.2,0.86827,0])
        C3_cor = np.array([-0.50584-3.2,-3.04181,0])
        C4_cor = np.array([-3.62612-3.2,-0.67887,0])
        D1_cor = np.array([2.4868-3.2,2.37672,0])
        D2_cor = np.array([1.05233-3.2,-2.67718,0])
        D3_cor = np.array([-3.40188-3.2,-1.6547,0])
        D4_cor = np.array([-2.65852-3.2,1.44647,0])

        A = Polygon(A1_cor, A2_cor, A3_cor, A4_cor).set_color(RED)
        B = Polygon(B1_cor, B2_cor, B3_cor, B4_cor).set_color(ORANGE)
        C = Polygon(C1_cor, C2_cor, C3_cor, C4_cor).set_color(YELLOW)
        D = Polygon(D1_cor, D2_cor, D3_cor, D4_cor).set_color(GREEN)

        captions = [
            HText("平面上给定两条圆锥曲线S,T").scale(0.8),
            HText("若存在一封闭n边形外切S且内接T").scale(0.8),
            HText("则T上每一个点").scale(0.8),
            HText("都可以是这种封闭n边形的顶点").scale(0.8),
        ]
        captions[0].next_to(name_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][-3].set_color(BLUE)
        captions[0][-1].set_color(PURPLE)
        captions[1][4:9].set_color(RED)
        captions[1][-5].set_color(BLUE)
        captions[1][-1].set_color(PURPLE)
        captions[2][1].set_color(PURPLE)
        captions[3][6:11].set_color(RED)

        self.play(Write(name),Write(name_eng))
        self.wait(1)
        self.play(Write(captions[0]))
        self.wait(.5)
        self.play(ShowCreation(small_func),ShowCreation(big_func))
        self.wait(1)
        self.play(Write(captions[1]))
        self.wait(.5)     
        self.play(FadeIn(A))
        self.wait(1)
        self.play(Write(captions[2]))
        self.wait(.5)
        self.play(Write(captions[3]))
        self.wait(.5)
        self.play(FadeIn(B))
        self.wait(.5)
        self.play(FadeIn(C))
        self.wait(.5)
        self.play(FadeIn(D))
        self.wait(2)

class FourConic(Scene): #四圆锥曲线定理
    def construct(self):
        name = HText("四圆锥曲线定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng = HText("Four Conics Theorem").set_color("#FFD700").scale(1.1).next_to(name,DOWN).to_edge(RIGHT)

        func_1 = ParametricFunction(lambda t: np.array([-1.13-2+3.35*np.cos(t)-0.17*np.sin(t),0.41+0.68*np.cos(t)+0.83*np.sin(t),0]), t_min = -PI, t_max = PI).set_color(RED)
        func_2 = ParametricFunction(lambda t: np.array([-0.78-2+2.88*np.cos(t)+0.61*np.sin(t),0.35-1.51*np.cos(t)+1.16*np.sin(t),0]), t_min = -PI, t_max = PI).set_color(ORANGE)
        func_3 = ParametricFunction(lambda t: np.array([-0.93-2+0.75*np.cos(t)-2*np.sin(t),0.49+3.37*np.cos(t)+0.45*np.sin(t),0]), t_min = -PI, t_max = PI).set_color(YELLOW)
        C = Circle(radius = 2.38168).move_to(np.array([-0.93232-2,0.4239,0])).set_color(GREEN)
        L1 = Line(np.array([-2.96786-2,0.78117,0]), np.array([1.10604-2,0.1996,0])).set_color("#FF00FF")
        L2 = Line(np.array([-3.0338-2,0.35553,0]), np.array([1.17061-2,0.61073,0])).set_color("#FF00FF")
        L3 = Line(np.array([-0.03546-2,1.43387,0]), np.array([-1.84383-2,-0.5607,0])).set_color("#FF00FF")
        M = Dot(np.array([-0.89546-2,0.48533,0])).set_color("#9400D3")

        A1 = Dot(np.array([-2.47179-2,2.24117,0])).set_color(BLUE)
        A2 = Dot(np.array([1.2048-2,1.47514,0])).set_color(BLUE)
        A3 = Dot(np.array([1.44838-2,0.35556,0])).set_color(BLUE)
        A5 = Dot(np.array([-3.05555-2,-0.65511,0])).set_color(BLUE)
        A6 = Dot(np.array([-3.30296-2,0.65295,0])).set_color(BLUE)
        A4 = Dot(np.array([0.48168-2,-1.4926,0])).set_color(BLUE)

        B1 = Dot(np.array([-2.96786-2,0.78117,0])).set_color(PURPLE)
        B2 = Dot(np.array([-0.03546-2,1.43387,0])).set_color(PURPLE)
        B3 = Dot(np.array([1.17061-2,0.61073,0])).set_color(PURPLE)
        B4 = Dot(np.array([1.10604-2,0.1996,0])).set_color(PURPLE)
        B5 = Dot(np.array([-1.84383-2,-0.5607,0])).set_color(PURPLE)
        B6 = Dot(np.array([-3.0338-2,0.35553,0])).set_color(PURPLE)

        captions = [
            HText("给出三个圆锥曲线").scale(0.8),
            HText("如果每两个之间的四个交点").scale(0.8),
            HText("都有两个位于第四个圆锥曲线上").scale(0.8),
            HText("则连接每对其他两个交点的线共点").scale(0.8),
        ]
        captions[0].next_to(name_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][-4:].set_color(RED)
        captions[2][6:13].set_color(GREEN)
        captions[3][-2:].set_color("#FF00FF")

        self.play(Write(name),Write(name_eng))
        self.play(Write(captions[0]))
        self.wait(.5)
        self.play(ShowCreation(VGroup(func_1,func_2,func_3)))
        self.wait(1)
        self.play(Write(VGroup(A1,A2,A3,A4,A5,A6)))
        self.wait(1)
        self.play(Write(captions[1]))
        self.wait(.5)
        self.play(Write(captions[2]))
        self.wait(.5)
        self.play(FadeOut(func_1),FadeOut(VGroup(A2,A3,A5,A6)))
        self.wait(.5)
        self.play(Write(C))
        self.wait(1.5)
        self.play(FadeIn(func_1),FadeOut(func_2),FadeIn(A5),FadeOut(A4),FadeOut(A1),FadeIn(A2))
        self.wait(1)
        self.play(FadeIn(func_2),FadeOut(func_3),FadeIn(A3),FadeIn(A6),FadeOut(A5),FadeOut(A2)) # A3, A6
        self.wait(1)
        self.play(FadeIn(func_3),FadeIn(VGroup(A1,A2,A4,A5)))
        self.play(Write(captions[3]))
        self.wait(.5)       
        self.play(Write(VGroup(B1,B2,B3,B4,B5,B6)))
        self.wait(1)
        self.play(Write(VGroup(L1,L2,L3)))
        self.wait(.5)
        self.play(Write(M))
        self.wait(2)

class Fregier(Scene): #弗雷吉尔定理
    def construct(self):
        name = HText("弗雷吉尔定理").set_color("#FFD700").scale(1.5).to_edge(UP+RIGHT)
        name_eng = HText("Frégier's Theorem").set_color("#FFD700").scale(1.1).next_to(name,DOWN).to_edge(RIGHT)

        func = ParametricFunction(lambda t: np.array([-0.03-3.2-3.43*np.cos(t)+1.07*np.sin(t),-0.1-1.43*np.cos(t)-2.58*np.sin(t),0]), t_min = -PI, t_max = PI).set_color(BLUE)

        P_cor = np.array([-3.35668-3.2,0.45681,0])
        M_cor = np.array([-0.57077-3.2,-0.85555,0])
        A1_cor = np.array([-3.59877-3.2,-1.03759,0])
        B1_cor = np.array([-3.46904-3.2,-1.50581,0])
        C1_cor = np.array([-3.25722-3.2,-1.90171,0])
        D1_cor = np.array([-2.65776-3.2,-2.5021,0])
        E1_cor = np.array([-1.67708-3.2,-2.93807,0])
        A2_cor = np.array([3.30585-3.2,-0.62249,0])
        B2_cor = np.array([3.52308-3.2,0.06295,0])
        C2_cor = np.array([3.54682-3.2,0.74794,0])
        D2_cor = np.array([2.99399-3.2,1.9569,0])
        E2_cor = np.array([1.36825-3.2,2.79444,0])

        P = Dot(P_cor).set_color("#FFD700")
        P_label = TextMobject("P").next_to(P,UP).set_color("#FFD700")
        M = Dot(M_cor).set_color("#FFD700")
        A1 = Dot(A1_cor).set_color(RED)
        B1 = Dot(B1_cor).set_color("#FF1493")
        C1 = Dot(C1_cor).set_color(PURPLE)
        D1 = Dot(D1_cor).set_color(ORANGE)
        E1 = Dot(E1_cor).set_color(GREEN)
        A2 = Dot(A2_cor).set_color(RED)
        B2 = Dot(B2_cor).set_color("#FF1493")
        C2 = Dot(C2_cor).set_color(PURPLE)
        D2 = Dot(D2_cor).set_color(ORANGE)
        E2 = Dot(E2_cor).set_color(GREEN)

        PA1 = Line(P_cor, A1_cor).set_color(RED)
        PB1 = Line(P_cor, B1_cor).set_color("#FF1493")
        PC1 = Line(P_cor, C1_cor).set_color(PURPLE)
        PD1 = Line(P_cor, D1_cor).set_color(ORANGE)
        PE1 = Line(P_cor, E1_cor).set_color(GREEN)

        PA2 = Line(P_cor, A2_cor).set_color(RED)
        PB2 = Line(P_cor, B2_cor).set_color("#FF1493")
        PC2 = Line(P_cor, C2_cor).set_color(PURPLE)
        PD2 = Line(P_cor, D2_cor).set_color(ORANGE)
        PE2 = Line(P_cor, E2_cor).set_color(GREEN)

        A1A2 = Line(A1_cor, A2_cor).set_color(RED)
        B1B2 = Line(B1_cor, B2_cor).set_color("#FF1493")
        C1C2 = Line(C1_cor, C2_cor).set_color(PURPLE)
        D1D2 = Line(D1_cor, D2_cor).set_color(ORANGE)
        E1E2 = Line(E1_cor, E2_cor).set_color(GREEN)

        captions = [
            HText("在圆锥曲线上选择一点P").scale(0.8),
            HText("画若干顶点在圆锥曲线上").scale(0.8),
            HText("且直角顶点为P的直角三角形").scale(0.8),
            HText("发现所有直角三角形的斜边共点").scale(0.8),
        ]
        captions[0].next_to(name_eng,2*DOWN).to_edge(RIGHT)
        for i in range(1,4):
            captions[i].next_to(captions[i-1],DOWN).to_edge(RIGHT)
        captions[0][1:5].set_color(BLUE)
        captions[0][-1].set_color("#FFD700")
        captions[1][6:10].set_color(BLUE)
        captions[2][-5:].set_color(RED)
        captions[2][6].set_color("#FFD700")
        captions[3][4:9].set_color(RED)
        captions[3][-2:].set_color("#FFD700")

        self.play(Write(name),Write(name_eng))
        self.play(ShowCreation(func))
        self.wait(1)
        self.play(Write(captions[0]))
        self.wait(.5)
        self.play(Write(P),Write(P_label))
        self.wait(1)
        self.play(Write(captions[1]))
        self.wait(.5)
        self.play(Write(captions[2]))
        self.wait(.5)
        self.play(Write(PA1),Write(PA2),Write(A1A2),run_time = 0.3)
        self.play(Write(PB1),Write(PB2),Write(B1B2),run_time = 0.3)
        self.play(Write(PC1),Write(PC2),Write(C1C2),run_time = 0.3)
        self.play(Write(PD1),Write(PD2),Write(D1D2),run_time = 0.3)
        self.play(Write(PE1),Write(PE2),Write(E1E2),run_time = 0.3)
        self.wait(1)
        self.play(Write(captions[3]))
        self.wait(.5)        
        self.play(Write(M))
        self.wait(2)

class thx(Scene): # Thanks for watching + 三连动画V
    def construct(self):
        sentence1 = HText("这就是这个视频的全部内容了").set_color("#FFD700").scale(1.9).to_edge(UP)
        sentence2 = HText("如果喜欢的话不妨四连支持一下！").set_color("#FFD700").scale(1.9).to_edge(UP)

        path = "D:\\manim-master\\manimlib\\files\\"
        sanlian2 = SVGMobject(path + 'good.svg', color=PINK).scale(0.9).shift(4.5*LEFT)
        sanlian3 = SVGMobject(path + 'coin.svg', color=BLUE).scale(0.9).shift(1.5*LEFT)
        sanlian4 = SVGMobject(path + 'favo.svg', color=YELLOW).scale(0.9).shift(1.5*RIGHT).set_opacity(0.85)
        sanlian5 = SVGMobject(path + 'share.svg', color="#ADFF2F").scale(0.9).shift(4.5*RIGHT).set_opacity(0.85)

        self.play(Write(sentence1))
        self.wait(2)
        self.play(ReplacementTransform(sentence1,sentence2))
        self.play(Write(VGroup(sanlian2,sanlian3,sanlian4,sanlian5)))
        self.wait(10)