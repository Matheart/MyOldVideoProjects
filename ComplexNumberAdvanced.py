from manimlib.imports import *
import numpy as np
import math

class MyText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
    }
# ----------- Write Text ----------------- #
class RightText(Scene):
    def construct(self):
        Top = MyText("前情提要")
        col = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        Top.set_color_by_gradient(col)
        Top.scale(0.75)
        Top.to_edge(UP)

        text = []
        text.append(MyText("在上期视频中"))
        text.append(MyText("我们通过单位根展示了复数的美"))
        text.append(MyText("并得出"))
        text.append(TexMobject(r"\bold{\text{1的n次根为：}}e^{\frac{2ki\pi}{n}} (k \in [0,n-1])",color=RED))
        text.append(TexMobject(r"\bold{W(\rho,\phi) \text{ 的n次根的表达形式为：}} (\rho^{\frac{1}{n}},\frac{\phi + 2k \pi}{n})",color=BLUE))
        text.append(MyText("同时亦发现单位根在极坐标能够更加优雅地被表示出来"))
        texts = VGroup(*text)
        texts.scale(0.5)
        texts.shift(UP*2.5+RIGHT*1)
        texts.shift(1.5*DOWN)

        for i in range(1,len(texts)):
            text[i].next_to(text[i-1],DOWN)
            text[i].align_to(text[0],LEFT)
        
        self.play(Write(Top))
        self.play(Write(texts), run_time = 5)
        self.wait(5)

# ----------- Write Circle ----------------- #
class PreviousVideoRewatch(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }

    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)
        self.wait(6)

        circle = Circle(color=WHITE,radius=4)
        self.play(Write(circle),run_time = 0.25)

        col = ["#800000","#8B0000","#A52A2A","#B22222","#DC143C","#FF0000","#FF6347","#FF7F50","#CD5C5C","#F08080","#E9967A","#FA8072","#FFA07A","#FF4500",
               "#FF8C00","#FFA500","#FFD700","#B8860B","#DAA520","#FFFF00","#9ACD32",
               "#556B2F","#6B8E23","#7CFC00","#7FFF00","#ADFF2F","#006400","#008000","#228B22","#00FF00","#32CD32","#90EE90","#98FB98","#00FA9A","#00FF7F","#2E8B57",
               "#20B2AA","#008080","#008B8B","#00FFFF","#00CED1","#40E0D0","#7FFFD4","#4682B4","#6495ED","#00BFFF","#1E90FF","#191970","#000080","#00008B","#0000FF",
               "#8A2BE2","#4B0082","#483D8B","#6A5ACD","#7B68EE","#9400D3","#9932CC","#BA55D3","#EE82EE","#FF00FF","#FF1493","#FF69B4"]

        old_field = VGroup()
        old_label = TextMobject("")
        old_label.to_edge(LEFT+UP)
        for n in range(1,len(col)+1):
            gp = []
            for k in range(n):
                x = math.cos(2*k*math.pi/n)
                y = math.sin(2*k*math.pi/n)
                line = Line(np.array([0,0,0]),np.array([x*3.0,y*3.0,0]),color = col[k])
                gp.append(line)
            draw_field = VGroup(*gp)
            new_label = TextMobject("n = "+str(n))
            new_label.to_edge(LEFT+UP)

            if n*2 <= len(col)+1:
                self.play(Transform(old_field,draw_field),Transform(old_label,new_label),run_time = 0.1-0.1*(n/(len(col)+1)))
            else:
                self.play(Transform(old_field,draw_field),Transform(old_label,new_label),run_time = 0.1-0.1*(1-n/(len(col)+1)))         

        self.wait(5)

# ----------- Introduction of the video ----------------- #
class ThisVideo(Scene):
    def construct(self):
        text = MyText("而在这期视频中")
        text2 = MyText("我们会更加深入地挖掘复数中单位根这个主题")
        text3 = MyText("展示复数更多的几何性质")
        text4 = MyText("并为这个系列之后更难的内容做铺垫")
        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text,text2))
        self.wait(1)
        self.play(Transform(text,text3))
        self.wait(1)
        self.play(Transform(text,text4))
        self.wait(2)

# ----------- Introduction of the topics ----------------- #
class Intro_MoreProperty(Scene):
    def construct(self):

        circle = Circle(color=WHITE,radius=2.5)
        self.play(Write(circle),run_time = 0.05)

        up = MyText("并发现通过解析方法能使单位根构成的多边形旋转")
        up1 = MyText("或求某个单位根沿实轴对称后的复数")
        up2 = MyText("能发现一些恒定不变的规律如：")
        up3 = MyText("最后还会留下拓展思考题")
        up.to_edge(DOWN)
        up1.to_edge(DOWN)
        up2.to_edge(DOWN)
        up3.to_edge(DOWN)                                                   

        pt = []
        lab = []

# ------------- Write Polygon ----------------- #
        for k in range(5):
            pt.append(np.array([math.cos(2*k*math.pi/5)*2.5,math.sin(2*k*math.pi/5)*2.5,0]))
            lab.append(TexMobject(r"\varepsilon_{"+str(k)+"}"))

        poly = Polygon(pt[0],pt[1],pt[2],pt[3],pt[4],color=RED)

        for k in range(5):
            lab[k].next_to(pt[k],RIGHT)

        self.play(Write(poly),Write(lab[0]),Write(lab[1]),Write(lab[2]),Write(lab[3]),Write(lab[4]))

# ----------- Sum of Roots ----------------- #      
        self.play(Write(up2))
        vec = []
        for i in poly.get_vertices():
            vec.append(Vector(i))
        form = TexMobject(r"\sum{\varepsilon_{i}} = 0")
        form.to_edge(RIGHT+UP)
        self.play(Write(form),Write(vec[0]),Write(vec[1]),Write(vec[2]),Write(vec[3]),Write(vec[4]))
        self.wait(3)
        self.remove(vec[0],vec[1],vec[2],vec[3],vec[4])
