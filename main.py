from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from kivy.core.window import Window

Window.size=(700,700)

class Program(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main=FloatLayout()

        self.sm=ScreenManager(transition=SlideTransition(),
                              size_hint=(1,0.9),
                              pos_hint={'x':0,'y':0})
        
        
###це калькулятор 1
        self.calculationscreen = Screen(name='calculation')
        
        self.calculation_layout=FloatLayout()


        self.priklad=''

        self.examplelabel=Label(
            text='',
            size_hint=(0.65,0.1),
            pos_hint={'x':0.1,'y':0.8},
            font_size=(30)

        )

        self.buttonC=Button(
            text='C',
            size_hint=(0.25,0.14),
            pos_hint={'x':0,'y':0.635}
        )
        self.buttonC.bind(on_press=lambda x:self.delcalcall1())
        self.buttonopen=Button(
            text='(',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.25,'y':0.635}
        )
        self.buttonopen.bind(on_press=lambda x:self.add_to_label1('('))
        self.buttonclose=Button(
            text=')',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.5,'y':0.635}
        )
        self.buttonclose.bind(on_press=lambda x:self.add_to_label1(')'))
        self.buttondivide=Button(
            text='÷',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.75,'y':0.635}
        )
        self.buttondivide.bind(on_press=lambda x:self.add_to_label1('÷','/'))

        self.button7=Button(
            text='7',
            size_hint=(0.25,0.14),
            pos_hint={'x':0,'y':0.495}
        )
        self.button7.bind(on_press=lambda x:self.add_to_label1('7'))
        self.button8=Button(
            text='8',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.25,'y':0.495}
        )
        self.button8.bind(on_press=lambda x:self.add_to_label1('8'))
        self.button9=Button(
            text='9',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.5,'y':0.495}
        )
        self.button9.bind(on_press=lambda x:self.add_to_label1('9'))
        self.buttonmultiplate=Button(
            text='x',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.75,'y':0.495}
        )
        self.buttonmultiplate.bind(on_press=lambda x:self.add_to_label1('x','*'))
        self.button4=Button(
            text='4',
            size_hint=(0.25,0.14),
            pos_hint={'x':0,'y':0.355}
        )
        self.button4.bind(on_press=lambda x:self.add_to_label1('4'))
        
        self.button5=Button(
            text='5',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.25,'y':0.355}
        )
        self.button5.bind(on_press=lambda x:self.add_to_label1('5'))
        self.button6=Button(
            text='6',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.5,'y':0.355}
        )
        self.button6.bind(on_press=lambda x:self.add_to_label1('6'))
        self.buttonminus=Button(
            text='-',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.75,'y':0.355}
        )
        self.buttonminus.bind(on_press=lambda x:self.add_to_label1('-'))
        self.buttonplus=Button(
            text='+',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.75,'y':0.215}
        )
        self.buttonplus.bind(on_press=lambda x:self.add_to_label1('+'))
        self.button3=Button(
            text='3',
            size_hint=(0.25,0.14),
            pos_hint={'x':0,'y':0.215}
        )
        self.button3.bind(on_press=lambda x:self.add_to_label1('3'))
        self.button2=Button(
            text='2',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.25,'y':0.215}
        )
        self.button2.bind(on_press=lambda x:self.add_to_label1('2'))

        self.button1=Button(
            text='1',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.5,'y':0.215}
        )
        self.button1.bind(on_press=lambda x:self.add_to_label1('1'))
        self.buttondot=Button(
            text=',',
            size_hint=(0.25,0.14),
            pos_hint={'x':0,'y':0.075}
        )
        self.buttondot.bind(on_press=lambda x:self.add_to_label1(',','.'))
        self.button0=Button(
            text='0',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.25,'y':0.075}
        )
        self.button0.bind(on_press=lambda x:self.add_to_label1('0'))
        self.buttondel=Button(
            text='del',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.5,'y':0.075}
        )
        self.buttondel.bind(on_press=lambda x:self.delcalcone1())
        


        self.buttonequvate=Button(
            text='=',
            size_hint=(0.25,0.14),
            pos_hint={'x':0.75,'y':0.075}
        )
        self.buttonequvate.bind(on_press=lambda x:self.equvate())



