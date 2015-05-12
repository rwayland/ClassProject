#-------------------------------------------------------------------------------
# Name:        TrivialPurfuitGUI.py
# Purpose:  Module that contains most of the visual elements to the game
#
# Author:      Rob Wayland
#-------------------------------------------------------------------------------

import wx
import random

#Globals for test purposes
VERSION = '1.0'
COLORS = ['RED','WHITE','BLUE','GREEN']
PLAYERS = ['Player 1','Player 2','Player 3','Player 4']
PLAYER_COLORS = ['CYAN','GRAY','YELLOW','BLACK']

class FrameMain(wx.Frame):
    '''
        Name:
        Description:
    '''
    def __init__(self,title):
        '''
            Name: __init__
            Description:  class constructor for FrameMain.  It constructs many of the assests needed for the display
            in: title - panel title
        '''
        #init parent
        wx.Frame.__init__(self,None,wx.ID_ANY,title)

        #Create menu bar
        mainMenuBar = self.MainMenu()
        self.SetMenuBar(mainMenuBar)

        #Gameboard
        szMain = wx.BoxSizer()
        gmBrd = Gameboard(self)
        gmBrd.BuildGameboard(6,5,COLORS,PLAYERS,PLAYER_COLORS)
        self.gameboard = gmBrd
##        self.scoreboard = gmBrd.scoreboard

        szMain.Add(gmBrd,1,flag = wx.EXPAND)

        self.SetSizerAndFit(szMain)

    def MainMenu(self):
        '''
            Name: MainMenu
            Description: constructs the main menu
            in:
        '''
        menuBar = wx.MenuBar()
        menu = wx.Menu()

        #file->load
        m_load = menu.Append(-1,'Load','Loads previously saved game')
        self.Bind(wx.EVT_MENU, self.OnLoad, m_load)

        #file->save
        m_save = menu.Append(-1,'Save','Saves the current game')
        self.Bind(wx.EVT_MENU, self.OnSave, m_save)

        #file->exit
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnExit, m_exit)
        menuBar.Append(menu, "&File")
        menu = wx.Menu()

        #About
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
        menuBar.Append(menu, "&Help")

        return menuBar

    def OnExit(self,event):
        '''
            Name: OnExit
            Description: event handler for exit menu
            in: self - class variaable
                event - event handler
        '''
        self.Close()

    def OnLoad(self,event):
        '''
            Name: OnLoad
            Description: Load menu item event handler
            in: self - class variaable
                event - event handler
        '''
        pass

    def OnSave(self,event):
        '''
            Name: OnSave
            Description: save menu item event handler
            in: self - class variaable
                event - event handler
        '''
        pass

    def OnAbout(self,event):
        '''
            Name: OnAbout
            Description:
            in: self - class variaable
                event - event handler
        '''
        pass

##class playerPiece():
##    '''
##    '''
##    def __init__(self,owner,color,position):
##        '''
##        '''
##        self.owner = owner
##        self.colr = color
##        self.position = position
##
##
##

class Gameboard(wx.Panel):
    '''
        Name: Gameboard
        Description: represents the main visuals of the game
    '''
    def __init__(self,parent):
        '''
            Name:__init__
            Description: class constructor
            ins: parent - parent of this panel
        '''
        wx.Panel.__init__(self,parent)
##        self.SetBackgroundColour(wx.NamedColor('Blue'))
##
##        numCategories = len(colorCats)
##        numSpaces = 2*height + 2*width
##        cats = range(0,numCategories)
##        icat = 0
##        board = []
##        for ii in range(0,numSpaces):
##            board.append(cats[icat])
##            icat += 1
####
##            if icat >= numCategories:
##                icat = 0
##
##        self.board = board
##        self.nSpaces = numSpaces
##
##        self.BuildGameboard(height,width,colorCats)


