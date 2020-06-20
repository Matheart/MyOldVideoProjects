from manimlib.imports import *
import itertools

class MyText(Text):
    CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
    }
"""
        test = TexMobject(r"\sum_{p=0}^{\infty}{\frac{B_p}{p!}x^p}")
        self.add(test)
        debugTeX(self,test[0])
"""
def debugTeX(self, texm):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Consolas").scale(0.3).set_color(PURPLE)
        tex_id.move_to(j)
        self.add(tex_id)

class Cover(Scene):
    def construct(self):
        text = MyText("等幂求和问题",color=RED).scale(3).shift(RIGHT/3.0)
        tex_ar = ["1^","p","+","2^","p","+","3^","p",r"+ \cdots + n^","p"]
        form = TexMobject(*tex_ar).scale(1.5).next_to(text,DOWN)
        form.set_color_by_tex_to_color_map({
            "p" : "#00FFFF"
        })
        form2 = TexMobject(r"\displaystyle\sum_{k=1}^{n}{k^p} = \frac{1}{p+1}\displaystyle\sum_{j=0}^{p}{(-1)^j {p+1 \choose j} B_j n^{p+1-j}}",color="#00BFFF").scale(0.8).to_edge(LEFT+UP)
        form3 = TexMobject(r"\displaystyle\sum_{k=0}^{n}{{n+1 \choose k} B_k} = 0",color=RED).scale(0.8).to_edge(RIGHT+UP)
        author = MyText("By MATHEART_EVER, 无懈可击99",color=GREEN).scale(0.8).to_edge(RIGHT+DOWN)
        self.play(FadeIn(text),FadeIn(form),FadeIn(author),FadeIn(form2),FadeIn(form3))
        self.wait(2)

# 开头引入
class Begin(Scene):
    def construct(self):
        text = MyText("大家应该在妈咪叔的母婴先修班和毕导学院就学过1到n的求和公式").scale(0.9).to_edge(DOWN)
        text2 = MyText("并能用数学归纳法证明平方和公式").to_edge(DOWN)
        text3 = MyText("那么，若幂为p，公式是什么呢？").to_edge(DOWN)
        text4 = VGroup(MyText("于是就引申出我们的"),MyText("等幂求和问题",color=ORANGE).scale(2)).arrange_submobjects(RIGHT/2)

        array1 = ["S","= ","1","+","2","+","3","+",r"\cdots","+","n"]
        array2 = ["S","= ","n","+","(n-1)","+","(n-2)","+",r"\cdots","+","1"]
        array3 = ["2S","= ","(n+1)","+","(n+1)","+","(n+1)","+",r"\cdots","+","(n+1)"]
        array4 = ["S ", "= ", r"\frac{n(n+1)}{2}"]

        for1 = TexMobject(*array1).to_edge(LEFT).shift(2*UP)
        for2 = TexMobject(*array2).next_to(for1,DOWN).to_edge(LEFT)
        for3 = TexMobject(*array3).next_to(for2,DOWN).to_edge(LEFT)
        for4 = TexMobject(*array4).next_to(for2,DOWN).to_edge(LEFT)
        for5_ar = ["1","^2" ,"+", "2", "^2", "+", "3", "^2" ,r"+ \cdots + n","^2",r" = \frac{n(n+1)(2n+1)}{6}"]
        for5 = TexMobject(*for5_ar)
        for5.set_color_by_tex_to_color_map({
            "^2" : "#00FFFF"
        })
        for6_ar = ["1^","p","+","2^","p","+","3^","p",r"+ \cdots + n^","p",r" = \text{ ?}"]
        for6 = TexMobject(*for6_ar)
        for6.set_color_by_tex_to_color_map({
            "p" : "#00FFFF"
        })


        for1[0].set_color(YELLOW)
        for2[0].set_color(YELLOW)
        for3[0].set_color(YELLOW)
        for4[0].set_color(YELLOW)

        self.play(FadeIn(text),FadeIn(for1))
        self.wait(1.5)

        for i in range(len(for1)):
            for1[i].align_to(for3[i], LEFT)
            for2[i].align_to(for3[i], LEFT)
        for i in range(len(for4)):
            for4[i].align_to(for3[i], LEFT)

        self.play(FadeIn(for2))
        self.wait(1.5)

        self.play(FadeIn(for3))    
        self.wait(1.5)
        ba = TexMobject(r"n(n+1)").move_to(for3[3])
        self.play(ReplacementTransform(for3[2:],ba))  
        self.wait(1)
        self.remove(ba) 
        self.play(ReplacementTransform(for3,for4))
        self.wait(2)
        self.remove(for1,for2,for3,for4,text)
        self.play(FadeIn(text2))
        self.play(FadeIn(for5))
        self.wait(1.5)
        self.remove(text2)
        self.play(FadeIn(text3))
        self.remove(for5)
        self.play(Write(for6))
        self.wait(2)
        self.play(FadeOut(text3),FadeOut(for6))
        self.play(FadeIn(text4))
        self.wait(2)
class Pre(Scene):
    def construct(self):
        text1 = MyText("这个问题看似简单，但实际上比较复杂")
        text2 = MyText("在开始之前，要先介绍两个比较简单的前置知识").shift(DOWN)
        text3 = MyText("碍于篇幅有限，在这里不给出详细证明，观众可自证")
        for1 = VGroup(MyText("级数相乘公式： ",color=RED),TexMobject(r"\left(\displaystyle\sum_{j=0}^{n}{a_j}\right) \left(\displaystyle\sum_{j=0}^{n}{b_j} \right)=\displaystyle\sum_{j=0}^{n}{\displaystyle\sum_{k=0}^{j}{\left(a_{k}b_{j-k}\right)}}")).arrange_submobjects(RIGHT/2)
        for2 = VGroup(MyText("麦克劳林级数展开式： ",color=RED),TexMobject(r"f(x)=\displaystyle\sum_{n=0}^{\infty}{\frac{f^{(n)}(0)}{n!}x^n}")).arrange_submobjects(RIGHT/2)
        for3 = MyText("(函数在x=0处的泰勒级数)",color=BLUE).scale(0.6).next_to(for2,0.3*DOWN).align_to(for2,LEFT)
        self.play(FadeIn(text1),FadeIn(text2))
        self.wait(2)
        self.remove(text1,text2)
        self.play(FadeIn(for1))
        self.wait(6)
        self.remove(for1)
        self.play(FadeIn(for2),FadeIn(for3))
        self.wait(6)
        self.remove(for2,for3)
        self.play(FadeIn(text3))
        self.wait(2.5)