####це калькулятор 2
        self.buttondict={'+':'-','-':'x','x':'÷','÷':'+'}
        self.fractioncalculationscreen=Screen(name='fraction_calculation')
        self.fractioncalculationlayout=FloatLayout()

        self.wholeinputtext1=TextInput(
            text='',
            size_hint=(0.1,0.08),
            pos_hint={'x':0.05,'y':0.5},
            font_size=(30)
        )
        self.numerationtextinput1=TextInput(
            text='',
            size_hint=(0.1,0.06),
            pos_hint={'x':0.15,'y':0.54},
            font_size=(30)
        )
        self.denominatortextinput1=TextInput(
            text='',
            size_hint=(0.1,0.06),
            pos_hint={'x':0.15,'y':0.48 },
            font_size=(30)
        )
        self.buttonaction=Button(
            text='+',
            size_hint=(0.1,0.08),
            pos_hint={'x':0.27,'y':0.5},
            font_size=(30)
        )
        self.buttonaction.bind(on_press= lambda x:self.changebuttonfraction(self.buttonaction.text))


        self.wholeinputtext2=TextInput(
            text='',
            size_hint=(0.1,0.08),
            pos_hint={'x':0.39,'y':0.5},
            font_size=(30)
        )
        self.numerationtextinput2=TextInput(
            text='',
            size_hint=(0.1,0.06),
            pos_hint={'x':0.49,'y':0.54},
            font_size=(30)
        )
        self.denominatortextinput2=TextInput(
            text='',
            size_hint=(0.1,0.06),
            pos_hint={'x':0.49,'y':0.48 },
            font_size=(30)
        )
        self.equalbutton=Button(
            text='=',
            size_hint=(0.1,0.08),
            pos_hint={'x':0.61,'y':0.5}
        )
        self.equalbutton.bind(on_press=lambda x:self.equation2(self.wholeinputtext1.text,self.numerationtextinput1.text,self.denominatortextinput1.text,self.wholeinputtext2.text,self.numerationtextinput2.text,self.denominatortextinput2.text))
        self.outputlabel1=Label(
            text='',
            size_hint=(0.1,0.08),
            pos_hint={'x':0.73,'y':0.5},
            font_size=(30)
        )
        self.outputlabel2=Label(
            text='',
            size_hint=(0.1,0.06),
            pos_hint={'x':0.85,'y':0.54},
            font_size=(30)
        )
        self.outputlabel3=Label(
            text='',
            size_hint=(0.1,0.06),
            pos_hint={'x':0.85,'y':0.48 },
            font_size=(30)
        )








