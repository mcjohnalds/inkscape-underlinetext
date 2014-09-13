#!/usr/bin/env python
import sys
sys.path.append('/usr/share/inkscape/extensions')
import inkex

class UnderlineEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

    def effect(self):
        for id in self.selected:
            sel = self.getElementById(id)
            if sel.tag == '{http://www.w3.org/2000/svg}text':
                for e in sel.getchildren():
                    if e.tag == '{http://www.w3.org/2000/svg}tspan':
                        toggleTspanUnderline(e)

def toggleTspanUnderline(e):
    if e.get('text-decoration') == None:
        e.set('text-decoration', '')

    e.set('style', '')

    styles = e.get('text-decoration').split(',')

    if '' in styles:
        styles.remove('')

    if 'underline' in styles:
        styles.remove('underline')
    else:
        styles.append('underline')

    e.set('text-decoration', ','.join(map(str, styles)))

effect = UnderlineEffect()
effect.affect()