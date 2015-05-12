#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Rob
#
# Created:     09/05/2015
# Copyright:   (c) Rob 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
import random

VERSION = '1.0'

class FrameMain(wx.Frame):
    '''
    '''
    def __init__(self,title):
        '''
        '''
        #init parent
        wx.Frame.__init__(self,None,wx.ID_ANY,title)

        #Create menu bar
        mainMenuBar = self.MainMenu()
        self.SetMenuBar(mainMenuBar)

        #Gameboard
##        PanelPlayer(self)
        szMain = wx.BoxSizer()
        gmBrd = Gameboard(self,10,10,4)
        self.gameboard = gmBrd
        self.scoreboard = gmBrd.scoreboard

        h = 10
        w = 10
        hRange = range(1,h-1)
        wRange = range(0,w)
        colors = ['RED','WHITE','BLUE','GRAY']
        playerColors = ['CYAN','GREEN','YELLOW','BLACK']
        players = ['Player 1','Player 2','Player 3','Player 4']
##        gmBrd = PanelScoreboard(self,players,colors)

        szMain.Add(gmBrd,1,flag = wx.EXPAND)
##        height = 10
##        width = 10
##        nCats = 4
##        spaces = 2*10
##        gmBrd = gameboard(height,width,nCats)

##        szMain = wx.BoxSizer()
##        szMain.Add(gmBrd)
##        self.SetSizer(szMain)
        self.SetSizerAndFit(szMain)

    def MainMenu(self):
        '''
        '''
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnExit, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
##        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")

        return menuBar
##        self.SetMenuBar(menuBar)


    def mainMenuItems(self):
        pass

    def OnExit(self,event):
        self.Close()


class playerPiece():
    '''
    '''
    def __init__(self,owner,color,position):
        '''
        '''
        self.owner = owner
        self.colr = color
        self.position = position




class Gameboard(wx.Panel):
    '''
    '''
    def __init__(self,parent,height,width,numCategories):
        '''
        '''
        wx.Panel.__init__(self,parent)
##        self.SetBackgroundColour(wx.NamedColor('Blue'))


        numSpaces = 2*height + 2*width
        cats = range(0,numCategories)
        icat = 0
        board = []
        for ii in range(0,numSpaces):
            board.append(cats[icat])
            icat += 1
##
            if icat >= numCategories:
                icat = 0

        self.board = board
        self.nSpaces = numSpaces

        self.BuildGameboard()


    def getCategory(self,pos):
        '''
        '''
        return self.board[pos]

    def MovePlayer(self,player,curPos,newPos):
        self.boardTiles[curPos].UnselectPlayer([player])
        self.boardTiles[newPos].SelectPlayer([player])


    def BuildGameboard(self):
        '''
        '''
        h = 10
        w = 10
        hRange = range(1,h-1)
        hRange2 = range(0,h)
        wRange = range(0,w)
        self.boardTiles = []
        colors = ['RED','WHITE','BLUE','GRAY']
        playerColors = ['CYAN','GREEN','YELLOW','BLACK']
        players = ['Player 1','Player 2','Player 3','Player 4']

        #GUI Gameboard
##        szMain = wx.BoxSizer(wx.VERTICAL)
        szMain = wx.GridBagSizer(1,w)
        colorCnt = 0

        #Top
        szTop = wx.BoxSizer(wx.HORIZONTAL)
        for ii in wRange:
            pan = PanelTile(self,colors[colorCnt%4],playerColors)
            self.boardTiles.append(pan)
##            szTop.Add(pan)
            szMain.Add(pan,(0,ii))
##            szMain.Add(pan,1,wx.EXPAND)
            colorCnt += 1


##        #Middle
##        szMiddle = wx.BoxSizer(wx.HORIZONTAL)

        #Right middle
        szLeftMid = wx.BoxSizer(wx.VERTICAL)
        for ii in hRange:
            pan = PanelTile(self,colors[(colorCnt)%4],playerColors)
            self.boardTiles.append(pan)