##    def getCategory(self,pos):
##        '''
##            Name:getCategory
##            Description: return
##            ins: self - class variable
##                pos - position on the board
##            out:
##                tile
##        '''
##        return self.board[pos]

    def MovePlayer(self,player,curPos,newPos):
        '''
            Name: MovePlayer
            Description: moves player piece on the board
            ins: self - class variable
                player - player to be moved
                curPos - current position
                newPos - new position
        '''

        if type(curPos) == list:
            outInd = curPos[0]
            inInd = curPos[1]

            spoke = self.boardTiles[outInd]
            spoke[inInd].UnselectPlayer([player])
        else:
            self.boardTiles[curPos].UnselectPlayer([player])

        if type(newPos) == list:
            outInd = newPos[0]
            inInd = newPos[1]

            spoke = self.boardTiles[outInd]
            spoke[inInd].SelectPlayer([player])

        else:
            self.boardTiles[newPos].SelectPlayer([player])


    def BuildGameboard(self,height,width,colors,players,playerColors):
        '''
            Name: BuildGameboard
            Description: build the gameboard
            ins: self - class variable
                height - height off board
                width - width of board
                colors - colors of tiles
                players - players name
                playerColors - player colors
        '''
        # Setup Board vector
##        numCategories = len(colors)
##        numSpaces = 2*height + 2*width
##        cats = range(0,numCategories)
##        icat = 0
##        board = []
##        for ii in range(0,numSpaces):
##            board.append(cats[icat])
##            icat += 1
####
##            if icat >= numCategories:
##                icat = 0
##
##        self.board = board
##        self.nSpaces = numSpaces

        # Ranges
        hRange = range(1,height-1)
        hRange2 = range(0,height)
        wRange = range(0,width)
        shortRange = range(0,3)
        self.boardTiles = []
##        colors = ['RED','WHITE','BLUE','GREEN']
##        playerColors = ['CYAN','GRAY','YELLOW','BLACK']
##        players = ['Player 1','Player 2','Player 3','Player 4']

        #GUI Gameboard
##        szMain = wx.BoxSizer(wx.VERTICAL)
        szMain = wx.GridBagSizer(height,width)
        colorCnt = 0

        #Top
        tColor = ['white', 'gray','blue','gray','green']
        for ii in range(5):
            pan = PanelTile(self,tColor[ii],playerColors)
            self.boardTiles.append(pan)
            if ii == 0:
                szMain.Add(pan,(0,ii),flag = wx.ALIGN_RIGHT)
            else:
                szMain.Add(pan,(0,ii),flag = wx.ALIGN_CENTER)

        #Right middle
        tColor = ['red', 'gray','white','gray','blue']
        for ii in range(5):
            pan = PanelTile(self,tColor[ii],playerColors)
            self.boardTiles.append(pan)
            szMain.Add(pan,(ii+1,width-1),flag = wx.ALIGN_CENTER)
##            colorCnt += 1

        #Center
        cenPan = PanelTile(self,'black',playerColors)
        szMain.Add(cenPan,(height/2,width/2),flag = wx.ALIGN_CENTER)


        #top center
        szTopCen = wx.BoxSizer(wx.VERTICAL)
        panTopCen = wx.Panel(self)
        tColor = ['green', 'red','white']
        spoke = []
        for ii in range(3):
            pan = PanelTile(panTopCen,tColor[ii],playerColors,size = (30,15))
            spoke.append(pan)
            szTopCen.Add(pan)

        panTopCen.SetSizer(szTopCen)
        szMain.Add(panTopCen,(1,width/2),(2,1),wx.ALIGN_CENTER)


        #center bottom
        szBotCen = wx.BoxSizer(wx.VERTICAL)
        panBotCen = wx.Panel(self)
        spoke2 = []
        tColor = ['green', 'blue','white']
        for ii in range(3):
            pan = PanelTile(panBotCen,tColor[ii],playerColors,size = (30,15))
            spoke2.append(pan)
            szBotCen.Add(pan)

        panBotCen.SetSizer(szBotCen)
        szMain.Add(panBotCen,(height/2+1,width/2),(2,1),wx.ALIGN_CENTER)

        #center right
        szRgtCen = wx.BoxSizer(wx.HORIZONTAL)
        panRgtCen = wx.Panel(self)
        spoke3 = []
        tColor = ['red','green', 'blue']
        for ii in range(3):
            pan = PanelTile(panRgtCen,tColor[ii],playerColors,size = (15,30))
            spoke3.append(pan)
            szRgtCen.Add(pan)

        panRgtCen.SetSizer(szRgtCen)
        szMain.Add(panRgtCen,(height/2,width/2+1),flag = wx.ALIGN_CENTER)

        #center left
        szLftCen = wx.BoxSizer(wx.HORIZONTAL)
        panLftCen = wx.Panel(self)
        spoke4 = []
        tColor = ['red', 'white','blue']
        for ii in range(3):
            pan = PanelTile(panLftCen,tColor[ii],playerColors,size = (15,30))
            spoke4.append(pan)
            szLftCen.Add(pan)

        panLftCen.SetSizer(szLftCen)
        szMain.Add(panLftCen,(height/2,1),flag = wx.ALIGN_CENTER)
        self.boardTiles.append(spoke + [cenPan])


        #Bottom
        tColor = ['white', 'gray','red','gray','green']
        for ii in range(5):
            pan = PanelTile(self,tColor[ii],playerColors)
            self.boardTiles.append(pan)
            if ii == 0:
                szMain.Add(pan,(height,ii),flag = wx.ALIGN_RIGHT)
            else:
                szMain.Add(pan,(height,ii),flag = wx.ALIGN_CENTER)