# --------------- Rotation ------------------- #
        for k in range(5):
            self.add(lab[k])  
        line = Line(np.array([0,0,0]),pt[0],color=BLUE)
        init_line = Line(np.array([0,0,0]),np.array([2.5,0,0]))
        arc = Arc(angle=0,color=ORANGE)
        arc_label = TexMobject("\Theta")
        arc_label.next_to(arc)
        self.add(line,arc,arc_label)

        def update_arc(obj):
            ang = math.acos(poly.get_vertices()[0][0]/2.5)
            if poly.get_vertices()[0][1] < 0:
                ang = 2*PI-ang
            obj.become(Arc(start_angle=0,angle=ang,color=ORANGE))

        lab[0].add_updater(lambda obj: obj.next_to(poly.get_vertices()[0],RIGHT)) 
        lab[1].add_updater(lambda obj: obj.next_to(poly.get_vertices()[1],RIGHT))   
        lab[2].add_updater(lambda obj: obj.next_to(poly.get_vertices()[2],RIGHT))   
        lab[3].add_updater(lambda obj: obj.next_to(poly.get_vertices()[3],RIGHT))   
        lab[4].add_updater(lambda obj: obj.next_to(poly.get_vertices()[4],RIGHT))   
        line.add_updater(lambda obj: obj.put_start_and_end_on(np.array([0,0,0]),poly.get_vertices()[0]))   

        arc.add_updater(update_arc)
        arc_label.add_updater(lambda obj: obj.next_to(arc))

        self.add(line,arc,arc_label)      

        for k in range(5):
            self.add(lab[k])  

        self.play(Write(init_line))
        self.play(Rotating(poly,angle=PI/2,about_point=np.array([0,0,0])),Transform(up2,up))
        self.wait(1.5)
        self.remove(line,arc,arc_label,init_line)

# ----------------- Flip -------------------- #
        self.play(Transform(up2,up1))
        self.wait(1)

        ano_vec = Vector(np.array([poly.get_vertices()[1][0],-poly.get_vertices()[1][1],0]))

        self.play(Write(vec[1]))
        self.wait(2)
        self.play(Write(ano_vec))
        self.wait(2)
        self.remove(ano_vec,vec[1])

# ----------- Supplementary Information ----------------- # 
        form2 = TexMobject(r"\sum{|P\varepsilon_{i}|}")
        form2.to_edge(RIGHT+UP)

        rotate_dot = Dot(np.array([math.sqrt(2)/2.0*2.5,math.sqrt(2)/2.0*2.5,0]),color=RED)
        self.play(Transform(up2,up3),Transform(form,form2),Write(rotate_dot))
        
        Rotate_Line = []

        for k in range(5):
            Rotate_Line.append(Line(rotate_dot,pt[k],color=YELLOW))

        for k in range(5):
            self.add(Rotate_Line[k])

        P_label = TextMobject("P")
        P_label.next_to(rotate_dot)
        self.add(P_label)

        def P_func(obj):
            P_label.next_to(rotate_dot)
        def ro0(obj):  
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),pt[0])
        def ro1(obj):
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),pt[1])
        def ro2(obj):
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),pt[2])
        def ro3(obj):
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),pt[3])
        def ro4(obj):
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),pt[4])

        Rotate_Line[0].add_updater(ro0)
        Rotate_Line[1].add_updater(ro1)
        Rotate_Line[2].add_updater(ro2)
        Rotate_Line[3].add_updater(ro3)      
        Rotate_Line[4].add_updater(ro4)
        P_label.add_updater(P_func)

        for k in range(5):
            self.add(Rotate_Line[k])
        self.add(P_label)

        self.play(Rotating(rotate_dot,about_point=np.array([0,0,0]),angle=2*PI))
        self.wait(2)

        explan = MyText("介绍到此为止，那就让我们正式开始吧！")
        explan.to_edge(DOWN)
        self.play(Transform(up2,explan))
        self.wait(1)


