from manimlib.imports import *
# 参考：https://baike.baidu.com/item/%E4%B8%89%E8%A7%92%E5%BD%A2%E5%86%85%E8%A7%92%E5%92%8C%E5%AE%9A%E7%90%86

class MySmallText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.175,
    }

class MyText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
    }

class MyHugeText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 2,
    }

class FengMian(Scene):
    def construct(self):
        
        text1 = VGroup(TextMobject(r"$i^i$"),MyText("的求法")).set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]).scale(5)
        text1.arrange_submobjects(RIGHT/2)

        text2 = MyText("-和对数学发展的一些小思考",size=0.5).to_edge(LEFT+DOWN)
        self.play(Write(text1),Write(text2))


class Introduction(Scene):
    def construct(self):
        text1 = MyText("我们都知道，")
        tex1 = TexMobject(r"i^1 = i \text{, } i^2 = -1 \text{, } i^3 = -i \text{, } i^4 = 1",size = 3.5)
        text2 = VGroup(MyText("那么你有想过"),TexMobject(r"i^i"),MyText("等于什么吗？"))
        text2.arrange_submobjects(RIGHT/2)
        text3 = MyText("现在就让我们来揭晓吧！")
        text3.next_to(text2,DOWN)       
        tex1.next_to(text1,DOWN)

        self.play(Write(text1))
        self.play(Write(tex1))
        self.play(ReplacementTransform(VGroup(text1,tex1),text2))
        self.play(Write(text3))
        self.wait(3)

class Main(Scene):
    def construct(self):
        text1 = VGroup(MyText("根据"),MyText("欧拉公式",color=ORANGE),MyText(": "),TexMobject(r"e^{i\theta} = \cos \theta + i \sin\theta")).arrange_submobjects(RIGHT/2)
        text2 = VGroup(MyText("代入"),TexMobject(r"\theta = \frac{\pi}{2} + 2k\pi"),MyText("得到： "),TexMobject(r"e^{i(\frac{\pi}{2}+2k\pi)} = \cos \frac{\pi}{2} + i \sin \frac{\pi}{2}")).arrange_submobjects(RIGHT/2)
        text3 = TexMobject(r"e^{i(\frac{\pi}{2}+2k\pi)} = i",color=RED)
        text4 = VGroup(MyText("于是"), TexMobject(r"i^i = (e^{i(\frac{\pi}{2}+2k\pi)})^i = e^{i^2 (\frac{\pi}{2}+2k\pi)}"),TexMobject(r" = e^{-(\frac{\pi}{2}+2k\pi)} (k\in \mathbb{Z})")).arrange_submobjects(RIGHT/2)
        text5 = TexMobject(r"i^i = e^{\frac{3\pi}{2}}, e^{-\frac{\pi}{2}}, e^{-\frac{5\pi}{2}}, ...}",color=BLUE)
        text6 = TexMobject(r"i^i \approx 111.32, 0.2079, 0.000388 ...",color=BLUE)
#i^i \approx 2.718^{-\frac{3.141}{2}} \approx 0.2079
        self.play(Write(text1))
        self.wait(1)
        self.play(ApplyMethod(text1.shift,1.5*UP))
        self.play(Write(text2))
        self.wait(2)
        self.play(ApplyMethod(text1.shift,1.5*UP),ApplyMethod(text2.shift,1.5*UP))
        self.play(Write(text3))
        self.wait(2)
        self.play(ApplyMethod(text1.shift,1.5*UP),ApplyMethod(text2.shift,1.5*UP),ApplyMethod(text3.shift,1.5*UP))
        self.play(Write(text4))
        self.wait(2)
        self.play(ApplyMethod(text1.shift,1.5*UP),ApplyMethod(text2.shift,1.5*UP),ApplyMethod(text3.shift,1.5*UP),ApplyMethod(text4.shift,1.5*UP))
        self.play(Write(text5))
        self.wait(2)
        self.play(ApplyMethod(text1.shift,1.5*UP),ApplyMethod(text2.shift,1.5*UP),ApplyMethod(text3.shift,1.5*UP),ApplyMethod(text4.shift,1.5*UP),ApplyMethod(text5.shift,1.5*UP))
        self.play(Write(text6))
        self.wait(3)

