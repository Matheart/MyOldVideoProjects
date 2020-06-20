from manimlib.imports import *
#[禁止套娃]谈常见数的连分数表示

class MyText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
    }

class Begin(Scene):
    def construct(self):
        text1 = VGroup(MyText("我们在幼儿园就学过"),MyText("三角函数",color=RED)).arrange_submobjects(RIGHT/2).to_edge(UP)
        text2 = VGroup(MyText("也学过圆周率"),TexMobject(r"\pi",color=BLUE)).arrange_submobjects(RIGHT/2).to_edge(UP)
        text3 = VGroup(MyText("和可爱的"),TexMobject(r"e^x",color=YELLOW)).arrange_submobjects(RIGHT/2).to_edge(UP)
        text4 = VGroup(MyText("接下来我们来看看它们的"),MyText("连分数",color=ORANGE).scale(2),MyText("表示")).arrange_submobjects(RIGHT/2)

        A = np.array([-2,-3,0])
        B = np.array([3,-3,0])
        C = np.array([-2,2,0])
        A_label = TexMobject("A")
        B_label = TexMobject("B")
        C_label = TexMobject("C")
        a_label = TexMobject("a")
        b_label = TexMobject("b")
        c_label = TexMobject("c")

        tri = MyTriangle(A, B, C)
        ang1, ang2, ang3 = tri.get_three_angle()

        formula1_1 = TexMobject(r"\sin \theta = \frac{b}{a}")
        formula1_2 = TexMobject(r"\cos \theta = \frac{c}{a}")
        formula1_3 = TexMobject(r"\tan \theta = \frac{b}{c}")
        arc = Arc(start_angle = PI - ang2, angle = ang2,radius = 1).move_arc_center_to(B)
        arc_label = TexMobject(r"\theta")

        self.play(Write(text1),Write(tri),
                  Write(A_label.next_to(A,DOWN)),
                  Write(B_label.next_to(B)),
                  Write(C_label.next_to(C,UP)))
        self.play(Write(a_label.next_to(np.array([0.5,-0.5,0]),UP+RIGHT)),
                  Write(b_label.next_to(np.array([-2,-0.5,0]),LEFT)),
                  Write(c_label.next_to(np.array([0.5,-3,0]),0.5*DOWN)),
                  Write(arc),
                  Write(arc_label.next_to(arc,LEFT)))
        self.play(Write(formula1_1.to_edge(RIGHT+UP)),
                  Write(formula1_2.next_to(formula1_1,DOWN)),
                  Write(formula1_3.next_to(formula1_2,DOWN)))

        self.wait(1)
        self.remove(A_label,B_label,C_label,a_label,b_label,c_label,arc,arc_label)
        vg_formula = VGroup(formula1_1,formula1_2,formula1_3)
        # pi

        circle = Circle(radius = 2.5)
        formula2_1 = TexMobject(r"S_{Circle} = ",r"\pi",r" r^2").to_edge(UP+RIGHT)
        formula2_1.set_color_by_tex_to_color_map({
            r"\pi" : BLUE,
        })

        vg2_1 = VGroup(circle,formula2_1)

        formula2_2 = TexMobject(r"\frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \cdots = ",r"{\pi^2",r"\over 6}")
        formula2_2.set_color_by_tex_to_color_map({
            r"\pi" : BLUE,
        })

        formula2_3 = MyText("巴塞尔问题").to_edge(UP+RIGHT)

        self.play(ReplacementTransform(text1,text2),ReplacementTransform(tri, circle),ReplacementTransform(vg_formula,formula2_1))
        self.wait(1.5)
        self.play(ReplacementTransform(circle,formula2_2),ReplacementTransform(formula2_1,formula2_3))
        self.wait(2.5)
        formula3_1 = TexMobject(r"\lim_{x\to\infty} (1+\frac{x}{n})^n = ",r"e^x")
        formula3_1.set_color_by_tex_to_color_map({
            r"e^x" : YELLOW,
        })        
        self.remove(formula2_3)
        self.play(ReplacementTransform(text2,text3),ReplacementTransform(formula2_2,formula3_1))
        self.wait(1)
        self.remove(formula3_1)
        self.play(ReplacementTransform(text3,text4))
        self.wait(2)