# ------------- Junyun ----------------- #
class JunYun(Scene):
    def construct(self):
        circle = Circle(color=WHITE,radius=2.5)
        self.play(Write(circle),run_time = 0.05)

        text1 = MyText("我们在上个视频已经知道")

        text2 = MyText("第k个单位根在极坐标下的坐标为：")
        tex2  = TexMobject(r"(1,\frac{2k\pi}{n})")

        text3 = MyText("于是")
        text4 = MyText("也就是说")

        text5 = MyText("每两单位根之间夹角是：")
        tex5  = TexMobject(r"\frac{2\pi}{n}")

        text6 = MyText("由此可见，单位根在圆上均匀分布")
        text7 = VGroup(MyText("每个单位根"),TexMobject(r"\varepsilon_{k}"),MyText("也就等于"),TexMobject(r"\varepsilon_{1}"),MyText("旋转k次"))

        text8 = MyText("根据两个复数相乘，模相乘，幅角相加的原则")
        text9 = MyText("而且在单位圆上每个矢量模长为1，所以：")
        text10 = TexMobject(r"\varepsilon_{i} = \varepsilon_{1}^i")
        text11 = TexMobject(r"\varepsilon_{i}^{k} = (\varepsilon_{1}^i)^k = \varepsilon_{1}^{ik}")

        text12 = MyText("容易知道，")
        tex12  = TexMobject(r"\varepsilon_{i}^k = \varepsilon_{i}^{k\mod n}")
        text13 = MyText("举个例子，如")
        tex13  = TexMobject(r"\varepsilon_{1}^7")
        text14 = MyText("经过一圈后它回到了")
        tex14 =  TexMobject(r"\varepsilon_{2}")

        text7.arrange_submobjects(RIGHT/2)

        tex2.to_edge(DOWN)
        tex5.to_edge(DOWN)
        tex12.to_edge(DOWN)
        tex13.to_edge(DOWN)
        tex14.to_edge(DOWN)


        text1.to_edge(DOWN)
        text2.to_edge(DOWN)
        text3.to_edge(DOWN)
        text4.to_edge(DOWN)
        text5.to_edge(DOWN)
        text6.to_edge(DOWN)
        text7.to_edge(DOWN)
        text8.to_edge(DOWN)
        text9.to_edge(DOWN)   
        text10.to_edge(DOWN)       
        text11.to_edge(DOWN)
        text12.to_edge(DOWN)
        text13.to_edge(DOWN)
        text14.to_edge(DOWN)

        tex2.next_to(text2,RIGHT)
        tex5.next_to(text5,RIGHT)
        tex12.next_to(text12,RIGHT)
        tex13.next_to(text13,RIGHT)
        tex14.next_to(text14,RIGHT)


        place = []
        pt = []
        lab = []
        spare = TexMobject(r"")

        for k in range(5):
            place.append(np.array([math.cos(2*k*math.pi/5)*2.5,math.sin(2*k*math.pi/5)*2.5,0]))
        
        for k in range(5):
            pt.append(Dot(place[k],color=ORANGE))
            lab.append(TexMobject(r"\varepsilon_{"+str(k)+"}"))
        for k in range(5):
            lab[k].next_to(place[k])

        self.play(Write(pt[0]),Write(pt[1]),Write(pt[2]),Write(pt[3]),Write(pt[4]),
                  Write(lab[0]),Write(lab[1]),Write(lab[2]),Write(lab[3]),Write(lab[4]),Write(text1))
        self.wait(1)
        self.play(ReplacementTransform(text1,text2),Write(tex2))
        self.wait(1)
        spare.move_to(tex2)
        self.play(ReplacementTransform(text2,text3),Transform(tex2,spare))
        self.wait(0.5)

        # Add vectors
        vec = []
        for k in range(5):
            vec.append(Vector(place[k]))

        self.play(Write(vec[0]),Write(vec[1]),Write(vec[2]),Write(vec[3]),Write(vec[4]))

        # Add angles
        arc = []
        arc_label = []
        col = [BLUE,PURPLE,RED,ORANGE,GREEN]
        for k in range(5):
            arc.append(Arc(angle=2*PI*(k+1)/5,radius = 0.15+k/3.0,color = col[k]))

        self.play(Write(arc[0]),Write(arc[1]),Write(arc[2]),Write(arc[3]),Write(arc[4]))
        self.wait(2)
        self.remove(arc[0],arc[1],arc[2],arc[3],arc[4])

        for k in range(5):
            arc[k] = (Arc(start_angle=2*PI*k/5,angle=2*PI/5,radius = 0.35,color = col[k]))

        self.play(ReplacementTransform(text3,text4),Write(arc[0]),Write(arc[1]),Write(arc[2]),Write(arc[3]),Write(arc[4]))
        self.wait(1)
        self.play(ReplacementTransform(text4,text5),ReplacementTransform(tex2,tex5))
        self.wait(1)
        spare.move_to(tex5)
        self.play(ReplacementTransform(text5,text6),Transform(tex5,spare))
        self.wait(2)
        self.play(ReplacementTransform(text6,text7))
        self.wait(2)        
        self.play(ReplacementTransform(text7,text8))
        self.wait(2)
        self.play(ReplacementTransform(text8,text9))
        self.wait(2)
        self.play(ReplacementTransform(text9,text10))
        self.wait(2)
        self.play(ReplacementTransform(text10,text11))
        self.wait(2)
        self.play(ReplacementTransform(text11,text12),ReplacementTransform(tex5,tex12))
        self.wait(2)

        example_vector = Vector(np.array([2.5,0,0]),color=RED)

        self.play(ReplacementTransform(text12,text13),ReplacementTransform(tex12,tex13))
        self.wait(2)
        self.play(Rotating(example_vector,radians=72*7/180.0*PI,about_point=np.array([0,0,0])))
        self.play(ReplacementTransform(text13,text14),ReplacementTransform(tex13,tex14))
        self.wait(3)