class General1(Scene):
    def construct(self):        
        tex_ar = ["1^","p","+","2^","p","+","3^","p",r"+ \cdots + n^","p"]
        form = TexMobject(*tex_ar)
        form.set_color_by_tex_to_color_map({"p" : "#00FFFF"})

        tex_ar2 = ["S^","p","(n)"]
        form2 = TexMobject(*tex_ar2)
        form2.set_color_by_tex_to_color_map({"p" : "#00FFFF"}) 

        #tex_ar3 = ["S^","p","(n)","=","1^","p","+","2^","p","+","3^","p",r"+ \cdots + n^","p"]
        #form3 = TexMobject(*tex_ar3).set_color_by_tex_to_color_map({"p" : "#00FFFF"}).scale(0.5).to_edge(UP+LEFT)

        tex_ar4 = ["G'(0)","=","0","+","1","^{1}","e^0","+","2","^{1}","e^{2\cdot 0}","+","3","^{1}","e^{3\cdot 0}","+","\cdots","+","n","^{1}","e^{n\cdot 0}","=","1","^{1}","+","2","^{1}","+",r"\cdots","+","n","^{1}","=","S","^{1}","(n)"]
        tex_ar5 = ["G''(0)","=","0","+","1","^{2}","e^0","+","2","^{2}","e^{2\cdot 0}","+","3","^{2}","e^{3\cdot 0}","+",r"\cdots","+","n","^{2}","e^{n\cdot 0}","=","1","^{2}","+","2","^{2}","+",r"\cdots","+","n","^{2}","=","S","^{2}","(n)"]
        tex_ar6 = ["G^{(p)}(0)","=","0","+","1","^{p}","e^0","+","2","^{p}","e^{2\cdot 0}","+","3","^{p}","e^{3\cdot 0}","+",r"\cdots","+","n","^{p}","e^{n\cdot 0}","=","1","^{p}","+","2","^{p}","+",r"\cdots","+","n","^{p}","=","S","^{p}","(n)"]

        form4 = TexMobject(*tex_ar4).scale(0.7).shift(1.5*UP)
        form5 = TexMobject(*tex_ar5).scale(0.7).next_to(form4,DOWN)
        form6 = TexMobject(*tex_ar6).scale(0.7).next_to(form5,DOWN)
        form7 = TexMobject(r"G(x)=\displaystyle\sum_{p=0}^{\infty}{\left(\frac{G^{(p)}(0)}{p!}x^p \right)}")
        form8 = TexMobject(r"=\displaystyle\sum_{p=0}^{\infty}{\left( \frac{S^{p}(n)}{p!}x^p\right)}")

        form4.set_color_by_tex_to_color_map({"^{1}" : "#00FFFF"}) 
        form5.set_color_by_tex_to_color_map({"^{2}" : "#00FFFF"}) 
        form6.set_color_by_tex_to_color_map({"^{p}" : "#00FFFF"}) 

        for i in range(len(form6)):
            form4[i].align_to(form6[i],LEFT)
            form5[i].align_to(form6[i],LEFT)

        text1 = MyText("现在我们步入正题").scale(2)
        text2 = VGroup(MyText("为简化过程，不妨将"),form,MyText("设为"),form2).arrange_submobjects(RIGHT/2)
        text3 = VGroup(MyText("如："),TexMobject(r"1+2+\cdots+n"),MyText("记为"),TexMobject("S^{1}(n)")).arrange_submobjects(RIGHT/2).next_to(text2,DOWN)
        text4 = VGroup(MyText("考虑构造一个函数"),TexMobject(r"G(x)=\displaystyle\sum_{k=0}^{n}{e^{kx}}=1+e^x+e^{2x}+\cdots+e^{nx}"),MyText("可以发现：")).arrange_submobjects(RIGHT/2).scale(0.8).to_edge(UP)
        text5 = VGroup(MyText("所以，将"),TexMobject("G(x)"),MyText("在0处泰勒展开可得：")).arrange_submobjects(RIGHT/2).scale(0.8).next_to(form6,DOWN)
        form7.next_to(text5,DOWN).shift(LEFT)
        form8.next_to(form7,RIGHT)

        VGroup(
            form7[0][7],form7[0][13],form7[0][19],form7[0][22],
            form8[0][3],form8[0][8],form8[0][13],form8[0][16]
        ).set_color("#00FFFF")

        self.play(FadeIn(text1))
        self.wait(1.5)
        self.remove(text1)
        self.play(FadeIn(text2))
        self.wait(1)
        self.play(FadeIn(text3))
        self.wait(2)
        self.play(FadeOut(text2),FadeOut(text3))

        #self.play(FadeIn(form3))
        self.wait(1)
        self.play(FadeIn(text4))
        self.wait(3)
        self.play(FadeIn(form4))
        self.wait(3)
        self.play(FadeIn(form5))
        self.wait(3)
        self.play(FadeIn(form6))
        self.wait(4)
        self.play(FadeIn(text5))
        self.wait(2)
        self.play(FadeIn(form7))
        self.wait(2)
        self.play(Write(form8))
        self.wait(4)
