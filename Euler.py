from manimlib.imports import *
import numpy as np
import math

class Schedule(Scene):
    def construct(self):
        t = []
        t.append(TextMobject("以下定理"))
        t.append(TextMobject("涉及三角形的巧合点--五心"))
        t.append(TextMobject("适合任何学历观看（除了幼儿园小朋友）"))
        t.append(TextMobject("保证看完视频后，能让你对其有不一样的了解"))
        t.append(TextMobject("其实部分是初中竞赛内容"))
        t.append(TextMobject("所以学过的同学可以直接跳到Van Lamoen圆部分"))
        t[0].to_edge(UP+LEFT)

        col = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        for i in range(1,6):
            t[i].set_color_by_gradient(col[(i-1)%6], col[i%6], col[(i+1)%6], col[(i+1)%6], col[(i+2)%6], col[(i+3)%6])
            t[i].align_to(t[0], LEFT)
            t[i].shift(TOP+0.65*(i+1)*DOWN) 
  
        t[5].shift(0.65*DOWN)

        for i in range(6):
            self.play(Write(t[i])) 
            self.wait(0.5)  

class Tri(Scene):
    def construct(self):
        A = Dot(np.array([-4.0,-2.0,0]))
        A_label = TextMobject("A")
        A_label.next_to(A)
        A_label.shift(0.25*DOWN+LEFT)
        B = Dot(np.array([4.0,-2.0,0]))
        B_label = TextMobject("B")
        B_label.next_to(B)
        C = Dot(np.array([-2.0,2.0,0]))
        C_label = TextMobject("C")
        C_label.next_to(C)
        C_label.shift(LEFT)

        triangle = Polygon(np.array([-4.0,-2.0,0]),np.array([4.0,-2.0,0]),np.array([-2.0,2.0,0]))
        intro = TextMobject("五心介绍")
        intro.to_edge(UP)
        self.play(Write(triangle),Write(intro))
        self.play(Write(A),Write(A_label),Write(B),Write(B_label),Write(C),Write(C_label))

        # orthocentre
        ortho = Dot(np.array([-2,1,0]))
        ortho_label = TextMobject("H")
        ortho_label.next_to(ortho)
        ortho_expl = TextMobject("垂心：三条垂线交点")
        ortho_expl.to_edge(DOWN)

        lineA = Line(np.array([-4,-2,0]),np.array([-1.5384,1.6923,0]),color="RED")
        dotA = Dot(np.array([-1.5384,1.6923,0]))
        dotA_label = TexMobject("H_{A}")
        dotA_label.next_to(dotA)

        lineB = Line(np.array([4,-2,0]),np.array([-2.4,1.2,0]),color="YELLOW")
        dotB = Dot(np.array([-2.4,1.2,0]))
        dotB_label = TexMobject("H_{B}")
        dotB_label.next_to(dotB)
        dotB_label.shift(1.5*LEFT)

        lineC = Line(np.array([-2,2,0]),np.array([-2,-2,0]),color="ORANGE")
        dotC = Dot(np.array([-2,-2,0]))
        dotC_label = TexMobject("H_{C}")
        dotC_label.next_to(dotC)
        dotC_label.shift(0.5*DOWN)

        self.wait(2)
        self.play(FadeIn(lineA),FadeIn(dotA),FadeIn(dotA_label),
                 FadeIn(lineB),FadeIn(dotB),FadeIn(dotB_label),
                 FadeIn(lineC),FadeIn(dotC),FadeIn(dotC_label))
        self.wait(1)
        self.play(Write(ortho),Write(ortho_label),FadeIn(ortho_expl))

        self.wait(2)
        self.play(FadeOut(lineA),FadeOut(dotA),FadeOut(dotA_label),
                  FadeOut(lineB),FadeOut(dotB),FadeOut(dotB_label),
                  FadeOut(lineC),FadeOut(dotC),FadeOut(dotC_label))     

        # centroid
        centr = Dot(np.array([-0.6667,0.3333-1,0]))
        centr_label = TextMobject("G")
        centr_label.next_to(centr)
        centr_expl = TextMobject("重心：三条中线交点")
        centr_expl.to_edge(DOWN)
        self.play(Transform(ortho_expl,centr_expl))

        lineA = Line(np.array([-4,-2,0]),np.array([1,0,0]),color="RED")
        dotA = Dot(np.array([1,0,0]))
        dotA_label = TexMobject("A_{1}")
        dotA_label.next_to(dotA)

        lineB = Line(np.array([4,-2,0]),np.array([-3,0,0]),color="YELLOW")
        dotB = Dot(np.array([-3,0,0]))
        dotB_label = TexMobject("B_{1}")
        dotB_label.next_to(dotB)
        dotB_label.shift(1.5*LEFT)

        lineC = Line(np.array([-2,2,0]),np.array([0,-2,0]),color="ORANGE")
        dotC = Dot(np.array([0,-2,0]))
        dotC_label = TexMobject("C_{1}")
        dotC_label.next_to(dotC)
        dotC_label.shift(0.5*DOWN)

        self.wait(2)
        self.play(FadeIn(lineA),FadeIn(dotA),FadeIn(dotA_label),
                 FadeIn(lineB),FadeIn(dotB),FadeIn(dotB_label),
                 FadeIn(lineC),FadeIn(dotC),FadeIn(dotC_label))
        self.wait(1)
        self.play(Write(centr),Write(centr_label))

        self.wait(2)
        self.play(FadeOut(lineA),
                  FadeOut(lineB),
                  FadeOut(lineC))   

        # circumcentre
        circr = Dot(np.array([0,-1.5,0]))
        circr_label = TextMobject("O")
        circr_label.next_to(circr)
        circr_expl = TextMobject("外心：外接圆圆心")
        circr_expl2 = TextMobject("也是三条垂直平分线的交点")
        circr_expl.to_edge(DOWN)
        circr_expl2.to_edge(DOWN)        
        self.play(Transform(ortho_expl,circr_expl))
        self.wait(2)
        self.play(Transform(ortho_expl,circr_expl2))

        lineA = Line(np.array([1,0,0]),np.array([-0.3333,-2,0]),color="RED")
        lineB = Line(np.array([-3,0,0]),np.array([1,-2,0]),color="YELLOW")
        lineC = Line(np.array([0,-2,0]),np.array([0,0.6667,0]),color="ORANGE")

        self.wait(1)
        self.play(FadeIn(lineA),FadeIn(lineB),FadeIn(lineC))
        self.wait(1)
        self.play(Write(circr),Write(circr_label))

        circl_out = Circle(radius=4.0311)
        circl_out.shift(np.array([0,-1.5,0]))
        self.play(FadeIn(circl_out))

        self.wait(2)
        self.play(FadeOut(lineA),FadeOut(dotA),FadeOut(dotA_label),
                  FadeOut(lineB),FadeOut(dotB),FadeOut(dotB_label),
                  FadeOut(lineC),FadeOut(dotC),FadeOut(dotC_label),FadeOut(circl_out))  

        # incentre
        incen = Dot(np.array([-1.3694,0.6257-1,0]))
        incen_label = TextMobject("I")
        incen_label.next_to(incen)
        incen_expl = TextMobject("内心：内切圆圆心")
        incen_expl2 = TextMobject("也是三条角平分线的交点")
        incen_expl.to_edge(DOWN)
        incen_expl2.to_edge(DOWN)
        self.play(Transform(ortho_expl,incen_expl))
        self.wait(2)
        self.play(Transform(ortho_expl,incen_expl2))

        lineA = Line(np.array([-4,-2,0]),np.array([0.1514,0.5657,0]),color="RED")
        dotA = Dot(np.array([0.1514,0.5657,0]))
        dotA_label = TexMobject("M_{A}")
        dotA_label.next_to(dotA)

        lineB = Line(np.array([4,-2,0]),np.array([-2.9481,0.1037,0]),color="YELLOW")
        dotB = Dot(np.array([-2.9481,0.1037,0]))
        dotB_label = TexMobject("M_{B}")
        dotB_label.next_to(dotB)
        dotB_label.shift(1.5*LEFT)

        lineC = Line(np.array([-2,2,0]),np.array([-0.9377,-2,0]),color="ORANGE")
        dotC = Dot(np.array([-0.9377,-2,0]))
        dotC_label = TexMobject("M_{C}")
        dotC_label.next_to(dotC)
        dotC_label.shift(0.5*DOWN)

        self.wait(2)
        self.play(FadeIn(lineA),FadeIn(dotA),FadeIn(dotA_label),
                 FadeIn(lineB),FadeIn(dotB),FadeIn(dotB_label),
                 FadeIn(lineC),FadeIn(dotC),FadeIn(dotC_label))
        self.wait(1)
        self.play(Write(incen),Write(incen_label))

        circl_in = Circle(radius=1.6257)
        circl_in.shift(np.array([-1.3694,0.6257-1,0]))
        self.play(FadeIn(circl_in))

        self.wait(2)
        self.play(FadeOut(lineA),FadeOut(dotA),FadeOut(dotA_label),
                  FadeOut(lineB),FadeOut(dotB),FadeOut(dotB_label),
                  FadeOut(lineC),FadeOut(dotC),FadeOut(dotC_label),FadeOut(circl_in)) 
        # excentre
        excr_expl = TextMobject("旁心：旁切圆圆心（总共有三个)")
        excr_expl.to_edge(DOWN)
        field = [triangle,incen,incen_label,circr,circr_label,centr,centr_label,ortho,ortho_label,A,A_label,B,B_label,C,C_label]
        draw_field = VGroup(*field)
        self.wait(1)                                     
        self.play(ApplyMethod(draw_field.scale,0.25))

        excr1 = Dot(np.array([2.9208/2.0,2.0412/2.0,0]),color="RED")
        excr1_label = TexMobject("J_{A}") # 1.5206
        excr1_label.next_to(excr1)
        excircle1 = Circle(radius=1.5206)
        excircle1.shift(np.array([2.9208/2.0,2.0412/2.0,0]))

        excr2 = Dot(np.array([-2.9208/2.0,0.4899/2.0,0]),color="YELLOW")
        excr2_label = TexMobject("J_{B}") #0.7449
        excr2_label.next_to(excr2)
        excr2_label.shift(LEFT)
        excircle2 = Circle(radius=0.7449)
        excircle2.shift(np.array([-2.9208/2.0,0.4899/2.0,0]))

        excr3 = Dot(np.array([0.6847/2.0,-5.3440/2.0,0]),color="ORANGE")
        excr3_label = TexMobject("J_{C}") #2.1720
        excr3_label.next_to(excr3)
        excr3_label.shift(0.5*UP)
        excircle3 = Circle(radius=2.1720)
        excircle3.shift(np.array([0.6847/2.0,-5.3440/2.0,0]))
        
        line1 = Line(np.array([-4,-0.5,0]),np.array([4,-0.5,0]),color="BLUE")
        line2 = Line(np.array([-3.7036/2.0,-4.4072/2.0,0]),np.array([1.0372/2.0,5.0744/2.0,0]),color="BLUE")
        line3 = Line(np.array([-4.8029/2.0,3.5353/2.0,0]),np.array([7.8230/2.0,-4.8820/2.0,0]),color="BLUE")

        self.play(Transform(ortho_expl,excr_expl),
                  Write(excr1),Write(excr1_label),Write(excr2),Write(excr2_label),
                  Write(excr3),Write(excr3_label),
                  FadeOut(triangle),FadeOut(A),FadeOut(A_label),FadeOut(B),FadeOut(B_label),FadeOut(C),FadeOut(C_label))
        self.wait(1)
        self.play(FadeIn(excircle1),FadeIn(excircle2),FadeIn(excircle3),
            FadeIn(line1),FadeIn(line2),FadeIn(line3))  
        self.wait(1)
        self.play(FadeOut(excircle1),FadeOut(excircle2),FadeOut(excircle3),
            FadeOut(line1),FadeOut(line2),FadeOut(line3),
            FadeIn(triangle),FadeIn(A),FadeIn(A_label),FadeIn(B),FadeIn(B_label),FadeIn(C),FadeIn(C_label)) 


