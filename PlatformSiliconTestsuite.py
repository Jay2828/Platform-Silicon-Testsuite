import datetime
import re
import subprocess
import time

import conplyent
import wx
from atkysy import atkysyglobal
from atm import atmcentral, _smu_interface
from atm.static.smu_definitions import *

from build import PlatformSiliconTestsuiteGUI


# --------------------------------------------------------------
# Live Console-Read Definition (Attempt)
# --------------------------------------------------------------
# def popenExecute(cmd):
#     print("popenExecute")
#     popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
#     for stdoutLine in iter(popen.stdout.readline, ""):
#         yield stdoutLine
#     popen.stdout.close()
#     returnCode = popen.wait()
#     if returnCode:
#         raise subprocess.CalledProcessError(returnCode, cmd)

# ----------------------------------------------------------------------------------------------------------------------
# For Voltage vs Frequency Testing.
# ----------------------------------------------------------------------------------------------------------------------
# Normalizing SUT After Finishing Voltage vs Frequency Testing.
def endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName):
    if cpuVDD == 8:
        if coreSelect == coreEnd:
            print("\nTest Completed.\nNormalizing System.\n")
            voltFreqChange(ipSelection, coreSelect, cpuVDD, 4000)
            subprocess.call(['cmd', '/c', "chiller " + comPort + "-t 25"], shell=True)
            return True
        else:
            print("End of Core-Run.")
            testResults = open(r".\build\GeneratedFiles\VoltageVsFrequency\Results\VoltageVsFrequencyTestResults_"
                               + str(outputName) + ".txt", "a+")
            testResults.write("\n")
            testResults.close()
            return False


# Writing to Voltage vs Frequency Test Results
def writeTest(coreSelect, cpuVDD, outputName, coreSelectFreq):
    cpuVDDtoC = 1.55 - (cpuVDD * 0.00625)
    testResults = open(r".\build\GeneratedFiles\VoltageVsFrequency\Results\VoltageVsFrequencyTestResults_"
                       + str(outputName) + ".txt", "a+")
    testResults.write((datetime.datetime.now().strftime('%H:%M')) + " Core" + str(coreSelect) + " " + str(cpuVDDtoC) +
                      " " + str(coreSelectFreq) + "\n")


# Changing CPU Voltage and Frequency.
def voltFreqChange(ipSelection, coreSelect, cpuVDD, coreSelectFreq):
    userScript = r".\VoltageVsFrequency\CoreMarginingAdjustable.pl"
    print("Unlocking Wombat.")
    atkysyglobal.wombat.unlock(straight=True)
    print("perl main.pl -user_script=\"" + userScript + "\" -wombat_ip=" + str(ipSelection) + " -coreSelect=" +
          str(coreSelect) + " -cpuVDD=" + str(cpuVDD) + " -coreSelectFreq=" + str(coreSelectFreq))
    subprocess.call("perl main.pl -user_script=\"" + userScript + "\" -wombat_ip=" + str(ipSelection) + " -coreSelect="
                    + str(coreSelect) + " -cpuVDD=" + str(cpuVDD) + " -coreSelectFreq=" + str(coreSelectFreq),
                    cwd=r"C:\PAPI\Vermeer PAPI")
    # Reconnecting to Wombat with atKysy.
    atkysyglobal.wombat.unlock(straight=True)
    print("Frequency set.")
    time.sleep(5)

    # _smu_interface.send_cmd(atmcentral.atm[0], SSP_SMU_MSG.TEST_SetCoreCksFddScalar, 0x0)
    # _smu_interface.send_cmd(atmcentral.atm[0], SSP_SMU_MSG.TEST_SetL3CksFddScalar, 0x0)


# Recovering SUT from Freezing or Crashes. (Fusing if Necessary.)
def sutActiveFail(sutIP, ipSelection, fuseSelection, filePath, comPort):
    print("SUT is down.")
    subprocess.call("atkysy -w " + ipSelection + " power on")
    subprocess.call("atkysy -w " + ipSelection + " cold-reset")
    time.sleep(2)
    if fuseSelection is True:
        subprocess.call("atkysy -w " + str(ipSelection) + " fuse -f " +
                        "\"" + str(filePath) + "\"")
    bootAttempt = 1
    for x in range(1, 41):
        try:
            if bootAttempt % 4 == 0:
                if bootAttempt == 40:
                    print("Unable to boot system.")
                    subprocess.call(['cmd', '/c', "chiller " + comPort + "-t 25"], shell=True)
                    return 0
                print("System not booting, and will perform another cold-reset/fusing.")
                subprocess.call("atkysy -w " + ipSelection + " cold-reset ")
                time.sleep(2)
                if fuseSelection is True:
                    subprocess.call("atkysy -w " + str(ipSelection) + " fuse -f " +
                                    "\"" + str(filePath) + "\"")
                bootAttempt += 1
                continue
            connection = conplyent.client.add(str(sutIP), 9922)
            connection.connect(timeout=90)
        except:
            print("System still not active. " + str(bootAttempt))
            bootAttempt += 1
            time.sleep(30)