##            szLeftMid.Add(pan)
            szMain.Add(pan,(ii,w-1))
            colorCnt += 1

        #Middle middle (scoreboard)
        pan = PanelScoreboard(self,players,colors)
        szMain.Add(pan,(1,1),(h-2,w-2),wx.EXPAND)
        self.scoreboard = pan

        #Bottom
        szBot = wx.BoxSizer(wx.HORIZONTAL)
        for ii in reversed(wRange):
            pan = PanelTile(self,colors[colorCnt%4],playerColors)
            self.boardTiles.append(pan)
####            szBot.Add(pan)
            szMain.Add(pan,(h-1,ii))
            colorCnt += 1

        #Left middle
        szRghtMid = wx.BoxSizer(wx.VERTICAL)
        for ii in reversed(hRange):
            pan = PanelTile(self,colors[colorCnt%4],playerColors)
            self.boardTiles.append(pan)
####            szRghtMid.Add(pan)
            szMain.Add(pan,(ii,0))
            colorCnt += 1


##        szMain.Add(szTop)
##        szMain.Add(szMiddle)
##        szMain.Add(szBot)
        self.boardTiles[0].SelectPlayer([0,1,2,3])

        for ii in wRange:
            szMain.AddGrowableCol(ii)
        for ii in hRange2:
            szMain.AddGrowableRow(ii)


##        szMain.AddGrowableRow(0)
##        szMain.AddGrowableCol(0)
        self.SetSizerAndFit(szMain)
        szMain.SetSizeHints(self)

class PanelScoreboard(wx.Panel):
    '''
    '''
    def __init__(self,parent,playerNames,catColors):
        '''
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER_SUNKEN)

        szMain = wx.BoxSizer(wx.VERTICAL)

        szStatus = wx.BoxSizer(wx.VERTICAL)
##        panStatus = PanelStatus(self)
        panDice = PanelDice(self)
##        szStatus.Add(panStatus,2,wx.EXPAND)
        szStatus.Add(panDice,1,wx.EXPAND)

        szPlayer = wx.BoxSizer(wx.HORIZONTAL)

        dicPlayers = {}
        for player in playerNames:
            dicPlayers[player] = PanelPlayer(self,player,catColors)
            szPlayer.Add(dicPlayers[player],1,wx.EXPAND)

        self.dicPlayers = dicPlayers

        szMain.Add(szPlayer,2,wx.EXPAND)
        szMain.Add(szStatus,1,wx.EXPAND)

        self.SetSizerAndFit(szMain)

    def awardCake(self,player,category):
        '''
        '''
        self.dicPlayers[player].awardCake(category)
class PanelStatus(wx.Panel):
    '''
    '''
    def __init__(self,parent):
        '''
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER)

        #player1
        szPly1 = wx.BoxSizer(wx.HORIZONTAL)
        ply1colorBox = wx.StaticBox(self)
        lblPly1 = wx.StaticBox(self,-1,'Player 1')

        szPly1.Add(ply1colorBox)
        szPly1.Add(lblPly1)

        self.SetSizer(szPly1)



