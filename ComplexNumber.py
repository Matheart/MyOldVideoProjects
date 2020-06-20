from manimlib.imports import *
import numpy as np
import math

class Titles(Scene):
    def construct(self):
        man = ImageMobject("icimages.jpg")
        title = TextMobject("Complex Number Theorems Visualisation")
        author = TextMobject("Made By Artanis")
        name = TextMobject("Abraham de Moivre (1667 - 1754)")
        name.shift(2*DOWN)
        author.shift(2*DOWN)
        self.play(Write(title))
        self.play(Write(author))
        self.wait(2)
        self.play(ApplyMethod(title.shift, 3*UP),FadeOut(author))
        self.play(FadeIn(man),Write(name))
        author.to_edge(RIGHT+DOWN)
        self.wait(3)

class Multiplication(Scene):
    def construct(self):
        label = TextMobject("Representation of Multiplication of Complex Numbers")
        self.play(FadeIn(label))
        self.wait(2)
        self.play(FadeOut(label))
        Say = TextMobject("Say $z$ and $w$ are two vectors on the plane")
        DefZ = TexMobject(r"Z = (r_{z}, \Theta_{z})")
        DefW = TexMobject(r"W = (r_{w}, \Theta_{w})")
        self.play(FadeIn(Say))
        self.wait(1)
        self.play(FadeOut(Say),FadeIn(DefZ))
        self.wait(1)
        self.play(FadeOut(DefZ),FadeIn(DefW))
        self.wait(2)
        Then = TexMobject(r"\text{Then } Z\cdot W = r_{z}(\cos \Theta_{z} + i \sin \Theta_{z}) \cdot\
                                           r_{w}(\cos \Theta_{w} + i \sin \Theta_{w})")
        Finally = TexMobject(r"Z\cdot W = [r_{z}r_{w}](\cos(\Theta_{z} + \Theta_{w}) + i \sin(\Theta_{z} + \Theta_{w}))")                                  
        self.play(FadeOut(DefW),ShowCreation(Then))
        self.wait(5)
        self.play(Transform(Then,Finally))
        self.wait(5)


class MultiplicationCoordin(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }

    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        vec_field = []
        L = Vector(1*RIGHT + 0.5*UP)
        R = Vector(1.5*RIGHT + 1*UP)

        Llabel = TexMobject("z")
        Rlabel = TexMobject("w")

        Llabel.shift(1.5*RIGHT + 0.5*UP)
        Rlabel.shift(2*RIGHT + 1*UP)

        vec_field.append(L)
        vec_field.append(R)
        
        draw_field = VGroup(*vec_field)

        self.play(ShowCreation(draw_field))              
        self.play(ShowCreation(Llabel))
        self.play(ShowCreation(Rlabel))

        #(2+i)*(3+2i)=6+7i-2=4+7i
        Result = Vector(2*RIGHT + 3.5*UP, color = RED)
        ResultLabel = TexMobject("z \cdot w")
        ResultLabel.shift(2.5*RIGHT+3.5*UP)
        self.play(ShowCreation(Result))
        self.play(ShowCreation(ResultLabel))
        self.wait(2)

        Accord = TextMobject("According to the formula :")
        Accord.shift(2*DOWN)
        self.play(FadeIn(Accord))
        self.wait(1)
        Finally = TexMobject(r"Z\cdot W = [r_{z}r_{w}](\cos(\Theta_{z} + \Theta_{w}) + i \sin(\Theta_{z} + \Theta_{w}))")             
        Finally.shift(2*DOWN)
        self.play(FadeOut(Accord),FadeIn(Finally))

        ArgA = TexMobject(r"\arg(z \cdot w)")
        ArgB = TexMobject(r"=")
        ArgC = TexMobject(r"\arg(z) + \arg(w)")
        ArgA.shift(DOWN)
        ArgB.next_to(ArgA)
        ArgC.next_to(ArgB)

        LengA = TexMobject("|z \cdot w|")
        LengB = TexMobject("=")
        LengC = TexMobject("|z||w|")

        LengA.align_to(ArgA, LEFT)
        LengB.align_to(ArgB, LEFT)
        LengC.align_to(ArgC, LEFT)

        LengA.shift(2*DOWN)
        LengB.shift(2*DOWN)
        LengC.shift(2*DOWN)

        eq_group = VGroup(ArgA, LengA)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("We can get:")

        self.wait(1)
        self.add(ArgA,ArgB,ArgC)
        self.add(LengA,LengB,LengC)
        self.play(Transform(Finally,braces), Write(eq_text))
        self.wait(1)

        Leng_Label = TexMobject("|z||w|")
        Leng_Label.shift(1.5*RIGHT+2.5*UP)

        #Arg_Label = TexMobject("\alpha + \beta")
        #zArg_label = TexMobject("\alpha")
        #wArg_label = TexMobject("beta")

        self.play(ShowCreation(Leng_Label))
        self.wait(2)