# ----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------------------------


class Main(PlatformSiliconTestsuiteGUI.MyFrame1):
    def __init__(self, parent):
        PlatformSiliconTestsuiteGUI.MyFrame1.__init__(self, parent)

        # --------------------------------------------------------------------------------------------------------------
        # Window-Resizing Code Snippet
        # --------------------------------------------------------------------------------------------------------------
        self.sizerGUI = wx.BoxSizer(wx.VERTICAL)
        self.sizerGUI.Add(self.m_panel17, 1, wx.EXPAND)
        self.SetSizerAndFit(self.sizerGUI)
        self.m_filePicker3.Hide()

        # --------------------------------------------------------------------------------------------------------------
        # Building Tree
        # --------------------------------------------------------------------------------------------------------------
        platSiTestSuiteRoot = self.m_treeCtrl1.AddRoot("Platform Silicon Test Suite")
        memNode = self.m_treeCtrl1.AppendItem(platSiTestSuiteRoot, "Memory")

        atablOverrideNode = self.m_treeCtrl1.AppendItem(memNode, "AT ABL Override")
        self.m_treeCtrl1.AppendItem(atablOverrideNode, "Force Speed")
        self.m_treeCtrl1.AppendItem(atablOverrideNode, "Frequency Sweep")
        self.m_treeCtrl1.AppendItem(atablOverrideNode, "Timing Scale")

        atDecoderNode = self.m_treeCtrl1.AppendItem(memNode, "AT Decoder")
        self.m_treeCtrl1.AppendItem(atDecoderNode, "MSB Decoder")
        self.m_treeCtrl1.AppendItem(atDecoderNode, "PMU Decoder")

        atKysyNode = self.m_treeCtrl1.AppendItem(memNode, "AT Kysy")
        self.m_treeCtrl1.AppendItem(atKysyNode, "Fuse")
        self.m_treeCtrl1.AppendItem(atKysyNode, "Read Clk (SSP+)")
        self.m_treeCtrl1.AppendItem(atKysyNode, "Read Postcodes (In Real Time)")
        self.m_treeCtrl1.AppendItem(atKysyNode, "Read VDDs (SSP+)")

        atmNode = self.m_treeCtrl1.AppendItem(memNode, "ATM")
        self.m_treeCtrl1.AppendItem(atmNode, "ABL Breakpoint")
        self.m_treeCtrl1.AppendItem(atmNode, "Address Decode")
        self.m_treeCtrl1.AppendItem(atmNode, "ATM Config")
        self.m_treeCtrl1.AppendItem(atmNode, "Enable FClk DPM through Messages")
        self.m_treeCtrl1.AppendItem(atmNode, "Force MP State")
        self.m_treeCtrl1.AppendItem(atmNode, "Memory Map")
        self.m_treeCtrl1.AppendItem(atmNode, "Read MPR")
        self.m_treeCtrl1.AppendItem(atmNode, "Read MR Commands")
        self.m_treeCtrl1.AppendItem(atmNode, "Read SPD (MTS Only)")
        self.m_treeCtrl1.AppendItem(atmNode, "Snapshot")
        self.m_treeCtrl1.AppendItem(atmNode, "Switch MP States Indefinitely")
        self.m_treeCtrl1.AppendItem(atmNode, "Unforce MP States")

        atmDumpsNode = self.m_treeCtrl1.AppendItem(memNode, "ATM Dumps")
        self.m_treeCtrl1.AppendItem(atmDumpsNode, "SRSM Dump")
        self.m_treeCtrl1.AppendItem(atmDumpsNode, "UMC Compare")
        self.m_treeCtrl1.AppendItem(atmDumpsNode, "UMC Dump")

        atmMiscNode = self.m_treeCtrl1.AppendItem(memNode, "ATM Miscellaneous")
        self.m_treeCtrl1.AppendItem(atmMiscNode, "Check Memory Configuration Populated")
        self.m_treeCtrl1.AppendItem(atmMiscNode, "Decode MR Commands")
        self.m_treeCtrl1.AppendItem(atmMiscNode, "Decode Part Number")
        self.m_treeCtrl1.AppendItem(atmMiscNode, "ECC Injector")

        atPMUNode = self.m_treeCtrl1.AppendItem(memNode, "AT PMU")
        self.m_treeCtrl1.AppendItem(atPMUNode, "Message Block Overrides")
        self.m_treeCtrl1.AppendItem(atPMUNode, "PMU Breakpoint")
        self.m_treeCtrl1.AppendItem(atPMUNode, "PMU Tuner")
        self.m_treeCtrl1.AppendItem(atPMUNode, "Set HDET Level")

        atRebootNode = self.m_treeCtrl1.AppendItem(memNode, "AT Reboot")
        self.m_treeCtrl1.AppendItem(atRebootNode, "ABL Parser")
        self.m_treeCtrl1.AppendItem(atRebootNode, "Functional (Rebooter + 3DMark)")
        self.m_treeCtrl1.AppendItem(atRebootNode, "MBIST Parser")
        self.m_treeCtrl1.AppendItem(atRebootNode, "Training Consistency")
        self.m_treeCtrl1.AppendItem(atRebootNode, "Training Consistency HDTOUT")

        atRebootMiscNode = self.m_treeCtrl1.AppendItem(memNode, "AT Reboot Miscellaneous")
        self.m_treeCtrl1.AppendItem(atRebootMiscNode, "Read COM-Port")

        atRRWNode = self.m_treeCtrl1.AppendItem(memNode, "AT RRW")
        self.m_treeCtrl1.AppendItem(atRRWNode, "RRW Cont")
        self.m_treeCtrl1.AppendItem(atRRWNode, "RRW Eye")
        self.m_treeCtrl1.AppendItem(atRRWNode, "RRW Parse")
        self.m_treeCtrl1.AppendItem(atRRWNode, "RRW Single")

        atTestSuiteNode = self.m_treeCtrl1.AppendItem(memNode, "AT Test Suite")
        self.m_treeCtrl1.AppendItem(atTestSuiteNode, "Margins 1D")
        self.m_treeCtrl1.AppendItem(atTestSuiteNode, "Margins 2D")

        powRoot = self.m_treeCtrl1.AppendItem(platSiTestSuiteRoot, "Power")
        print(powRoot)

        marginingNode = self.m_treeCtrl1.AppendItem(powRoot, "Margining")
        self.m_treeCtrl1.AppendItem(marginingNode, "Voltage vs Frequency Margining")

        self.m_treeCtrl1.Expand(platSiTestSuiteRoot)

        # ------------------------------------------------------------------------------------------------------------------
        # GUI Interactions
        # ------------------------------------------------------------------------------------------------------------------
        # Populating Wombat IP Addresses
        # ------------------------------------------------------------------------------------------------------------------
        wombatList = open(r'./build/GeneratedFiles/WombatList.txt', "r")
        self.m_choice2.Clear()
        for item in wombatList:
            self.m_choice2.Append(item)

    def renoirSelect(self, event):
        self.m_statusBar1.SetStatusText("Renoir Selected.")
        titleIP = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", self.GetTitle())
        if str(titleIP) == "[]":
            self.SetTitle("Platform Silicon Test Suite - Renoir")
        else:
            self.SetTitle("Platform Silicon Test Suite - Renoir - " + str(titleIP[0]))
        self.m_menuItem1.Check(True)
        self.m_menuItem2.Check(False)

    def vermeerSelect(self, event):
        self.m_statusBar1.SetStatusText("Vermeer Selected.")
        titleIP = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", self.GetTitle())
        if str(titleIP) == "[]":
            self.SetTitle("Platform Silicon Test Suite - Vermeer")
        else:
            self.SetTitle("Platform Silicon Test Suite - Vermeer - " + str(titleIP[0]))
        self.m_menuItem1.Check(False)
        self.m_menuItem2.Check(True)

    def newIPSelect(self, event):
        self.m_statusBar1.SetStatusText("New Wombat IP Selected.")
        wombatDialog = wx.TextEntryDialog(self, "", "New Wombat IP")
        # --------------------------------------------------------------------------------------------------------------
        # "Add IP' Dialog Box Interactions.
        # --------------------------------------------------------------------------------------------------------------
        if wombatDialog.ShowModal() == wx.ID_CANCEL:
            return 0
        if wombatDialog.ShowModal() == wx.ID_OK:
            # Ensuring proper IP is inputted.
            wombatIP = re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
                                r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', wombatDialog.GetValue())
            if wombatIP is not None:
                # Checking for IP duplicates.
                ipCheck = open(r'./build/GeneratedFiles/WombatList.txt', "r")
                ipFileLines = ipCheck.readlines()
                for ip in ipFileLines:
                    ipMatch = re.search(wombatDialog.GetValue(), ip)
                    if ipMatch is not None:
                        wx.MessageBox('Wombat IP already exists.', 'IP Duplicate', wx.OK | wx.ICON_INFORMATION)
                        return 0
                # Writing IP address into WombatList.txt.
                wombatList = open(r'./build/GeneratedFiles/WombatList.txt', "a+")
                wombatList.write("\n" + str(wombatDialog.GetValue()))
                wombatList.close()
                # Sorting IP addresses found in WombatList.txt.
                with open(r'./build/GeneratedFiles/WombatList.txt', "r") as infile:
                    iplist = sorted([i.strip() for i in infile.readlines()], key=lambda x: int(''.join(
                        (lambda a: lambda v: a(a, v))(lambda s, x: x if len(x) == 3 else s(s, '0' + x))(i) for i in
                        x.split('.'))))
                # Updating WombatList.txt with sorted IP addresses.
                with open(r'./build/GeneratedFiles/WombatList.txt', "w+") as outfile:
                    outfile.write("\n".join(i for i in iplist))
                wombatList.close()
                self.m_statusBar1.SetStatusText("New Wombat Added.")
                # Updating Wombat IP address' ChoiceBox.
                wombatList = open(r'./build/GeneratedFiles/WombatList.txt', "r")
                self.m_choice2.Clear()
                for item in wombatList:
                    self.m_choice2.Append(item)
            else:
                wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
                return 0

    def itemSelect(self, event):
        # --------------------------------------------------------------------------------------------------------------
        # Showing Selected Test-Panels
        # --------------------------------------------------------------------------------------------------------------
        # Memory
        # --------------------------------------------------------------------------------------------------------------
        # atKysy
        # --------------------------------------------------------------------------------------------------------------
        if str(self.m_treeCtrl1.GetItemText(event.GetItem())) == "Fuse":
            self.m_statusBar1.SetStatusText("Fuse Selected.")
            self.fusePanel.Show()
        else:
            self.fusePanel.Hide()

        if str(self.m_treeCtrl1.GetItemText(event.GetItem())) == "Read Clk (SSP+)":
            self.m_statusBar1.SetStatusText("Read Clk (SSP+) Selected.")
            self.readClkPanel.Show()
        else:
            self.readClkPanel.Hide()

        if str(self.m_treeCtrl1.GetItemText(event.GetItem())) == "Read Postcodes (In Real Time)":
            self.m_statusBar1.SetStatusText("Read Postcodes Selected.")
            self.readPostCodesPanel.Show()
        else:
            self.readPostCodesPanel.Hide()

        if str(self.m_treeCtrl1.GetItemText(event.GetItem())) == "Read VDDs (SSP+)":
            self.m_statusBar1.SetStatusText("Read VDDs Selected.")
            self.readVDDsPanel.Show()
        else:
            self.readVDDsPanel.Hide()
        # --------------------------------------------------------------------------------------------------------------
        # atReboot
        # --------------------------------------------------------------------------------------------------------------
        if str(self.m_treeCtrl1.GetItemText(event.GetItem())) == "Training Consistency":
            self.m_statusBar1.SetStatusText("Training Consistency Selected.")
            self.trainConPanel.Show()
            wx.MessageBox('Please ensure that ABL Logging is enabled in SUT\'s BIOS, and that the logger-hardware is '
                          'properly communicating with your host.', 'Logging Setup', wx.OK | wx.ICON_WARNING)
        else:
            self.trainConPanel.Hide()

        # --------------------------------------------------------------------------------------------------------------
        # Power
        # --------------------------------------------------------------------------------------------------------------
        if str(self.m_treeCtrl1.GetItemText((event.GetItem()))) == "Voltage vs Frequency Margining":
            self.m_statusBar1.SetStatusText("Voltage vs Frequency Margining Selected.")
            self.voltVSTempPanel.Show()
        else:
            self.voltVSTempPanel.Hide()
            self.m_gauge1.Hide()

    # ------------------------------------------------------------------------------------------------------------------
    # Reveal Miscellaneous Hidden Elements
    # ------------------------------------------------------------------------------------------------------------------
    def guiInteract(self, event):
        # --------------------------------------------------------------------------------------------------------------
        # Training Consistency Window
        # --------------------------------------------------------------------------------------------------------------
        # Training Consistency "Fuse File" Check Box
        if self.m_checkBox1.GetValue() is True:
            self.m_filePicker2.Show()
        else:
            self.m_filePicker2.Hide()

        # Training Consistency "Custom Settings" Check Box
        if self.m_checkBox12.GetValue() is True:
            self.m_panel15.Show()
        else:
            self.m_panel15.Hide()

        # Training Consistency "Username/Password" Check Box
        if self.m_checkBox3.GetValue() is True:
            self.m_staticText27.Show()
            self.m_textCtrl15.Show()
            self.m_staticText28.Show()
            self.m_textCtrl16.Show()
            self.SetSizerAndFit(self.sizerGUI, deleteOld=False)
            self.Layout()
        else:
            self.m_staticText27.Hide()
            self.m_textCtrl15.Hide()
            self.m_staticText28.Hide()
            self.m_textCtrl16.Hide()
            self.SetSizerAndFit(self.sizerGUI, deleteOld=False)
            self.Layout()

        # Training Consistency "ABL Timeout" Check Box
        if self.m_checkBox4.GetValue() is True:
            self.m_textCtrl17.Show()
        else:
            self.m_textCtrl17.Hide()

        # Training Consistency "1D String" Check Box
        if self.m_checkBox5.GetValue() is True:
            self.m_dirPicker1.Show()
        else:
            self.m_dirPicker1.Hide()

        # Training Consistency "2D String" Check Box
        if self.m_checkBox6.GetValue() is True:
            self.m_dirPicker2.Show()
        else:
            self.m_dirPicker2.Hide()

        # Training Consistency "End-Flag String" Check Box
        if self.m_checkBox7.GetValue() is True:
            self.m_textCtrl18.Show()
        else:
            self.m_textCtrl18.Hide()

        # Training Consistency "Connect to SUT IP" Check Box
        if self.m_checkBox8.GetValue() is True:
            self.m_textCtrl19.Show()
        else:
            self.m_textCtrl19.Hide()

        # Training Consistency "MST Loops" Check Box
        if self.m_checkBox9.GetValue() is True:
            self.m_textCtrl20.Show()
        else:
            self.m_textCtrl20.Hide()

        # Training Consistency "Memory Snapshot" Check Box
        if self.m_checkBox10.GetValue() is True:
            self.m_textCtrl21.Show()
        else:
            self.m_textCtrl21.Hide()
        # --------------------------------------------------------------------------------------------------------------
        # Voltage vs Frequency Window
        # --------------------------------------------------------------------------------------------------------------
        # Voltage vs Frequency "Fuse File" Check Box
        if self.m_checkBox13.GetValue() is True:
            self.m_filePicker3.Show()
        else:
            self.m_filePicker3.Hide()

    # ------------------------------------------------------------------------------------------------------------------
    # Setting Wombat IP in Frame Title and all "Wombat-IP Boxes"
    # ------------------------------------------------------------------------------------------------------------------
    def ipSet(self, ipname):
        # Setting Frame Title
        titleIP = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", self.GetTitle())
        self.m_statusBar1.SetStatusText(str(titleIP))
        if str(titleIP) == "[]":
            self.SetTitle(str(self.GetTitle()) + " - " + str(ipname))
        else:
            newTitle = re.sub(str(titleIP[0]), str(ipname), str(self.GetTitle()))
            self.SetTitle(newTitle)

    # ------------------------------------------------------------------------------------------------------------------
    # Button-Event Definitions (Test Procedures)
    # ------------------------------------------------------------------------------------------------------------------
    # atKysy
    # ------------------------------------------------------------------------------------------------------------------
    def coldReset(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
                            r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ipSelection)
        if wombatIP is not None:
            coldResetWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Cold-Resetting System.")
        print("atkysy " + coldResetWombatIP + "cold-reset ")
        subprocess.call("atkysy " + coldResetWombatIP + "cold-reset ")

    def fuse(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            fuseWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText(str(self.m_filePicker1.GetPath()))
        if self.m_filePicker1.GetPath() is not "":
            fuseFile = "fuse -f " + "\"" + str(self.m_filePicker1.GetPath()) + "\""
        else:
            wx.MessageBox('Please Choose a Valid Fuse File.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0

        self.m_statusBar1.SetStatusText("Fusing System.")
        print("atkysy " + fuseWombatIP + fuseFile)
        subprocess.call("atkysy " + fuseWombatIP + fuseFile)

    def powerOff(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            powerOffWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Shutting System Down.")
        print("atkysy " + powerOffWombatIP + "power off")
        subprocess.call("atkysy " + powerOffWombatIP + "power off")

    def powerOn(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            powerOnWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Turning System On.")
        print("atkysy " + powerOnWombatIP + "power on")
        subprocess.call("atkysy " + powerOnWombatIP + "power on")

    def readClk(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            readClkWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Reading System Clocks.")
        print("atkysy " + readClkWombatIP + "read-clk")
        subprocess.Popen("atkysy " + readClkWombatIP + "read-clk", creationflags=subprocess.CREATE_NEW_CONSOLE,
                         universal_newlines=True)
        # for line in readClk.stdout:
        #     print(line)

    def readPostcodes(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            readPostcodesWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Reading Postcodes.")
        print("atkysy " + readPostcodesWombatIP + "post-read")
        subprocess.Popen("atkysy " + readPostcodesWombatIP + "post-read", creationflags=subprocess.CREATE_NEW_CONSOLE,
                         universal_newlines=True)

    def readVDDs(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            readVDDsWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Reading VDDs.")
        print("atkysy " + readVDDsWombatIP + "read-vdds")
        subprocess.Popen("atkysy " + readVDDsWombatIP + "read-vdds", creationflags=subprocess.CREATE_NEW_CONSOLE,
                         universal_newlines=True)

    def unlockWombat(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ipSelection)
        if wombatIP is not None:
            unlockWombatWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Unlocking Wombat.")
        print("atkysy " + unlockWombatWombatIP + "unlock-wombat")
        subprocess.call("atkysy " + unlockWombatWombatIP + "unlock-wombat")
        self.m_statusBar1.SetStatusText("Wombat Unlocked.")

    def warmReset(self, event):
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetSelection())).rstrip()
        wombatIP = re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
                            r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ipSelection)
        if wombatIP is not None:
            warmResetWombatIP = "-w " + ipSelection + " "
            self.ipSet(ipSelection)
        else:
            wx.MessageBox('Please Input a Valid Wombat-IP Address.', 'Error', wx.OK | wx.ICON_ERROR)
            return 0
        self.m_statusBar1.SetStatusText("Warm-Resetting System.")
        print("atkysy " + warmResetWombatIP + "warm-reset ")
        subprocess.call("atkysy " + warmResetWombatIP + "warm-reset ")

    # ------------------------------------------------------------------------------------------------------------------
    # atReboot
    # ------------------------------------------------------------------------------------------------------------------
    def trainConsistency(self, event):
        print("Start Training Consistency.\n(This procedure is a work in progress.)")

    # ------------------------------------------------------------------------------------------------------------------
    # Voltage vs Frequency Margining
    # ------------------------------------------------------------------------------------------------------------------
    def voltVsFreqMarg(self, event):
        global thmCore0, thmCore0Ave, thm, inCstate, cstateDisable, mp1Val, mp1, dfCstateDisable, dfInCstate, thread1, \
            thread0

        # Creating test results document, if needed.
        try:
            open(r".\build\GeneratedFiles\VoltageVsFrequency\Results\VoltageVsFrequencyTestResults_" +
                 str(self.m_textCtrl12.GetValue()) + ".txt", "x")
        except Exception:
            print("File name exists, and will be appended.")

        # Declaring Initial Variable Values. (cpuVDD = 104 = 0.9V)
        coreSelect = int(self.m_radioBox2.GetString(self.m_radioBox2.GetSelection()))  # Core Selection
        coreEnd = int(self.m_radioBox3.GetString(self.m_radioBox3.GetSelection()))  # Core Selection
        coreArrayValue0 = coreSelect * 2  # CPU Selection on SUT
        coreArrayValue1 = (coreSelect * 2) + 1  # CPU Selection on SUT
        cpuVDD = round((1.55 - float(self.m_radioBox4.GetString(self.m_radioBox4.GetSelection()))) / 0.00625, 0)
        coreSelectFreq = 3600  # MHz
        ipSelection = str(self.m_choice2.GetString(self.m_choice2.GetCurrentSelection())).rstrip()
        self.ipSet(ipSelection)
        sutIP = str(self.m_textCtrl11.GetValue())
        fuseSelection = self.m_checkBox13.GetValue()
        filePath = str(self.m_filePicker3.GetPath())
        outputName = str(self.m_textCtrl12.GetValue())

        systemHoldTemp = 50
        chillerHoldTemp = 10
        if self.m_radioBox1.GetSelection() is 1:
            systemHoldTemp = 70
            chillerHoldTemp = 30
        if self.m_radioBox1.GetSelection() is 2:
            systemHoldTemp = 90
            chillerHoldTemp = 50

        # Setting Initial Chiller Temperature.
        self.m_statusBar1.SetStatusText("Starting Voltage VS Frequency Margining at " +
                                        str(self.m_radioBox1.GetString(self.m_radioBox1.GetSelection())))
        comPort = "-p " + str(str(self.m_choice3.GetString(self.m_choice3.GetSelection()))) + " "
        print((datetime.datetime.now().strftime('%H:%M')) + " - chiller " + comPort + "-t " + str(chillerHoldTemp))
        self.m_statusBar1.SetStatusText("Setting Initial Chiller Temperature.")
        try:
            subprocess.call(["cmd", "/c", "chiller " + comPort + "-t " + str(chillerHoldTemp)], shell=True)
            self.m_statusBar1.SetStatusText("Initial Chiller Temperature Reached.")

            # Setting up Wombat platform, and checking for Wombat errors.
            atkysyglobal.init_platform(ipSelection, pdm=False)
            atmcentral.setup_atm(new_atm=True)
        except RuntimeError:
            wx.MessageBox("Please turn on system, and try again.  Please, also ensure that Wombat is connected to the"
                          "power-jumper on SUT.", 'Error', wx.OK | wx.ICON_ERROR)
            return 0
            # sutActiveFail(str(self.m_textCtrl11.GetValue()), ipSelection, self.m_checkBox13.GetValue(),
            #               str(self.m_filePicker3.GetPath()))
        except Exception:
            from atmisc import atlogger
            atlogger.capture_error()
            wx.MessageBox("Please verify IP selection.", 'Error', wx.OK | wx.ICON_ERROR)
            return 0

        # Connecting to SUT with Conplyent, and launching Prime95.exe.
        connection = conplyent.client.add(str(self.m_textCtrl11.GetValue()), 9922)
        try:
            connection.connect(timeout=5)
            print(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches\Launch"
                  + str(coreSelect) + ".bat")
            connection.exec(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches\Launch"
                            + str(coreSelect) + ".bat", complete=False)
            time.sleep(2)
        except ConnectionError:
            sutActiveFail(sutIP, ipSelection, fuseSelection, filePath, comPort)

        # Register path can be found in HDT: Container Tree -> PPR Container
        # Setting Up to Read MP1.
        for mp1 in atmcentral.atm.dies():
            mp1.setup_register("MP1_LX3_PDEBUGPC", "PPR::MP::MP1CRU::socket{}::{}::MP1MP1::MP1_LX3_PDEBUGPC", iod=True)

        # Setting Up to Read Temperature.
        for thm in atmcentral.atm.dies():
            thm.setup_register("THM_DIE1_TEMP", "PPR::SMU::THM::socket{}::{}::THM_DIE1_TEMP", iod=True)
            self.m_statusBar1.SetStatusText("Successfully connected to Wombat and system.")
        # Reading highest temperature of cores (Active core will be the highest due to affinity being set to it).
        thm["THM_DIE1_TEMP"].read()
        thmCore0Ave = (thm["THM_DIE1_TEMP"]["TEMP"]) / 8 - 49
        # Reading THM_TMON0_RDIL6_DATA::TEMP register.
        # for thm in atmcentral.atm.dies():
        #     thm.setup_register("THM_TMON0_RDIL6_DATA",
        #                        "PPR::SMU::THM::socket{}::{}::THM_TMON0_RDIL6_DATA", iod=True)
        #     # Register path can be found in HDT: Container Tree -> PPR Container
        #     thm["THM_TMON0_RDIL6_DATA"].read()
        #     thmCore0 = (thm["THM_TMON0_RDIL6_DATA"]["TEMP"])/8-49
        #     print(thmCore0)
        # Reading THM_DIE1_TEMP register.

        self.m_statusBar1.SetStatusText("Maintaining temperature, and beginning test.")

        # Setting voltage and frequency using PAPI.
        voltFreqChange(ipSelection, coreSelect, cpuVDD, coreSelectFreq)

        # Test-Loop.
        while True:
            startTime = datetime.datetime.now()
            print("Loop start: " + str(startTime))
            for i in range(0, 3001):
                mp1Val = mp1["MP1_LX3_PDEBUGPC"].read()
                thm["THM_DIE1_TEMP"].read()
                thmCore0 = round(((thm["THM_DIE1_TEMP"]["TEMP"]) / 8 - 49), 1)
                thmCore0Ave = round((thmCore0 + thmCore0Ave) / 2)

                # Temperature control on the average of 150 temperature readings.
                if i % 150 == 0:
                    print(str(thmCore0Ave) + "°C")
                    if (systemHoldTemp - 2) > thmCore0Ave:
                        if thmCore0Ave - thmCore0 > 4:
                            continue
                        print("Too Cold.")
                        tempAdjustment = (systemHoldTemp - 2) - thmCore0Ave
                        chillerHoldTemp = chillerHoldTemp + tempAdjustment
                        print((datetime.datetime.now().strftime('%H:%M')) + " - chiller " + comPort + "-t " +
                              str(chillerHoldTemp))
                        subprocess.call(['cmd', '/c', "chiller " + comPort + "-t " + str(chillerHoldTemp)], shell=True)
                    if (systemHoldTemp + 2) < thmCore0Ave:
                        print("Too Hot.")
                        tempAdjustment = thmCore0Ave - (systemHoldTemp + 2)
                        chillerHoldTemp = chillerHoldTemp - tempAdjustment
                        print((datetime.datetime.now().strftime('%H:%M')) + " - chiller " + comPort + "-t " +
                              str(chillerHoldTemp))
                        subprocess.call(['cmd', '/c', "chiller " + comPort + "-t " + str(chillerHoldTemp)], shell=True)

                # Reading SUT's Core0 (Thread0 and Thread1) Active-Percentage.
                try:
                    thread0 = float(connection.core_percentage(timeout=5, max_interval=5)[coreArrayValue0])
                except conplyent.ClientTimeout:
                    print("Timed out while running thread0 check...")
                    writeTest(coreSelect, cpuVDD, outputName, coreSelectFreq)
                    sutActiveFail(sutIP, ipSelection, fuseSelection, filePath, comPort)
                    cpuVDD -= 8
                    coreSelectFreq -= 150
                    if endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName) is True:
                        return 0
                    elif endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName) is False:
                        coreSelect += 1
                        coreArrayValue0 += 2
                        coreArrayValue1 += 2
                        cpuVDD = 104
                        coreSelectFreq = 3600
                    connection.connect(timeout=5)
                    voltFreqChange(ipSelection, coreSelect, cpuVDD, coreSelectFreq)
                    print(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches"
                          r"\Launch" + str(coreSelect) + ".bat")
                    connection.exec(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches"
                                    r"\Launch" + str(coreSelect) + ".bat",
                                    complete=False)

                try:
                    thread1 = float(connection.core_percentage(timeout=5, max_interval=5)[coreArrayValue1])
                except conplyent.ClientTimeout:
                    print("Timed out while running thread1 check...")
                    writeTest(coreSelect, cpuVDD, outputName, coreSelectFreq)
                    sutActiveFail(sutIP, ipSelection, fuseSelection, filePath, comPort)
                    cpuVDD -= 8
                    coreSelectFreq -= 150
                    if endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName) is True:
                        return 0
                    elif endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName) is False:
                        coreSelect += 1
                        coreArrayValue0 += 2
                        coreArrayValue1 += 2
                        cpuVDD = 104
                        coreSelectFreq = 3600
                    connection.connect(timeout=5)
                    voltFreqChange(ipSelection, coreSelect, cpuVDD, coreSelectFreq)
                    print(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches"
                          r"\Launch" + str(coreSelect) + ".bat")
                    connection.exec(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches"
                                    r"\Launch" + str(coreSelect) + ".bat",
                                    complete=False)

                # Watching for Prime95 Failure/Stop, using SUT's Thread0 and Thread1 Utilization.
                if thread0 < 90.0 and thread1 < 90.0:
                    primeFail = 0
                    for failCheck in range(1, 11):
                        try:
                            thread0 = float(connection.core_percentage(timeout=5, max_interval=5)[coreArrayValue0])
                        except conplyent.ClientTimeout:
                            break
                        try:
                            thread1 = float(connection.core_percentage(timeout=5, max_interval=5)[coreArrayValue1])
                        except conplyent.ClientTimeout:
                            break
                        if thread0 < 100.0 and thread1 < 100.0:
                            primeFail += 1
                            if primeFail > 7:
                                print("Prime95 has stopped.")
                                writeTest(coreSelect, cpuVDD, outputName, coreSelectFreq)
                                cpuVDD -= 8
                                coreSelectFreq -= 150
                                if endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName) is True:
                                    return 0
                                elif endOfTest(coreSelect, cpuVDD, ipSelection, comPort, coreEnd, outputName) is False:
                                    coreSelect += 1
                                    coreArrayValue0 += 2
                                    coreArrayValue1 += 2
                                    cpuVDD = 104
                                    coreSelectFreq = 3600
                                voltFreqChange(ipSelection, coreSelect, cpuVDD, coreSelectFreq)
                                print(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95\TestSuiteBatches"
                                      r"\Launch" + str(coreSelect) + ".bat")
                                connection.exec(r"C:\Platform Silicon Testsuite\Voltage vs Frequency\Prime95"
                                                r"\TestSuiteBatches\Launch" + str(coreSelect) + ".bat",
                                                complete=False)
                                break

                # Checking if Test-Loop has Run for 60 Seconds, and Increasing Frequency if Needed.
                endTime = datetime.datetime.now()
                timeDuration = endTime - startTime
                timeDuration = timeDuration.total_seconds()
                if timeDuration > 60:
                    print("Elapsed Time with Current Setpoints: " + str(timeDuration) + " seconds")
                    coreSelectFreq += 25
                    print("Increasing frequency to: " + str(coreSelectFreq))
                    voltFreqChange(ipSelection, coreSelect, cpuVDD, coreSelectFreq)
                    break


# Run the program
app = wx.App(False)
frame = Main(None)
frame.Show(True)
# start the applications
app.MainLoop()
