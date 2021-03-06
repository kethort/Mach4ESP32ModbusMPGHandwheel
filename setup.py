from distutils.core import setup
import py2exe
import os

installer_script = os.path.join(os.getcwd(), 'src\\installer\\MPGInstaller.py')
module_script = os.path.join(os.getcwd(), 'src\\Mach4Module\\ModbusMPG.lua')
wizard_script = os.path.join(os.getcwd(), 'src\\Mach4Wizard\\MPGWiz.mcs')
global_regs_ini = os.path.join(os.getcwd(), 'src\\ini_settings\\gReg_ini_settings')
modbus_ini = os.path.join(os.getcwd(), 'src\\ini_settings\\modbus_ini_settings')
modbus_ini_display = os.path.join(os.getcwd(), 'src\\ini_settings\\modbus_ini_settings_display')
update_plc = os.path.join(os.getcwd(), 'src\\ini_settings\\update_plc')
update_screen_load = os.path.join(os.getcwd(), 'src\\ini_settings\\update_screen_load')

data_files = [('', [module_script, wizard_script, global_regs_ini, modbus_ini, modbus_ini_display, update_plc, update_screen_load])]
setup(windows=[installer_script], data_files = data_files)