class DeMoivresTheorem(Scene):
    def construct(self):
        therefore = TextMobject("Therefore:")
        self.play(FadeIn(therefore))
        self.wait(2)
        self.play(FadeOut(therefore))
        for1 = TexMobject(r"z^2")
        for2 = TexMobject(r"z \cdot z")
        for3 = TexMobject(r"z^2 = r^2 (\cos 2\Theta + i \sin 2\Theta)")

        self.play(FadeIn(for1))
        self.wait(3)
        self.play(Transform(for1,for2))
        self.wait(3)
        self.play(Transform(for1,for3))
        self.wait(3)
        self.play(ApplyMethod(for1.shift, 3*UP))

        for4 = TexMobject(r"z^3")
        for5 = TexMobject(r"z \cdot z^2")
        for6 = TexMobject(r"[z \cdot z^2](\cos(\Theta + 2\Theta) + \sin(\Theta + 2\Theta))")
        for7 = TexMobject(r"z^3 = r^3 (\cos 3\Theta + i \sin 3\Theta)")
        self.play(FadeIn(for4))
        self.wait(3)
        self.play(Transform(for4,for5))
        self.wait(3)
        self.play(Transform(for4,for6))
        self.wait(3)
        self.play(Transform(for4,for7))
        self.play(ApplyMethod(for4.shift, 2*UP))

        General = TextMobject("More generally")
        self.play(FadeIn(General))
        self.wait(3)
        self.play(FadeOut(General))

        for8 = TexMobject(r"z^n = r^n (\cos n\Theta + i \sin n\Theta) (n \in \mathbf{N})")
        self.play(Write(for8))
        self.wait(3)
        call_theo = TextMobject("Which is called De Moivres Theorem")
        self.play(ApplyMethod(for8.shift, UP),FadeIn(call_theo))
        self.wait(2)
        self.play(FadeOut(call_theo))
        self.play(FadeIn(TextMobject("For Example:")))
        self.wait(2)

 
class DeMoivresTheoremCoordin(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }

    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        X = Vector(0.5*RIGHT + 1*UP,color = "RED") # 1+2i
        Y = Vector(-1.5*RIGHT + 2*UP, color = "GREEN") # -3+4i
        Z = Vector(-5.5*RIGHT + -1*UP, color = "BLUE") # -11-2i

        Xlabel = TexMobject("z:1+2i")
        Xlabel.shift(1.5*RIGHT + 1.5*UP)

        Ylabel = TexMobject("z^2:-3+4i")
        Ylabel.shift(-0.5*RIGHT + 2.5*UP)

        Zlabel = TexMobject("z^3:-11-2i")
        Zlabel.shift(-4.5*RIGHT -1.5*UP)      

        disc = TextMobject("We can discover that:")
        deg = TextMobject("The line rotates by a certain degree")
        lng = TextMobject("Its length is " + "$|z|$" + " times larger than the previous one")  
        disc.shift(2.5*DOWN)
        deg.shift(2.5*DOWN)
        lng.shift(2.5*DOWN)

        self.play(ShowCreation(X))              
        self.play(ShowCreation(Xlabel))
        self.wait(2)
        self.play(ShowCreation(Y))              
        self.play(ShowCreation(Ylabel))
        self.wait(2)
        self.play(ShowCreation(Z))              
        self.play(ShowCreation(Zlabel))
        self.wait(2)
        self.play(Write(disc))
        self.wait(1)
        self.play(Transform(disc, deg))
        self.wait(3)
        self.play(Transform(disc,lng))
        self.wait(4)