class General2(Scene):
    def construct(self):
        for1 = TexMobject(r"G(x)=\displaystyle\sum_{p=0}^{\infty}{\left( \frac{S^{p}(n)}{p!}x^p\right)}").scale(0.7).to_edge(UP+LEFT)
        for1_bg = SurroundingRectangle(for1, fill_opacity = .2)
        for2 = TexMobject(r"G(x) = ",r"\left( \frac{e^{(n+1)x}-1}{x} \right)", r"\left( \frac{x}{e^x-1} \right)")

        forrs = [
            r"\frac{e^{(n+1)x}-1}{x}", # for3
            r"= \frac{ \left( \displaystyle\sum_{p=0}^{\infty}{\frac{{((n+1)x)}^p}{p!}} \right) -1}{x}}", #for4
            r"=\frac{1+\left( \displaystyle\sum_{p=1}^{\infty}{\frac{{((n+1)x)}^p}{p!}} \right) -1}{x}}",#for5
            r"=\displaystyle\sum_{p=1}^{\infty}{\frac{(n+1)^p}{p!}x^{p-1}}",#for6
            r"=\displaystyle\sum_{p=0}^{\infty}{\frac{(n+1)^{p+1}}{(p+1)!}x^{p}}"#for7
        ]
        forr = TexMobject(*forrs).scale(0.8).shift(2*DOWN)

        for_text1 = TexMobject("S^{p}(n)")
        text1 = VGroup(MyText("我们可尝试将"),TexMobject("G(x)"),MyText("用另一种形式表达以便求出"),for_text1).arrange_submobjects(RIGHT/2).scale(0.7).to_edge(UP+RIGHT)
        text2 = VGroup(MyText("根据"),TexMobject("G(x)"),MyText("定义，我们有"),TexMobject(r"G(x)=\displaystyle\sum_{k=0}^{n}{e^{kx}}=\frac{e^{(n+1)x-1}}{e^x-1}"),MyText("（等比数列求和）")).arrange_submobjects(RIGHT/2).scale(0.9).next_to(for1,DOWN).to_edge(LEFT)
        text3 = MyText("容易得到:").scale(0.8)
        tex4 = TexMobject(r"\frac{x}{e^x-1}")
        for_text4 = TexMobject(r"\sum_{p=0}^{\infty}{\frac{B_p}{p!}x^p}")
        text4 = VGroup(MyText("而"),tex4,MyText("可定义为"),for_text4).arrange_submobjects(RIGHT/2).shift(0.2*DOWN)
        text5 = VGroup(MyText("(",color=RED),TexMobject("B_p",color=RED),MyText("又被称为伯努利数，其运算方法将在后面介绍)",color=RED)).arrange_submobjects(RIGHT/2).scale(0.5).next_to(text4,DOWN)

        VGroup(
            for1[0][7],for1[0][12],for1[0][17],for1[0][20],
            forr[1][4],forr[1][15],forr[1][17],
            forr[2][6],forr[2][17],forr[2][19],
            forr[3][3],forr[3][11],forr[3][13],forr[3][16],
            forr[4][3],forr[4][11],forr[4][16],forr[4][22],
            for_text4[0][2],for_text4[0][6],for_text4[0][8],for_text4[0][11],
            for_text1[0][1]
        ).set_color(
            "#00FFFF"
        )
        
        self.play(FadeIn(for1))
        self.play(Write(for1_bg))
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeIn(text2))
        self.wait(2)
        self.play(FadeIn(for2))
        self.wait(2)
        self.remove(text2)
        self.play(ApplyMethod(for2.shift,1.5*UP))
        text3.to_edge(LEFT).shift(2*DOWN)

        for2_1_bg = SurroundingRectangle(for2[1], color=BLUE, fill_opacity = .2)
        for2_2_bg = SurroundingRectangle(for2[2], color=ORANGE, fill_opacity = .2)

        forr[0].shift(LEFT*(forr[0].get_left()[0]-text3.get_right()[0]-0.25))
        forr[1].shift(LEFT*(forr[1].get_left()[0]-forr[0].get_right()[0]-0.25))

        self.play(FadeIn(text3),FadeIn(forr[0]),FadeIn(forr[1]))
        self.wait(3)
        self.remove(text3)
        self.play(ApplyMethod(forr[0].to_edge,LEFT))
        self.play(ApplyMethod(forr[1].shift,LEFT*(forr[1].get_left()[0]-forr[0].get_right()[0]-0.25)))
        
        self.wait(3)
        forr[2].shift(LEFT*(forr[2].get_left()[0]-forr[1].get_right()[0]-0.25))
        self.play(FadeIn(forr[2]))
        self.wait(3)

        self.play(FadeOut(forr[1]),ApplyMethod(forr[2].shift,LEFT*(forr[2].get_left()[0]-forr[0].get_right()[0]-0.25)))
        self.wait(3)
        forr[3].shift(LEFT*(forr[3].get_left()[0]-forr[2].get_right()[0]-0.25))
        self.play(FadeIn(forr[3]))
        self.wait(3)
        self.play(FadeOut(forr[2]),ApplyMethod(forr[3].shift,LEFT*(forr[3].get_left()[0]-forr[0].get_right()[0]-0.25)))
        forr[4].shift(LEFT*(forr[4].get_left()[0]-forr[3].get_right()[0]-0.25))
        self.play(FadeIn(forr[4]))
        self.wait(3)
        self.play(FadeOut(forr[3]),ApplyMethod(forr[4].shift,LEFT*(forr[4].get_left()[0]-forr[0].get_right()[0]-0.25)))
        self.wait(2)
        vg = VGroup(forr[0],forr[3])
        bg = SurroundingRectangle(vg, color=BLUE, fill_opacity = .2)
        self.play(Write(bg),Write(for2_1_bg))
        self.wait(2)
        self.play(FadeIn(text4))
        tex4_bg = SurroundingRectangle(tex4, color=ORANGE, fill_opacity = .2)
        self.play(Write(tex4_bg),Write(for2_2_bg))
        self.play(FadeIn(text5))
        self.wait(2.5)