class Introduction(Scene):
    def construct(self):
        text1 = MyText("正所谓连分数，就是以下形式的分数：").to_edge(UP+LEFT)
        text2 = MyText("在将初等函数用连分数表示之前，要先介绍").to_edge(UP+LEFT)
        text3 = MyText("欧拉连分数公式",color=RED).to_edge(UP).next_to(text2,RIGHT)
        text4 = MyText("证明：").to_edge(UP+LEFT)

        text1[3:6].set_color(ORANGE)
        tex1 = TexMobject(r"x = a_0 + \cfrac{1}{a_1+\cfrac{1}{a_2+\cfrac{1}{a_3+\cfrac{1}{a_4+\cfrac{1}{a_5+\cfrac{1}{a_6+\cdots}}}}}}")
        
        tex2 = TexMobject(r"a_0+a_0a_1+a_0a_1a_2+ \cdots +a_0a_1a_2\cdots a_n\
             = \cfrac{a_0}{1-\cfrac{a_1}{\
                                      1+a_1-\cfrac{a_2}{\
                                                       1+a_2-\cfrac{\
                                                                    \cdots}{\cdots \cfrac{\
                                                                                         a_{n-1}}{1+a_{n-1}-\cfrac{a_n}{1+a_n\
                                                                                        }\
                                                                   }\
                                                      }\
                                       }").scale(0.6*0.6)
        self.play(Write(text1),Write(tex1))
        self.wait(1)

        self.play(ReplacementTransform(text1,VGroup(text2,text3)))
        self.wait(1)
        self.play(FadeOut(text2),ApplyMethod(text3.shift,5.5*LEFT),ReplacementTransform(tex1,tex2))
        self.wait(1.5)
        self.play(ReplacementTransform(text3,text4),ApplyMethod(tex2.scale,0.4),ApplyMethod(tex2.to_edge,RIGHT+UP))
        self.wait(1.5)

        prove_s_1 = VGroup(MyText("令",color=YELLOW),TexMobject(r"s_i = a_i + a_{i}a_{i+1} + a_{i}a_{i+1}a_{i+2} + \cdots + a_{i}a_{i+1}\cdots a_{n}",color=YELLOW)).arrange_submobjects(RIGHT/2).scale(0.45).to_edge(LEFT+UP).shift(DOWN)
        prove_s_1_bg = SurroundingRectangle(prove_s_1, fill_color = BLUE, fill_opacity = .2)

        prove_s_2 = VGroup(MyText("那么",color=YELLOW).to_edge(LEFT),TexMobject(r"s_{i+1} = \text{     } a_{i+1} + \text{  } a_{i+1}a_{i+2} + \cdots + \text{  } a_{i+1} \cdots a_{n}",color=YELLOW)).to_edge(LEFT).arrange_submobjects(RIGHT/2).next_to(prove_s_1,DOWN).scale(0.45)
        prove_s_2_bg = SurroundingRectangle(prove_s_2, fill_color = RED, fill_opacity = .2)

        prove_s_3 = TexMobject(r"s_0 = a_0 + a_0 a_1 + a_0 a_1 a_2 + \cdots + a_0 a_1 \cdots a_n",color=YELLOW).to_edge(LEFT).next_to(prove_s_2,DOWN).scale(0.45)
        prove_s_3_bg = SurroundingRectangle(prove_s_3, fill_color = RED, fill_opacity = .2)

        not_diff = MyText("不难得到",color=YELLOW)
        zhong = TexMobject(r"s_{i} = a_i (1 + ",color=YELLOW)
        la = TexMobject(r"(a_{i+1} + a_{i+1}a_{i+2} + \cdots))",color=YELLOW)
        prove_s_4 = VGroup(not_diff,zhong,la).to_edge(LEFT).arrange_submobjects(RIGHT/2).next_to(prove_s_3,DOWN).scale(0.45)
        la_bg = SurroundingRectangle(la, fill_color = RED, fill_opacity = .2)

        self.play(Write(prove_s_1))
        self.wait(1)
        self.play(Write(prove_s_2))
        self.wait(2)
        self.play(Write(prove_s_3))
        self.wait(1.5)
        self.play(Write(prove_s_1_bg))
        self.wait(2)
        self.play(Write(prove_s_4))
        self.wait(2)
        self.remove(prove_s_1_bg)
        self.play(Write(prove_s_2_bg),Write(la_bg))
        self.wait(3)
        self.remove(la_bg)
        self.play(ReplacementTransform(la, TexMobject("s_{i+1})",color=YELLOW).scale(0.45).next_to(zhong,RIGHT/2)))
        la_vg = VGroup(zhong,la)
        la_vg_bg = SurroundingRectangle(la_vg, fill_color = RED, fill_opacity = .2)

        self.remove(prove_s_2_bg)
        self.wait(2)
        
        eq = TexMobject(r"=",color=BLUE)
        prove_f_1 = VGroup(TexMobject(r"\frac{s_i}{1+s_i}",color=BLUE),eq,TexMobject(r"\frac{a_i(1+s_{i+1})}{1+s_i}",color=BLUE)).arrange_submobjects(RIGHT/2).scale(0.6).to_edge(LEFT)
        
        prove_f_2 = TexMobject(r"=\frac{a_i}{\frac{1+s_i}{1+s_{i+1}}}",color=BLUE).scale(0.6).next_to(prove_f_1,0.2*DOWN).align_to(eq,LEFT)
        prove_f_3 = TexMobject(r"=\frac{a_i}{\frac{1+a_i(1+s_{i+1})}{1+s_{i+1}}}",color=BLUE).scale(0.6).next_to(prove_f_2,0.2*DOWN).align_to(eq,LEFT)
        prove_f_4 = TexMobject(r"=\frac{a_i}{\frac{(1+s_{i+1})+a_i(1+s_{i+1})}{1+s_{i+1}} - \frac{s_{i+1}}{1+s_{i+1}}}",color=BLUE).scale(0.6).next_to(prove_f_3,0.2*DOWN).align_to(eq,LEFT)
        prove_f_5 = TexMobject(r"=\frac{a_i}{1+a_{i}-\frac{s_{i+1}}{1+s_{i+1}}}",color=BLUE).scale(0.6).next_to(prove_f_4,0.2*DOWN).align_to(eq,LEFT)
        
   
        eq_fi = TexMobject(r"=",color=RED)
        final1 = TexMobject(r"a_0+a_0a_1+a_0a_1a_2+ \cdots +a_0a_1a_2\cdots a_n",color=RED).scale(0.6).shift(2*UP+1.5*RIGHT)
        final2 = VGroup(eq_fi,TexMobject(r"s_0",color=RED)).arrange_submobjects(RIGHT/2).scale(0.6).next_to(final1,0.2*DOWN).align_to(final1,LEFT)
        final3 = TexMobject(r"=a_0(1+s_1)",color=RED).scale(0.6).next_to(final2,0.2*DOWN).align_to(eq_fi,LEFT)
        final4 = TexMobject(r"=\frac{a_0}{\frac{1}{1+s_1}}",color=RED).scale(0.6).next_to(final3,0.2*DOWN).align_to(eq_fi,LEFT)
        final5 = TexMobject(r"=\frac{a_0}{1-\frac{s_1}{1+s_1}}",color=RED).scale(0.6).next_to(final4,0.2*DOWN).align_to(eq_fi,LEFT)
        
        final6 = TexMobject(r"=\cfrac{a_0}{1-\cfrac{a_1}{1+a_1-\cfrac{s_2}{1+s_2}}}",color=RED).scale(0.45*1.5).next_to(final5,0.2*DOWN).align_to(eq_fi,LEFT)        
        final7 = TexMobject(r"=\cfrac{a_0}{1-\cfrac{a_1}{1+a_1-\cfrac{a_2}{1+a_2-\cfrac{s_3}{1+s_3}}}}",color=RED).scale(0.45*1.5).next_to(final5,0.2*DOWN).align_to(eq_fi,LEFT)
        final8 = TexMobject(r"=\cfrac{a_0}{1-\cfrac{a_1}{\
                                      1+a_1-\cfrac{a_2}{\
                                                       1+a_2-\cfrac{\
                                                                    \cdots}{\cdots \cfrac{\
                                                                                         a_{n-1}}{1+a_{n-1}-\cfrac{a_n}{1+a_n\
                                                                                        }\
                                                                   }\
                                                      }\
                                       }",color=RED).scale(0.45*1.25).next_to(final5,0.2*DOWN).align_to(eq_fi,LEFT)


        self.play(Write(final1))
        self.play(Write(prove_s_3_bg))
        self.wait(1.5)
        self.play(Write(final2))
        self.wait(1.5)
        self.remove(prove_s_3_bg)
        self.play(Write(final3))
        self.wait(1.5)
        self.play(Write(final4))
        self.wait(1.5)
        self.play(Write(final5))
        self.wait(1.5)

        self.play(Write(la_vg_bg))
        self.play(Write(prove_f_1))
        self.wait(1)
        self.play(Write(prove_f_2))
        self.wait(1.5)   
        self.play(Write(prove_f_3))
        self.wait(2.5)
        self.remove(la_vg_bg)
        self.play(Write(prove_f_4))
        self.wait(2.5)
        self.play(Write(prove_f_5))
        self.wait(1.5)
        self.remove(prove_f_2,prove_f_3,prove_f_4)
        self.play(ApplyMethod(prove_f_5.scale,1.5))
        self.play(ApplyMethod(prove_f_5.shift, 1.5*UP))
        self.play(ApplyMethod(prove_f_5.align_to,eq,LEFT))

        prove_f_5_bg = SurroundingRectangle(prove_f_5, color=BLUE, fill_color = PURPLE, fill_opacity = .2)
        self.play(Write(prove_f_5_bg))

        self.wait(1)
        self.play(Write(final6))
        self.wait(1.5)
        self.play(ReplacementTransform(final6,final7))
        self.wait(1.5)
        self.play(ReplacementTransform(final7,final8))
        self.wait(2)