# ----------- Sum of Roots --------------- #
class SumOfRoots(Scene):
    def construct(self):
        circle = Circle(color=WHITE,radius=2.5)

        text1 = MyText("有了以上的推论，我们很容易得到：")
        tex1  = TexMobject(r"\sum_{i=0}^{n-1}{\varepsilon_i} = \sum_{i=0}^{n-1}{\varepsilon_1^{i}}")

        text2 = MyText("根据等比数列求和公式，我们进一步有：")  
        tex2 = TexMobject(r"\sum_{i=0}^{n-1}{\varepsilon_i} = \frac{\varepsilon_{1}^{0}(1-\varepsilon_{1}^{n})}{1-\varepsilon_1}")

        text3 = MyText("而因为单位根的定义")
        tex3 = TexMobject(r"\varepsilon_{1}^{n} = 1")

        text4 = MyText("所以")
        tex4 = TexMobject(r"\sum_{i=0}^{n-1}{\varepsilon_i} = 0")

        text5 = MyText("同理")
        tex5  = TexMobject(r"\sum_{i=0}^{n-1}{\varepsilon_{1}^{-i}} = \frac{\varepsilon_{1}^{0}(1-\varepsilon_{1}^{-n})}{1-\varepsilon_{1}^{-1}} = 0")

        text6 = MyText("刚才的等比数列证明可能比较抽象")
        text7 = MyText("如果用感性的角度应该更加容易理解")
        text8 = MyText("可以将圆心看成整个图形的重心")

        text9 = VGroup(TexMobject(r"\varepsilon_i"),MyText("可以看成是向外拉扯的力"))

        text10 = MyText("因为力恰好均匀分布在不同的方向")
        text11 = MyText("因此最后互相抵消")

        text9.arrange_submobjects(RIGHT/2)

        text1.to_edge(UP+LEFT)
        text2.to_edge(UP+LEFT)
        text3.to_edge(UP+LEFT)
        text4.to_edge(UP+LEFT)
        text5.to_edge(UP+LEFT)
        text6.to_edge(UP+LEFT)
        text7.to_edge(UP+LEFT)
        text8.to_edge(UP+LEFT)
        text9.to_edge(UP+LEFT)
        text10.to_edge(UP+LEFT)
        text11.to_edge(UP+LEFT)

        tex1.to_edge(UP)
        tex2.to_edge(UP)
        tex3.to_edge(UP)
        tex4.to_edge(UP)
        tex5.to_edge(UP)

        tex1.next_to(text1,RIGHT)
        tex2.next_to(text2,RIGHT)
        tex3.next_to(text3,RIGHT)
        tex4.next_to(text4,RIGHT)

        pt = []
        lab = []
        dot = []

        for k in range(5):
            pt.append(np.array([math.cos(2*k*math.pi/5)*2.5,math.sin(2*k*math.pi/5)*2.5,0]))
            lab.append(TexMobject(r"\varepsilon_{"+str(k)+"}"))

        for k in range(5):
            lab[k].next_to(pt[k],RIGHT)
            dot.append(Dot(pt[k],color=RED))
        lab[1].shift(DOWN)

        self.play(Write(circle),Write(lab[0]),Write(lab[1]),Write(lab[2]),Write(lab[3]),Write(lab[4]),
                                Write(dot[0]),Write(dot[1]),Write(dot[2]),Write(dot[3]),Write(dot[4]),run_time = 0.05)
 
        self.play(Write(text1),Write(tex1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2),ReplacementTransform(tex1,tex2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3),ReplacementTransform(tex2,tex3))
        self.wait(3.5)
        self.play(ReplacementTransform(text3,text4),ReplacementTransform(tex3,tex4))
        self.wait(3.5)
        self.play(ReplacementTransform(text4,text5),ReplacementTransform(tex4,tex5))
        self.wait(3.5)
        noth = TexMobject(r"")
        noth.next_to(tex5)
        self.play(ReplacementTransform(text5,text6),Transform(tex5,noth))
        self.wait(1.5)       
        O = Dot(np.array([0,0,0]),color=YELLOW)
        O_Label = TexMobject("O")
        O_Label.next_to(O)
        self.play(ReplacementTransform(text6,text7),Write(O),Write(O_Label))
        self.wait(1.5)

        vec = []
        for i in pt:
            vec.append(Vector(i))

        self.play(Write(vec[0]),Write(vec[1]),Write(vec[2]),Write(vec[3]),Write(vec[4]),ReplacementTransform(text7,text8))
        self.wait(1.5)
        self.play(ReplacementTransform(text8,text9))
        self.wait(1.5)
        self.play(ReplacementTransform(text9,text10))
        self.wait(1.5)
        self.play(ReplacementTransform(text10,text11))
        self.wait(3)

class Sum_More(Scene):
    def construct(self):
        circle = Circle(color=WHITE,radius=2.5)
        self.play(Write(circle),run_time = 0.05)

        Text1 = MyText("当n,m互质时")
        Text2 = MyText("0, m, 2m, ... , (n-1)m恰好构成模n的完全剩余系")
        Text3 = VGroup(MyText("于是"),TexMobject(r"\sum_{i=0}^{n-1}{\varepsilon_i^m} = \sum_{i=0}^{n-1}{\varepsilon_{1}^{(i \times m) mod n}}"))
        Text4 = VGroup(MyText("于是"),TexMobject(r"\sum_{i=0}^{n-1}{\varepsilon_i^m} = \sum_{i=0}^{n-1}{\varepsilon_{1}^{i} = 1"))

        Text3.arrange_submobjects(RIGHT/2)
        Text4.arrange_submobjects(RIGHT/2)

        Text1.to_edge(UP)
        Text2.to_edge(UP)
        Text3.to_edge(UP)
        Text4.to_edge(UP)

        pt = []
        lab = []
        dot = []

        for k in range(5):
            pt.append(np.array([math.cos(2*k*math.pi/5)*2.5,math.sin(2*k*math.pi/5)*2.5,0]))
            lab.append(TexMobject(r"\varepsilon_{"+str(k)+"}"))

        for k in range(5):
            lab[k].next_to(pt[k],RIGHT)
            dot.append(Dot(pt[k],color=RED))
        lab[1].shift(DOWN)

        vec = []
        for i in pt:
            vec.append(Vector(i))

        self.play(Write(vec[0]),Write(vec[1]),Write(vec[2]),Write(vec[3]),Write(vec[4]),
                  Write(dot[0]),Write(dot[1]),Write(dot[2]),Write(dot[3]),Write(dot[4]),
                  Write(lab[0]),Write(lab[1]),Write(lab[2]),Write(lab[3]),Write(lab[4]))
        self.play(Write(Text1))
        self.wait(2)
        self.play(Transform(Text1,Text2))
        self.wait(4)
        self.play(Transform(Text1,Text3))
        self.wait(4)
        self.play(Transform(Text1,Text4))
        self.wait(2)       