class General3(Scene):
    def construct(self):
        forr_ar = [
            r"G(x)",
            r"= \left( \frac{x}{e^x-1} \right) \left( \frac{e^{(n+1)x}-1}{x} \right)",
            r"= \left( \displaystyle \sum_{p=0}^{\infty}{\frac{B_p}{p!}x^p} \right) \left( \displaystyle \sum_{p=0}^{\infty}{\frac{(n+1)^{p+1}}{(p+1)!}x^p} \right)",
            r"= \displaystyle \sum_{p=0}^{\infty}{\displaystyle \sum_{k=0}^{p}{\left( \frac{B_k}{k!}x^k \cdot \frac{(n+1)^{p+1-k}}{(p+1-k)!}x^{p-k} \right)}}",
            r"= \displaystyle \sum_{p=0}^{\infty}{\left( \displaystyle \sum_{k=0}^{p}{\frac{B_k{(n+1)}^{p+1-k}}{k!(p+1-k)!}}\right)x^p}",
            r"= \displaystyle \sum_{p=0}^{\infty}{\left( \frac{S^{p}(n)}{p!}\right)x^p}"
        ]
        gen_ar = [
            r"S^{p}(n)",
            r"=p!\displaystyle \sum_{k=0}^{p}{\frac{(n+1)^{p+1-k}B_k}{k!(p+1-k)!}}",
            r"=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \frac{(p+1)!}{k!(p+1-k)!} B_k (n+1)^{p+1-k} \right)}",
            r"=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \displaystyle {p+1 \choose k}  B_k {(n+1)}^{p+1-k} \right)}",
        ]

        display = TexMobject(r"\displaystyle \sum_{p=0}^{\infty}{\left( \displaystyle \sum_{k=0}^{p}{\frac{B_k{(n+1)}^{p+1-k}}{k!(p+1-k)!}}\right)x^p} = \displaystyle \sum_{p=0}^{\infty}{\left( \frac{S^{p}(n)}{p!}\right)x^p}").to_edge(UP)
        text = MyText("因为对应系数相等，所以：").next_to(display,DOWN)
        form = TexMobject(r"\frac{S^{p}(n)}{p!}=\displaystyle \sum_{k=0}^{p}{\frac{(n+1)^{p+1-k}}{k!(p+1-k)!}B_k}").next_to(text,DOWN)

        forr = TexMobject(*forr_ar).scale(0.8)
        gen = TexMobject(*gen_ar).scale(0.8)

        """test = TexMobject(r"= \displaystyle \sum_{p=0}^{\infty}{\left( \displaystyle \sum_{k=0}^{p}{\frac{B_k{(n+1)}^{p+1-k}}{k!(p+1-k)!}}\right)x^p}")
        self.add(test)
        debugTeX(self,test[0])"""

        VGroup(
            forr[2][4],forr[2][8],forr[2][10],forr[2][13],forr[2][18],forr[2][26],forr[2][31],forr[2][37],
            forr[3][3],forr[3][6],forr[3][25],forr[3][32],forr[3][40],
            forr[4][3],forr[4][7],forr[4][19],forr[4][28],forr[4][-1],
            forr[5][3],forr[5][8],forr[5][13],forr[5][17],
            display[0][2],display[0][6],display[0][18],display[0][27],display[0][36],display[0][40],display[0][45],display[0][50],display[0][54],
            form[0][1],form[0][6],form[0][9],form[0][19],form[0][28],
            gen[0][1],
            gen[1][1],gen[1][3],gen[1][13],gen[1][24],
            gen[2][3],gen[2][6],gen[2][13],gen[2][22],gen[2][36],
            gen[3][3],gen[3][6],gen[3][13],gen[3][25],
        ).set_color("#00FFFF")

        forr[0].to_edge(UP+LEFT)
        for i in range(1,len(forr)-1):
            forr[i].next_to(forr[i-1],DOWN)
            forr[i].align_to(forr[i-1],LEFT)
        forr[-1].next_to(forr[-2],RIGHT)
        
        bg = SurroundingRectangle(forr[-1], color=YELLOW, fill_opacity = .2)
        
        self.play(FadeIn(forr[0]),FadeIn(forr[1]))
        self.wait(1)
        self.play(FadeIn(forr[2]))
        self.wait(2)
        self.play(FadeIn(forr[3]))
        self.wait(5)    
        self.play(FadeIn(forr[4]))   
        self.wait(5)
        self.play(FadeIn(forr[5]))
        self.play(Write(bg))
        self.wait(4)
        self.remove(forr[0],forr[1],forr[2],forr[3],forr[4],forr[5],bg)
        self.play(FadeIn(display))
        self.wait(2)
        self.play(FadeIn(text))
        self.play(FadeIn(form))
        self.wait(2)
        self.remove(display,text)
        self.play(ApplyMethod(form.to_edge,UP))
        gen[0].next_to(form,DOWN).to_edge(LEFT)
        for i in range(1,len(gen)):
            gen[i].next_to(gen[i-1],DOWN).align_to(gen[i-1],LEFT)

        self.wait(1)
        self.play(FadeIn(gen[0]))
        self.wait(1.5)
        self.play(FadeIn(gen[1]))
        self.wait(3.5)
        self.play(FadeIn(gen[2]))  
        self.wait(3.5)     
        self.play(FadeIn(gen[3]))
        self.wait(3.5)