class PanelDice(wx.Panel):
    '''
    '''
    def __init__(self,parent):
        '''
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER)

        szMain = wx.BoxSizer(wx.HORIZONTAL)
        btnDice = wx.Button(self,-1,'Roll\n Me')
        font = wx.Font(26, wx.NORMAL, wx.NORMAL, wx.BOLD)
        btnDice.SetFont(font)
        szMain.Add(btnDice,1,wx.EXPAND)

        lblDice = wx.Button(self,-1,'1')
        font = wx.Font(26, wx.NORMAL, wx.NORMAL, wx.BOLD)
        lblDice.SetFont(font)
        szMain.Add(lblDice,1,wx.EXPAND)
        lblDice.Enable(False)

        self.Bind(wx.EVT_BUTTON,self.btnRollClickEvent,btnDice)

        self.dice = lblDice
        self.SetSizer(szMain)


    def btnRollClickEvent(self,event):
        '''
        '''
        val = rollDie()
        self.SetDiceReadout(val)

    def SetDiceReadout(self,newValue):
        '''
        '''
        self.dice.SetLabel(str(newValue))

class PanelPlayer(wx.Panel):
    '''
    '''
    def __init__(self,parent,owner,catColors):
        '''
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER)

        szMain = wx.BoxSizer(wx.VERTICAL)


        lblPlayer = wx.StaticText(self,label = owner)
        lblQuestion = wx.StaticText(self,-1,'Questions attempted: ')
        szGroup = self.GroupScore(catColors)
        cakePan = PanelTile(self,'gray',catColors,(-1,-1))

        szMain.Add(lblPlayer,1,wx.EXPAND)
        szMain.Add(lblQuestion,1,wx.EXPAND)
        szMain.Add(szGroup,1,wx.EXPAND)

        szMain.Add(cakePan,3,wx.EXPAND)

        self.cakePan = cakePan
        self.colors = catColors
        self.SetSizerAndFit(szMain)

    def GroupScore(self,catColors):
        '''
        '''
        szGroup = wx.GridSizer(2,2)
        for colors in catColors:
            szCat = wx.BoxSizer(wx.HORIZONTAL)
            lblCat1 = wx.StaticText(self,-1,colors + ':')
            lblCatAnswer = wx.StaticText(self,-1,'0/0')
            szCat.Add(lblCat1)
            szCat.Add(lblCatAnswer)

            szGroup.Add(szCat)

        return szGroup

    def awardCake(self,category):
        '''
        '''
        self.cakePan.SelectPlayer([category])

    def UpdateScore(self,color,answerCorrectly):
        '''
        '''
        pass