# ------------- Rotation ----------------- #
class Self_Rotate(Scene):
    def construct(self):
        circle = Circle(color=WHITE,radius=2.5)
        self.play(Write(circle),run_time = 0.05)
        # Add why is Zheng Duo Bian Xing\
        text0 = MyText("正如上面所说单位根在圆上均匀分布")
        text0_1 = MyText("所以它所构成的多边形是正n边形")
        text1 = VGroup(MyText("容易知道，要实现这个正n边形旋转"),TexMobject(r"\Theta"))
        text2 = VGroup(MyText("只需要每个向量分别沿原点旋转"),TexMobject(r"\Theta"),MyText("即可"))
        text3 = VGroup(MyText("也就是每个向量乘上"),TexMobject(r"\omega(1,\Theta)"))
        text4 = VGroup(MyText("根据n次单位根的定义："),TexMobject(r"\varepsilon_i^n = 1"))
        text5 = TexMobject(r"(\varepsilon_i \cdot \omega)^n = \omega^n")
        text6 = VGroup(MyText("那么旋转后这些就变成了"),TexMobject("w^n"),MyText("的n次根"))

        text1.arrange_submobjects(RIGHT/2)
        text2.arrange_submobjects(RIGHT/2)       
        text3.arrange_submobjects(RIGHT/2)
        text4.arrange_submobjects(RIGHT/2)
        text6.arrange_submobjects(RIGHT/2)

        text0.to_edge(DOWN)
        text0_1.to_edge(DOWN)
        text1.to_edge(DOWN)
        text2.to_edge(DOWN)
        text3.to_edge(DOWN)
        text4.to_edge(DOWN)
        text5.to_edge(DOWN)
        text6.to_edge(DOWN)

        place = []
        pt = []
        lab = []

        for k in range(5):
            place.append(np.array([math.cos(2*k*math.pi/5)*2.5,math.sin(2*k*math.pi/5)*2.5,0]))
        
        for k in range(5):
            pt.append(Dot(place[k],color=ORANGE))
            lab.append(TexMobject(r"\varepsilon_{"+str(k)+"}"))

        self.play(Write(pt[0]),Write(pt[1]),Write(pt[2]),Write(pt[3]),Write(pt[4]),Write(text0))
        self.wait(2)
        self.play(Transform(text0,text0_1))
        self.wait(2)
        self.play(Transform(text0,text1))

        for k in range(5):
            self.add(lab[k])  

        line = Line(np.array([0,0,0]),pt[0],color=BLUE)
        init_line = Line(np.array([0,0,0]),np.array([2.5,0,0]),color=GREEN)

        arc = Arc(angle=0,color=ORANGE)
        arc_label = TexMobject(r"\Theta")
        arc_label.next_to(arc)
        self.add(line,arc,arc_label,init_line)

        def update_arc(obj):
            ang = math.acos(pt[0].get_x()/2.5)
            if pt[0].get_y() < 0:
                ang = 2*PI-ang
            obj.become(Arc(start_angle=0,angle=ang,color=ORANGE))

        lab[0].add_updater(lambda obj: obj.next_to(np.array([pt[0].get_x(),pt[0].get_y(),0]),RIGHT)) 
        lab[1].add_updater(lambda obj: obj.next_to(np.array([pt[1].get_x(),pt[1].get_y(),0]),RIGHT))   
        lab[2].add_updater(lambda obj: obj.next_to(np.array([pt[2].get_x(),pt[2].get_y(),0]),RIGHT))   
        lab[3].add_updater(lambda obj: obj.next_to(np.array([pt[3].get_x(),pt[3].get_y(),0]),RIGHT))   
        lab[4].add_updater(lambda obj: obj.next_to(np.array([pt[4].get_x(),pt[4].get_y(),0]),RIGHT))   
        line.add_updater(lambda obj: obj.put_start_and_end_on(np.array([0,0,0]),np.array([pt[0].get_x(),pt[0].get_y(),0])))  

        arc.add_updater(update_arc)
        arc_label.add_updater(lambda obj: obj.next_to(arc))

        self.add(line,arc,arc_label)      

        for k in range(5):
            self.add(lab[k])  

        self.play(Rotating(pt[0],radians = PI/5.0,about_point=np.array([0,0,0])),
                  Rotating(pt[1],radians = PI/5.0,about_point=np.array([0,0,0])),
                  Rotating(pt[2],radians = PI/5.0,about_point=np.array([0,0,0])),
                  Rotating(pt[3],radians = PI/5.0,about_point=np.array([0,0,0])),
                  Rotating(pt[4],radians = PI/5.0,about_point=np.array([0,0,0])),
                  Transform(text0,text2),run_time = 1)

        self.wait(2)
        poly = Polygon(np.array([pt[0].get_x(),pt[0].get_y(),0]),
                       np.array([pt[1].get_x(),pt[1].get_y(),0]),
                       np.array([pt[2].get_x(),pt[2].get_y(),0]),
                       np.array([pt[3].get_x(),pt[3].get_y(),0]),
                       np.array([pt[4].get_x(),pt[4].get_y(),0]),
                       color=RED)
        self.play(Write(poly))
        self.wait(2.5)
        self.play(Transform(text0,text3))
        self.play(Transform(lab[0],TexMobject(r"\varepsilon_0 \cdot \omega").next_to(pt[0])),
                  Transform(lab[1],TexMobject(r"\varepsilon_1 \cdot \omega").next_to(pt[1])),
                  Transform(lab[2],TexMobject(r"\varepsilon_2 \cdot \omega").next_to(pt[2])),
                  Transform(lab[3],TexMobject(r"\varepsilon_3 \cdot \omega").next_to(pt[3])),
                  Transform(lab[4],TexMobject(r"\varepsilon_4 \cdot \omega").next_to(pt[4])))
        self.wait(2.5)
        self.play(Transform(text0,text4))
        self.wait(2.5)
        self.play(Transform(text0,text5))
        self.wait(2.5)
        self.play(Transform(text0,text6))
        self.wait(3)

