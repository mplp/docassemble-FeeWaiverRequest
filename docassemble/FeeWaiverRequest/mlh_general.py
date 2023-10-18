from docassemble.AssemblyLine.al_general import (
  ALIndividual
)

class MLHAttorney(ALIndividual):
    def init(self, *pargs, **kwargs):
        super(ALIndividual, self).init(*pargs, **kwargs)

    def f(self):
        return 'wtf mate?'