class Bernoulli1(Scene): # Simplify general formula
    def construct(self):
        text1 = MyText("接下来会介绍伯努利数的性质，并应用到公式里面").to_edge(DOWN)
        text2 = MyText("根据定义，我们有：").to_edge(UP)
        text3 = MyText("两式相减").to_edge(UP)
        text4 = MyText("所以").to_edge(UP)
        text5 = MyText("由对应系数相等可得：").to_edge(UP)

        form_ar = [
            r"\displaystyle \sum_{p=0}^{\infty}{\frac{x^p}{p!}B_p}=\frac{x}{e^x-1}",
            r"\displaystyle \sum_{p=0}^{\infty}{{(-1)}^{p}\frac{x^p}{p!}B_p}=\displaystyle \sum_{p=0}^{\infty}{\frac{(-x)^p}{p!}B_p}=\frac{-x}{e^{-x}-1}",
            r"\displaystyle \sum_{p=0}^{\infty}{B_{p}\frac{x^p}{p!}(1-(-1)^p)} = \frac{x}{e^x-1} - \frac{-x}{e^{-x}-1} = -x",
            r"2 \displaystyle \sum_{p=0}^{\infty}{B_{2p+1}\frac{x^{2p+1}}{(2p+1)!}}=-x",
            r" \displaystyle \sum_{p=0}^{\infty}{B_{2p+1}\frac{x^{2p+1}}{(2p+1)!}}",
            r"= B_1 x + \displaystyle \sum_{p=1}^{\infty}{B_{2p+1}\frac{x^{2p+1}}{(2p+1)!}}",
            r"= -\frac{1}{2}x + 0x^3 + 0x^5 + \cdots",
            r"B_1 = -\frac{1}{2}, B_{2p+1} = 0 (p \in \mathbb{Z}^+)"
        ]
        form = TexMobject(*form_ar).scale(0.8)
    
        """test = TexMobject(r"B_1 = -\frac{1}{2}, B_{2p+1} = 0 (p \in \mathbb{Z}^+)")
        self.add(test)
        debugTeX(self,test[0])"""

        VGroup(
            form[0][2],form[0][6],form[0][8],form[0][11],
            form[1][2],form[1][9],form[1][11],form[1][13],form[1][16],form[1][20],form[1][27],form[1][29],form[1][32],
            form[2][2],form[2][6],form[2][8],form[2][10],form[2][19],
            form[3][3],form[3][8],form[3][13],form[3][19],
            form[4][2],form[4][7],form[4][12],form[4][18],
            form[5][7],form[5][12],form[5][17],form[5][23],
            form[7][10],form[7][16],
        ).set_color("#00FFFF")

        form[0].next_to(text2,DOWN)
        form[1].next_to(form[0],DOWN)
        form[2].next_to(form[1],DOWN)

        self.play(FadeIn(text1))
        self.wait(1.5)
        self.play(FadeOut(text1),FadeIn(text2))
        self.play(FadeIn(form[0]))
        self.wait(2)
        self.play(FadeIn(form[1]))
        self.wait(1)
        self.play(FadeOut(text2),FadeIn(text3))
        self.play(FadeIn(form[2]))
        self.wait(3)
        self.remove(form[0],form[1])
        self.play(FadeOut(text3),FadeIn(text4))
        self.play(ApplyMethod(form[2].next_to,text4,DOWN))
        self.play(FadeIn(form[3].next_to(form[2],DOWN)))
        self.wait(2)
        self.play(FadeOut(form[2]))
        self.play(ApplyMethod(form[3].next_to,text4,DOWN)) 
        self.play(FadeIn(form[4].next_to(form[3],DOWN)))
        self.wait(2)
        self.play(FadeOut(form[3]))
        self.play(ApplyMethod(form[4].next_to,text4,DOWN))
        self.play(FadeIn(form[5].next_to(form[4],DOWN).align_to(form[4],LEFT)))
        self.wait(1.5)
        self.play(FadeIn(form[6].next_to(form[5],DOWN).align_to(form[5],LEFT)))
        self.wait(1.5)
        form[7].next_to(form[6],DOWN)
        bg = SurroundingRectangle(form[7], color=ORANGE, fill_opacity = .2)
        self.play(FadeOut(text4),FadeIn(text5))
        self.wait(2)
        self.play(FadeIn(form[7]))
        self.play(Write(bg))
        self.wait(2)
class Final_Form(Scene):
    def construct(self):
        tp = TexMobject(r"B_1 = -\frac{1}{2}, B_{2p+1} = 0 (p \in \mathbb{Z}^+)").scale(0.7).to_edge(UP)
        tp_bg = SurroundingRectangle(tp, color=ORANGE, fill_opacity = .2)
        text1 = VGroup(MyText("有了以上这个性质后，我们可以将通项公式进一步简化，不妨设"),TexMobject("N=n+1"),MyText(",则公式变为:")).arrange_submobjects(RIGHT/2).scale(0.7).next_to(tp,DOWN)
        form1 = TexMobject(r"S^{p}(n)=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \displaystyle {p+1 \choose k}  B_k {(n+1)}^{p+1-k} \right)}").scale(0.7).next_to(text1,DOWN)
        form2 = TexMobject(r"S^{p}(n)=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \displaystyle {p+1 \choose k}  B_k {N}^{p+1-k} \right)}").scale(0.7).next_to(text1,DOWN)
        form_ar = [
            r"S^{p}(N)",
            r"=(1^p+2^p+\cdots+n^p)+(n+1)^p",
            r"=S^{p}(n)+N^p",
            r"=N^p+\frac{1}{p+1}\left(\displaystyle {p+1 \choose 1}B_1 N^p + \displaystyle \sum_{k \in [3,p]}^{(k\text{为奇数})}{{p+1 \choose k}B_k N^{p+1-k}} + \displaystyle \sum_{k \in [0,p]}^{(k\text{为偶数})}{{p+1 \choose k}B_k N^{p+1-k}}\right)",
            r"=\frac{1}{p+1}\left(\frac{-(p+1)N^p}{2} + (p+1)N^p + \displaystyle \sum_{k \in [3,p]}^{(k\text{为奇数})}{{p+1 \choose k}B_k N^{p+1-k}} + \displaystyle \sum_{k \in [0,p]}^{(k\text{为偶数})}{{p+1 \choose k}B_k N^{p+1-k}}\right)",
            
            r"=\frac{1}{p+1}\left(-\displaystyle {p+1 \choose 1}B_1 N^p - \displaystyle \sum_{k \in [3,p]}^{(k\text{为奇数})}{{p+1 \choose k}B_k N^{p+1-k}} + \displaystyle \sum_{k \in [0,p]}^{(k\text{为偶数})}{{p+1 \choose k}B_k N^{p+1-k}}\right)", 
            r"=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \displaystyle (-1)^k {p+1 \choose k}  B_k {N}^{p+1-k} \right)}"
        ]
        form = TexMobject(*form_ar).scale(0.8)
        form5_1 = TexMobject(r"=\frac{1}{p+1}\left(-\displaystyle {p+1 \choose 1}B_1 N^p + 0 + \displaystyle \sum_{k \in [0,p]}^{(k\text{为偶数})}{{p+1 \choose k}B_k N^{p+1-k}}\right)").scale(0.8*0.78)
        form5_2 = TexMobject(r"=\frac{1}{p+1}\left(-\displaystyle {p+1 \choose 1}B_1 N^p + (-1)0 + \displaystyle \sum_{k \in [0,p]}^{(k\text{为偶数})}{{p+1 \choose k}B_k N^{p+1-k}}\right)").scale(0.8*0.78)      

        VGroup(
            tp[0][10],tp[0][16],
            form1[0][1],form1[0][8],form1[0][11],form1[0][18],form1[0][30],
            form2[0][1],form2[0][8],form2[0][11],form2[0][18],form2[0][26],
            form5_1[0][3],form5_1[0][10],form5_1[0][18],form5_1[0][34],form5_1[0][37],form5_1[0][45],
            form5_2[0][3],form5_2[0][10],form5_2[0][18],form5_2[0][38],form5_2[0][41],form5_2[0][49],
            form[0][1],
            form[1][3],form[1][6],form[1][13],form[1][21],
            form[2][2],form[2][8],
            form[3][2],form[3][6],form[3][12],form[3][20],form[3][34],form[3][37],form[3][45],form[3][63],form[3][66],form[3][74],
            form[4][3],form[4][10],form[4][15],form[4][20],form[4][25],form[4][39],form[4][42],form[4][50],form[4][68],form[4][71],form[4][79],
            form[5][3],form[5][10],form[5][18],form[5][32],form[5][35],form[5][43],form[5][61],form[5][64],form[5][72],
            form[6][3],form[6][6],form[6][18],form[6][26],
        ).set_color("#00FFFF")

        form[3].scale(0.82)
        form[4].scale(0.78)
        form[5].scale(0.78)

        form[4].to_edge(LEFT)
        form[0].next_to(form1,DOWN).align_to(form[4],LEFT)
        form[1].next_to(form[0],DOWN).align_to(form[4],LEFT)
        form[2].next_to(form[1],DOWN).align_to(form[4],LEFT)
        form[3].next_to(form[2],DOWN).align_to(form[4],LEFT)  
        form[5].align_to(form[4],LEFT)  

        self.play(FadeIn(tp),FadeIn(tp_bg))
        self.play(FadeIn(form1))
        self.wait(2)
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(ReplacementTransform(form1,form2))
        self.play(FadeIn(form[0]))
        self.wait(1)
        self.play(FadeIn(form[1]))
        self.wait(2.5)
        self.play(FadeIn(form[2]))
        self.wait(2)
        self.play(FadeIn(form[3]))
        self.wait(4.5)
        self.play(FadeOut(form[1]),FadeOut(form[2]))
        self.play(ApplyMethod(form[3].shift,1.75*UP))
        form[4].next_to(form[3],DOWN)
        self.play(FadeIn(form[4]))
        self.wait(5)
        form[5].next_to(form[4],DOWN)
        form[5].to_edge(LEFT)
        form5_1.move_to(form[5])
        form5_2.move_to(form[5])
        form5_1.to_edge(LEFT)
        form5_2.to_edge(LEFT)
        self.play(FadeIn(form5_1))
        self.wait(3)
        self.play(FadeOut(form5_1))
        self.play(FadeIn(form5_2))
        self.wait(3)
        self.play(FadeOut(form5_2))
        self.play(FadeIn(form[5]))
        self.wait(3.5)
        self.play(FadeOut(form[3]),FadeOut(form[4]))
        self.play(ApplyMethod(form[5].shift,2.75*UP))
        form[6].next_to(form[5],DOWN)
        form[6].to_edge(LEFT)
        self.play(FadeIn(form[6]))
        self.wait(4)
