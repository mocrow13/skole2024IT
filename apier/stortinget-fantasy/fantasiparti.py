from politiker import Politiker

class Fantasiparti:
    def __init__ (self,navn:str, eier: str)->None:
        self.navn: str=navn
        self.eier:str=eier
        self.poeng:int=0
        self.saldo:int=100_000
        self.partileder:Politiker=None
        self.politikere:list[Politiker]=[]
    def kjøp_politiker(self,politiker:Politiker):
        if self.saldo>=politiker.verdi:
                self.politikere.append(politiker)
                self.saldo-=politiker.verdi 
       
    def selg_politiker(self,politiker:Politiker):
        if politiker in self.politikere:
            self.politikere.remove(politiker)
            self.saldo+=politiker.verdi 
    def vis_partioversikt(self,politiker:Politiker):
        for politiker in self.politikere:
            print(politiker, politiker.id)
    def __str__(self)->str:
        return f"{self.navn}-{self.eier}({self.poeng})"