class Behind(Scene):
    def construct(self):
        text1 = MyText("这样一个以前被认为不能被计算，甚至被当作不存在的数").to_edge(DOWN)
        text2 = TexMobject(r"i^i=\sqrt{-1}^{\sqrt{-1}}",size=3).to_edge(LEFT)
        text3 = MyText("竟然能用实数表示").to_edge(DOWN)
        text4 = TexMobject(r"\approx 111.32, 0.2079, 0.000388 ...").next_to(text2,RIGHT)
        text5 = MyText("而这条式子，虽然简单，却代表着数学发展的规律，就是：").to_edge(UP)
        text6 = MyHugeText("以已知表未知",color=RED)

        L1 = Line(np.array([-7,1,0]),np.array([-3,-1,0]),color=RED)
        L2 = Line(np.array([-3,1,0]),np.array([-7,-1,0]),color=RED)

        self.play(Write(text1),Write(text2))
        self.wait(1.5)
        self.play(Write(L1))
        self.play(Write(L2))
        self.wait(1.5)
        self.remove(L1,L2)
        self.play(ReplacementTransform(text1,text3))
        self.play(Write(text4))
        self.wait(2)
        self.play(FadeOut(text3),ApplyMethod(text2.to_edge,DOWN),ApplyMethod(text4.to_edge,DOWN))
        self.wait(1)
        self.play(Write(text5))
        self.wait(1)
        self.play(Write(text6))
        self.wait(1.5)

class Law(Scene):
    def construct(self):
        textup1 = MyText("平行公理：两直线平行，同位角相等",color=ORANGE).to_edge(UP)
        textup2 = TexMobject(r"\angle A + \angle B + \angle C = 180^\circ",color=ORANGE).to_edge(UP)

        textdown1 = MyText("以平面几何为例，从这条公理开始").to_edge(DOWN)
        textdown2 = MyText("由此可以推出三角形的内角和公式").to_edge(DOWN)
        textdown3 = MyText("从而再得到几个推论").to_edge(DOWN)
        
        text1 = MyText("推论1 直角三角形的两个锐角互余",color=BLUE)
        text2 = MyText("推论2 三角形的一个外角等于和它不相邻的两个内角和",color=BLUE).next_to(text1,DOWN)
        text3 = MyText("推论3 三角形的一个外角大于任何一个和它不相邻的内角",color=BLUE).next_to(text2,DOWN)
        vg = VGroup(text1,text2,text3)

        L1 = Line(np.array([-5,2,0]),np.array([5,2,0]),color=RED)
        L2 = Line(np.array([-5,-1,0]),np.array([5,-1,0]),color=RED)

        L = Line(np.array([-6,-3,0]),np.array([7,5,0]),color=BLUE)
        arc1 = Arc(angle = 31.60750/180.0*PI).move_arc_center_to(np.array([2.125,2,0]))
        arc2 = Arc(angle = 31.60750/180.0*PI).move_arc_center_to(np.array([-2.75,-1,0]))
        arc1_label = TexMobject(r"\theta").next_to(arc1,RIGHT)
        arc2_label = TexMobject(r"\theta").next_to(arc2,RIGHT)
        tri = MyTriangle(np.array([-4,-2,0]),np.array([2,-2,0]),np.array([0,1,0]))
        up_line = Line(np.array([-5,1,0]),np.array([5,1,0]))

        angleA, angleB, angleC = tri.get_three_angle()
        arcA = Arc(angle = angleA,color = RED).move_arc_center_to(np.array([-4,-2,0]))
        arcB = Arc(start_angle = PI-angleB, angle = angleB,color=YELLOW).move_arc_center_to(np.array([2,-2,0]))
        arcC = Arc(start_angle = PI+angleA, angle = angleC,color=GREEN).move_arc_center_to(np.array([0,1,0]))
        arcA_2 = Arc(start_angle = PI, angle = angleA,color=RED).move_arc_center_to(np.array([0,1,0]))
        arcB_2 = Arc(start_angle = 2*PI-angleB, angle = angleB,color=YELLOW).move_arc_center_to(np.array([0,1,0]))
        self.play(Write(textdown1))

        self.play(Write(L1),Write(L2))
        self.play(Write(L))
        self.play(Write(arc1),Write(arc2),Write(textup1),
                  Write(arc1_label),
                  Write(arc2_label))
        self.wait(1.5)
        self.remove(L,L1,L2,arc1,arc2,arc1_label,arc2_label)
        self.play(ReplacementTransform(textup1,textup2),ReplacementTransform(textdown1,textdown2))
        self.play(Write(tri),Write(up_line))
        self.play(Write(arcA),Write(arcB),Write(arcC),Write(arcA_2),Write(arcB_2))
        self.wait(1.5)
        self.remove(tri,arcA,arcB,arcC,arcA_2,arcB_2,up_line)
        self.play(ReplacementTransform(textdown2,textdown3),Write(vg))
        self.wait(2)
        