class Bernoulli2(Scene):
    def construct(self):
        text1 = MyText("于是我们得到最终的通项公式：").to_edge(UP)
        tex_2 = TexMobject("B","_{p}")
        tex_2[1].set_color("#00FFFF")
        text2 = VGroup(MyText("接下来会给出"),tex_2,MyText("的计算方法")).arrange_submobjects(RIGHT/2).to_edge(UP)
        tex_3 = TexMobject(r"\frac{x}{e^x-1}=\displaystyle \sum_{p=0}^{\infty}{\frac{x^p}{p!}B_p}")
        text3 = VGroup(MyText("首先还是根据定义有："),tex_3).arrange_submobjects(RIGHT/2).to_edge(UP)
        text4 = VGroup(MyText("将"),TexMobject("e^x"),MyText("泰勒展开后")).arrange_submobjects(RIGHT/2).to_edge(UP)
        text5 = MyText("因为等式右边只有常数项，根据对应系数相等，可以得到").to_edge(DOWN)
        tp = TexMobject(r"S^{p}(N)=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \displaystyle (-1)^k {p+1 \choose k}  B_k {N}^{p+1-k} \right)}").scale(0.8)

        form_ar = [
            r"\displaystyle \sum_{p=0}^{\infty}{\frac{x^p}{p!}B_p}",
            r"=\frac{x}{e^x-1}",
            r"=\frac{x}{\displaystyle \sum_{p=0}^{\infty}{\frac{x^p}{p!}-1}}",
            r"=\frac{x}{\displaystyle \sum_{p=1}^{\infty}{\frac{x^p}{p!}}}",
            r"=\frac{1}{\displaystyle \sum_{p=1}^{\infty}{\frac{x^{p-1}}{p!}}}",
            r"=\frac{1}{\displaystyle \sum_{p=0}^{\infty}{\frac{x^{p}}{(p+1)!}}}",
            r"\left( \displaystyle \sum_{p=0}^{\infty}{\frac{x^p}{p!}B_p} \right) \cdot \left( \displaystyle \sum_{p=0}^{\infty}{\frac{x^{p}}{(p+1)!}} \right) = 1",
            r"\displaystyle \sum_{p=0}^{\infty}{\sum_{k=0}^{p}{\left( \frac{x^k}{k!} B_k \cdot \frac{x^{p-k}}{(p-k+1)!} \right)}} = \displaystyle \sum_{p=0}^{\infty}{\left( \displaystyle \sum_{k=0}^{p}{\frac{B_k}{k!(p-k+1)!}} \right)x^p = 1}",
            r"\frac{B_0}{0!(0-0+1)!}=1, \displaystyle \sum_{k=0}^{p}{\frac{B_k}{k!(p-k+1)!}}=0 (p \neq 0)",
            r"B_0=1, \displaystyle \sum_{k=0}^{p}{\frac{(p+1)!}{k!(p-k+1)!}}B_k=0 (p \neq 0)",
            r"B_0=1, \displaystyle \sum_{k=0}^{p}{{p+1 \choose k}B_k=0 (p \neq 0)",
        ]
        form = TexMobject(*form_ar)

        VGroup(
            tp[0][1],tp[0][11],tp[0][23],tp[0][8],tp[0][31],
            tex_3[0][9],tex_3[0][13],tex_3[0][15],tex_3[0][18],
            form[0][2],form[0][6],form[0][8],form[0][11],
            form[2][5],form[2][9],form[2][11],
            form[3][5],form[3][9],form[3][11],
            form[4][5],form[4][9],form[4][13],
            form[5][5],form[5][9],form[5][12],
            form[6][3],form[6][7],form[6][9],form[6][12],form[6][18],form[6][22],form[6][25],
            form[7][2],form[7][5],form[7][20],form[7][25],form[7][36],form[7][40],form[7][51],form[7][60],
            form[8][16],form[8][27],form[8][37],
            form[9][5],form[9][11],form[9][20],form[9][32],
            form[10][5],form[10][11],form[10][21],
        ).set_color("#00FFFF")

        form[0].to_edge(LEFT)
        form[1].shift(LEFT*(form[1].get_left()[0]-form[0].get_right()[0]-0.25))
        form[2].shift(LEFT*(form[2].get_left()[0]-form[1].get_right()[0]-0.25))
        form[3].shift(LEFT*(form[3].get_left()[0]-form[2].get_right()[0]-0.25))
        form[7].scale(0.8)

        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeIn(tp))
        self.wait(5)
        self.remove(text1,tp)
        self.play(FadeIn(text2))
        self.wait(2)
        self.play(FadeOut(text2))
        self.play(FadeIn(text3))
        self.wait(2)
        self.play(FadeOut(text3))
        self.play(FadeIn(text4))
        self.play(FadeIn(form[0]),FadeIn(form[1].next_to(form[0],RIGHT)))
        self.wait(1)
        self.play(FadeIn(form[2]))
        self.wait(2)
        self.play(FadeOut(text4),FadeIn(form[3]))
        self.wait(2)
        self.play(FadeOut(form[1]),FadeOut(form[2]))
        self.play(ApplyMethod(form[3].shift,(LEFT*(form[3].get_left()[0]-form[0].get_right()[0]-0.25))))
        form[4].shift(LEFT*(form[4].get_left()[0]-form[3].get_right()[0]-0.25))
        form[5].shift(LEFT*(form[5].get_left()[0]-form[4].get_right()[0]-0.25))        
        self.play(FadeIn(form[4]))
        self.wait(2)
        self.play(FadeIn(form[5]))
        self.wait(3)
        self.play(FadeOut(form[3]),FadeOut(form[4]))
        self.play(ApplyMethod(form[5].shift,(LEFT*(form[5].get_left()[0]-form[0].get_right()[0]-0.25))))
        self.wait(2)
        self.play(ReplacementTransform(VGroup(form[0],form[5]),form[6].to_edge(LEFT)))
        self.wait(2)
        self.play(ApplyMethod(form[6].to_edge,UP))
        self.play(FadeIn(form[7].to_edge(LEFT)))
        self.wait(5.5)
        self.play(FadeOut(form[6]))
        self.wait(2)
        self.play(FadeIn(text5))
        self.wait(0.5)
        self.play(FadeIn(form[8].next_to(form[7],DOWN)))
        self.wait(4.5)
        self.play(ReplacementTransform(form[8],form[9].next_to(form[7],DOWN)))
        self.wait(4.5)
        self.play(ReplacementTransform(form[9],form[10].next_to(form[7],DOWN)))        
        self.wait(3)