class NthRoot(Scene):
    def construct(self):
        ass = TexMobject(r"\text{The formula } z^n = r^n (\cos n\alpha + i \sin n\alpha) (n \in \mathbf{N})")
        know = TextMobject("Can also be used to get the n-th root of complex number")
        assume = TextMobject(r"Find the n-th root of $W(\rho,\phi)$, denoted as $(r,\Theta)$")
        Form = TexMobject(r"r^n (\cos n\alpha + i \sin n\alpha) = \rho (\cos \phi + i \sin \phi)")
        self.play(Write(ass))
        self.wait(1)
        self.play(Transform(ass,know))
        self.wait(3)
        self.play(Transform(ass,assume))
        self.play(ApplyMethod(ass.shift,2*UP))
        self.play(Write(Form))
        self.wait(2)
        self.play(ApplyMethod(Form.shift,UP))

        ha1 = [r"\cos n \Theta",r"=",r"\cos \phi"]
        ha2 = [r"\sin n \Theta",r"=",r"\sin \phi"]
        ha3 = [r"\rho",r"=",r"r^{n}"]

        eq1 = [TexMobject(i,color="ORANGE") for i in ha1]
        eq2 = [TexMobject(i,color="YELLOW") for i in ha2]
        eq3 = [TexMobject(i,color="RED") for i in ha3]

        eq1[1].next_to(eq1[0])
        eq1[2].next_to(eq1[1])

        for i in range(3):
            eq2[i].align_to(eq1[i], LEFT)
            eq3[i].align_to(eq1[i], LEFT)
            eq2[i].shift(DOWN)
            eq3[i].shift(2*DOWN)
        
        eq_group = VGroup(eq1[0],eq2[0],eq3[0])
        braces = Brace(eq_group, LEFT)

        for i in range(3):
            self.add(eq1[i])
            self.add(eq2[i])
            self.add(eq3[i])
        self.play(Write(braces))

        self.wait(5)

        for i in range(3):
            self.remove(eq1[i])
            self.remove(eq2[i])
            self.remove(eq3[i])

        lq = TexMobject(r"r = \rho^{\frac{1}{n}}")
        rq = TexMobject(r"n \Theta = \phi + 2k \pi")
        lrq = TexMobject(r"\Theta = \frac{\phi + 2k \pi}{n}")

        ex = TexMobject(r"\text{The n-th root can be expressed as } (\rho^{\frac{1}{n}},\frac{\phi + 2k \pi}{n})",color="GREEN")
        rq.shift(DOWN)
        rq.align_to(lq,LEFT)
        lrq.shift(DOWN)
        lrq.align_to(lq,LEFT)
        grp = VGroup(lq,rq)
        br = Brace(grp, LEFT)
        self.add(lq)
        self.add(rq)
        self.play(Transform(braces,br))
        self.wait(3)
        self.play(Transform(rq,lrq))
        self.wait(2)
        self.remove(lq)
        self.remove(rq)
        self.play(Transform(braces,ex))

        self.wait(5)
        self.remove(assume)
        self.remove(Form)
        self.remove(braces)

        geo = TextMobject("Geometrically, to find the n-th root of one complex number")
        find = TextMobject(r"is to find $(r,\Theta)$, which will reach that target (in polar coord.)")
        afte = TextMobject(r"after rotating n times by $\Theta$")
        fina = TextMobject("and its length becomes the n-th power of the original length")
        self.play(Write(geo))
        self.wait(2)
        self.play(Transform(geo,find))
        self.wait(2)
        self.play(Transform(geo,afte))
        self.wait(2)
        self.play(Transform(geo,fina))
        self.wait(3)

