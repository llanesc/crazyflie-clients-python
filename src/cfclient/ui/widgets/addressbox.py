#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     ||          ____  _ __
#  +------+      / __ )(_) /_______________ _____  ___
#  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
#  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
#  Copyright (C) 2011-2013 Bitcraze AB
#
#  Crazyflie Nano Quadcopter Client
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License along with
#  this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
This class provides a spin box with hexadecimal numbers and arbitrarily length
(i.e. not limited by 32 bit).
"""

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QAbstractSpinBox

__author__ = 'Bitcraze AB'
__all__ = ['AddressBox']


class AddressBox(QLineEdit):
    valueChanged = pyqtSignal(object)
    sitlChanged = pyqtSignal(object)
    HEX_ADDRESS_TYPE = 0
    IP_ADDRESS_TYPE = 1
    address_types = [HEX_ADDRESS_TYPE, IP_ADDRESS_TYPE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.address_type = self.HEX_ADDRESS_TYPE
        self.regexp = QtCore.QRegularExpression('^0x[0-9A-Fa-f]{1,10}$')
        self.validator = QtGui.QRegularExpressionValidator(self.regexp)
        self.setValidator(self.validator)

    def validate(self, text, pos):
        self.validator.validate(text, pos)
    
    def change_type(self, address_type):
        if address_type in self.address_types:
            self.address_type = address_type
            match address_type:
                case self.HEX_ADDRESS_TYPE:
                    self.regexp = QtCore.QRegularExpression('^0x[0-9A-Fa-f]{1,10}$')
                case self.IP_ADDRESS_TYPE:
                    self.regexp = QtCore.QRegularExpression('^(([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5])\\.){3}([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5]){1}$')

            self.validator = QtGui.QRegularExpressionValidator(self.regexp)
            self.setValidator(self.validator)
    # def validate(self, text, pos):
    #     if self.address_type == self.HEX_ADDRESS_TYPE:
            
    #     elif self.address_type == self.IP_ADDRESS_TYPE:
    #         regexp = QtCore.QRegExp('[0-2][0-9][0-9][.][0-2][0-9][0-9][.][0-2][0-9][0-9][.][0-2][0-9][0-9]')
    #         self.validator = QtGui.QRegExpValidator(regexp)
    #     return self.validator.validate(text, pos)

    # def textFromValue(self, value):
    #     return "0x%X" % value

    # def valueFromText(self, text):
    #     return int(str(text), 0)

    # def setValue(self, value):
    #     self._value = value
    #     self.setText(self.textFromValue(value))
    #     self.valueChanged.emit(self._value)
        
    # def value(self):
    #     self._value = self.valueFromText(self.text())
    #     return self._value

    # def stepBy(self, steps):
    #     self.setValue(self._value + steps)

    # def stepEnabled(self):
    #     return (QLineEdit.StepUpEnabled |
    #             QLineEdit.StepDownEnabled)

    # def is_text_different_from_value(self):
    #     return self._value != self.valueFromText(self.text())