class Computation(Scene):
    def construct(self):
        tex1 = TexMobject(r"B_0 = 1, B_1 = -\frac{1}{2}, B_{2p+1} = 0 (p \in \mathbb{Z}^+)").scale(0.8).to_edge(UP+LEFT)
        tex2 = TexMobject(r"\displaystyle \sum_{k=0}^{p}{{p+1 \choose k}B_k=0 (p \neq 0)").scale(0.8).to_edge(LEFT).next_to(tex1,DOWN)
        tex3 = TexMobject(r"{3 \choose 0}B_0 + {3 \choose 1}B_1 + {3 \choose 2}B_2 = 0").shift(0.5*DOWN)
        tex4 = TexMobject(r"B_0 + 3B_1 + 3B_2 = 1 - \frac{3}{2} + 3B_2 = 0").next_to(tex3,DOWN)
        tex5 = TexMobject(r"B_2 = \frac{1}{6}").next_to(tex4,DOWN)

        #self.add(tex2)
        #debugTeX(self,tex2[0])

        text1_ = TexMobject("B_p")
        text1_[0][1].set_color("#00FFFF")
        text1 = VGroup(MyText("有了这几条，我们就能将"),text1_,MyText("一项项计算出来，如:")).arrange_submobjects(RIGHT/2).to_edge(UP+RIGHT)
        text2 = VGroup(TexMobject("B_3"),MyText("由上可知为0")).arrange_submobjects(RIGHT/2).shift(0.5*DOWN)
        text3 = VGroup(MyText("于是"),TexMobject(r"1^3+2^3+\cdots+N^3")).arrange_submobjects(RIGHT/2).to_edge(UP+LEFT)
        text4 = VGroup(TexMobject("S^4(N),S^5(N),\cdots"),MyText("的求法也与之类似")).arrange_submobjects(RIGHT/2)
        text5 = MyText("所以到这里，我们就把等幂求和问题解决了")

        ha_arr = [
            r"=S^3(N)",
            r"=\frac{1}{p+1}\displaystyle \sum_{k=0}^{p}{\left( \displaystyle (-1)^k {p+1 \choose k}  B_k {N}^{p+1-k} \right)}",
            r"=\frac{1}{4}\displaystyle \sum_{k=0}^{3}{\left( \displaystyle (-1)^k {4 \choose k}  B_k {N}^{4-k} \right)}",
            r"=\frac{1}{4}(B_0 N^4 - 4B_1 N^3 + 6 B_2 N^2 - 4 B_3 N)",
            r"=\frac{1}{4}(N^4-4(-\frac{1}{2})N^3 + 6\cdot \frac{1}{6} N^2 - 4 \cdot 0 \cdot N)",
            r"=\frac{1}{4}(N^4+2N^3+N^2)",
            r"=\frac{N^2(N+1)^2}{4}"
        ]
        ha = TexMobject(*ha_arr).scale(0.8)

        VGroup(
            tex1[0][15],tex1[0][21],
            tex2[0][6],tex2[0][16],
            ha[1][6],ha[1][18],ha[1][3],ha[1][26],
        ).set_color("#00FFFF")

        ha[0].to_edge(UP).next_to(text3,RIGHT)
        for i in range(1,len(ha)):
            ha[i].next_to(ha[i-1],DOWN).align_to(ha[i-1],LEFT)

        tex1.next_to(text1,DOWN)
        tex2.next_to(tex1,DOWN)
        bg = SurroundingRectangle(VGroup(tex1,tex2), color=ORANGE, fill_opacity = .2)

        self.play(FadeIn(text1),FadeIn(tex1),FadeIn(tex2),FadeIn(bg))
        self.wait(1.5)
        self.play(FadeIn(tex3))
        self.wait(1.5)
        self.play(FadeIn(tex4))
        self.wait(1.5)
        self.play(FadeIn(tex5)) 
        self.wait(1.5)    
        self.remove(tex3,tex4,tex5)
        self.wait(1.5)
        self.play(FadeIn(text2))
        self.wait(2.5)
        self.remove(text1,text2,tex1,tex2,bg)
        self.play(FadeIn(text3))
        self.wait(1.5)
        self.play(FadeIn(ha[0]))
        self.wait(1.5)
        self.play(FadeIn(ha[1]))
        self.wait(3)
        self.play(FadeIn(ha[2]))
        self.wait(3)
        self.play(FadeIn(ha[3]))
        self.wait(2.5)
        self.play(FadeIn(ha[4]))
        self.wait(2.5)
        self.play(FadeIn(ha[5]))
        self.wait(2)
        self.remove(ha[1],ha[2],ha[3],ha[4])
        self.play(ApplyMethod(ha[5].shift,5.25*UP))
        self.wait(1)
        ha[6].align_to(ha[5],LEFT)
        self.play(FadeIn(ha[6].next_to(ha[5],DOWN).align_to(ha[5],LEFT)))
        self.wait(3)
        self.play(FadeOut(ha[0]),FadeOut(ha[5]),FadeOut(ha[6]),FadeOut(text3))
        self.play(FadeIn(text4))
        self.wait(2)
        self.play(ReplacementTransform(text4,text5))
        self.wait(2)
        self.play(FadeOut(text5))