class Property(Scene):
    def construct(self):  
        A = Dot(np.array([-4.0,-2.0,0]))
        A_label = TextMobject("A")
        A_label.next_to(A)
        A_label.shift(0.25*DOWN+LEFT)
        B = Dot(np.array([4.0,-2.0,0]))
        B_label = TextMobject("B")
        B_label.next_to(B)
        C = Dot(np.array([-2.0,2.0,0]))
        C_label = TextMobject("C")
        C_label.next_to(C)
        C_label.shift(LEFT)

        triangle = Polygon(np.array([-4.0,-2.0,0]),np.array([4.0,-2.0,0]),np.array([-2.0,2.0,0]))
        intro = TextMobject("简单性质")
        intro.to_edge(UP)
        self.play(Write(triangle),Write(intro))
        self.play(Write(A),Write(A_label),Write(B),Write(B_label),Write(C),Write(C_label))

        ortho = Dot(np.array([-2,1,0]))
        ortho_label = TextMobject("H")
        ortho_label.next_to(ortho)
        ortho_label.shift(LEFT)

        centr = Dot(np.array([-0.6667,-0.6667,0]))
        centr_label = TextMobject("G")
        centr_label.next_to(centr)

        circr = Dot(np.array([0,-1.5,0]))
        circr_label = TextMobject("O")
        circr_label.next_to(circr)

        incen = Dot(np.array([-1.3694,-0.3743,0]))
        incen_label = TextMobject("I")
        incen_label.next_to(incen)

        self.play(Write(ortho),Write(ortho_label),
                  Write(centr),Write(centr_label),
                  Write(circr),Write(circr_label),
                  Write(incen),Write(incen_label))      