class Development(Scene):
    def construct(self):
        text1 = MyText("数学便是这样子，从刚开始的几条公理").to_edge(DOWN)
        text2 = MyText("发展到现在的枝繁叶茂").to_edge(DOWN)
        text3 = MyText("再向未知拓展").to_edge(DOWN)
        text4 = MyText("如此一步一步地堆砌起来，才构成我们现在已知的数学").to_edge(DOWN)

        rec2_1 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([-0.6*2,-1.9,0]))
        rec2_2 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([0.6*2,-1.9,0]))

        rec3_1 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([-1.2*2,-1.1,0]))
        rec3_2 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([0*2,-1.1,0]))
        rec3_3 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([1.2*2,-1.1,0]))

        rec4_1 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([-1.8*2,-0.3,0]))
        rec4_2 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([-0.6*2,-0.3,0]))
        rec4_3 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([0.6*2,-0.3,0]))
        rec4_4 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([1.8*2,-0.3,0]))

        rec5_1 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([-2.4*2,0.5,0]))
        rec5_2 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([-1.2*2,0.5,0]))
        rec5_3 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([0*2,0.5,0]))
        rec5_4 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([1.2*2,0.5,0]))
        rec5_5 = Rectangle(height = 0.2*2, width = 0.4*2).move_to(np.array([2.4*2,0.5,0]))

        rec_text2_1 = MySmallText("集合论").move_to(rec2_1.get_center())
        rec_text2_2 = MySmallText("逻辑").move_to(rec2_2.get_center())
        rec_text3_1 = MySmallText("线性代数").move_to(rec3_1.get_center())
        rec_text3_2 = MySmallText("拓扑").move_to(rec3_2.get_center())
        rec_text3_3 = MySmallText("微积分").move_to(rec3_3.get_center())
        rec_text4_1 = MySmallText("近世代数").move_to(rec4_1.get_center())
        rec_text4_2 = MySmallText("代数拓扑").move_to(rec4_2.get_center())
        rec_text4_3 = MySmallText("微分几何").move_to(rec4_3.get_center())
        rec_text4_4 = MySmallText("泛函分析").move_to(rec4_4.get_center())

        rec_text5_1 = MySmallText("表示论").move_to(rec5_1.get_center())
        rec_text5_2 = MySmallText("代数几何").move_to(rec5_2.get_center())
        rec_text5_3 = MySmallText("上同调").move_to(rec5_3.get_center())
        rec_text5_4 = MySmallText("非交换几何").move_to(rec5_4.get_center())
        rec_text5_5 = MySmallText("调和分析").move_to(rec5_5.get_center())

        L_2_1to3_1 = Line(np.array([-0.6*2,-1.9 +0.2,0]), np.array([-1.2*2,-1.1 -0.2,0]))    
        L_2_1to3_2 = Line(np.array([-0.6*2,-1.9 +0.2,0]), np.array([ 0*2  ,-1.1 -0.2,0]))     
        L_2_1to3_3 = Line(np.array([-0.6*2,-1.9 +0.2,0]), np.array([1.2*2,-1.1 -0.2,0]))  

        L_2_2to3_1 = Line(np.array([ 0.6*2,-1.9 +0.2,0]), np.array([-1.2*2,-1.1 -0.2,0])) 
        L_2_2to3_2 = Line(np.array([ 0.6*2,-1.9 +0.2,0]), np.array([0*2  ,-1.1 -0.2,0]))    
        L_2_2to3_3 = Line(np.array([ 0.6*2,-1.9 +0.2,0]), np.array([1.2*2,-1.1 -0.2,0]))     

        L_3_1to_4_1 = Line(np.array([-1.2*2,-1.1 +0.2,0]), np.array([-1.8*2  ,-0.3 -0.2,0]))  
        L_3_1to_4_2 = Line(np.array([-1.2*2,-1.1 +0.2,0]), np.array([-0.6*2  ,-0.3 -0.2,0]))  
        L_3_2to_4_2 = Line(np.array([    0*2,-1.1 +0.2,0]), np.array([-0.6*2  ,-0.3 -0.2,0]))  
        L_3_2to_4_3 = Line(np.array([    0*2,-1.1 +0.2,0]), np.array([0.6*2  ,-0.3 -0.2,0]))  
        L_3_3to_4_3 = Line(np.array([ 1.2*2,-1.1 +0.2,0]), np.array([0.6*2  ,-0.3 -0.2,0]))  
        L_3_3to_4_4 = Line(np.array([ 1.2*2,-1.1 +0.2,0]), np.array([1.8*2  ,-0.3 -0.2,0]))  

        L_4_1to_5_1 = Line(np.array([-1.8*2,-0.3 +0.2,0]), np.array([-2.4*2  ,0.5 -0.2,0]))  
        L_4_1to_5_2 = Line(np.array([-1.8*2,-0.3 +0.2,0]), np.array([-1.2*2  ,0.5 -0.2,0]))         
        L_4_2to_5_2 = Line(np.array([-0.6*2,-0.3 +0.2,0]), np.array([-1.2*2  ,0.5 -0.2,0]))  
        L_4_2to_5_3 = Line(np.array([-0.6*2,-0.3 +0.2,0]), np.array([ 0*2  ,0.5 -0.2,0]))  
        L_4_3to_5_3 = Line(np.array([ 0.6*2,-0.3 +0.2,0]), np.array([ 0*2  ,0.5 -0.2,0]))  
        L_4_3to_5_4 = Line(np.array([ 0.6*2,-0.3 +0.2,0]), np.array([ 1.2*2  ,0.5 -0.2,0]))  
        L_4_4to_5_4 = Line(np.array([ 1.8*2,-0.3 +0.2,0]), np.array([ 1.2*2  ,0.5 -0.2,0]))  
        L_4_4to_5_5 = Line(np.array([ 1.8*2,-0.3 +0.2,0]), np.array([ 2.4*2  ,0.5 -0.2,0]))  

        L5_3toL = Line(np.array([ 0*2  ,0.5 +0.2,0]), np.array([-0.6*2, 1.3 -0.2, 0]))
        L5_3toR = Line(np.array([ 0*2  ,0.5 +0.2,0]), np.array([ 0.6*2, 1.3 -0.2, 0]))

        self.play(Write(text1))
        self.play(FadeIn(rec2_1),FadeIn(rec2_2),FadeIn(rec_text2_1),FadeIn(rec_text2_2))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.play(FadeIn(rec3_1),FadeIn(rec3_2),FadeIn(rec3_3),
                  FadeIn(rec_text3_1),FadeIn(rec_text3_2),FadeIn(rec_text3_3),
                  Write(L_2_1to3_1),Write(L_2_1to3_2),Write(L_2_1to3_3),
                  Write(L_2_2to3_1),Write(L_2_2to3_2),Write(L_2_2to3_3))
        self.play(FadeIn(rec4_1),FadeIn(rec4_2),FadeIn(rec4_3),FadeIn(rec4_4),
                  FadeIn(rec_text4_1),FadeIn(rec_text4_2),FadeIn(rec_text4_3),FadeIn(rec_text4_4),
                  Write(L_3_1to_4_1),Write(L_3_1to_4_2),Write(L_3_2to_4_2),Write(L_3_2to_4_3),Write(L_3_3to_4_3),Write(L_3_3to_4_4))
        self.play(FadeIn(rec5_1),FadeIn(rec5_2),FadeIn(rec5_3),FadeIn(rec5_4),FadeIn(rec5_5),
                  FadeIn(rec_text5_1),FadeIn(rec_text5_2),FadeIn(rec_text5_3),FadeIn(rec_text5_4),FadeIn(rec_text5_5),
                  Write(L_4_1to_5_1),Write(L_4_1to_5_2),Write(L_4_2to_5_2),Write(L_4_2to_5_3),
                  Write(L_4_3to_5_3),Write(L_4_3to_5_4),Write(L_4_4to_5_4),Write(L_4_4to_5_5))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3),Write(L5_3toL),Write(L5_3toR),
                  Write(MyText("...",color=RED).next_to(np.array([-0.6*2, 1.3 -0.2, 0]),UP)),
                  Write(MyText("...",color=RED).next_to(np.array([ 0.6*2, 1.3 -0.2, 0]),UP)),)
        self.wait(2)
        self.play(ReplacementTransform(text3,text4))
        self.wait(3)
    
class Last(Scene):
    def construct(self):
        text1 = MyText("关注@MATHEART_EVER").set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        text2 = MyText("欣赏有趣硬核内容").next_to(text1,DOWN).align_to(text1,LEFT)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)