##            colorCnt += 1

        #Left middle
        tColor = ['red', 'gray','green','gray','blue']
        for ii in range(5):
            pan = PanelTile(self,tColor[ii],playerColors)
            self.boardTiles.append(pan)
            szMain.Add(pan,(ii+1,0),flag = wx.ALIGN_RIGHT)
##            colorCnt += 1

        #Adding spokes to list
        isp = 2
        isp2 = 7
        isp3 = 12
        isp4 = 17

        spoke.insert(0,self.boardTiles[isp])
        spoke2.insert(0,self.boardTiles[isp2])
        spoke3.insert(0,self.boardTiles[isp3])
        spoke4.insert(0,self.boardTiles[isp4])

        self.boardTiles.pop(isp)
        self.boardTiles.insert(isp,spoke + [cenPan])
        self.boardTiles.pop(isp2)
        self.boardTiles.insert(isp2,spoke2 + [cenPan])
        self.boardTiles.pop(isp3)
        self.boardTiles.insert(isp3,spoke3 + [cenPan])
        self.boardTiles.pop(isp4)
        self.boardTiles.insert(isp4,spoke4 + [cenPan])

        #making resizable row/cols
        for ii in wRange:
            szMain.AddGrowableCol(ii)
        for ii in hRange2:
            szMain.AddGrowableRow(ii)

        pan = PanelScoreboard(self,players,colors)
        szMain.Add(pan,(height+1,0),(1,5),flag = wx.EXPAND)
##        szMain.AddGrowableCol(width+1)
        self.scoreboard = pan
        #Middle middle (scoreboard)
##        playPan = PanelPlayer(self,PLAYERS[0],COLORS)
##        szMain.Add(playPan,(height+1,0),flag = wx.ALIGN_CENTER)

        self.SetSizerAndFit(szMain)
        szMain.SetSizeHints(self)

