import dilloTools
dilloTools.init()
import maya.cmds as mc

mc.commandPort(name=":7001",sourceType="mel")

mc.commandPort(name=":7002",sourceType="python")