####це інформація
        self.informationscreen=Screen(name='information')

        self.informationlabel=Label(
            text=(' Програма створена Кошинським Станіславом \n друга програма в ківі,а саме калькулятор + калькулятор дробів \n обираєте режим і вводите дані і натискаєте на обчислити \n дякую за увагу'),
            size_hint=(0.5,0.5),
            pos_hint={'x':0.25,'y':0.25}
        
        )




        


        self.changescreen=FloatLayout(
            size_hint=(1,0.1),
            pos_hint={'x':0,'y':0.9}

        )

        self.buttonscreen1=Button(
            text='oo',
            size_hint=(0.33,1),
            pos_hint={'x':0,'y':0}
        )
        self.buttonscreen1.bind(on_press=lambda x:self.change_screen('calculation'))
        self.buttonscreen2=Button(
            text='oo',
            size_hint=(0.33,1),
            pos_hint={'x':0.33,'y':0}
        
        )
        self.buttonscreen2.bind(on_press=lambda x:self.change_screen('fraction_calculation'))
        self.buttonscreen3=Button(
            text='oo',
            size_hint=(0.33,1),
            pos_hint={'x':0.66,'y':0}
        )
        self.buttonscreen3.bind(on_press=lambda x:self.change_screen('information'))











        self.main.add_widget(self.changescreen)#add to main
        self.main.add_widget(self.sm)




        self.sm.add_widget(self.calculationscreen)#add to sm
        self.sm.add_widget(self.fractioncalculationscreen)
        self.sm.add_widget(self.informationscreen)




        self.calculationscreen.add_widget(self.calculation_layout)#add to calculationscreen



        self.calculation_layout.add_widget(self.examplelabel)
        self.calculation_layout.add_widget(self.buttonC)
        self.calculation_layout.add_widget(self.buttonopen)
        self.calculation_layout.add_widget(self.buttonclose)
        self.calculation_layout.add_widget(self.buttondivide)
        self.calculation_layout.add_widget(self.button7)
        self.calculation_layout.add_widget(self.button8)
        self.calculation_layout.add_widget(self.button9)
        self.calculation_layout.add_widget(self.buttonmultiplate)
        self.calculation_layout.add_widget(self.button6)
        self.calculation_layout.add_widget(self.button5)
        self.calculation_layout.add_widget(self.button4)
        self.calculation_layout.add_widget(self.buttonminus)
        self.calculation_layout.add_widget(self.button0)
        self.calculation_layout.add_widget(self.buttondot)
        self.calculation_layout.add_widget(self.buttonplus)
        self.calculation_layout.add_widget(self.buttondel)
        self.calculation_layout.add_widget(self.buttonequvate)
        self.calculation_layout.add_widget(self.button1)
        self.calculation_layout.add_widget(self.button2)
        self.calculation_layout.add_widget(self.button3)



        self.changescreen.add_widget(self.buttonscreen1)#add to chamgescreen
        self.changescreen.add_widget(self.buttonscreen2)
        self.changescreen.add_widget(self.buttonscreen3)
  




        self.fractioncalculationscreen.add_widget(self.fractioncalculationlayout)
        self.fractioncalculationlayout.add_widget(self.wholeinputtext1)
        self.fractioncalculationlayout.add_widget(self.numerationtextinput1)
        self.fractioncalculationlayout.add_widget(self.denominatortextinput1)
        self.fractioncalculationlayout.add_widget(self.buttonaction)
        self.fractioncalculationlayout.add_widget(self.wholeinputtext2)
        self.fractioncalculationlayout.add_widget(self.numerationtextinput2)
        self.fractioncalculationlayout.add_widget(self.denominatortextinput2)
        self.fractioncalculationlayout.add_widget(self.equalbutton)
        self.fractioncalculationlayout.add_widget(self.outputlabel1)
        self.fractioncalculationlayout.add_widget(self.outputlabel2)
        self.fractioncalculationlayout.add_widget(self.outputlabel3)



        self.informationscreen.add_widget(self.informationlabel)

    def equvate(self,a=None):
        try:
            self.priklad=str(eval(self.priklad))
            self.examplelabel.text=self.priklad
        except:
            self.examplelabel.text='Некоректні дужки'
            self.priklad=''
    def delcalcone1(self,a=None):
        if self.examplelabel.text=='Некоректні дужки':
            self.examplelabel.text=''
            self.priklad=''
        
        else:
            self.examplelabel.text=self.examplelabel.text[:-1]
            self.priklad=self.priklad[:-1]

    def delcalcall1(self,a=None):
        

        self.examplelabel.text=''
        self.priklad=''

    def add_to_label1(self,a,b=None):

        if b==None:b=a
        if self.examplelabel.text=='Некоректні дужки':
            self.examplelabel.text=a
            self.priklad=b
        else:
            self.examplelabel.text+=a
            self.priklad+=b



    def changebuttonfraction(self,a):
        self.buttonaction.text={'+':'-','-':'x','x':'÷','÷':'+'}[a]

    def equation2(self,a1,a2,a3,b1,b2,b3):
        try:
            a1,a2,a3,b1,b2,b3=int(a1),int(a2),int(a3),int(b1),int(b2),int(b3)
        except:
            self.outputlabel1='Введено некоректні дані'
            return
        if a3!=0 and b3!=0:

            up1=a1*a3+a2
            up2=b1*b3+b2
            if self.buttonaction.text=='+':
                up1*=b2
                up2*=a3
                a3*=b3
                ansver=up1+up2
            elif self.buttonaction.text=='-':
                up1*=b3
                up2*=a3
                a3*=b3
                ansver=up1-up2
            elif self.buttonaction.text=='x':
                ansver=up1*up2
                a3=a3*b3
            elif self.buttonaction.text=='÷':
                ansver=up1*b3
                a3=a3*up2
            self.outputlabel1.text=str(ansver//a3)
            up=ansver-(ansver//a3)*a3
            for i in range(up,1,-1):
                if up%i==0 and a3%i==0:
                    up,a3=up/i,a3/i
            if up==0:a3=1
            self.outputlabel2.text=str(up)
            self.outputlabel3.text=str(a3)
        else:self.outputlabel1='Введено некоректні дані'


    def change_screen(self,a):
        if self.sm.current_screen==self.informationscreen:self.sm.transition.direction='right'
        elif self.sm.current_screen==self.calculationscreen:self.sm.transition.direction='left'
        elif a=='calculation':self.sm.transition.direction='right'
        else:self.sm.transition.direction='left'
        self.sm.current=(a)




    def build(self):
        return self.main



if __name__=='__main__':
    Program().run()