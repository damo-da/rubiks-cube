'''Links the program with the databse for algorithms.'''

from headers import *
from sqlite3 import dbapi2 as sqlite

class Algorithm(object):
    '''The class for the linker.'''
    def open(self):
        '''Opens the database'''
        self.db=DBhandler()
    def __init__(self):
        self.open()

    def getRulesSQLFilter(self,rules):
        '''Returns a SQL check for a list of rules.
        [1,2,4] would returl (ruleID=1 or ruleID=2 or ruleID=4).'''
        string="( "
        for rule in rules:
            string += " ruleID={} ".format(rule)
            if rule != rules[len(rules)-1]:
                string += " or "
        string += ")"
        return string
        
    def getAnswerForF2lSecondLineBringBoxToTopTransformation(self,pos):
        '''Returns answer for the second layer solving, bringing box from second layer to top.
        For eg, a front-left side of second layer is not solved and it lies in position (2,0,0),
        it returns an algorithm for bringing an item from (2,0,0) into the top layer.'''
        ruleID=self.getRulesOfCategory("f2l-secondLineBringBoxToTop")
        boxID=getIdFromPos(pos)
        
        c1=self.getRulesSQLFilter(ruleID)
        c2="boxID={}".format(boxID)
        
        SQL="SELECT ruleID from boxPosition where {} and {}".format(c1,c2)
        return self.getAnswerForRuleID(self.getRuleIDfromBoxesBySQL(SQL)[0])
    
    def getRulesOfCategory(self,cat):
        '''Generate SQL condition for a category, which returns all the rules involved with then category.
        getRulesOfCategory('f2l') woud return all ruleIDs of category f2l.'''
        SQL="SELECT id from rule where categoryName='{0}'".format(cat)
        cursor=self.db.query(SQL)
        lista=cursor.fetchall()
        for i in range(len(lista)):
            lista[i]=lista[i][0]
        return lista
    
    def getPlaneColorSearchSQL(self,color):
        '''Generates a color search SQL.
        For the return string, use .format("xz") or whatever in the form you use it.'''        
        ret="( {0}='-1' or "
        ret += "{0}='%s'"%FaceColor.getSideForColor(color)+" or "
        
        colors=FaceColor.getSidesExcludingColor(color)
        for c in colors:
            ret += "{0}='!%s'"%(str(c))
            if c!=colors[len(colors)-1]:
                ret +=" or "
        ret += ")"
        
        return ret
        
    def getPlaneColorSearchSQLOpposite(self,color):#accepts a color, then searches its negative, eg, yellow would give rise to {0}="!yellow"
        '''just opposite of getPlaneColorSearchSQL.
        SQL such that a given color is made not to exist in the database.'''
        
        ret = "( not({0}='%s')"%FaceColor.getSideForColor(color)+" and ( "
        
        colors=FaceColors.getSidesExcludingColor(color)
        for i in range(len(colors)):
            ret += "{0}='%s'"%(str(c))
            if i != (len(colors)-1):
                ret +=" or "
        ret += "))"

        return ret
        
    def getRuleIDfromBoxesBySQL(self,SQL):
        '''Returns an array of ruleIDs of the records of the boxposition table of database as from the SQL argument supplied.'''
        ID=0
        ret=self.db.query(SQL).fetchall()
        for i in range(len(ret)):
            ret[i]=ret[i][0]
        return ret
        
    def getAnswerForf2lSecondLineTransformation(self,level,box):
        '''Returns for f2l-secondLine transformation, from top level to its right position.'''
        ruleID=self.getRulesOfCategory("f2l-secondLineSolve")
        
        #create rules
        rule1="(xz='' or not(xz=''))"
        rule2="(xy='' or not(xy=''))"
        rule3="(yz='' or not(yz=''))"
        
        if box.xz:
            rule1= self.getPlaneColorSearchSQL(box.xz).format("xz")
        if box.xy:
            rule2= self.getPlaneColorSearchSQL(box.xy).format("xy")
        if box.yz:
            rule3=self.getPlaneColorSearchSQL(box.yz).format("yz")
        rule4="boxID={}".format(getIdFromPos(box.pos))
        rule5="isInitial=1"
        SQL="SELECT ruleID from boxPosition where {} and {} and {} and {} and {}".format(rule1,rule2,rule3,rule4,rule5)
        
        ret=self.getRuleIDfromBoxesBySQL(SQL)
        
        for item in ret:
            if item in ruleID:
                return self.getAnswerForRuleID(item)
        print box
        print "RULE NOT FOUND"
        return None

    def getAnswerForRuleID(self,index):
        '''Returns answer for the ruleid from the rule table of database.'''
        SQL="SELECT answer from rule where id=%s"%(index)
        cursor=self.db.query(SQL)
            
        return cursor.fetchall()[0][0]
        
    def close(self):
        pass


class BoxPosition(object):
    '''Class for boxposition table entity.'''
    def __init__(self):
        self.id=0
        self.boxID=1
        self.xy=""
        self.xz=""
        self.yz=""
        self.isInitial=False
        self.ruleID=0
        
class Rule(object):
    '''Class for rule table entity.'''
    def __init__(self):
        self.id=0
        self.categoryName=""
        self.answer=""
        self.remarks="no remarks"

class Category(object):
    '''Class for category table entity.'''
    def __init__(self):
        self.categoryName=""
        self.description=""


class DBhandler(object):
    '''Handler for the SQL database.'''
    def createDatabases(self):
        create1='CREATE TABLE IF NOT EXISTS rule (id INTEGER PRIMARY KEY AUTOINCREMENT,\
categoryName TEXT,answer TEXT,remarks TEXT)'
        create2='CREATE TABLE IF NOT EXISTS boxPosition (id INTEGER PRIMARY KEY AUTOINCREMENT,\
boxID INTEGER, xy TEXT,yz TEXT, xz TEXT, isInitial INTEGER,\
ruleID INTEGER)'
        create3='CREATE TABLE IF NOT EXISTS category (categoryName TEXT PRIMARY KEY,\
description TEXT)'
        self.cursor.execute(create3)
        self.cursor.execute(create1)
        self.cursor.execute(create2)
        self.conn.commit()
    def commit(self):
        self.conn.commit()
    def query(self,q):
        return self.cursor.execute(q)
    def initialise(self):
        self.createDatabases()
        
    def __init__(self):
        self.conn=sqlite.connect("database.db")
        self.memory=sqlite.connect(":memory:")
        self.cursor=self.conn.cursor()
        self.initialise()

if __name__=="__main__":
    import main