#The line connecting the incentre with arbitrary vertices bisects the angle formed 
# by the vertex, circumcentre, and orthocentre connected in order
        expl = TextMobject("内心和任意顶点连成的直线")                    
        expl_2 = TextMobject("平分该顶点，外心和垂心依次连结所成的角")     
        expl.to_edge(DOWN)
        expl_2.to_edge(DOWN)  
        expl.shift(0.65*UP)

        lH = Line(np.array([-2,1,0]),np.array([-4.0,-2.0,0]))
        lI = Line(np.array([-1.3694,-0.3743,0]),np.array([-4.0,-2.0,0]))
        lO = Line(np.array([0,-1.5,0]),np.array([-4.0,-2.0,0]))

        ArcHI = Arc(start_angle = 31.9808482/180.0 * 3.1415927,angle = 24.3290843/180.0 * 3.1415927,color = "RED", fill_opacity = 0.7)
        ArcHI.shift(np.array([-4.0,-2.0,0]))
        ArcHI_label = TexMobject(r"\alpha")
        ArcHI_label.next_to(ArcHI)
        ArcHI_label.shift(0.5*UP)

        ArcIO = Arc(start_angle = 7.1250163/180.0 * 3.1415927, angle = 24.8558318/180.0 * 3.1415927, color = "BLUE", fill_opacity = 0.7)
        ArcIO.shift(np.array([-4.0,-2.0,0]))
        ArcIO_label = TexMobject(r"\alpha")
        ArcIO_label.next_to(ArcIO)

        self.play(Write(expl),Write(lH),Write(lI),Write(lO),Write(ArcHI),Write(ArcHI_label),Write(ArcIO),Write(ArcIO_label))
        self.wait(5)
        self.remove(lH,lI,lO,ArcHI,ArcIO,ArcHI_label,ArcIO_label)

        lH = Line(np.array([-2,1,0]),np.array([-2.0,2.0,0]))
        lI = Line(np.array([-1.3694,-0.3743,0]),np.array([-2.0,2.0,0]))
        lO = Line(np.array([0,-1.5,0]),np.array([-2.0,2.0,0]))

        ArcHI = Arc(start_angle = -0.5 * 3.1415927,angle = (14.2637055/180.0) * 3.1415927,color = "RED", fill_opacity = 0.7, radius = 0.5)
        ArcHI.shift(np.array([-2.0,2.0,0]))
        ArcHI_label = TexMobject(r"\small \alpha")
        ArcHI_label.next_to(ArcHI)
        ArcHI_label.shift(0.5*LEFT+0.25*DOWN)

        ArcIO = Arc(start_angle = (14.2637055/180.0-0.5) * 3.1415927, angle = ((14.2637055+15.4811758)/180.0) * 3.1415927, color = "BLUE", fill_opacity = 0.7, radius = 0.5)
        ArcIO.shift(np.array([-2.0,2.0,0]))
        ArcIO_label = TexMobject(r"\small \alpha")
        ArcIO_label.next_to(ArcIO)
        ArcIO_label.shift(0.25*LEFT+0.25*DOWN)

        self.play(Write(expl_2),Write(lH),Write(lI),Write(lO),Write(ArcHI),Write(ArcHI_label),Write(ArcIO),Write(ArcIO_label))    
        self.wait(4)
        self.remove(lH,lI,lO,ArcHI,ArcIO,ArcHI_label,ArcIO_label,expl,expl_2) # 7 animations

        expl = TextMobject("三角形的任一顶点到垂心的距离")                    
        expl_2 = TextMobject("等于外心到对边距离的两倍")     
        expl.to_edge(DOWN)
        expl_2.to_edge(DOWN)

        lH = Line(np.array([-2,1,0]),np.array([-2.0,2.0,0]),color="RED")
        lO = Line(np.array([0,-1.5,0]),np.array([0,-2.0,0]),color="BLUE")
        lH_comp = Line(np.array([1,2,0]),np.array([2,2,0]),color="RED")
        lO_comp = Line(np.array([1,1.8,0]),np.array([1.5,1.8,0]),color="BLUE")
        D = Dot(np.array([0,-2,0]))
        D_label  = TextMobject("D")
        D_label.next_to(D)

        md = Dot(np.array([1.5,2,0]))
        theo = TexMobject("e.g.: CH = 2OD")
        theo.to_edge(DOWN)

        self.play(Write(expl),Write(lH),Write(lO),Write(D),Write(D_label))
        self.wait(6)
        self.play(Transform(expl,expl_2))
        self.wait(6)
        self.play(Transform(expl,theo),Transform(lH,lH_comp),Transform(lO,lO_comp),Write(md))   
        self.wait(5)
        self.remove(lH,lO,md,expl,D,D_label)

        HtoA = Line(np.array([-2,1,0]),np.array([-1.5385,1.6923,0]),color="RED")
        HtoB = Line(np.array([-2,1,0]),np.array([-2.4,1.2,0]),color="RED")
        HtoC = Line(np.array([-2,1,0]),np.array([-2,-2,0]),color="RED")

        GtoA = Line(np.array([-0.6667,-0.6667,0]),np.array([0.1538,0.5641,0]),color="ORANGE")
        GtoB = Line(np.array([-0.6667,-0.6667,0]),np.array([-2.8000,0.4,0]),color="ORANGE")
        GtoC = Line(np.array([-0.6667,-0.6667,0]),np.array([-0.6667,-2,0]),color="ORANGE")

        OtoA = Line(np.array([0,-1.5,0]),np.array([1,0,0]),color="BLUE")
        OtoB = Line(np.array([0,-1.5,0]),np.array([-3,0,0]),color="BLUE")
        OtoC = Line(np.array([0,-1.5,0]),np.array([0,-2,0]),color="BLUE")

        self.play(Write(HtoA),Write(HtoB),Write(HtoC))
        self.wait(2)
        self.play(Write(GtoA),Write(GtoB),Write(GtoC))
        self.wait(2)
        self.play(Write(OtoA),Write(OtoB),Write(OtoC))

        rd = TexMobject(r"Red: d_{H}",color="RED")
        oge = TexMobject(r"Orange: d_{G}",color="ORANGE")
        ble = TexMobject(r"Blue:d_{O}",color="BLUE")
        d = TextMobject("d: 垂足到该点距离的长度和")
        rd.to_edge(RIGHT)
        oge.to_edge(RIGHT)
        ble.to_edge(RIGHT)
        d.to_edge(DOWN)

        oge.shift(0.65*UP)
        rd.shift(1.3*UP)

        form = TexMobject("1*","d_{H}"," + 2*","d_{O}"," = 3*","d_{G}")
        form.set_color_by_tex_to_color_map({
            "d_{H}" : RED,
            "d_{O}" : BLUE,
            "d_{G}" : ORANGE
        })
        form.to_edge(DOWN)
        self.wait(2)
        self.play(Write(rd),Write(oge),Write(ble),Write(d))
        self.wait(2)
        self.play(Transform(d,form))
        self.wait(3)


