from ptg2.zos.emul import get_emulator
from ptg2.zos.emul_apps import TPXApp, TSOApp, ISPFApp
from ptg2.context import use_system, set_system, get_system, get_userid, set_userid
from ptg2 import zos


# This test will run Model Reports

def HEMMModelReports(em):
    
    em.screen.log()