class Inf(Scene):
    def construct(self):
        text1 = MyText("由以上这条公式，容易得知，当n趋向无穷时:").to_edge(UP)
        tex1 = TexMobject(r"a_0+a_0a_1+a_0a_1a_2+ \cdots +a_0a_1a_2\cdots\
                    = \cfrac{a_0}{1-\cfrac{a_1}{\
                                            1+a_1-\cfrac{a_2}{\
                                                            1+a_2-\cfrac{\
                                                                            a_3}{1+a_3- \cfrac{\
                                                                                                a_{4}}{1+a_{4}-\cdots\
                                                                        }\
                                                            }\
                                            }",color=ORANGE).scale(0.65*0.6).next_to(text1,DOWN)

        self.play(Write(text1))
        self.play(Write(tex1))
        self.wait(2)
        self.play(FadeOut(text1),ApplyMethod(tex1.to_edge,UP))
        tex1_bg = SurroundingRectangle(tex1, fill_color = RED, fill_opacity = .1)

        so = MyText("所以泰勒展开后：")
        eq = TexMobject(r"=")

        for1 = VGroup(so,TexMobject(r"e^x"),eq,TexMobject(r"1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots")).arrange_submobjects(RIGHT/2).scale(0.65).to_edge(UP+LEFT).shift(2*DOWN)
        for2 = TexMobject(r"= 1 + x + 1 \cdot x \cdot \frac{x}{2} + 1 \cdot x \cdot \frac{x}{2} \cdot \frac{x}{3} + \cdots").scale(0.65).next_to(for1,0.2*DOWN).align_to(eq,LEFT)
        for3 = TexMobject(r"= \cfrac{1}{1-\cfrac{x}{1+x-\cfrac{\frac{1}{2}x}{1+\frac{1}{2}x-\cfrac{\frac{1}{3}x}{1+\frac{1}{3}x-\cdots}}}}").scale(0.65*0.6).next_to(for2,0.2*DOWN).align_to(eq,LEFT) 
        for4 = TexMobject(r"= \cfrac{1}{1-\cfrac{x}{1+x-\cfrac{x}{2+x-\cfrac{\frac{2}{3}x}{1+\frac{1}{3}x-\cdots}}}}").scale(0.65*0.6).next_to(for3,0.2*DOWN).align_to(eq,LEFT) 
        for5 = TexMobject(r"= \cfrac{1}{1-\cfrac{x}{1+x-\cfrac{x}{2+x-\frac{2x}{3+x-\cdots}}}}").scale(0.65*0.6).next_to(for3,0.2*DOWN).align_to(eq,LEFT) 
        self.play(Write(for1))
        self.wait(1.5)
        self.play(Write(for2))
        self.play(Write(tex1_bg))
        self.wait(2)
        self.play(Write(for3))
        self.wait(1.5)
        self.play(Write(for4))
        self.wait(2.5)
        self.play(ReplacementTransform(for4,for5))
        self.wait(2.5)
        self.remove(tex1_bg,for1,for2,for3,for5)

        sin1 = VGroup(MyText("同理"),TexMobject(r"\sin x"),eq,TexMobject(r"x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots")).arrange_submobjects(RIGHT/2).scale(0.65).to_edge(UP+LEFT).shift(1.5*DOWN)
        sin2 = TexMobject(r"= x + (x)(\frac{-x^2}{2\cdot 3}) + (x)(\frac{-x^2}{2\cdot 3})(\frac{-x^2}{4\cdot 5})+ (x)(\frac{-x^2}{2\cdot 3})(\frac{-x^2}{4\cdot 5})(\frac{-x^2}{6\cdot 7})").scale(0.65).next_to(sin1,0.2*DOWN).align_to(eq,LEFT)
        sin3 = TexMobject(r"=\cfrac{x}{1-\cfrac{\frac{-x^2}{2\cdot 3}}{1+\frac{-x^2}{2\cdot 3}-\cfrac{\frac{-x^2}{4\cdot 5}}{1+\frac{-x^2}{4\cdot 5}-\cdots}}}").scale(0.65*0.6).next_to(sin2,0.2*DOWN).align_to(eq,LEFT)
        sin4 = TexMobject(r"=\cfrac{x}{1+\cfrac{x^2}{2\cdot 3 - x^2 + \frac{2\cdot 3x^2}{4\cdot 5 - x^2 + \cdots}}}").scale(0.65*0.6).next_to(sin3,0.2*DOWN).align_to(eq,LEFT)
        self.play(Write(sin1))
        self.play(Write(sin2))
        self.wait(1.5)
        self.play(Write(sin3))
        self.wait(1.5)
        self.play(Write(sin4))
        self.wait(2.5)
        self.remove(sin1,sin2,sin3,sin4)

        eq = TexMobject(r"=")
        tan1 = VGroup(TexMobject(r"\tan^{-1}x"),eq,TexMobject(r"x-\frac{x^3}{3}+\frac{x^5}{5}-\frac{x^7}{7}+\cdots")).arrange_submobjects(RIGHT/2).scale(0.65).to_edge(UP+LEFT).shift(1.5*DOWN)
        tan2 = TexMobject(r"=x+x(\frac{-x^2}{3})+x(\frac{-x^2}{3})(\frac{-3x^2}{5})+x(\frac{-x^2}{3})(\frac{-3x^2}{5})(\frac{-5x^2}{7})").scale(0.65).next_to(tan1,0.2*DOWN).align_to(eq,LEFT)
        tan3 = TexMobject(r"=\cfrac{x}{1-\cfrac{\frac{-x^2}{3}}{1+\frac{-x^2}{3}-\cfrac{\frac{-3x^2}{5}}{1+\frac{-3x^2}{5}-\cdots}}}").scale(0.65*0.6).next_to(tan2,0.2*DOWN).align_to(eq,LEFT)
        tan4 = TexMobject(r"=\cfrac{x}{1+\cfrac{x^2}{3-x^2+\cfrac{(3x)^2}{5-3x^2+\frac{(5x)^2}{7-5x^2+\cdots}}}}").scale(0.65*0.6).next_to(tan3,0.2*DOWN).align_to(eq,LEFT)
        self.play(Write(tan1))
        self.play(Write(tan2))
        self.wait(1.5)
        self.play(Write(tan3))
        self.wait(1.5)
        self.play(Write(tan4))
        self.wait(2.5)
        te = VGroup(MyText("特别地，当",color=BLUE), TexMobject(r"x=1, \tan^{-1} x = \frac{\pi}{4}",color=BLUE)).arrange_submobjects(RIGHT/2).scale(0.65).next_to(tan4,0.2*DOWN).to_edge(LEFT)
        te2 = TexMobject(r"\pi = \cfrac{4}{1+\cfrac{1^2}{2+\cfrac{3^2}{2+\cfrac{5^2}{2+\cfrac{7^2}{2+\cdots}}}}}",color=RED).arrange_submobjects(RIGHT/2).scale(0.6).shift(DOWN)
        self.play(Write(te))
        self.wait(1.5)
        self.play(Write(te2))
        self.wait(3)

class Exercise(Scene):
    def construct(self):
        text1 = VGroup(MyText("最后留下一道思考题：求"),TexMobject(r"\ln(1+x)"),MyText("的连分数展开式")).arrange_submobjects(RIGHT/2)
        text2 = MyText("会的同学可以在评论区留言").next_to(text1,DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)

class Last(Scene):
    def construct(self):
        text1 = MyText("关注@MATHEART_EVER").set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        text2 = MyText("欣赏有趣硬核内容").next_to(text1,DOWN).align_to(text1,LEFT)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)

class Cover(Scene):
    def construct(self):
        tex = TexMobject(r"e^x = \cfrac{1}{1-\cfrac{x}{1+x-\cfrac{x}{2+x-\cfrac{2x}{3+x-\cfrac{3x}{4+x-\cfrac{4x}{5+x-\cdots}}}}}}",color=RED).scale(0.9)
        text = MyText("谈常见数的连分数表示",color=BLUE).scale(2).to_edge(DOWN)
        self.play(Write(tex),Write(text))