class ShenCircle(Scene):
    def construct(self):
        A = Dot(np.array([-4.0,-2.0,0]))
        A_label = TextMobject("A")
        A_label.next_to(A)
        A_label.shift(0.25*DOWN+LEFT)
        B = Dot(np.array([4.0,-2.0,0]))
        B_label = TextMobject("B")
        B_label.next_to(B)
        C = Dot(np.array([-2.0,2.0,0]))
        C_label = TextMobject("C")
        C_label.next_to(C)
        C_label.shift(LEFT)

        triangle = Polygon(np.array([-4.0,-2.0,0]),np.array([4.0,-2.0,0]),np.array([-2.0,2.0,0]))
        intro = TextMobject("Van Lamoen圆")
        intro.to_edge(UP)
        self.play(Write(triangle),Write(intro))
        self.play(Write(A),Write(A_label),Write(B),Write(B_label),Write(C),Write(C_label))

        centr = Dot(np.array([-0.6667,-0.6667,0]))
        centr_label = TextMobject("G")
        centr_label.next_to(centr)
        
        lineA = Line(np.array([-4,-2,0]),np.array([1,0,0]),color="RED")
        dotA = Dot(np.array([1,0,0]))
        dotA_label = TexMobject("A_{1}")
        dotA_label.next_to(dotA)

        lineB = Line(np.array([4,-2,0]),np.array([-3,0,0]),color="YELLOW")
        dotB = Dot(np.array([-3,0,0]))
        dotB_label = TexMobject("B_{1}")
        dotB_label.next_to(dotB)
        dotB_label.shift(1.5*LEFT)

        lineC = Line(np.array([-2,2,0]),np.array([0,-2,0]),color="ORANGE")
        dotC = Dot(np.array([0,-2,0]))
        dotC_label = TexMobject("C_{1}")
        dotC_label.next_to(dotC)
        dotC_label.shift(0.5*DOWN)

        cgd = Dot(np.array([-1.5834,0.5416,0]),color="RED")
        cge = Dot(np.array([-0.4167,1.1250,0]),color="RED")
        agd = Dot(np.array([-2.2083,-1.6459,0]),color="RED")
        agf = Dot(np.array([-2.0000,-2.1666,0]),color="RED")
        bgf = Dot(np.array([1.9999,-0.1667,0]),color="RED")
        bge = Dot(np.array([1.2083,-2.9375,0]),color="RED")

        cgd_label = TexMobject("O_{CGD}",color="RED")
        cge_label = TexMobject("O_{CGE}",color="RED")
        agd_label = TexMobject("O_{AGD}",color="RED")
        agf_label = TexMobject("O_{AGF}",color="RED")
        bgf_label = TexMobject("O_{BGF}",color="RED")
        bge_label = TexMobject("O_{BGE}",color="RED")

        cgd_label.next_to(cgd)
        cge_label.next_to(cge)
        agd_label.next_to(agd)
        agf_label.next_to(agf)
        bgf_label.next_to(bgf)
        bge_label.next_to(bge)

        six_point_circle = Circle(radius = 2.2372)
        six_point_circle.shift(np.array([-0.0426,-1.0816,0]))
        
        rem = TextMobject("六个由中线分割成的三角形的外心共圆")
        rem.to_edge(DOWN)

        self.wait(2) 
        self.play(Write(centr),Write(centr_label),Write(lineA),Write(dotA),Write(dotA_label),
                 Write(lineB),Write(dotB),Write(dotB_label),
                 Write(lineC),Write(dotC),Write(dotC_label)) 
        self.wait(2)
        self.play(Write(cgd),Write(cge),Write(agd),Write(agf),Write(bgf),Write(bge),
                  Write(cgd_label),Write(cge_label),Write(agd_label),Write(agf_label),Write(bgf_label),Write(bge_label))
        self.wait(3)
        self.play(Write(six_point_circle),Write(rem))
        self.wait(5)

        self.remove(lineA,dotA,dotA_label,
                    lineB,dotB,dotB_label,
                    lineC,dotC,dotC_label,
                    cgd,cge,agd,agf,bgf,bge,
                    cgd_label,cge_label,agd_label,agf_label,bgf_label,bge_label,
                    six_point_circle)
        # euler line
        
        intro2 = TextMobject("欧拉线")
        intro2.to_edge(UP)
        rem2 = TextMobject("垂心，重心，外心共线")
        rem2.to_edge(DOWN)

        ortho = Dot(np.array([-2,1,0]))
        ortho_label = TextMobject("H")
        ortho_label.next_to(ortho)

        circr = Dot(np.array([0,-1.5,0]))
        circr_label = TextMobject("O")
        circr_label.next_to(circr)

        Euler_Line = Line(np.array([-2,1,0]),np.array([0,-1.5,0]),color="PURPLE")
        self.play(Write(ortho),Write(circr),Write(ortho_label),Write(circr_label),Transform(intro,intro2),Write(Euler_Line),Transform(rem,rem2))
        self.wait(5)
        
        # taylor circle
        intro3 = TextMobject("泰勒圆")
        intro3.to_edge(UP)
        rem3 = TextMobject("将垂心往三点做垂线")
        rem3.to_edge(DOWN)

        lineA = Line(np.array([-4,-2,0]),np.array([-1.5384,1.6923,0]),color="RED")
        dotA = Dot(np.array([-1.5384,1.6923,0]),color="RED")
        dotA_label = TexMobject("H_{A}",color="RED")
        dotA_label.next_to(dotA)

        lineB = Line(np.array([4,-2,0]),np.array([-2.4,1.2,0]),color="YELLOW")
        dotB = Dot(np.array([-2.4,1.2,0]),color="YELLOW")
        dotB_label = TexMobject("H_{B}",color="YELLOW")
        dotB_label.next_to(dotB)
        dotB_label.shift(1.5*LEFT)

        lineC = Line(np.array([-2,2,0]),np.array([-2,-2,0]),color="ORANGE")
        dotC = Dot(np.array([-2,-2,0]),color="ORANGE")
        dotC_label = TexMobject("H_{C}",color="ORANGE")
        dotC_label.next_to(dotC)
        dotC_label.shift(0.5*DOWN)

        self.wait(2)
        self.play(Transform(intro,intro3),Transform(rem,rem3),Write(lineA),Write(dotA),Write(dotA_label),
                 Write(lineB),Write(dotB),Write(dotB_label),
                 Write(lineC),Write(dotC),Write(dotC_label))

        rem3_2 = TextMobject("再分别往另两边作垂线")
        rem3_2.to_edge(DOWN)

        Hab = Dot(np.array([-2.0307,1.9385,0]),color="RED")
        Hac = Dot(np.array([-1.5385,-2,0]),color="RED") 
        Hba = Dot(np.array([-1.9077,1.9385,0]),color="YELLOW")
        Hbc = Dot(np.array([-2.4,-2,0]),color="YELLOW")
        Hca = Dot(np.array([-0.1538,0.7692,0]),color="ORANGE")
        Hcb = Dot(np.array([-3.6,-1.2,0]),color="ORANGE")

        Lineab = Line(np.array([-1.5384,1.6923,0]),np.array([-2.0307,1.9385,0]),color="RED")
        Lineac = Line(np.array([-1.5384,1.6923,0]),np.array([-1.5385,-2,0]),color="RED")
        Lineba = Line(np.array([-2.4,1.2,0]),np.array([-1.9077,1.9385,0]),color="YELLOW")
        Linebc = Line(np.array([-2.4,1.2,0]),np.array([-2.4,-2,0]),color="YELLOW")
        Lineca = Line(np.array([-2,-2,0]),np.array([-0.1538,0.7692,0]),color="ORANGE")
        Linecb = Line(np.array([-2,-2,0]),np.array([-3.6,-1.2,0]),color="ORANGE")

        self.play(Write(Lineab),Write(Hab),Write(Lineac),Write(Hac),Transform(rem,rem3_2))
        self.play(Write(Lineba),Write(Hba),Write(Linebc),Write(Hbc))
        self.play(Write(Lineca),Write(Hca),Write(Linecb),Write(Hcb))
        self.wait(3)

        tay_circle = Circle(radius=1.9932)
        tay_circle.shift(np.array([-1.9692,-0.0538,0]))
        rem4 = TextMobject("所形成的点都在泰勒圆上")
        rem4.to_edge(DOWN)

        self.play(Transform(rem,rem4),Write(tay_circle))
        self.wait(4)
        self.remove(Lineab,Hab,Lineac,Hac,Lineba,Hba,Linebc,Hbc,Lineca,Hca,Linecb,Hcb,tay_circle)

        intro4 = TextMobject("欧拉圆（九点圆）")
        intro4.to_edge(UP)

        rem4 = TextMobject("垂心的三个垂足，垂心与顶点连线后的三个中点")
        rem4_2 = TextMobject("与三角形的三个中点，九个点共圆")
        rem4_3 = TextMobject("同时九点圆圆心正好在欧拉线上")
        rem4.to_edge(DOWN)
        rem4_2.to_edge(DOWN)
        rem4_3.to_edge(DOWN)

        self.play(Write(dotA),Write(dotA_label),Write(dotB),Write(dotB_label),Write(dotC),Write(dotC_label),Transform(intro,intro4),Transform(rem,rem4))

        ah = Line(np.array([-4.0,-2.0,0]),np.array([-2,1,0]))
        bh = Line(np.array([4.0,-2.0,0]),np.array([-2,1,0]))
        ch = Line(np.array([-2.0,2.0,0]),np.array([-2,1,0]))

        mah = Dot(np.array([-3,-0.5,0]))
        mbh = Dot(np.array([1,-0.5,0]))
        mch = Dot(np.array([-2,1.5,0]))

        mA = Dot(np.array([1,0,0]))
        mB = Dot(np.array([-3,0,0]))
        mC = Dot(np.array([0,-2,0]))

        O9 = Dot(np.array([-1,-0.25,0]))
        O9_label = TexMobject("O_9")
        O9_label.next_to(O9)

        O9circle = Circle(radius = 1.993)
        O9circle.shift(np.array([-1,-0.25,0]))
        self.play(Write(ah),Write(bh),Write(ch),Write(mah),Write(mbh),Write(mch),Write(mA),Write(mB),Write(mC))
        self.wait(2)
        self.play(Write(O9),Write(O9_label),Write(O9circle),Transform(rem,rem4_2))
        self.wait(1)
        self.play(Transform(rem,rem4_3))
        self.wait(3)
        self.remove(O9_label,O9,O9circle,ah,bh,ch,mah,mbh,mch,mA,mB,mC,
                   dotA,dotB,dotC,dotA_label,dotB_label,dotC_label,lineA,lineB,lineC)

        # schiffler point 
        intro4 = TextMobject("Schiffler点")
        intro4.to_edge(UP)

        rem5 = TextMobject(r"$\Delta$ AIC, $\Delta$ BIC, $\Delta$ AIB 的欧拉线共点")
        rem5_2 = TextMobject("这个点被称为Schiffler点")
        rem5.to_edge(DOWN)
        rem5_2.to_edge(DOWN)

        self.play(Transform(intro,intro4),Transform(rem,rem5))
        self.wait(2)

        incen = Dot(np.array([-1.3694,-0.3743,0]))
        incen_label = TextMobject("I")
        incen_label.next_to(incen)

        Ia = Line(np.array([-1.3694,-0.3743,0]),np.array([-4.0,-2.0,0]))
        Ib = Line(np.array([-1.3694,-0.3743,0]),np.array([4.0,-2.0,0]))
        Ic = Line(np.array([-1.3694,-0.3743,0]),np.array([-2.0,2.0,0]))

        Euler_AIC = Line(np.array([-6.0028,1.2143,0]),np.array([6.0291,-3.3405,0]),color="RED")
        Euler_BIC = Line(np.array([-5.9493,-6.0526,0]),np.array([5.8510,5.3205,0]),color="ORANGE")
        Euler_AIB = Line(np.array([-1.3964,6.6425,0]),np.array([0,-5.5084,0]),color="YELLOW")
        S = Dot(np.array([-0.5508,-0.8496,0]))
        S_label = TextMobject("S")
        S_label.next_to(S)

        self.play(Write(incen),Write(incen_label),Write(Ia),Write(Ib),Write(Ic))
        self.wait(2)
        self.play(Write(Euler_AIC),Write(Euler_BIC),Write(Euler_AIB))
        self.wait(2)
        self.play(Write(S),Write(S_label),Transform(rem,rem5_2))