class Conjugate(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }

    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        Text0 = MyText("另外，要求单位根沿实轴对称后的复数值")
        Text1 = MyText("就等于求这个单位根的共轭复数")
        Text2 = MyText("共轭复数是指一对模(长度)相等，但幅角相反的复数")
        Text3 = MyText("举个例子如果有一个复数u")
        Text4 = VGroup(MyText("那么"),TexMobject(r"(1,-\frac{\pi}{3})"),MyText("就是u的共轭复数"))
        Text5 = VGroup(MyText("被称作"),TexMobject(r"\bar{u}"))
        Text6 = MyText("也很容易看出他们沿实轴对称")
        Text7 = VGroup(MyText("所以对于"),TexMobject(r"u(r,\Theta)"))
        Text8 = VGroup(MyText("它沿实轴对称后的值为"),TexMobject(r"\bar{u}(r,-\Theta)"))

        Text4.arrange_submobjects(RIGHT/2)
        Text5.arrange_submobjects(RIGHT/2)
        Text7.arrange_submobjects(RIGHT/2)
        Text8.arrange_submobjects(RIGHT/2)

        Text0.to_edge(DOWN)
        Text1.to_edge(DOWN)
        Text2.to_edge(DOWN)
        Text3.to_edge(DOWN)
        Text4.to_edge(DOWN)
        Text5.to_edge(DOWN)
        Text6.to_edge(DOWN)
        Text7.to_edge(DOWN)
        Text8.to_edge(DOWN)

        u = Vector(np.array([0.5,math.sqrt(3)/2.0]),color=RED)
        v = Vector(np.array([0.5,-math.sqrt(3)/2.0]),color=ORANGE)

        u_label = TexMobject(r"u(1,\frac{\pi}{3})",color=RED)
        v_label = TexMobject(r"\bar{u}(1,-\frac{\pi}{3})",color=ORANGE)

        u_label.next_to(u)
        v_label.next_to(v)
        v_label.shift(DOWN)

        self.play(Write(Text0))
        self.wait(2)
        self.play(Transform(Text0,Text1))
        self.wait(2)
        self.play(Transform(Text0,Text2))                
        self.wait(2)
        self.play(Transform(Text0,Text3),Write(u),Write(u_label))
        self.wait(2)
        self.play(Transform(Text0,Text4),Write(v))
        self.wait(2)
        self.play(Transform(Text0,Text5),Write(v_label))  
        self.wait(2)
        self.play(Transform(Text0,Text6))    
        self.wait(2)
        self.play(Transform(Text0,Text7))   
        self.wait(2)
        self.play(Transform(Text0,Text8))   
        self.wait(3)                                      

class Self_Flip(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }
    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        Text1 = MyText("对称和旋转也是差不多")
        Text2 = MyText("要实现这个多边形沿实轴对称")
        Text3 = MyText("只要每个单位根分别沿实轴对称即可")
        Text4 = MyText("如下：")

        Text1.to_edge(DOWN)
        Text2.to_edge(DOWN)
        Text3.to_edge(DOWN)
        Text4.to_edge(DOWN)

        pt = []
        lab = []
        dot = []

        pt_dc = []
        lab_dc = []
        dot_dc = []

        for k in range(5):
            pt.append(np.array([math.cos(2*k*math.pi/5)*2.5,math.sin(2*k*math.pi/5)*2.5,0]))
            pt_dc.append(np.array([math.cos(2*k*math.pi/5)*2.5,-math.sin(2*k*math.pi/5)*2.5,0]))

            lab.append(TexMobject(r"\varepsilon_{"+str(k)+"}",color=RED))
            lab_dc.append(TexMobject(r"\bar{\varepsilon}_{"+str(k)+"}",color=YELLOW))

        print(pt)
        print(pt_dc)

        for k in range(5):
            dot.append(Dot(pt[k],color=RED))
            dot_dc.append(Dot(pt_dc[k],color=YELLOW))
        for k in range(5):
            lab[k].next_to(dot[k])
            lab_dc[k].next_to(dot_dc[k])

        poly = Polygon(pt[0],pt[1],pt[2],pt[3],pt[4],color=RED)
        poly_dc = Polygon(pt_dc[0],pt_dc[1],pt_dc[2],pt_dc[3],pt_dc[4],color=YELLOW)

        for k in range(5):
            lab[k].next_to(pt[k],RIGHT)


        self.play(Write(Text1),Write(poly),Write(lab[0]),Write(lab[1]),Write(lab[2]),Write(lab[3]),Write(lab[4]),
                                           Write(dot[0]),Write(dot[1]),Write(dot[2]),Write(dot[3]),Write(dot[4]))
        self.wait(2)
        self.play(Transform(Text1,Text2))
        self.wait(2)
        self.play(Transform(Text1,Text3))       
        self.wait(2)
        self.play(Transform(Text1,Text4))
        self.play(Write(poly_dc),Write(lab_dc[0]),Write(lab_dc[1]),Write(lab_dc[2]),Write(lab_dc[3]),Write(lab_dc[4]),
                                 Write(dot_dc[0]),Write(dot_dc[1]),Write(dot_dc[2]),Write(dot_dc[3]),Write(dot_dc[4]))

        

