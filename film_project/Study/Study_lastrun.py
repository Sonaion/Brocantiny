#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on November 24, 2021, at 01:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

from psychopy import monitors

mon = None
for tmp_mon in monitors.getAllMonitors():
    mon = tmp_mon
    
width = monitors.Monitor(mon).getSizePix()[0]
height = monitors.Monitor(mon).getSizePix()[1]
lm = -0.4 * width
mm = 0.0 * width
rm = 0.4 * width
md = -0.4 * height
mu = 0.4 * height


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'Study'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jonas\\Documents\\GitHub\\Brocantiny\\film_project\\Study\\Study_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=-1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Startup"
StartupClock = core.Clock()

# Initialize components for Routine "Begrüßung"
BegrüßungClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Viel Spaß!\n\nUm das Experiment zu starten, drücken Sie die \n\n<Leertaste>\n\n',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Einweisung"
EinweisungClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Im Folgenden wird Ihn ein Endlicher Automat gezeigt. Ebnso wird Ihnen ein Mapping von Automat Variablen auf diverse Wörter vorgestellt. Ihre Aufgabe ist es, zu entscheiden ob ein Gegebener Satz Richtig oder Falsch ist.\n\nDrücken Sie dafür jeweils die <Linke Pfeiltaste> oder die <Rechte Pfeiltaste>. Doch beginnen wir mit einem Beispiel.\n\nWeiter mit <Leertaste> ',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "CodeStartup"
CodeStartupClock = core.Clock()
global use_eyetracking
global logger
use_eyetracking = False
logger = None

if use_eyetracking:
    from EyetrackerUtils.base_functionalities.logger import Logger
    logger = Logger("./Eyedata_S" + str(int(expInfo["session"])) + "_P" + str(int(expInfo["participant"])) +".csv")
    logger.add_key_to_log('left_gaze_point_validity')
    logger.add_key_to_log('right_gaze_point_validity')
    logger.add_key_to_log('left_gaze_point_on_display_area')
    logger.add_key_to_log('right_gaze_point_on_display_area')
    logger.add_key_to_log('system_time_stamp')
    
if use_eyetracking:
    logger.start_recording()