class Euler_formula(Scene):
    def construct(self):
        A = Dot(np.array([-1*4,-0.5*4,0]))
        A_label = TextMobject("A")
        A_label.next_to(A)
        A_label.shift(0.25*DOWN+LEFT)
        B = Dot(np.array([1.0*4,-0.5*4,0]))
        B_label = TextMobject("B")
        B_label.next_to(B)
        C = Dot(np.array([-0.5*4,0.5*4,0]))
        C_label = TextMobject("C")
        C_label.next_to(C)
        C_label.shift(LEFT)

        triangle = Polygon(np.array([-1.0*4,-0.5*4,0]),np.array([1.0*4,-0.5*4,0]),np.array([-0.5*4,0.5*4,0]))
        intro = TextMobject("平面几何的欧拉公式")
        intro.to_edge(UP)
        self.play(Write(triangle),Write(intro))
        self.play(Write(A),Write(A_label),Write(B),Write(B_label),Write(C),Write(C_label))

        I = Dot(np.array([-0.3424*4,-0.0936*4,0]))
        O = Dot(np.array([0,-0.375*4,0]))

        I_label = TextMobject("I")
        O_label = TextMobject("O")

        I_label.next_to(I)
        O_label.next_to(O)

        io = Line(np.array([-0.3424*4,-0.0936*4,0]),np.array([0,-0.375*4,0]),color="RED")
        io_label = TexMobject("d",color="RED")
        io_label.next_to(io)

        r = Line(np.array([-0.6252*4,-0.3854*4,0]),np.array([-0.3424*4,-0.0936*4,0]),color="GREEN")
        r_label = TexMobject("r",color="GREEN")

        R = Line(np.array([1.0*4,-0.5*4,0]),np.array([0,-0.375*4,0]),color="BLUE")
        R_label = TexMobject("R",color="BLUE")

        r_label.next_to(r)
        R_label.next_to(R)

        r_label.shift(LEFT+0.5*UP)
        R_label.shift(0.5*UP+2*LEFT)
        io_label.shift(LEFT+0.5*UP)

        I_circle = Circle(radius = 0.4064*4)
        O_circle = Circle(radius = 1.0078*4)

        I_circle.shift(np.array([-0.3424*4,-0.0936*4,0]))
        O_circle.shift(np.array([0,-0.375*4,0]))

        rem = TexMobject(r"\frac{1}{R-d} + \frac{1}{R+d} = \frac{1}{r}")
        rem.to_edge(DOWN)

        self.play(Write(I),Write(I_label),Write(O),Write(O_label),Write(I_circle),Write(O_circle),
                  Write(r),Write(R),Write(r_label),Write(R_label))
        self.wait(2)
        self.play(Write(io),Write(io_label),Write(rem))
        self.wait(3)