class PanelScoreboard(wx.Panel):
    '''
        Name: Gameboard
        Description: represents the main visuals of the game
    '''
    def __init__(self,parent,playerNames,catColors):
        '''
            Name:__init__
            Description: class constructor
            ins: parent - parent of this panel
                playerNames - player names
                catColors - question category colors
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER_SUNKEN)

        szMain = wx.BoxSizer(wx.VERTICAL)

##        szStatus = wx.BoxSizer(wx.VERTICAL)
##        panStatus = PanelStatus(self)
##        panDice = PanelDice(self)
##        szStatus.Add(panStatus,2,wx.EXPAND)
##        szStatus.Add(panDice,1,wx.EXPAND)

        szPlayer = wx.BoxSizer(wx.HORIZONTAL)

        dicPlayers = {}
        for player in playerNames:
            dicPlayers[player] = PanelPlayer(self,player,catColors)
            szPlayer.Add(dicPlayers[player],1,wx.EXPAND)

        self.dicPlayers = dicPlayers

        szMain.Add(szPlayer,1,wx.EXPAND)
##        szMain.Add(szStatus,1,wx.EXPAND)

        self.SetSizerAndFit(szMain)

    def AwardCake(self,player,category):
        '''
            Name:AwardCake
            Description: awards cake to the selected player
            ins: player - player
                category - question category
        '''
        self.dicPlayers[player].AwardCake(category)

    def UpdateScore(self,player,category,answerCorrectly,totalQuestions):
        '''
            Name:UpdateScore
            Description: updates the score of the player
            ins: player - player
                category - category
                answerCorrectly - questions answered correctly
                totalQuestion - total questions attempted
        '''
        self.dicPlayers[player].UpdateScore(category,answerCorrectly,totalQuestions)

##class PanelStatus(wx.Panel):
##    '''
##        Name: PanelStatus
##        Description: Status panel for a player
##    '''
##    def __init__(self,parent):
##        '''
##            Name:__init__
##            Description: class constructor
##            ins: parent - parent wx object
##
##        '''
##        wx.Panel.__init__(self,parent,style = wx.BORDER)
##
##        #player1
##        szPly1 = wx.BoxSizer(wx.HORIZONTAL)
##        ply1colorBox = wx.StaticBox(self)
##        lblPly1 = wx.StaticBox(self,-1,'Player 1')
##
##        szPly1.Add(ply1colorBox)
##        szPly1.Add(lblPly1)
##
##        self.SetSizer(szPly1)



##class PanelDice(wx.Panel):
##    '''
##        Name: Gameboard
##        Description: represents the main visuals of the game
##    '''
##    def __init__(self,parent):
##        '''
##        '''
##        wx.Panel.__init__(self,parent,style = wx.BORDER)
##
##        szMain = wx.BoxSizer(wx.HORIZONTAL)
##        btnDice = wx.Button(self,-1,'Roll\n Me')
##        font = wx.Font(26, wx.NORMAL, wx.NORMAL, wx.BOLD)
##        btnDice.SetFont(font)
##        szMain.Add(btnDice,1,wx.EXPAND)
##
##        lblDice = wx.Button(self,-1,'1')
##        font = wx.Font(26, wx.NORMAL, wx.NORMAL, wx.BOLD)
##        lblDice.SetFont(font)
##        szMain.Add(lblDice,1,wx.EXPAND)
##        lblDice.Enable(False)
##
##        self.Bind(wx.EVT_BUTTON,self.btnRollClickEvent,btnDice)
##
##        self.dice = lblDice
##        self.SetSizer(szMain)
##
##
##    def btnRollClickEvent(self,event):
##        '''
##        '''
##        val = rollDie()
##        self.SetDiceReadout(val)
##
##    def SetDiceReadout(self,newValue):
##        '''
##        '''
##        self.dice.SetLabel(str(newValue))