# Initialize components for Routine "BrocantinyErklärung"
BrocantinyErklärungClock = core.Clock()
Brocantiny = visual.ImageStim(
    win=win,
    name='Brocantiny', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
BrocantinyMapping = visual.ImageStim(
    win=win,
    name='BrocantinyMapping', units='pix', 
    image='../CodeSnippets/Snippets/BrocantinyErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(504, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Brocantiny_Beispiel = visual.ImageStim(
    win=win,
    name='Brocantiny_Beispiel', units='pix', 
    image='../CodeSnippets/Snippets/BrocantinyBeispiel.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(257, 49),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Stop"
StopClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Weiter um den nächsten Teil des Experiments zu starten\n\n<Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Brocantiny1"
Brocantiny1Clock = core.Clock()
Brocantiny_3 = visual.ImageStim(
    win=win,
    name='Brocantiny_3', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
BrocantinyMapping_2 = visual.ImageStim(
    win=win,
    name='BrocantinyMapping_2', units='pix', 
    image='../CodeSnippets/Snippets/BrocantinyErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(504, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
BS1 = visual.ImageStim(
    win=win,
    name='BS1', units='pix', 
    image='../CodeSnippets/Snippets/Brocantiny1.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(270, 88),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
BSI1 = keyboard.Keyboard()

# Initialize components for Routine "Brocantiny2"
Brocantiny2Clock = core.Clock()
Brocantiny_4 = visual.ImageStim(
    win=win,
    name='Brocantiny_4', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
BrocantinyMapping_3 = visual.ImageStim(
    win=win,
    name='BrocantinyMapping_3', units='pix', 
    image='../CodeSnippets/Snippets/BrocantinyErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(504, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
BS2 = visual.ImageStim(
    win=win,
    name='BS2', units='pix', 
    image='../CodeSnippets/Snippets/Brocantiny2.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(257, 88),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
BSI2 = keyboard.Keyboard()

# Initialize components for Routine "Brocantiny3"
Brocantiny3Clock = core.Clock()
Brocantiny_5 = visual.ImageStim(
    win=win,
    name='Brocantiny_5', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
BrocantinyMapping_4 = visual.ImageStim(
    win=win,
    name='BrocantinyMapping_4', units='pix', 
    image='../CodeSnippets/Snippets/BrocantinyErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(504, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
BS3 = visual.ImageStim(
    win=win,
    name='BS3', units='pix', 
    image='../CodeSnippets/Snippets/Brocantiny3.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(400, 88),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
BSI3 = keyboard.Keyboard()

# Initialize components for Routine "Brocantiny4"
Brocantiny4Clock = core.Clock()
Brocantiny_6 = visual.ImageStim(
    win=win,
    name='Brocantiny_6', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
BrocantinyMapping_5 = visual.ImageStim(
    win=win,
    name='BrocantinyMapping_5', units='pix', 
    image='../CodeSnippets/Snippets/BrocantinyErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(504, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
BS4 = visual.ImageStim(
    win=win,
    name='BS4', units='pix', 
    image='../CodeSnippets/Snippets/Brocantiny4.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(387, 49),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
BSI4 = keyboard.Keyboard()

# Initialize components for Routine "Einweisung2"
Einweisung2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Im Folgenden wird das Mapping der Variablen auf die Wörter geändert. Ihre Aufgabe bleibt die Gleiche.\n\nWeiter mit <Leertaste> ',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()

# Initialize components for Routine "ProgrammErklärung"
ProgrammErklärungClock = core.Clock()
Brocantiny_2 = visual.ImageStim(
    win=win,
    name='Brocantiny_2', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ProgrammMapping = visual.ImageStim(
    win=win,
    name='ProgrammMapping', units='pix', 
    image='../CodeSnippets/Snippets/ProgrammErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(452, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Programm_Beispiel = visual.ImageStim(
    win=win,
    name='Programm_Beispiel', units='pix', 
    image='../CodeSnippets/Snippets/ProgrammBeispiel.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(504, 88),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Stop"
StopClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Weiter um den nächsten Teil des Experiments zu starten\n\n<Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Programm1"
Programm1Clock = core.Clock()
Brocantiny_7 = visual.ImageStim(
    win=win,
    name='Brocantiny_7', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ProgrammMapping_2 = visual.ImageStim(
    win=win,
    name='ProgrammMapping_2', units='pix', 
    image='../CodeSnippets/Snippets/ProgrammErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(452, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PS1 = visual.ImageStim(
    win=win,
    name='PS1', units='pix', 
    image='../CodeSnippets/Snippets/Programm1.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(244, 88),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
PSI1 = keyboard.Keyboard()

# Initialize components for Routine "Programm2"
Programm2Clock = core.Clock()
Brocantiny_8 = visual.ImageStim(
    win=win,
    name='Brocantiny_8', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ProgrammMapping_3 = visual.ImageStim(
    win=win,
    name='ProgrammMapping_3', units='pix', 
    image='../CodeSnippets/Snippets/ProgrammErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(452, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PS2 = visual.ImageStim(
    win=win,
    name='PS2', units='pix', 
    image='../CodeSnippets/Snippets/Programm2.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(452, 166),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
PSI2 = keyboard.Keyboard()

# Initialize components for Routine "Programm3"
Programm3Clock = core.Clock()
Brocantiny_9 = visual.ImageStim(
    win=win,
    name='Brocantiny_9', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ProgrammMapping_4 = visual.ImageStim(
    win=win,
    name='ProgrammMapping_4', units='pix', 
    image='../CodeSnippets/Snippets/ProgrammErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(452, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PS3 = visual.ImageStim(
    win=win,
    name='PS3', units='pix', 
    image='../CodeSnippets/Snippets/Programm3.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(270, 205),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
PSI3 = keyboard.Keyboard()

# Initialize components for Routine "Programm4"
Programm4Clock = core.Clock()
Brocantiny_10 = visual.ImageStim(
    win=win,
    name='Brocantiny_10', units='pix', 
    image='Resources/Brokantiny.PNG', mask=None,
    ori=0.0, pos=(rm, mu), size=(593, 414),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ProgrammMapping_5 = visual.ImageStim(
    win=win,
    name='ProgrammMapping_5', units='pix', 
    image='../CodeSnippets/Snippets/ProgrammErklärung.png', mask=None,
    ori=0.0, pos=(rm, md), size=(452, 361),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
PS4 = visual.ImageStim(
    win=win,
    name='PS4', units='pix', 
    image='../CodeSnippets/Snippets/Programm4.png', mask=None,
    ori=0.0, pos=(lm, 0), size=(387, 205),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
PSI4 = keyboard.Keyboard()

# Initialize components for Routine "Einweisung3"
Einweisung3Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Im Nachfolgenden werden Ihnen Sätze natürlicher Sprache gezeigt. Geben Sie Bitte an, ob Sie einen intuitven Zusammenhang zwischen der Grammatik der Sätze und dem bisher gezeigten Automaten gibt.\n\nWeiter mit <Leetaste>',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "Satz1"
Satz1Clock = core.Clock()
satz_1 = visual.ImageStim(
    win=win,
    name='satz_1', units='pix', 
    image='../CodeSnippets/Snippets/Satz1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(933, 49),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Satz2"
Satz2Clock = core.Clock()
satz_2 = visual.ImageStim(
    win=win,
    name='satz_2', units='pix', 
    image='../CodeSnippets/Snippets/Satz3.png', mask=None,
    ori=0.0, pos=(0, 0), size=(894, 49),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Satz3"
Satz3Clock = core.Clock()
satz_3 = visual.ImageStim(
    win=win,
    name='satz_3', units='pix', 
    image='../CodeSnippets/Snippets/Satz1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(764, 49),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Danke"
DankeClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Vielen Dank für Ihre Teilnahme\n\nBeenden mit <Leertaste>',
    font='Open Sans',
    pos=(0, 0), height=26.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Startup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
StartupComponents = []
for thisComponent in StartupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Startup"-------
while continueRoutine:
    # get current time
    t = StartupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Startup"-------
for thisComponent in StartupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Startup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Begrüßung"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
BegrüßungComponents = [text, key_resp]
for thisComponent in BegrüßungComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BegrüßungClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Begrüßung"-------
while continueRoutine:
    # get current time
    t = BegrüßungClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BegrüßungClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BegrüßungComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Begrüßung"-------
for thisComponent in BegrüßungComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Begrüßung" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Einweisung"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
EinweisungComponents = [text_4, key_resp_13]
for thisComponent in EinweisungComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EinweisungClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Einweisung"-------
while continueRoutine:
    # get current time
    t = EinweisungClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EinweisungClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EinweisungComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Einweisung"-------
for thisComponent in EinweisungComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
# the Routine "Einweisung" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "CodeStartup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
CodeStartupComponents = []
for thisComponent in CodeStartupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CodeStartupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "CodeStartup"-------
while continueRoutine:
    # get current time
    t = CodeStartupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CodeStartupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CodeStartupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CodeStartup"-------
for thisComponent in CodeStartupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CodeStartup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BrocantinyErklärung"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
BrocantinyErklärungComponents = [Brocantiny, BrocantinyMapping, Brocantiny_Beispiel, key_resp_6]
for thisComponent in BrocantinyErklärungComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BrocantinyErklärungClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BrocantinyErklärung"-------
while continueRoutine:
    # get current time
    t = BrocantinyErklärungClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BrocantinyErklärungClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny* updates
    if Brocantiny.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny.frameNStart = frameN  # exact frame index
        Brocantiny.tStart = t  # local t and not account for scr refresh
        Brocantiny.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny, 'tStartRefresh')  # time at next scr refresh
        Brocantiny.setAutoDraw(True)
    
    # *BrocantinyMapping* updates
    if BrocantinyMapping.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BrocantinyMapping.frameNStart = frameN  # exact frame index
        BrocantinyMapping.tStart = t  # local t and not account for scr refresh
        BrocantinyMapping.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BrocantinyMapping, 'tStartRefresh')  # time at next scr refresh
        BrocantinyMapping.setAutoDraw(True)
    
    # *Brocantiny_Beispiel* updates
    if Brocantiny_Beispiel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_Beispiel.frameNStart = frameN  # exact frame index
        Brocantiny_Beispiel.tStart = t  # local t and not account for scr refresh
        Brocantiny_Beispiel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_Beispiel, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_Beispiel.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BrocantinyErklärungComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BrocantinyErklärung"-------
for thisComponent in BrocantinyErklärungComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny.started', Brocantiny.tStartRefresh)
thisExp.addData('Brocantiny.stopped', Brocantiny.tStopRefresh)
thisExp.addData('BrocantinyMapping.started', BrocantinyMapping.tStartRefresh)
thisExp.addData('BrocantinyMapping.stopped', BrocantinyMapping.tStopRefresh)
thisExp.addData('Brocantiny_Beispiel.started', Brocantiny_Beispiel.tStartRefresh)
thisExp.addData('Brocantiny_Beispiel.stopped', Brocantiny_Beispiel.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "BrocantinyErklärung" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stop"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
StopComponents = [text_5, key_resp_9]
for thisComponent in StopComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stop"-------
while continueRoutine:
    # get current time
    t = StopClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StopClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stop"-------
for thisComponent in StopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "Stop" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Brocantiny1"-------
continueRoutine = True
# update component parameters for each repeat
BSI1.keys = []
BSI1.rt = []
_BSI1_allKeys = []
# keep track of which components have finished
Brocantiny1Components = [Brocantiny_3, BrocantinyMapping_2, BS1, BSI1]
for thisComponent in Brocantiny1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Brocantiny1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Brocantiny1"-------
while continueRoutine:
    # get current time
    t = Brocantiny1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Brocantiny1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_3* updates
    if Brocantiny_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_3.frameNStart = frameN  # exact frame index
        Brocantiny_3.tStart = t  # local t and not account for scr refresh
        Brocantiny_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_3, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_3.setAutoDraw(True)
    
    # *BrocantinyMapping_2* updates
    if BrocantinyMapping_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BrocantinyMapping_2.frameNStart = frameN  # exact frame index
        BrocantinyMapping_2.tStart = t  # local t and not account for scr refresh
        BrocantinyMapping_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BrocantinyMapping_2, 'tStartRefresh')  # time at next scr refresh
        BrocantinyMapping_2.setAutoDraw(True)
    
    # *BS1* updates
    if BS1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BS1.frameNStart = frameN  # exact frame index
        BS1.tStart = t  # local t and not account for scr refresh
        BS1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BS1, 'tStartRefresh')  # time at next scr refresh
        BS1.setAutoDraw(True)
    
    # *BSI1* updates
    waitOnFlip = False
    if BSI1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSI1.frameNStart = frameN  # exact frame index
        BSI1.tStart = t  # local t and not account for scr refresh
        BSI1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSI1, 'tStartRefresh')  # time at next scr refresh
        BSI1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BSI1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BSI1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BSI1.status == STARTED and not waitOnFlip:
        theseKeys = BSI1.getKeys(keyList=['left', 'right'], waitRelease=False)
        _BSI1_allKeys.extend(theseKeys)
        if len(_BSI1_allKeys):
            BSI1.keys = _BSI1_allKeys[-1].name  # just the last key pressed
            BSI1.rt = _BSI1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Brocantiny1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Brocantiny1"-------
for thisComponent in Brocantiny1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_3.started', Brocantiny_3.tStartRefresh)
thisExp.addData('Brocantiny_3.stopped', Brocantiny_3.tStopRefresh)
thisExp.addData('BrocantinyMapping_2.started', BrocantinyMapping_2.tStartRefresh)
thisExp.addData('BrocantinyMapping_2.stopped', BrocantinyMapping_2.tStopRefresh)
thisExp.addData('BS1.started', BS1.tStartRefresh)
thisExp.addData('BS1.stopped', BS1.tStopRefresh)
# check responses
if BSI1.keys in ['', [], None]:  # No response was made
    BSI1.keys = None
thisExp.addData('BSI1.keys',BSI1.keys)
if BSI1.keys != None:  # we had a response
    thisExp.addData('BSI1.rt', BSI1.rt)
thisExp.addData('BSI1.started', BSI1.tStartRefresh)
thisExp.addData('BSI1.stopped', BSI1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Brocantiny1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Brocantiny2"-------
continueRoutine = True
# update component parameters for each repeat
BSI2.keys = []
BSI2.rt = []
_BSI2_allKeys = []
# keep track of which components have finished
Brocantiny2Components = [Brocantiny_4, BrocantinyMapping_3, BS2, BSI2]
for thisComponent in Brocantiny2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Brocantiny2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Brocantiny2"-------
while continueRoutine:
    # get current time
    t = Brocantiny2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Brocantiny2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_4* updates
    if Brocantiny_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_4.frameNStart = frameN  # exact frame index
        Brocantiny_4.tStart = t  # local t and not account for scr refresh
        Brocantiny_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_4, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_4.setAutoDraw(True)
    
    # *BrocantinyMapping_3* updates
    if BrocantinyMapping_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BrocantinyMapping_3.frameNStart = frameN  # exact frame index
        BrocantinyMapping_3.tStart = t  # local t and not account for scr refresh
        BrocantinyMapping_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BrocantinyMapping_3, 'tStartRefresh')  # time at next scr refresh
        BrocantinyMapping_3.setAutoDraw(True)
    
    # *BS2* updates
    if BS2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BS2.frameNStart = frameN  # exact frame index
        BS2.tStart = t  # local t and not account for scr refresh
        BS2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BS2, 'tStartRefresh')  # time at next scr refresh
        BS2.setAutoDraw(True)
    
    # *BSI2* updates
    waitOnFlip = False
    if BSI2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSI2.frameNStart = frameN  # exact frame index
        BSI2.tStart = t  # local t and not account for scr refresh
        BSI2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSI2, 'tStartRefresh')  # time at next scr refresh
        BSI2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BSI2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BSI2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BSI2.status == STARTED and not waitOnFlip:
        theseKeys = BSI2.getKeys(keyList=['left', 'right'], waitRelease=False)
        _BSI2_allKeys.extend(theseKeys)
        if len(_BSI2_allKeys):
            BSI2.keys = _BSI2_allKeys[-1].name  # just the last key pressed
            BSI2.rt = _BSI2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Brocantiny2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Brocantiny2"-------
for thisComponent in Brocantiny2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_4.started', Brocantiny_4.tStartRefresh)
thisExp.addData('Brocantiny_4.stopped', Brocantiny_4.tStopRefresh)
thisExp.addData('BrocantinyMapping_3.started', BrocantinyMapping_3.tStartRefresh)
thisExp.addData('BrocantinyMapping_3.stopped', BrocantinyMapping_3.tStopRefresh)
thisExp.addData('BS2.started', BS2.tStartRefresh)
thisExp.addData('BS2.stopped', BS2.tStopRefresh)
# check responses
if BSI2.keys in ['', [], None]:  # No response was made
    BSI2.keys = None
thisExp.addData('BSI2.keys',BSI2.keys)
if BSI2.keys != None:  # we had a response
    thisExp.addData('BSI2.rt', BSI2.rt)
thisExp.addData('BSI2.started', BSI2.tStartRefresh)
thisExp.addData('BSI2.stopped', BSI2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Brocantiny2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Brocantiny3"-------
continueRoutine = True
# update component parameters for each repeat
BSI3.keys = []
BSI3.rt = []
_BSI3_allKeys = []
# keep track of which components have finished
Brocantiny3Components = [Brocantiny_5, BrocantinyMapping_4, BS3, BSI3]
for thisComponent in Brocantiny3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Brocantiny3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Brocantiny3"-------
while continueRoutine:
    # get current time
    t = Brocantiny3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Brocantiny3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_5* updates
    if Brocantiny_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_5.frameNStart = frameN  # exact frame index
        Brocantiny_5.tStart = t  # local t and not account for scr refresh
        Brocantiny_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_5, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_5.setAutoDraw(True)
    
    # *BrocantinyMapping_4* updates
    if BrocantinyMapping_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BrocantinyMapping_4.frameNStart = frameN  # exact frame index
        BrocantinyMapping_4.tStart = t  # local t and not account for scr refresh
        BrocantinyMapping_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BrocantinyMapping_4, 'tStartRefresh')  # time at next scr refresh
        BrocantinyMapping_4.setAutoDraw(True)
    
    # *BS3* updates
    if BS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BS3.frameNStart = frameN  # exact frame index
        BS3.tStart = t  # local t and not account for scr refresh
        BS3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BS3, 'tStartRefresh')  # time at next scr refresh
        BS3.setAutoDraw(True)
    
    # *BSI3* updates
    waitOnFlip = False
    if BSI3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSI3.frameNStart = frameN  # exact frame index
        BSI3.tStart = t  # local t and not account for scr refresh
        BSI3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSI3, 'tStartRefresh')  # time at next scr refresh
        BSI3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BSI3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BSI3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BSI3.status == STARTED and not waitOnFlip:
        theseKeys = BSI3.getKeys(keyList=['left', 'right'], waitRelease=False)
        _BSI3_allKeys.extend(theseKeys)
        if len(_BSI3_allKeys):
            BSI3.keys = _BSI3_allKeys[-1].name  # just the last key pressed
            BSI3.rt = _BSI3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Brocantiny3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Brocantiny3"-------
for thisComponent in Brocantiny3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_5.started', Brocantiny_5.tStartRefresh)
thisExp.addData('Brocantiny_5.stopped', Brocantiny_5.tStopRefresh)
thisExp.addData('BrocantinyMapping_4.started', BrocantinyMapping_4.tStartRefresh)
thisExp.addData('BrocantinyMapping_4.stopped', BrocantinyMapping_4.tStopRefresh)
thisExp.addData('BS3.started', BS3.tStartRefresh)
thisExp.addData('BS3.stopped', BS3.tStopRefresh)
# check responses
if BSI3.keys in ['', [], None]:  # No response was made
    BSI3.keys = None
thisExp.addData('BSI3.keys',BSI3.keys)
if BSI3.keys != None:  # we had a response
    thisExp.addData('BSI3.rt', BSI3.rt)
thisExp.addData('BSI3.started', BSI3.tStartRefresh)
thisExp.addData('BSI3.stopped', BSI3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Brocantiny3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Brocantiny4"-------
continueRoutine = True
# update component parameters for each repeat
BSI4.keys = []
BSI4.rt = []
_BSI4_allKeys = []
# keep track of which components have finished
Brocantiny4Components = [Brocantiny_6, BrocantinyMapping_5, BS4, BSI4]
for thisComponent in Brocantiny4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Brocantiny4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Brocantiny4"-------
while continueRoutine:
    # get current time
    t = Brocantiny4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Brocantiny4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_6* updates
    if Brocantiny_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_6.frameNStart = frameN  # exact frame index
        Brocantiny_6.tStart = t  # local t and not account for scr refresh
        Brocantiny_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_6, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_6.setAutoDraw(True)
    
    # *BrocantinyMapping_5* updates
    if BrocantinyMapping_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BrocantinyMapping_5.frameNStart = frameN  # exact frame index
        BrocantinyMapping_5.tStart = t  # local t and not account for scr refresh
        BrocantinyMapping_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BrocantinyMapping_5, 'tStartRefresh')  # time at next scr refresh
        BrocantinyMapping_5.setAutoDraw(True)
    
    # *BS4* updates
    if BS4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BS4.frameNStart = frameN  # exact frame index
        BS4.tStart = t  # local t and not account for scr refresh
        BS4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BS4, 'tStartRefresh')  # time at next scr refresh
        BS4.setAutoDraw(True)
    
    # *BSI4* updates
    waitOnFlip = False
    if BSI4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BSI4.frameNStart = frameN  # exact frame index
        BSI4.tStart = t  # local t and not account for scr refresh
        BSI4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BSI4, 'tStartRefresh')  # time at next scr refresh
        BSI4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BSI4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BSI4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BSI4.status == STARTED and not waitOnFlip:
        theseKeys = BSI4.getKeys(keyList=['left', 'right'], waitRelease=False)
        _BSI4_allKeys.extend(theseKeys)
        if len(_BSI4_allKeys):
            BSI4.keys = _BSI4_allKeys[-1].name  # just the last key pressed
            BSI4.rt = _BSI4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Brocantiny4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Brocantiny4"-------
for thisComponent in Brocantiny4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_6.started', Brocantiny_6.tStartRefresh)
thisExp.addData('Brocantiny_6.stopped', Brocantiny_6.tStopRefresh)
thisExp.addData('BrocantinyMapping_5.started', BrocantinyMapping_5.tStartRefresh)
thisExp.addData('BrocantinyMapping_5.stopped', BrocantinyMapping_5.tStopRefresh)
thisExp.addData('BS4.started', BS4.tStartRefresh)
thisExp.addData('BS4.stopped', BS4.tStopRefresh)
# check responses
if BSI4.keys in ['', [], None]:  # No response was made
    BSI4.keys = None
thisExp.addData('BSI4.keys',BSI4.keys)
if BSI4.keys != None:  # we had a response
    thisExp.addData('BSI4.rt', BSI4.rt)
thisExp.addData('BSI4.started', BSI4.tStartRefresh)
thisExp.addData('BSI4.stopped', BSI4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Brocantiny4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Einweisung2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
# keep track of which components have finished
Einweisung2Components = [text_6, key_resp_14]
for thisComponent in Einweisung2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Einweisung2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Einweisung2"-------
while continueRoutine:
    # get current time
    t = Einweisung2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Einweisung2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Einweisung2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Einweisung2"-------
for thisComponent in Einweisung2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStartRefresh)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
thisExp.nextEntry()
# the Routine "Einweisung2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ProgrammErklärung"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
ProgrammErklärungComponents = [Brocantiny_2, ProgrammMapping, Programm_Beispiel, key_resp_7]
for thisComponent in ProgrammErklärungComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProgrammErklärungClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProgrammErklärung"-------
while continueRoutine:
    # get current time
    t = ProgrammErklärungClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProgrammErklärungClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_2* updates
    if Brocantiny_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_2.frameNStart = frameN  # exact frame index
        Brocantiny_2.tStart = t  # local t and not account for scr refresh
        Brocantiny_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_2, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_2.setAutoDraw(True)
    
    # *ProgrammMapping* updates
    if ProgrammMapping.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ProgrammMapping.frameNStart = frameN  # exact frame index
        ProgrammMapping.tStart = t  # local t and not account for scr refresh
        ProgrammMapping.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ProgrammMapping, 'tStartRefresh')  # time at next scr refresh
        ProgrammMapping.setAutoDraw(True)
    
    # *Programm_Beispiel* updates
    if Programm_Beispiel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Programm_Beispiel.frameNStart = frameN  # exact frame index
        Programm_Beispiel.tStart = t  # local t and not account for scr refresh
        Programm_Beispiel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Programm_Beispiel, 'tStartRefresh')  # time at next scr refresh
        Programm_Beispiel.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProgrammErklärungComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProgrammErklärung"-------
for thisComponent in ProgrammErklärungComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_2.started', Brocantiny_2.tStartRefresh)
thisExp.addData('Brocantiny_2.stopped', Brocantiny_2.tStopRefresh)
thisExp.addData('ProgrammMapping.started', ProgrammMapping.tStartRefresh)
thisExp.addData('ProgrammMapping.stopped', ProgrammMapping.tStopRefresh)
thisExp.addData('Programm_Beispiel.started', Programm_Beispiel.tStartRefresh)
thisExp.addData('Programm_Beispiel.stopped', Programm_Beispiel.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "ProgrammErklärung" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Stop"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
StopComponents = [text_5, key_resp_9]
for thisComponent in StopComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stop"-------
while continueRoutine:
    # get current time
    t = StopClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StopClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StopComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stop"-------
for thisComponent in StopComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "Stop" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Programm1"-------
continueRoutine = True
# update component parameters for each repeat
PSI1.keys = []
PSI1.rt = []
_PSI1_allKeys = []
# keep track of which components have finished
Programm1Components = [Brocantiny_7, ProgrammMapping_2, PS1, PSI1]
for thisComponent in Programm1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Programm1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Programm1"-------
while continueRoutine:
    # get current time
    t = Programm1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Programm1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_7* updates
    if Brocantiny_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_7.frameNStart = frameN  # exact frame index
        Brocantiny_7.tStart = t  # local t and not account for scr refresh
        Brocantiny_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_7, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_7.setAutoDraw(True)
    
    # *ProgrammMapping_2* updates
    if ProgrammMapping_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ProgrammMapping_2.frameNStart = frameN  # exact frame index
        ProgrammMapping_2.tStart = t  # local t and not account for scr refresh
        ProgrammMapping_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ProgrammMapping_2, 'tStartRefresh')  # time at next scr refresh
        ProgrammMapping_2.setAutoDraw(True)
    
    # *PS1* updates
    if PS1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PS1.frameNStart = frameN  # exact frame index
        PS1.tStart = t  # local t and not account for scr refresh
        PS1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PS1, 'tStartRefresh')  # time at next scr refresh
        PS1.setAutoDraw(True)
    
    # *PSI1* updates
    waitOnFlip = False
    if PSI1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PSI1.frameNStart = frameN  # exact frame index
        PSI1.tStart = t  # local t and not account for scr refresh
        PSI1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PSI1, 'tStartRefresh')  # time at next scr refresh
        PSI1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PSI1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PSI1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PSI1.status == STARTED and not waitOnFlip:
        theseKeys = PSI1.getKeys(keyList=['left', 'right'], waitRelease=False)
        _PSI1_allKeys.extend(theseKeys)
        if len(_PSI1_allKeys):
            PSI1.keys = _PSI1_allKeys[-1].name  # just the last key pressed
            PSI1.rt = _PSI1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Programm1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Programm1"-------
for thisComponent in Programm1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_7.started', Brocantiny_7.tStartRefresh)
thisExp.addData('Brocantiny_7.stopped', Brocantiny_7.tStopRefresh)
thisExp.addData('ProgrammMapping_2.started', ProgrammMapping_2.tStartRefresh)
thisExp.addData('ProgrammMapping_2.stopped', ProgrammMapping_2.tStopRefresh)
thisExp.addData('PS1.started', PS1.tStartRefresh)
thisExp.addData('PS1.stopped', PS1.tStopRefresh)
# check responses
if PSI1.keys in ['', [], None]:  # No response was made
    PSI1.keys = None
thisExp.addData('PSI1.keys',PSI1.keys)
if PSI1.keys != None:  # we had a response
    thisExp.addData('PSI1.rt', PSI1.rt)
thisExp.addData('PSI1.started', PSI1.tStartRefresh)
thisExp.addData('PSI1.stopped', PSI1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Programm1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Programm2"-------
continueRoutine = True
# update component parameters for each repeat
PSI2.keys = []
PSI2.rt = []
_PSI2_allKeys = []
# keep track of which components have finished
Programm2Components = [Brocantiny_8, ProgrammMapping_3, PS2, PSI2]
for thisComponent in Programm2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Programm2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Programm2"-------
while continueRoutine:
    # get current time
    t = Programm2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Programm2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_8* updates
    if Brocantiny_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_8.frameNStart = frameN  # exact frame index
        Brocantiny_8.tStart = t  # local t and not account for scr refresh
        Brocantiny_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_8, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_8.setAutoDraw(True)
    
    # *ProgrammMapping_3* updates
    if ProgrammMapping_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ProgrammMapping_3.frameNStart = frameN  # exact frame index
        ProgrammMapping_3.tStart = t  # local t and not account for scr refresh
        ProgrammMapping_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ProgrammMapping_3, 'tStartRefresh')  # time at next scr refresh
        ProgrammMapping_3.setAutoDraw(True)
    
    # *PS2* updates
    if PS2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PS2.frameNStart = frameN  # exact frame index
        PS2.tStart = t  # local t and not account for scr refresh
        PS2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PS2, 'tStartRefresh')  # time at next scr refresh
        PS2.setAutoDraw(True)
    
    # *PSI2* updates
    waitOnFlip = False
    if PSI2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PSI2.frameNStart = frameN  # exact frame index
        PSI2.tStart = t  # local t and not account for scr refresh
        PSI2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PSI2, 'tStartRefresh')  # time at next scr refresh
        PSI2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PSI2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PSI2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PSI2.status == STARTED and not waitOnFlip:
        theseKeys = PSI2.getKeys(keyList=['left', 'right'], waitRelease=False)
        _PSI2_allKeys.extend(theseKeys)
        if len(_PSI2_allKeys):
            PSI2.keys = _PSI2_allKeys[-1].name  # just the last key pressed
            PSI2.rt = _PSI2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Programm2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Programm2"-------
for thisComponent in Programm2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_8.started', Brocantiny_8.tStartRefresh)
thisExp.addData('Brocantiny_8.stopped', Brocantiny_8.tStopRefresh)
thisExp.addData('ProgrammMapping_3.started', ProgrammMapping_3.tStartRefresh)
thisExp.addData('ProgrammMapping_3.stopped', ProgrammMapping_3.tStopRefresh)
thisExp.addData('PS2.started', PS2.tStartRefresh)
thisExp.addData('PS2.stopped', PS2.tStopRefresh)
# check responses
if PSI2.keys in ['', [], None]:  # No response was made
    PSI2.keys = None
thisExp.addData('PSI2.keys',PSI2.keys)
if PSI2.keys != None:  # we had a response
    thisExp.addData('PSI2.rt', PSI2.rt)
thisExp.addData('PSI2.started', PSI2.tStartRefresh)
thisExp.addData('PSI2.stopped', PSI2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Programm2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Programm3"-------
continueRoutine = True
# update component parameters for each repeat
PSI3.keys = []
PSI3.rt = []
_PSI3_allKeys = []
# keep track of which components have finished
Programm3Components = [Brocantiny_9, ProgrammMapping_4, PS3, PSI3]
for thisComponent in Programm3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Programm3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Programm3"-------
while continueRoutine:
    # get current time
    t = Programm3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Programm3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_9* updates
    if Brocantiny_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_9.frameNStart = frameN  # exact frame index
        Brocantiny_9.tStart = t  # local t and not account for scr refresh
        Brocantiny_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_9, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_9.setAutoDraw(True)
    
    # *ProgrammMapping_4* updates
    if ProgrammMapping_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ProgrammMapping_4.frameNStart = frameN  # exact frame index
        ProgrammMapping_4.tStart = t  # local t and not account for scr refresh
        ProgrammMapping_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ProgrammMapping_4, 'tStartRefresh')  # time at next scr refresh
        ProgrammMapping_4.setAutoDraw(True)
    
    # *PS3* updates
    if PS3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PS3.frameNStart = frameN  # exact frame index
        PS3.tStart = t  # local t and not account for scr refresh
        PS3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PS3, 'tStartRefresh')  # time at next scr refresh
        PS3.setAutoDraw(True)
    
    # *PSI3* updates
    waitOnFlip = False
    if PSI3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PSI3.frameNStart = frameN  # exact frame index
        PSI3.tStart = t  # local t and not account for scr refresh
        PSI3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PSI3, 'tStartRefresh')  # time at next scr refresh
        PSI3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PSI3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PSI3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PSI3.status == STARTED and not waitOnFlip:
        theseKeys = PSI3.getKeys(keyList=['left', 'right'], waitRelease=False)
        _PSI3_allKeys.extend(theseKeys)
        if len(_PSI3_allKeys):
            PSI3.keys = _PSI3_allKeys[-1].name  # just the last key pressed
            PSI3.rt = _PSI3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Programm3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Programm3"-------
for thisComponent in Programm3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_9.started', Brocantiny_9.tStartRefresh)
thisExp.addData('Brocantiny_9.stopped', Brocantiny_9.tStopRefresh)
thisExp.addData('ProgrammMapping_4.started', ProgrammMapping_4.tStartRefresh)
thisExp.addData('ProgrammMapping_4.stopped', ProgrammMapping_4.tStopRefresh)
thisExp.addData('PS3.started', PS3.tStartRefresh)
thisExp.addData('PS3.stopped', PS3.tStopRefresh)
# check responses
if PSI3.keys in ['', [], None]:  # No response was made
    PSI3.keys = None
thisExp.addData('PSI3.keys',PSI3.keys)
if PSI3.keys != None:  # we had a response
    thisExp.addData('PSI3.rt', PSI3.rt)
thisExp.addData('PSI3.started', PSI3.tStartRefresh)
thisExp.addData('PSI3.stopped', PSI3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Programm3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Programm4"-------
continueRoutine = True
# update component parameters for each repeat
PSI4.keys = []
PSI4.rt = []
_PSI4_allKeys = []
# keep track of which components have finished
Programm4Components = [Brocantiny_10, ProgrammMapping_5, PS4, PSI4]
for thisComponent in Programm4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Programm4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Programm4"-------
while continueRoutine:
    # get current time
    t = Programm4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Programm4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Brocantiny_10* updates
    if Brocantiny_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Brocantiny_10.frameNStart = frameN  # exact frame index
        Brocantiny_10.tStart = t  # local t and not account for scr refresh
        Brocantiny_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Brocantiny_10, 'tStartRefresh')  # time at next scr refresh
        Brocantiny_10.setAutoDraw(True)
    
    # *ProgrammMapping_5* updates
    if ProgrammMapping_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ProgrammMapping_5.frameNStart = frameN  # exact frame index
        ProgrammMapping_5.tStart = t  # local t and not account for scr refresh
        ProgrammMapping_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ProgrammMapping_5, 'tStartRefresh')  # time at next scr refresh
        ProgrammMapping_5.setAutoDraw(True)
    
    # *PS4* updates
    if PS4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PS4.frameNStart = frameN  # exact frame index
        PS4.tStart = t  # local t and not account for scr refresh
        PS4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PS4, 'tStartRefresh')  # time at next scr refresh
        PS4.setAutoDraw(True)
    
    # *PSI4* updates
    waitOnFlip = False
    if PSI4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PSI4.frameNStart = frameN  # exact frame index
        PSI4.tStart = t  # local t and not account for scr refresh
        PSI4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PSI4, 'tStartRefresh')  # time at next scr refresh
        PSI4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(PSI4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(PSI4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if PSI4.status == STARTED and not waitOnFlip:
        theseKeys = PSI4.getKeys(keyList=['left', 'right'], waitRelease=False)
        _PSI4_allKeys.extend(theseKeys)
        if len(_PSI4_allKeys):
            PSI4.keys = _PSI4_allKeys[-1].name  # just the last key pressed
            PSI4.rt = _PSI4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Programm4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Programm4"-------
for thisComponent in Programm4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Brocantiny_10.started', Brocantiny_10.tStartRefresh)
thisExp.addData('Brocantiny_10.stopped', Brocantiny_10.tStopRefresh)
thisExp.addData('ProgrammMapping_5.started', ProgrammMapping_5.tStartRefresh)
thisExp.addData('ProgrammMapping_5.stopped', ProgrammMapping_5.tStopRefresh)
thisExp.addData('PS4.started', PS4.tStartRefresh)
thisExp.addData('PS4.stopped', PS4.tStopRefresh)
# check responses
if PSI4.keys in ['', [], None]:  # No response was made
    PSI4.keys = None
thisExp.addData('PSI4.keys',PSI4.keys)
if PSI4.keys != None:  # we had a response
    thisExp.addData('PSI4.rt', PSI4.rt)
thisExp.addData('PSI4.started', PSI4.tStartRefresh)
thisExp.addData('PSI4.stopped', PSI4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Programm4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Einweisung3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
Einweisung3Components = [text_2, key_resp_8]
for thisComponent in Einweisung3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Einweisung3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Einweisung3"-------
while continueRoutine:
    # get current time
    t = Einweisung3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Einweisung3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Einweisung3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Einweisung3"-------
for thisComponent in Einweisung3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "Einweisung3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Satz1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
Satz1Components = [satz_1, key_resp_2]
for thisComponent in Satz1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Satz1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Satz1"-------
while continueRoutine:
    # get current time
    t = Satz1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Satz1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *satz_1* updates
    if satz_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        satz_1.frameNStart = frameN  # exact frame index
        satz_1.tStart = t  # local t and not account for scr refresh
        satz_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(satz_1, 'tStartRefresh')  # time at next scr refresh
        satz_1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['left', 'right'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Satz1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Satz1"-------
for thisComponent in Satz1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('satz_1.started', satz_1.tStartRefresh)
thisExp.addData('satz_1.stopped', satz_1.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Satz1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Satz2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
Satz2Components = [satz_2, key_resp_4]
for thisComponent in Satz2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Satz2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Satz2"-------
while continueRoutine:
    # get current time
    t = Satz2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Satz2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *satz_2* updates
    if satz_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        satz_2.frameNStart = frameN  # exact frame index
        satz_2.tStart = t  # local t and not account for scr refresh
        satz_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(satz_2, 'tStartRefresh')  # time at next scr refresh
        satz_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['left', 'right'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Satz2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Satz2"-------
for thisComponent in Satz2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('satz_2.started', satz_2.tStartRefresh)
thisExp.addData('satz_2.stopped', satz_2.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Satz2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Satz3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Satz3Components = [satz_3, key_resp_5]
for thisComponent in Satz3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Satz3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Satz3"-------
while continueRoutine:
    # get current time
    t = Satz3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Satz3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *satz_3* updates
    if satz_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        satz_3.frameNStart = frameN  # exact frame index
        satz_3.tStart = t  # local t and not account for scr refresh
        satz_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(satz_3, 'tStartRefresh')  # time at next scr refresh
        satz_3.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['left', 'right'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Satz3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Satz3"-------
for thisComponent in Satz3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('satz_3.started', satz_3.tStartRefresh)
thisExp.addData('satz_3.stopped', satz_3.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "Satz3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Danke"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
if use_eyetracking:
    logger.stop_recording()
# keep track of which components have finished
DankeComponents = [text_3, key_resp_3]
for thisComponent in DankeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DankeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Danke"-------
while continueRoutine:
    # get current time
    t = DankeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DankeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DankeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Danke"-------
for thisComponent in DankeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Danke" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