class Exercise(Scene):
    def construct(self):
        text1 = MyText("最后给大家留了几道思考题以供练习")
        text1.to_edge(DOWN)
        question1 = VGroup(MyText("1. 有两个复数"),TexMobject(r"u,v,"),MyText("而"),TexMobject(r"\varepsilon_i \text{,} \var_i"),
        MyText("分别是"),TexMobject("u^n,v^n"),MyText("的n次根，"))
        
        question1_2 = VGroup(MyText("请问"),
        TexMobject(r"\angle \varepsilon_i O \var_i"),MyText("等于多少？"))

        question2 = MyText("2. a次单位根与b次单位根有多少个共同根？")
        question3 = MyText("3. 如何用解析式描述沿直线对称变换后的单位根？")

        question4 = VGroup(MyText("4. 对于n次单位根"),TexMobject(r"\varepsilon_{i} \text{, } \sum_{0}^{n-1}{|P\varepsilon_{i}|^2}"),MyText("的值是否与P的位置无关"))
        question5 = VGroup(TexMobject(r"\text{5}^{*}\text{.}"),MyText("对于n次单位根"),TexMobject(r"\varepsilon_{i}"),MyText(", 若"),TexMobject(r"\sum_{0}^{n-1}{|P\varepsilon_{i}|^{k}}"),MyText("的值与P的位置无关"))
        question5_2 = MyText("求k的取值范围")

        question1.arrange_submobjects(RIGHT/2)
        question1_2.arrange_submobjects(RIGHT/2)
        question4.arrange_submobjects(RIGHT/2)        
        question5.arrange_submobjects(RIGHT/2)

        question1.to_edge(UP+RIGHT)
        question1_2.to_edge(UP+RIGHT)
        question1_2.shift(0.65*DOWN)
        question2.to_edge(UP+RIGHT)
        question3.to_edge(UP+RIGHT)
        question4.to_edge(UP+RIGHT)
        question5.to_edge(UP+RIGHT)  
        question5_2.to_edge(UP+RIGHT)
        question5_2.shift(DOWN)

        circle = Circle(color=WHITE,radius=2.5)
        self.play(Write(circle),run_time = 0.05)
        self.play(Write(text1))
        self.wait(2)
        self.remove(text1)

# --------- Question 1 ---------------------#
        place3 = []
        dot3 = []
        dot3_label = []
        dot3_rotate = []
        dot3_rotate_label = []

        for k in range(3):
            place3.append(np.array([math.cos(2*k*math.pi/3)*2.5,math.sin(2*k*math.pi/3)*2.5,0]))

        for k in range(3):
            dot3.append(Dot(place3[k],color=RED))
            dot3_label.append(TexMobject(r"\varepsilon_{"+str(k)+r"}",color=RED))
        for k in range(3):
            dot3_label[k].next_to(dot3[k])

        poly = Polygon(place3[0],place3[1],place3[2],color=RED)

        poly_rotate = Polygon(place3[0],place3[1],place3[2],color=BLUE)
        poly_rotate.rotate(PI/5.0,about_point=np.array([0,0,0]))

        for k in range(3):
            dot3_rotate_label.append(TexMobject(r"\var_{"+str(k)+r"}",color=BLUE))
        for k in range(3):
            dot3_rotate.append(Dot(poly_rotate.get_vertices()[k],color=BLUE))
            dot3_rotate_label[k].next_to(poly_rotate.get_vertices()[k])
        
        Centre = Dot(np.array([0,0,0]))
        Centre_label = TexMobject("O")
        Centre_label.next_to(Centre)

        arc = Arc(start_angle = PI+math.atan(place3[1][1]/place3[1][0]), angle = math.atan(dot3_rotate[1].get_y()/dot3_rotate[1].get_x())-math.atan(place3[1][1]/place3[1][0]),color=ORANGE)

        L1 = Line(np.array([0,0,0]),np.array([dot3[1].get_x(),dot3[1].get_y(),0]),color=YELLOW)
        L2 = Line(np.array([0,0,0]),np.array([dot3_rotate[1].get_x(),dot3_rotate[1].get_y(),0]),color=YELLOW)

        self.play(Write(question1),
                  Write(poly),
                  Write(dot3[0]),Write(dot3[1]),Write(dot3[2]),
                  Write(dot3_label[0]),Write(dot3_label[1]),Write(dot3_label[2]),
                  Write(poly_rotate),
                  Write(dot3_rotate_label[0]),Write(dot3_rotate_label[1]),Write(dot3_rotate_label[2]),
                  Write(dot3_rotate[0]),Write(dot3_rotate[1]),Write(dot3_rotate[2]),
                  Write(Centre),Write(Centre_label))

        self.play(Write(question1_2),Write(L1),Write(L2),Write(arc))
        self.wait(10)
        self.remove(L1,L2,arc,poly_rotate,dot3_rotate[0],dot3_rotate[1],dot3_rotate[2],dot3_rotate_label[0],dot3_rotate_label[1],dot3_rotate_label[2],
                    dot3_label[0],dot3_label[1],dot3_label[2],question1,question1_2)
# --------- Question 2 ---------------------#
        place6 = []
        dot6 = []
        dot6_label = []

        for k in range(6):
            place6.append(np.array([math.cos(2*k*math.pi/6)*2.5,math.sin(2*k*math.pi/6)*2.5,0]))

        for k in range(6):
            dot6.append(Dot(place6[k],color=BLUE))

        poly6 = Polygon(place6[0],place6[1],place6[2],place6[3],place6[4],place6[5],color=BLUE)
        self.play(Write(poly6),Write(dot6[0]),Write(dot6[1]),Write(dot6[2]),Write(dot6[3]),Write(dot6[4]),Write(dot6[5]))
        self.wait(2)
        self.play(Write(question2))
        self.wait(10)

        self.remove(poly6,dot6[0],dot6[1],dot6[2],dot6[3],dot6[4],dot6[5],question2)
