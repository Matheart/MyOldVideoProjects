from manimlib.imports import *

class MyText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
    }

class Cover(Scene):
    def construct(self):
        title = MyText("数学定理测试 ",color=ORANGE).scale(3)
        self.play(FadeIn(title))
        self.wait(1.5)
        self.play(FadeOut(title))

class Begin(Scene):
    def construct(self):
        title = MyText("数学定理测试 ",color=ORANGE).scale(1.5)
        text1 = MyText("此测试一共有八道题（不一定按照难度排序）").shift(UP)
        text2 = MyText("给出定理的具体内容，让你填入空缺的部分")
        text3 = MyText("来测测你会几道题吧！").shift(DOWN)
        self.play(FadeIn(title))
        self.wait(1.5)
        self.play(FadeOut(title))
        self.play(ShowCreation(text1),ShowCreation(text2),ShowCreation(text3))
        self.wait(4)

class End(Scene):
    def construct(self):
        title = MyText("回答完了，来看看结果吧！",color=RED).scale(1.5)
        self.play(FadeIn(title))
        self.wait(2)

class End1(Scene):
    def construct(self):
        title = MyText("你一共答对了0-2题",color=RED).scale(1.5)
        text = MyText("你的进步空间很大，加油哦！").shift(1.5*DOWN)
        self.play(FadeIn(title),FadeIn(text))
        self.wait(3)

class End2(Scene):
    def construct(self):
        title = MyText("你一共答对了3-4题",color=RED).scale(1.5)
        text = MyText("只答对小半，要多了解数学知识哦！").shift(1.5*DOWN)
        self.play(FadeIn(title),FadeIn(text))
        self.wait(3)

class End3(Scene):
    def construct(self):
        title = MyText("你一共答对了5-7题",color=RED).scale(1.5)
        text = MyText("答对了大半，但还有一些不对，要继续努力！").shift(1.5*DOWN)
        self.play(FadeIn(title),FadeIn(text))
        self.wait(3)

class End4(Scene):
    def construct(self):
        title = MyText("你一共答对了8题",color=RED).scale(1.5)
        text = MyText("全部答对，说明你对数学基础领域已经有一些了解了，继续加油！").scale(0.9).shift(1.5*DOWN)
        self.play(FadeIn(title),FadeIn(text))
        self.wait(3)

# 1
class Fermat(Scene):
    def construct(self):
        title = MyText("问题Ⅰ--费马小定理",color=RED).scale(1.5).to_edge(UP)
        iff = MyText("若a是整数，p是质数，且a不是p的倍数")
        name = VGroup(MyText("那么",color=BLUE),TexMobject(r"a^{p-1} \equiv \rule[-2pt]{1.5cm}{0.5pt}\pmod{p}",color=BLUE)).arrange_submobjects(RIGHT/2).next_to(iff,DOWN)#.align_to(iff,LEFT)
        self.play(FadeIn(title),FadeIn(iff))
        self.play(FadeIn(name))
        self.wait(3)

# 2,2,2
class Gougu(Scene):
    def construct(self):
        title = MyText("问题Ⅱ--勾股定理",color=RED).scale(1.5).to_edge(UP)
        tri = MyTriangle(np.array([0,2,0]),np.array([2,-1.5,0]),np.array([0,-1.5,0]))
        A_label = TexMobject("a").next_to(np.array([0,0.25,0]),LEFT)
        B_label = TexMobject("b").next_to(np.array([1,-1.5,0]),DOWN)
        C_label = TexMobject("c").next_to(np.array([1,0.25,0]),RIGHT)
        text = TexMobject(r"a^{\rule[2pt]{0.2cm}{0.3pt}}+b^{\rule[2pt]{0.2cm}{0.3pt}}=c^{\rule[2pt]{0.2cm}{0.3pt}}").scale(2).to_edge(DOWN)       
        self.play(FadeIn(title),FadeIn(tri),
                  FadeIn(A_label),FadeIn(B_label),FadeIn(C_label))
        self.play(FadeIn(text))
        self.wait(3)

#B|A
class Bayes(Scene):
    def construct(self):
        title = MyText("问题Ⅲ -- 贝叶斯定理",color=RED).scale(1.5).to_edge(UP)
        Tex = TexMobject(r"P(A|B) = \frac{P(\rule[-2pt]{0.5cm}{0.5pt})P(A)}{P(B)}")
        self.play(FadeIn(title),FadeIn(Tex))
        self.wait(3)

