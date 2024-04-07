class Character():
  def __init__(self, username):
    self.__username=username
    self.__hp=100
    self.__mana=100
    self.__damage=5
    self.__str=0 #strength stat
    self.__vit=0 #vitality stat
    self.__int=0 #intelligence stat
    self.__agi=0 #agility stat
    self.__SPWins=0 #Singleplayer Wins
    self.__PVPWins=0 #Player Vs Player Wins
    self.__MaxHp=100 #Max HP
  def getUsername(self):
    return self.__username
  def setUsername(self, new_username):
    self.__username=new_username
  def getHp(self):
    return self.__hp
  def setHp(self, new_hp):
    self.__hp=new_hp
  def getMaxHp(self):
    return self.__MaxHp
  def setMaxHp(self, new_MaxHp):
    self.__MaxHp=new_MaxHp
  def getDamage(self):
    return self.__damage
  def setDamage(self, new_damage):
    self.__damage=new_damage
  def getStr(self):
    return self.__str
  def setStr(self, new_str):
    self.__str=new_str
  def getVit(self):
    return self.__vit
  def setVit(self, new_vit):
    self.__vit=new_vit
  def getInt(self):
    return self.__int
  def setInt(self, new_int):
    self.__int=new_int
  def getAgi(self):
    return self.__agi
  def setAgi(self, new_agi):
    self.__agi=new_agi
  def reduceHp(self, damage_amount):
    self.__hp=self.__hp-damage_amount
  def addHp(self, heal_amount):
    self.__hp=self.__hp+heal_amount
  def getSPWins(self):
    return self.__SPWins
  def addSPWins(self):
    self.__SPWins += 1
  def getPVPWins(self):
    return self.__PVPWins
  def addPVPWins(self):
    self.__PVPWins += 1
  def ClassAscension(self):
      self.__SPWins = 3
  def restoreHp(self):
      self.__Hp = self.__MaxHp