# --------- Question 3 ---------------------#
        poly3_inver = Polygon(np.array([dot3[0].get_y(),dot3[0].get_x(),0]),
                              np.array([dot3[1].get_y(),dot3[1].get_x(),0]),
                              np.array([dot3[2].get_y(),dot3[2].get_x(),0]),
                              color=BLUE)
        line_duicheng = Line(np.array([-5,-5,0]),np.array([5,5,0]),color=YELLOW)
        line_label =  TexMobject("y = kx")
        line_label.next_to(line_duicheng)
        line_label.shift(UP+LEFT)

        dot3_inver = [Dot(np.array([dot3[0].get_y(),dot3[0].get_x(),0]),color=BLUE),Dot(np.array([dot3[1].get_y(),dot3[1].get_x(),0]),color=BLUE),Dot(np.array([dot3[2].get_y(),dot3[2].get_x(),0]),color=BLUE)]
        
        self.play(Write(line_duicheng),Write(line_label),Write(question3))
        self.wait(2)

        self.play(Write(poly3_inver),Write(dot3_inver[0]),Write(dot3_inver[1]),Write(dot3_inver[2]))
        self.wait(10)
# --------- Question 4 ---------------------#     
        self.remove(question3,poly3_inver,dot3_inver[0],dot3_inver[1],dot3_inver[2],line_duicheng,line_label)   

        rotate_dot = Dot(np.array([math.sqrt(2)/2.0*2.5,math.sqrt(2)/2.0*2.5,0]),color=RED)
        self.play(Write(rotate_dot))
        
        Rotate_Line = []

        for k in range(3):
            Rotate_Line.append(Line(rotate_dot,dot3[k],color=YELLOW))

        for k in range(3):
            self.add(Rotate_Line[k])

        P_label = TextMobject("P")
        P_label.next_to(rotate_dot)
        self.add(P_label)

        def P_func(obj):
            P_label.next_to(rotate_dot)
        def ro0(obj):  
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),place3[0])
        def ro1(obj):
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),place3[1])
        def ro2(obj):
            obj.put_start_and_end_on(np.array([rotate_dot.get_x(),rotate_dot.get_y(),rotate_dot.get_z()]),place3[2])

        Rotate_Line[0].add_updater(ro0)
        Rotate_Line[1].add_updater(ro1)
        Rotate_Line[2].add_updater(ro2)
        P_label.add_updater(P_func)

        for k in range(3):
            self.add(Rotate_Line[k])
        self.add(P_label)

        dot3_label[1].shift(LEFT)
        self.play(Write(question4),Write(dot3_label[0]),Write(dot3_label[1]),Write(dot3_label[2]))        
        self.play(Rotating(rotate_dot,about_point=np.array([0,0,0]),angle=2*PI))
        self.wait(2)

        self.remove(question4)
        self.play(Write(question5),Write(question5_2))
        self.wait(8)

class Final(Scene):
    def construct(self):
        Text1 = MyText("思考题的解法将在下期视频公布")
        Text2 = MyText("如果想和其他数学爱好者一起分享讨论")
        Text3 = MyText("可以加交流群726542042")

        self.play(Write(Text1))
        self.wait(1.5)
        self.play(Transform(Text1,Text2))
        self.wait(1.5)
        self.play(Transform(Text1,Text3))
        self.wait(1.5)

class First(Scene):
    def construct(self):
        Text4 = MyText("祝三连这个视频的今年好运不停！")
        self.play(Write(Text4))
        self.wait(3)





# ----------- Introduction of polar representation (Not used)  ----------------- #      
class intro_PolarMean(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }
    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        circle = Circle(color=WHITE,radius=3)
        self.play(Write(circle),run_time = 0.05)

        up = VGroup(MyText("我们将理解"),TexMobject("e^{ki}"),MyText("在极坐标下的意义"))
        up.arrange_submobjects(RIGHT/2)
        up.to_edge(UP)
        self.play(Write(up))
        
        line = Line(np.array([0,0,0]),np.array([3,0,0]),color=BLUE)

        label = TexMobject("e^{i*0}")
        label.to_edge(UP+LEFT)
        self.add(label)

        def label_updater(obj):
            point = line.get_points_defining_boundary()[1]
            if point[1] == 1:
                val = PI/2
            elif point[1] == -1:
                val = 1.5*PI
            else:
                val = round(math.atan(point[1]/point[0]),1)

            if point[0] < 0:
                val += PI
            elif point[1] < 0:
                val += 2*PI
            
            val = round(val,1)
            obj.become(TexMobject("e^{"+str(val)+"i}"))
            obj.to_edge(UP+LEFT)

        label.add_updater(label_updater)
        self.add(label)

        self.play(Rotating(line,about_point=np.array([0,0,0]),angle=2*PI))

# ----------- Applications in polynomials (not covered in this video) ----------------- #      
class intro_Polyno(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "y_min" : -10,
        "y_max" : 10,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-5,5,2),
    }

    def construct(self):
        self.setup_axes(animate = True)

        self.func = lambda x: pow(x,7)-21*pow(x,5)+35*pow(x,3)-7*x

        func_graph = self.get_graph(self.func, self.function_color)

        graphlab = self.get_graph_label(func_graph, label = r"f(x)=x^7-21x^5+35x^3-7x", x_val = -10, direction = UP/2)

        up = MyText("最后，讨论单位根在求函数零点的应用")
        up.to_edge(UP)
        root_one = Dot(self.coords_to_point(-4.381286,0),color=YELLOW)
        root_two = Dot(self.coords_to_point(-0.481525,0),color=YELLOW)
        root_thr = Dot(self.coords_to_point(0,0),color=YELLOW)
        root_fur = Dot(self.coords_to_point(0.481525,0),color=YELLOW)
        root_fve = Dot(self.coords_to_point(-1.253960,0),color=YELLOW)
        root_six = Dot(self.coords_to_point(1.253960,0),color=YELLOW)
        root_sen = Dot(self.coords_to_point(4.381286,0),color=YELLOW)

        Triangle
        self.play(Write(func_graph),Write(graphlab))
        self.wait(1)
        self.play(Write(up),Write(root_one),
                  Write(root_two),Write(root_thr),
                  Write(root_fur),Write(root_fve),
                  Write(root_six),Write(root_sen))
        self.wait(2)