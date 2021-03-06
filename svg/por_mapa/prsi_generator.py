#!/bin/python2.7
# -*- coding: utf-8 -*-

from lxml import etree, objectify
import simplejson as json
import sys


class prsi():
    def __init__(self, tabulka_barev, pattern):
        """
        """
        self.prsi = str(pattern)[0:3]
        self.barva_1 = str(pattern)[3]
        self.barva_2 = str(pattern)[4]

        self.tabulka_barev = tabulka_barev

        self.E = objectify.ElementMaker(annotate=False)

        self.generuj_pattern()

        self.svg = self.E.svg(
                *self.pattern,
                width="8", height="8"
                , viewBox = "0 0 8 8"
                , version = "1.1"
                )

        print(etree.tostring(self.svg, pretty_print = True))

    def generuj_pattern(self):

        if self.prsi == '100':
            self.pattern = [
                    self.E.rect(
                        width="8", height="8", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "0", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "2", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "4", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "6", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    ]

        elif self.prsi == '101':
            self.pattern = [
                    self.E.rect(
                        width="8", height="8", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    ]
        elif self.prsi == '200':
            self.pattern = [
                    self.E.rect(
                        width="8", height="8", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "0", y = "0", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "2", y = "4", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "4", y = "0", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "6", y = "4", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    ]
        elif self.prsi == '250' :
            self.pattern = [
                    self.E.rect(
                        x = "0", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "2", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "4", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "6", y = "0", width="1", height="8", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "1", y = "0", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "3", y = "4", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "5", y = "0", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "7", y = "4", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    ]
        elif self.prsi == '260' :
            self.pattern = [
                    self.E.rect(
                        x = "0", y = "0", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "2", y = "4", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "4", y = "0", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "6", y = "4", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_1]
                        )
                    , self.E.rect(
                        x = "1", y = "2", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "3", y = "6", width="1", height="2", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "3", y = "0", width="1", height="1", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "5", y = "2", width="1", height="3", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "7", y = "6", width="1", height="2", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    , self.E.rect(
                        x = "7", y = "0", width="1", height="1", 
                        fill=self.tabulka_barev[self.barva_2]
                        )
                    ]



###tabulka barev
with open('barvy.json','r') as f:
    barvy = json.load(f)

with open('barvy_prsi.json','r') as f:
    barvy_prsi = json.load(f)

tabulka_barev = {
        k:barvy[v] for k, v in barvy_prsi.iteritems()}

prsi(tabulka_barev, str(sys.argv[1]))
