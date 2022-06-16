from tokenize import String


class PdgaPlayer:
    def __init__(self,pdgaNumber,name,roundTotal,ratingRound,payout) :
      self.pdgaNumber = pdgaNumber
      self.name = name
      self.roundTotal = roundTotal
      self.ratingRound = ratingRound
      self.payout = payout
    def __repr__(self):
          return "%s %s %s %s %s" % (self.pdgaNumber,self.name,self.roundTotal,self.ratingRound,self.payout)
    def __str__(self):
        return "%s %s %s %s %s" % (self.pdgaNumber,self.name,self.roundTotal,self.ratingRound,self.payout)
    def get_pdgaNumber(self):
        return self.pdgaNumber
    def get_name(self):
        return self.name
    def get_roundTotal(self):
        return self.roundTotal
    def get_ratingRound(self):
        return self.ratingRound
    def get_payout(self):
        return self.payout
    