class MoreApplications(Scene):
    def construct(self):
        text = MyText("伯努利数除了能应用于等幂求和问题，在很多三角函数的泰勒展开中也能起到作用").scale(0.7).to_edge(DOWN)
        arra = [r"\tan x =\displaystyle\sum _{n=1}^{\infty }{{(-1)^{n-1}2^{2n}(2^{2n}-1)",r"B_{2n}",r"}\over{(2n)!}}\;x^{2n-1},\left|x\right|<{\frac {\pi }{2}}}"]
        form = TexMobject(*arra)
        form[1].set_color(RED)

        self.play(Write(text),FadeIn(form))
        self.wait(2)
class MoreApplicationsGraph(GraphScene):
    CONFIG = {
        "x_min" : -PI/2+0.1,
        "x_max" : PI/2-0.1,
        "y_min" : -PI/2+0.1,
        "y_max" : PI/2-0.1,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
    }

    def construct(self):
        self.setup_axes(animate = False)
        self.x_axis.remove(self.x_axis[1])
        self.y_axis.remove(self.y_axis[1])

        func_to_tan = lambda x: np.tan(x)

        ap = []
        fun_ap = []
        ap.append(lambda x: x)
        ap.append(lambda x: x+x**3/3)
        ap.append(lambda x: x+x**3/3+2*x**5/15)
        ap.append(lambda x: x+x**3/3+2*x**5/15+17*x**7/315)

        for i in range(len(ap)):
            fun_ap.append(self.get_graph(ap[i], BLUE))

        func_tan = self.get_graph(func_to_tan, self.function_color)

        text = TexMobject(r"f(x) = \tan x",color=RED).scale(0.8).to_edge(UP+LEFT)
        ap_for = []
        ap_for.append(TexMobject(r"g(x)=x"))
        ap_for.append(TexMobject(r"g(x)=x+\frac{1}{3}x^3"))
        ap_for.append(TexMobject(r"g(x)=x+\frac{1}{3}x^3+\frac{2}{15}x^5"))
        ap_for.append(TexMobject(r"g(x)=x+\frac{1}{3}x^3+\frac{2}{15}x^5+\frac{17}{315}x^7"))

        for i in range(len(ap_for)):
            ap_for[i].scale(0.8).next_to(text,DOWN).align_to(text,LEFT).set_color(BLUE)

        self.play(Write(text))
        self.play(ShowCreation(func_tan))

        for i in range(len(fun_ap)):
            if i == 0:
                self.play(ShowCreation(fun_ap[0]),FadeIn(ap_for[0]))
            else:
                self.play(ReplacementTransform(fun_ap[i-1],fun_ap[i]),ReplacementTransform(ap_for[i-1],ap_for[i]))
            self.wait(1.5)
        self.wait(1.5)
#引用
class End(Scene):
    def construct(self):
        text = MyText("引用",color=YELLOW).scale(2).to_edge(UP)
        line =  Line(np.array([-10,0,0]),np.array([10,0,0])).next_to(text,DOWN)
        
        link1 = VGroup(Dot(color=BLUE),MyText("https://en.wikipedia.org/wiki/Bernoulli_number").scale(0.9)).arrange_submobjects(RIGHT/2).to_edge(LEFT)
        link2 = VGroup(Dot(color=BLUE),MyText("https://en.wikipedia.org/wiki/Faulhaber%27s_formula").scale(0.9)).arrange_submobjects(RIGHT/2).next_to(link1,DOWN).align_to(link1,LEFT)
        link3 = VGroup(Dot(color=BLUE),MyText("https://www.emis.de/journals/AMEN/2018/AMEN-170803.pdf").scale(0.9)).arrange_submobjects(RIGHT/2).next_to(link2,DOWN).align_to(link2,LEFT)

        self.play(FadeIn(text),FadeIn(line))
        self.play(Write(link1),Write(link2),Write(link3))