class PanelPlayer(wx.Panel):
    '''
        Name: PanelPlayer
        Description: player panel containing a cake pan
    '''
    def __init__(self,parent,owner,catColors):
        '''
            Name:__init__
            Description: class constructor
            ins: parent - parent of this panel
        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER)

        szMain = wx.BoxSizer(wx.VERTICAL)

        #Owner, questions attempted
        lblPlayer = wx.StaticText(self,label = owner)
        lblQuestion = wx.StaticText(self,-1,'Questions attempted: ')
        szGroup = self.GroupScore(catColors)
        cakePan = PanelTile(self,'white',catColors,(10,10))

        szMain.Add(lblPlayer,1,wx.EXPAND)
        szMain.Add(lblQuestion,1,wx.EXPAND)
        szMain.Add(szGroup,1,wx.EXPAND)

        szMain.Add(cakePan,3,wx.EXPAND)

        self.cakePan = cakePan
        self.colors = catColors
        self.SetSizerAndFit(szMain)

    def GroupScore(self,catColors):
        '''
            Name:GroupScore
            Description: updates the score
            ins: self - class constructor
                catColors - category colors
        '''
        szGroup = wx.GridSizer(2,2)
        self.dicCatColor = {}
        for colors in catColors:
            szCat = wx.BoxSizer(wx.HORIZONTAL)
            lblCat1 = wx.StaticText(self,-1,colors + ':')
            lblCatAnswer = wx.StaticText(self,-1,'0/0')
            szCat.Add(lblCat1)
            szCat.Add(lblCatAnswer)

            szGroup.Add(szCat)
            self.dicCatColor[colors] = lblCatAnswer

        return szGroup

    def AwardCake(self,category):
        '''
            Name:AwardCake
            Description: toggles panel to shhow cake pieces
            ins: category - question category
        '''
        self.cakePan.SelectPlayer([category])

    def UpdateScore(self,category,answerCorrectly,totalAnswered):
        '''
            Name:UpdateScore
            Description: updates player score
            ins: category - question category
                answerCorrectly - questions answered correctly
                totalAnswered - Total questions attempted
        '''
        strScore = str(answerCorrectly) + '/' + str(totalAnswered)
        self.dicCatColor[self.colors[category]].SetLabel(strScore)

class PanelTile(wx.Panel):
    '''
        Name: PanelTile
        Description: represents a single game tile
    '''
    def __init__(self,parent,namedColor,namedPlayerColors,rollAgain = False,size = (30,30)):
        '''
            Name:__init__
            Description: class constructor
            ins: parent - parent of this panel
                namedColor - color of the panel
                namedPlayerColors - color of the players

        '''
        wx.Panel.__init__(self,parent,style = wx.BORDER_RAISED)

        #if not roll again add the play panels
        if namedColor != 'gray':
            szMain = wx.GridSizer(2,2)
            self.rollAgain = False

            pnPlay1 = self.SubpanelPlayer(size)
            pnPlay1.SetBackgroundColour(wx.NamedColor('gray'))
            szMain.Add(pnPlay1,1,wx.EXPAND)

            pnPlay2 = self.SubpanelPlayer(size)
            szMain.Add(pnPlay2,1,wx.EXPAND)

            pnPlay3 = self.SubpanelPlayer(size)
            szMain.Add(pnPlay3,1,wx.EXPAND)

            pnPlay4 = self.SubpanelPlayer(size)
            szMain.Add(pnPlay4,1,wx.EXPAND)

            self.players = [pnPlay1,pnPlay2,pnPlay3,pnPlay4]

        else:
            szMain = wx.BoxSizer()
            lblStatic = wx.Button(self,-1,'Roll\nAgain',size = (60,60), style = wx.CENTER)
            szMain.Add(lblStatic,1,wx.EXPAND)
            self.rollAgain = True

        self.SetSizer(szMain)

        self.ChangeColor(namedColor)
        self.defaultColor = namedColor
        self.playerColors = namedPlayerColors


    def SubpanelPlayer(self,size):
        '''
            Name:SubpanelPlayer
            Description: player subpane
            ins: size - size of panel
        '''
        pan = wx.Panel(self,style = wx.BORDER_SIMPLE,size = size)
        return pan

    def SelectPlayer(self,selection):
        '''
            Name:SelectPlayer
            Description: selects player
            ins: selection - selects player on panel
        '''
        if not self.rollAgain:
            for sel in selection:
                player = self.players[sel]
                player.SetBackgroundColour(wx.NamedColor(self.playerColors[sel]))
                self.Refresh()

    def UnselectPlayer(self,selection):
        '''
            Name:UnselectPlayer
            Description: unselect player on tile
            ins: selection - player selected
        '''
        if not self.rollAgain:
            for sel in selection:
                player = self.players[sel]
                player.SetBackgroundColour(wx.NamedColor(self.defaultColor))
                self.Refresh()


    def ChangeColor(self,newNamedColor):
        '''
            Name:ChangeColor
            Description: changed tile color
            ins: newNamedColor 0 new coloe
        '''
        if not self.rollAgain:
            for player in self.players:
    ##            player = self.players[key]
                player.SetBackgroundColour(wx.NamedColor(newNamedColor))

class DialogDice(wx.Dialog):
    '''
        Name: DialogQuestion
        Description:  Dialogbox that displays a question and four possible answers
    '''
    def __init__(self,result,size = (40,70)):
        '''
            Name:__init__
            Description: Main constructor
            Ins:
                self - class variable
                question - string representing a question
                queestionChoices - list of string representing answer to a question
        '''

        #init parent
        wx.Dialog.__init__(self,None,wx.ID_ANY,'Roll Die',size = size)

        #Main Sizer
        szMain = wx.BoxSizer(wx.VERTICAL)

        #results
        szResult = wx.BoxSizer()
        lbl = wx.StaticText(self,-1,'Result: ')
        lblResult = wx.StaticText(self,-1,size = (150,40))
        font = wx.Font(18, wx.NORMAL, wx.NORMAL, wx.BOLD)
        lblResult.SetFont(font)
        self.lblResult = lblResult
        szResult.Add(lbl,1,wx.EXPAND)
        szResult.Add(lblResult,3,wx.EXPAND)

        #Button
        szButton = wx.BoxSizer(wx.HORIZONTAL)

        btnRoll = wx.Button(self,-1,'Roll')
        szButton.Add(btnRoll)
        self.btnRoll = btnRoll
        self.Bind(wx.EVT_BUTTON,self.OnRoll,btnRoll)

        btnSubmit = wx.Button(self,wx.ID_OK,'Ok')
        szButton.Add(btnSubmit)
        btnSubmit.Enable(False)
        self.btnSubmit = btnSubmit

        szMain.Add(szResult,1,wx.EXPAND)
        szMain.Add(szButton,1,wx.EXPAND)

        self.SetSizerAndFit(szMain)
        self.result = result

    def OnRoll(self,event):
        '''
            Name:OnRoll
            Description: roll button event handler
            ins: event - event obj
        '''
        res1 = self.result[0]
        res2 = self.result[1]
        self.lblResult.SetLabel(str(res1) + ' + ' + str(res2) + ' = ' + str(res1+res2))
        self.btnSubmit.Enable(True)
        self.btnRoll.Enable(False)


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

        self.pos = 0
        self.mainFrame.gameboard.MovePlayer(1,0,0)

    def question(self,event):
        ques = 'This is a question!'
        choices = ['A','B','C','D']

##        dlg = DialogQuestion(ques,choices)
##
##        if dlg.ShowModal() == wx.ID_OK:
##            val = dlg.getSelection()
##            print(val)

##        dlg.Destroy()

        res = rollDie()
        dlg = DialogDice(res)
        if dlg.ShowModal() == wx.ID_OK:
            print(str(res))

        dlg.Destroy()

    def advancePlayer1(self,event):
        self.mainFrame.gameboard.MovePlayer(1,0,[2,self.pos])
        self.pos += 1

    def awardCake(self,event):
        self.mainFrame.scoreboard.AwardCake('Player 1',0)
        self.mainFrame.scoreboard.UpdateScore('Player 1',0,self.score[0],self.score[0])
        self.score[0] += 1

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

        #Create menu bar
        mainMenuBar = self.MainMenu()
        self.SetMenuBar(mainMenuBar)

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

    def MainMenu(self):
        '''
        '''
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_load = menu.Append(-1,'Load','Loads previously saved game')
        self.Bind(wx.EVT_MENU, self.OnLoad, m_load)
        m_save = menu.Append(-1,'Save','Saves the current game')
        self.Bind(wx.EVT_MENU, self.OnSave, m_save)
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnExit, m_exit)
        menuBar.Append(menu, "&File")
##        menu = wx.Menu()
##        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
##        self.Bind(wx.EVT_MENU, self.OnAbout, m_about)
##        menuBar.Append(menu, "&Help")

        return menuBar

    def OnExit(self,event):
        '''
        '''
        self.Close()

    def OnLoad(self,event):
        '''
        '''
        pass

    def OnSave(self,event):
        '''
        '''
        pass

def rollDie():
    newValue = random.randint(1,6)
    newValue2 = random.randint(1,6)
    return (newValue,newValue2)

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
##
    frm = FrameTest(frmTrival)
    frm.Show()

##    frmQues = FrameQuestionEditor(None,'Question Editor')
##    testQuestion(frmQues)
##    frmQues.Show()

    app.MainLoop()

if __name__ == '__main__':
    main()