class Feubach(Scene):
    def construct(self):
        A = Dot(np.array([-4.0,-2.0,0]))
        A_label = TextMobject("A")
        A_label.next_to(A)
        A_label.shift(0.25*DOWN+LEFT)
        B = Dot(np.array([4.0,-2.0,0]))
        B_label = TextMobject("B")
        B_label.next_to(B)
        C = Dot(np.array([-2.0,2.0,0]))
        C_label = TextMobject("C")
        C_label.next_to(C)
        C_label.shift(LEFT)

        triangle = Polygon(np.array([-4.0,-2.0,0]),np.array([4.0,-2.0,0]),np.array([-2.0,2.0,0]))
        intro = TextMobject("Feuerbach定理")
        intro.to_edge(UP)

        rem = TextMobject("九点圆分别与内切圆和旁切圆相切")
        rem.to_edge(DOWN)

        self.play(Write(triangle),Write(intro))
        self.play(Write(A),Write(A_label),Write(B),Write(B_label),Write(C),Write(C_label),Write(rem))

        excircle1 = Circle(radius=1.5206*4)
        excircle1.shift(np.array([2.9208*2.0,2.0412*2.0,0]))

        excircle2 = Circle(radius=0.7449*4)
        excircle2.shift(np.array([-2.9208*2.0,0.4899*2.0,0]))

        excircle3 = Circle(radius=2.1720*4)
        excircle3.shift(np.array([0.6847*2.0,-5.3440*2.0,0]))

        circl_in = Circle(radius=1.6257)
        circl_in.shift(np.array([-1.3694,0.6257-1,0]))

        O9circle = Circle(radius = 1.993,color="BLUE")
        O9circle.shift(np.array([-1,-0.25,0]))

        self.wait(2)
        self.play(Write(excircle1),Write(excircle2),Write(excircle3),Write(circl_in))
        self.wait(2)
        self.play(Write(O9circle))

class End(Scene):
    def construct(self):
        a = TextMobject("这就是这个视频的全部了")
        b = TextMobject("非常感谢你能看到这里")
        c = TextMobject("如果对数学感兴趣的同学")
        d = TextMobject("可以加入交流群726542042")
        e = TextMobject("如果对视频制作过程")
        f = TextMobject("和IT技术（网络爬虫，软件工程等）有兴趣")
        g = TextMobject("可以三连并关注私信我后加入1014495189")
        h = TextMobject("下个视频见！")

        self.play(Write(a))
        self.wait(1)
        self.play(Transform(a,b))
        self.wait(1)
        self.play(Transform(a,c))
        self.wait(1)
        self.play(Transform(a,d))
        self.wait(1)
        self.play(Transform(a,e))
        self.wait(1)
        self.play(Transform(a,f))
        self.wait(1)
        self.play(Transform(a,g))   
        self.wait(1)
        self.play(Transform(a,h))    