class PanelTile(wx.Panel):
    '''
    '''

    def __init__(self,parent,namedColor,namedPlayerColors,size = (30,30)):
        '''
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER_RAISED)

        szMain = wx.GridSizer(2,2)

        pnPlay1 = self.SubpanelPlayer(size)
        pnPlay1.SetBackgroundColour(wx.NamedColor('gray'))
        szMain.Add(pnPlay1,1,wx.EXPAND)

        pnPlay2 = self.SubpanelPlayer(size)
        szMain.Add(pnPlay2,1,wx.EXPAND)

        pnPlay3 = self.SubpanelPlayer(size)
        szMain.Add(pnPlay3,1,wx.EXPAND)

        pnPlay4 = self.SubpanelPlayer(size)
        szMain.Add(pnPlay4,1,wx.EXPAND)

        self.SetSizer(szMain)

        self.players = [pnPlay1,pnPlay2,pnPlay3,pnPlay4]
        self.ChangeColor(namedColor)
        self.defaultColor = namedColor
        self.playerColors = namedPlayerColors


    def SubpanelPlayer(self,size):
        '''
        '''
        pan = wx.Panel(self,style = wx.BORDER_SIMPLE,size = size)
        return pan

    def SelectPlayer(self,selection):
        '''
        '''
        for sel in selection:
            player = self.players[sel]
            player.SetBackgroundColour(wx.NamedColor(self.playerColors[sel]))
            self.Refresh()

    def UnselectPlayer(self,selection):
        '''
        '''
        for sel in selection:
            player = self.players[sel]
            player.SetBackgroundColour(wx.NamedColor(self.defaultColor))
            self.Refresh()


    def ChangeColor(self,newNamedColor):
        '''
        '''
        for player in self.players:
##            player = self.players[key]
            player.SetBackgroundColour(wx.NamedColor(newNamedColor))


class DialogQuestion(wx.Dialog):
    '''
        Name: DialogQuestion
        Description:  Dialogbox that displays a question and four possible answers
    '''
    def __init__(self,question,questionChoices):
        '''
            Name:__init__
            Description: Main constructor
            Ins:
                self - class variable
                question - string representing a question
                queestionChoices - list of string representing answer to a question
        '''

        #init parent
        wx.Dialog.__init__(self,None,wx.ID_ANY,'Question')

        #Main Sizer
        szMain = wx.BoxSizer(wx.VERTICAL)

        ques = wx.StaticText(self,-1,question)
        szMain.Add(ques)

        #Questions
        choices = []
        for question in questionChoices:
            choice = wx.RadioButton(self,-1,question)
            choices.append(choice)
            szMain.Add(choice)

        btnSubmit = wx.Button(self,wx.ID_OK,'Submit')
        szMain.Add(btnSubmit)

        self.SetSizerAndFit(szMain)
        self.choices = choices

    def getSelection(self):
        '''
            Name: getSelection
            Description:  Return the selection
            In: self - class variable
        '''
        cnt = 0
        val = 0
        for choice in self.choices:
            if choice.GetValue():
                val = cnt
            cnt += 1

        return val

class FrameTest(wx.Frame):
    '''
    '''
    def __init__(self,mainFrame):
        '''
        '''
        wx.Frame.__init__(self,None)

        szMain = wx.BoxSizer()

        btnQuestion = wx.Button(self,-1,'Question')
        self.Bind(wx.EVT_BUTTON,self.question,btnQuestion)

        btnAdvance = wx.Button(self,-1,'Advance')
        self.Bind(wx.EVT_BUTTON,self.advancePlayer1,btnAdvance)

        btnCake = wx.Button(self,-1,'Cake')
        self.Bind(wx.EVT_BUTTON,self.awardCake,btnCake)

        szMain.Add(btnQuestion)
        szMain.Add(btnAdvance)
        szMain.Add(btnCake)

        self.mainFrame = mainFrame

        self.SetSizer(szMain)

    def question(self,event):
        ques = 'This is a question!'
        choices = ['A','B','C','D']

        dlg = DialogQuestion(ques,choices)

        if dlg.ShowModal() == wx.ID_OK:
            val = dlg.getSelection()
            print(val)

        dlg.Destroy()

    def advancePlayer1(self,event):
        self.mainFrame.gameboard.MovePlayer(1,0,4)

    def awardCake(self,event):
        self.mainFrame.scoreboard.awardCake('Player 1',0)

class FrameQuestionEditor(wx.Frame):
    '''
        Name: FrameQuestionEditor
        Description:  This class build a GUI for a question editor
    '''
    def __init__(self,parent,title):
        '''
            Name: __init__
            Description: Main class constructor
            In: self - class variable
            parent: parent to this frame
            title: title for the frame
        '''
        wx.Frame.__init__(self,parent,-1,title)

        szMain = wx.BoxSizer(wx.VERTICAL)

        #Category Dropdown
        szCatDrop = wx.BoxSizer(wx.HORIZONTAL)

        catDropDown = wx.ComboBox(self)
        btnLoadCat = wx.Button(self,-1,'Load Category')
        self.Bind(wx.EVT_BUTTON,self.OnLoadCategory,btnLoadCat)
        szCatDrop.Add(catDropDown)
        szCatDrop.Add(btnLoadCat)

        #Question Dropdown
        szQuesDrop = wx.BoxSizer(wx.HORIZONTAL)

        quesDropDown = wx.ComboBox(self)
        btnLoadQues = wx.Button(self,-1,'Load Question')
        self.Bind(wx.EVT_BUTTON,self.OnLoadQuestion,btnLoadQues)
        szQuesDrop.Add(quesDropDown)
        szQuesDrop.Add(btnLoadQues)

        #Question Body
        szBody = wx.BoxSizer(wx.HORIZONTAL)
        lblQues = wx.StaticText(self,-1,'Body')
        tbQues = wx.TextCtrl(self)
        szBody.Add(lblQues)
        szBody.Add(tbQues,1,wx.EXPAND)

        #Answers 1-4
        szAns = wx.BoxSizer(wx.HORIZONTAL)
        lblAns = wx.StaticText(self,-1,'Correct Answer')
        tbAns = wx.TextCtrl(self)
        szAns.Add(lblAns)
        szAns.Add(tbAns,1,wx.EXPAND)

        szAns2 = wx.BoxSizer(wx.HORIZONTAL)
        lblAns2 = wx.StaticText(self,-1,'Choice 1')
        tbAns2 = wx.TextCtrl(self)
        szAns2.Add(lblAns2)
        szAns2.Add(tbAns2,1,wx.EXPAND)

        szAns3 = wx.BoxSizer(wx.HORIZONTAL)
        lblAns3 = wx.StaticText(self,-1,'Choice 2')
        tbAns3 = wx.TextCtrl(self)
        szAns3.Add(lblAns3)
        szAns3.Add(tbAns3,1,wx.EXPAND)

        szAns4 = wx.BoxSizer(wx.HORIZONTAL)
        lblAns4 = wx.StaticText(self,-1,'Choice 3')
        tbAns4 = wx.TextCtrl(self)
        szAns4.Add(lblAns4)
        szAns4.Add(tbAns4,1,wx.EXPAND)

        #Add to main
        szMain.Add(szCatDrop)
        szMain.Add(szQuesDrop)
        szMain.Add(szBody,0,wx.EXPAND)
        szMain.Add(szAns,0,wx.EXPAND)
        szMain.Add(szAns2,0,wx.EXPAND)
        szMain.Add(szAns3,0,wx.EXPAND)
        szMain.Add(szAns4,0,wx.EXPAND)

        self.SetSizerAndFit(szMain)

        self.cbQuestion = quesDropDown
        self.cbCat = catDropDown
        self.question = tbQues
        self.answers = [tbAns,tbAns2,tbAns3,tbAns4]

    def loadQuestionDictionary(self,dicQuestion):
        '''
            Name: loadQuestionDictionary
            Description: Loads the question dictionary
            In: self - class variable
            dicQuestion - dictionary containing each dictionary of questions
        '''
        self.questionDict = dicQuestion

        cats = dicQuestion.keys()
##        ques = dicQuestion[cats[0]].keys()
        cats.sort()
        self.cbCat.SetItems(cats)
        self.cbCat.Select(0)
        self.loadCategory(cats[0])

        self.loadQuestion(self.curQues)

    def loadCategory(self,category):
        '''
            Name: loadCategory
            Description: loads the selected category
            In: self - class variable
                category - key in the category dictionary
        '''
        ques = self.questionDict[category]
        qs = ques.keys()
        qs.sort()
        self.cbQuestion.SetItems(qs)
        self.cbQuestion.Select(0)
        self.curCategory = category
        self.curQues = qs[0]

    def loadQuestion(self,question):
        '''
            Name: loadQuestion
            Description: load a question into the display
            In: self - class variable
                question - key in the question dictionary
        '''
        ques = self.questionDict[self.curCategory]
        newQues = ques[question]

        self.question.SetLabel(newQues[0])
        self.answers[0].SetLabel(newQues[1])
        self.answers[1].SetLabel(newQues[2])
        self.answers[2].SetLabel(newQues[3])
        self.answers[3].SetLabel(newQues[4])

        self.curQues = question

    def OnLoadCategory(self,event):
        '''
            Name: OnLoadCategory
            Description: event handler for load category button
            In: self - class variable
                event - event structure
        '''
        cati = self.cbCat.GetSelection()
        cat = self.cbCat.GetString(cati)
        self.loadCategory(cat)
        self.loadQuestion(self.curQues)

    def OnLoadQuestion(self,event):
        '''
            Name: OnLoadQuestion
            Description: Event handler for the load question button
            In: self - variable
                event - event structure
        '''
        seli = self.cbQuestion.GetSelection()
        sel = self.cbQuestion.GetString(seli)
        self.loadQuestion(sel)

def rollDie():
    newValue = random.randint(1,6)
    return newValue

def testQuestion(frmQuestion):

    q0 = ['This is question one','A','B','C','D']
    q1 = ['This is question two','A','B','C','D']
    cat1 = {'Question 1':q0,'Question 2':q1}
    cat2 = {'Question 1':q0,'Question 2':q1}

    questions = {'Category 1':cat1,'Category 2':cat2}

    frmQuestion.loadQuestionDictionary(questions)

def main():
    app = wx.PySimpleApp()
    title = 'Trivial Purfuit' + ' v' + VERSION
    frmTrival = FrameMain(title)
    frmTrival.Show()

    frm = FrameTest(frmTrival)
    frm.Show()

##    frmQues = FrameQuestionEditor(None,'Question Editor')
##    testQuestion(frmQues)
##    frmQues.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()