class NthRootCoordin(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }

    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        exam = TextMobject("For Example: Find the 3-rd roots of $-1$, denoted as $w$")
        exam.shift(0.5*DOWN)
        Method1 = TextMobject("Method 1")
        Method2 = TextMobject("Method 2")
        Method3 = TextMobject("Method 3")
        Method1.to_edge(UP+LEFT)
        Method2.to_edge(UP+LEFT)    
        Method3.to_edge(UP+LEFT)

        self.play(Write(exam))
        self.wait(2)
        self.play(FadeOut(exam))

        Orig = Vector(1*LEFT,color = "RED") # -1
        Fina = Vector(1*LEFT+0.01*UP,color="GREEN")
        FinaLabel = TexMobject(r"w^3(1,\pi)")
        FinaLabel.next_to(Fina)

        X = Vector((1/2)*RIGHT+(math.sqrt(3)/2)*UP,color="GREEN") # (1,pi/3)
        XLabel = TexMobject(r"w(1,\frac{\pi}{3})")
        XLabel.next_to(X)
        X1 = Vector((1/2)*LEFT+(math.sqrt(3)/2)*UP,color="GREEN") # (1,2/3 pi)
        X1Label = TexMobject(r"w^2(1,\frac{2}{3}\pi)")
        X1Label.next_to(X1)

        Y = Vector(1*LEFT+0.01*UP,color="GREEN") # (-1,0)
        YLabel = TexMobject(r"w(1,\pi)")
        YLabel.next_to(Y)
        Y1 = Vector(1*RIGHT,color="GREEN") #(1,0)
        Y1Label = TexMobject(r"w^2(1,0)")
        Y1Label.next_to(Y1)

        Z = Vector((1/2)*RIGHT+(math.sqrt(3)/2)*DOWN,color="GREEN") # (1,5/3 pi)
        ZLabel = TexMobject(r"w(1,\frac{5}{3}\pi)")
        ZLabel.next_to(Z)
        Z1 = Vector((1/2)*LEFT+(math.sqrt(3)/2)*DOWN,color="GREEN") # (1,4/3 pi)
        Z1Label = TexMobject(r"w^2(1,\frac{4}{3}\pi)")
        ZLabel.next_to(Z1)
 
        self.play(ShowCreation(Orig))

        self.play(Write(Method1))
        self.play(Write(X))
        self.play(Write(XLabel))
        self.wait(1)
        self.play(Transform(X,X1))
        self.play(Transform(XLabel,X1Label))
        self.wait(1)
        self.play(Transform(X,Fina),FadeOut(XLabel))
        self.play(Write(FinaLabel))

        self.wait(2)

        self.play(Transform(Method1,Method2))
        self.play(FadeOut(X),FadeOut(FinaLabel))
        self.play(Write(Y))
        self.play(Write(YLabel))
        self.wait(1)
        self.play(Transform(Y,Y1))
        self.play(Transform(YLabel,Y1Label))
        self.wait(1)
        self.play(Transform(Y,Fina),FadeOut(YLabel))
        self.play(Write(FinaLabel))

        self.wait(2)

        self.play(Transform(Method1,Method3))
        self.play(FadeOut(Y),FadeOut(FinaLabel))
        self.play(Write(Z))
        self.play(Write(ZLabel))
        self.wait(1)
        self.play(Transform(Z,Z1))
        self.play(Transform(ZLabel,Z1Label))
        self.wait(1)
        self.play(Transform(Z,Fina),FadeOut(ZLabel))
        self.play(Write(FinaLabel))

        self.wait(2)
        self.play(FadeOut(Method1))
        self.play(FadeOut(Z))
        self.wait(2)

class RootOfUnity(Scene):
    def construct(self):
        Supple = TextMobject("Supplementary Information:")
        uni = TextMobject("Roots of Unity: n-th roots of 1")
        iss = TexMobject(r"(1^{\frac{1}{n}},\frac{0+2k\pi}{n})")
        zing = TexMobject(r"(1,\frac{2k\pi}{n})")
        cs = TexMobject(r"\cos \frac{2k\pi}{n} + i \sin \frac{2k\pi}{n}")
        es = TexMobject(r"e^{\frac{2ki\pi}{n}}")
        self.play(Write(Supple))
        self.wait(1)
        self.play(Transform(Supple,uni))
        self.wait(2)
        self.play(Transform(Supple,iss))
        self.wait(2)
        self.play(Transform(Supple,zing))
        self.wait(3)
        self.play(Transform(Supple,cs))
        self.wait(4)
        self.play(Transform(Supple,es))
        self.wait(2)
        
class RootOfUnityCoordin(Scene):
    CONFIG = { "plane_kwargs" : { 
        "color" : RED,
        },
    }

    def construct(self):
        my_plane = ComplexPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels(x_label_tex="Re",y_label_tex="Im"))
        self.add(my_plane)

        prope = TextMobject("By ultilising the property of rotation")
        get = TextMobject("We can visualise the result")
        self.play(Write(prope))
        self.wait(2)
        self.play(Transform(prope,get))
        self.wait(2)
        self.play(FadeOut(prope))

        circle = Circle(color=WHITE,radius=4)
        self.play(ShowCreation(circle))

        col = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE,GREY,PINK,BLACK]
        old_field = VGroup(circle)
        old_label = TextMobject("")
        old_label.to_edge(LEFT+UP)
        for n in range(1,9):
            gp = [circle]
            for k in range(n):
                x = math.cos(2*k*math.pi/n)
                y = math.sin(2*k*math.pi/n)
                line = Line(np.array([0,0,0]),np.array([x*4,y*4,0]),color = col[k])
                gp.append(line)
            draw_field = VGroup(*gp)
            new_label = TextMobject("n = "+str(n))
            new_label.to_edge(LEFT+UP)
            self.play(Transform(old_field,draw_field))
            self.play(Transform(old_label,new_label))
            self.wait(1-n/20)

class GoodBye(Scene):
    def construct(self):
        creature = ImageMobject("SupportIcon.jpg")
        gb = TextMobject("Good Bye!")
        snt = TextMobject("And see you next time!")
        gb.to_edge(UP)
        snt.to_edge(UP)

        self.play(Write(gb),FadeIn(creature))
        self.wait(2)
        self.play(Transform(gb,snt))
        self.wait(10)
#SupportIcon.png