# nx;nx
class Demoivre(Scene):
    def construct(self):
        title = MyText("问题Ⅳ -- 棣莫弗公式",color=RED).scale(1.5).to_edge(UP)
        Tex = TexMobject(r"(\cos(x) + i\sin(x))^n = \cos(\rule[-2pt]{0.5cm}{0.5pt}) + i \sin(\rule[-2pt]{0.5cm}{0.5pt})")
        self.play(FadeIn(title),FadeIn(Tex))
        self.wait(3)
#<=
class Cauchy(Scene):
    def construct(self):
        title = MyText("问题Ⅴ -- 柯基不等式",color=RED).scale(1.5).to_edge(UP)
        Tex = TexMobject(r"(a_{1}b_{1}+a_{2}b_{2}+\cdots+a_{n}b_{n})^2 \rule[-4pt]{0.5cm}{0.5pt} (a_{1}^2 + a_{2}^2 + \cdots + a_{n}^2)(b_{1}^2 + b_{2}^2 + \cdots + b_{n}^2)").scale(0.8)
        #Tex = TexMobject(r"\left(\sum_{i=1}^{n}{x_{i}y_{i}}\right)^2 \rule[-8pt]{0.5cm}{0.5pt} \left(\sum_{i=1}^{n}{x_{i}^{2}}\right) \left(\sum_{i=1}^{n}{y_{i}^{2}}\right)")
        self.play(FadeIn(title),FadeIn(Tex))
        self.wait(3)

#海伦公式
class Helen(Scene):
    def construct(self):
        title = MyText("问题Ⅵ -- 海伦公式",color=RED).scale(1.5).to_edge(UP)
        Tex1 = VGroup(MyText("若三角形边长分别为"),TexMobject("a,b,c")).arrange_submobjects(RIGHT/2)
        Tex2 = TexMobject(r"S_{\Delta} = \sqrt{p(p-a)(p-b)(p-c)}",color=BLUE).next_to(Tex1,DOWN)
        Tex3 = TexMobject(r"p = \rule[-2pt]{0.5cm}{0.5pt}").next_to(Tex2,DOWN)
        self.play(FadeIn(title),FadeIn(Tex1))
        self.play(FadeIn(Tex2))
        self.play(FadeIn(Tex3))
        self.wait(3)

# 
class Basic(Scene):
    def construct(self):
        title = MyText("问题Ⅶ -- 微积分基本定理",color=RED).scale(1.5).to_edge(UP)
        Tex1 = VGroup(MyText("若函数"),TexMobject(r"f(x)"),MyText("在区间"),TexMobject("[a,b]"),MyText("上连续，并存在原函数"),TexMobject("F(x)")).arrange_submobjects(RIGHT/2)
        Tex2 = TexMobject(r"\int_{a}^{b}{f(x)}\mathrm{d}x = \rule[-2pt]{1.5cm}{0.5pt}",color=BLUE).next_to(Tex1,DOWN)
        self.play(FadeIn(title),FadeIn(Tex1))
        self.play(FadeIn(Tex2))
        self.wait(3)       

# Pdx + Qdy
#ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ
class Green(Scene):
    def construct(self):
        title = MyText("问题Ⅷ -- 格林公式",color=RED).scale(1.5).to_edge(UP)
        Tex1 = VGroup(MyText("设闭区域"),TexMobject(r"D"),MyText("由分段光滑的简单曲线"),TexMobject("L"),MyText("围成，")).arrange_submobjects(RIGHT/2).shift(UP)
        Tex2 = VGroup(TexMobject(r"P(x,y),Q(x,y)"),MyText("在"),TexMobject("D"),MyText("上有一阶连续偏导数，则有：")).arrange_submobjects(RIGHT/2).next_to(Tex1,DOWN)
        Tex3 = TexMobject(r"\iint \limits _{D}({\frac {\partial Q}{\partial x}}-{\frac {\partial P}{\partial y}})\mathrm {d} x\mathrm {d} y=\oint _{L^{+}}(\rule[-2pt]{1.5cm}{0.5pt})}",color=BLUE).next_to(Tex2,DOWN)
        Tex4 = VGroup(MyText("其中"),TexMobject(r"L^{+}"),MyText("是"),TexMobject("D"),MyText("的取正向的边界曲线")).arrange_submobjects(RIGHT/2).next_to(Tex3,DOWN)
        self.play(FadeIn(title),FadeIn(Tex1),FadeIn(Tex2))
        self.play(FadeIn(Tex3))
        self.play(FadeIn(Tex4))
        self.wait(4.5)    