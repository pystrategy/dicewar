# -*- coding: utf-8 -*-
import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox



class ButtonTestApp(App):
    def onPressBtn( self, instance ):
        print 'press button : %s' % instance.text
        self.tmpLabel.text = '%s' % instance.text

    def onCheckboxActive(self, checkbox, value):
        if value:
            self.tmpLabel.text = 'active : %s' % checkbox.btnName
        else:
            self.tmpLabel.text = 'inactive : %s' % checkbox.btnName

    def onRadioActive( self, radio, value ):
        self.tmpLabel.text = 'radio : %s' % radio.btnName

    def build(self):
        # 레이아웃
        layout = FloatLayout()

        # 표기에 사용할 라벨
        textLabel = Label(
            text='___________',
            size_hint=(1.0, 0.2),
            pos_hint={'x':0.0, 'y':0.8 } )
        layout.add_widget( textLabel )

        self.tmpLabel = textLabel

        btn1 = Button(
            text='Hello',
            size_hint=(0.5,0.2))

        btn1.bind( on_press=self.onPressBtn )
        layout.add_widget(btn1)

        btn2 = Button(
            text='World',
            pos_hint = {'x':0.5, 'y':0},
            size_hint=(0.5,0.2))

        btn2.bind( on_press=self.onPressBtn )
        layout.add_widget(btn2)

        # 여기서 라디
        btnInfoList = [ '1111', '2222', '3333' ]

        for idx, name in enumerate( btnInfoList ):
            widthStep = 1.0 / len(btnInfoList)
            _sizeHint = ( widthStep, 0.2 )
            _posHint = {'x':idx*widthStep, 'y':0.2 }
            tBtn = ToggleButton(
                text=name,
                group='sex',
                pos_hint=_posHint,
                size_hint=_sizeHint,
                state='down' if idx == 1 else 'normal' )

            tBtn.bind( on_press=self.onPressBtn )
            layout.add_widget(tBtn )


        #checkLayout = GridLayout( row=2, spacing=2, pos_hint={'x':0,'y':0.6}, size_hint=(1.0,0.2))
        #layout.add_widget(checkLayout)

        for idx in xrange(3):
            checkbox = CheckBox( active=0, pos_hint={'x':float(idx)/3, 'y':0.4}, size_hint=(0.3, 0.2))
            checkbox.bind(active=self.onCheckboxActive)
            checkbox.btnName = 'check %s' % idx
            layout.add_widget( checkbox )

        #------------------------------------------------------------------------------
        # 라디오
        for idx in xrange(3):
            radioBtn = CheckBox(
                active = 1 if idx == 1 else 0,
                group='tmp_group',
                pos_hint={'x': float(idx)/3, 'y':0.6},
                size_hint=(0.3, 0.2))

            radioBtn.btnName = 'radio %s' % idx
            radioBtn.bind(active=self.onRadioActive)
            layout.add_widget( radioBtn )

        return layout


if __name__ == '__main__':
    ButtonTestApp().run()
