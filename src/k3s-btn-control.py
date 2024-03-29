#!/usr/bin/python3

import signal
import buttonshim
import os
import subprocess
import threading
import time

print("""
Control the k3s-arm-demo
Press Ctrl+C to exit.
""")

##############
# Button A
##############
buttonA_was_held = False
deployDSPin4 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/blue-ds.yaml"]
undeployDSPin4 =["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/blue-ds.yaml"]

@buttonshim.on_press(buttonshim.BUTTON_A)
def button_A_press(button, pressed):
    global buttonA_was_held
    buttonshim.set_pixel(0x94, 0x00, 0xd3)
    buttonA_was_held = False

@buttonshim.on_release(buttonshim.BUTTON_A)
def button_A_release(button, pressed):
    global buttonA_was_held
    if not buttonA_was_held:
        subprocess.check_call(deployDSPin4)
        print(deployDSPin4)

@buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
def button_A_hold(button):
    global buttonA_was_held
    buttonA_was_held = True
    subprocess.check_call(undeployDSPin4)
    print(undeployDSPin4)

##############
# Button B
##############
buttonB_was_held = False
deployPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/white-pod.yaml"]
undeployPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/white-pod.yaml"]

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_B_press(button, pressed):
    global buttonB_was_held
    buttonshim.set_pixel(0x00, 0x00, 0xff)
    buttonB_was_held = False

@buttonshim.on_release(buttonshim.BUTTON_B)
def button_B_release(button, pressed):
    global buttonB_was_held
    if not buttonB_was_held:
        subprocess.check_call(deployPodPin5)
        print(deployPodPin5)

@buttonshim.on_hold(buttonshim.BUTTON_B, hold_time=2)
def button_B_hold(button):
    global scale
    global buttonB_was_held
    buttonB_was_held = True
    subprocess.check_call(undeployPodPin5)
    scale = 1
    print(undeployPodPin5)

##############
# Button C
##############
buttonC_was_held = False
scale=1
def upScale():
    global scale
    scale=scale+1
    return scale

def downScale():
    global scale
    scale=scale-1
    return scale

@buttonshim.on_press(buttonshim.BUTTON_C)
def button_C_press(button, pressed):
    global buttonC_was_held
    buttonshim.set_pixel(0x00, 0xff, 0x00)
    buttonC_was_held = False

@buttonshim.on_release(buttonshim.BUTTON_C)
def button_C_release(button, pressed):
    global buttonC_was_held
    if not buttonC_was_held:
        scaleUpPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "scale", "--replicas=" + str(upScale()), "deployment/white-pod", "-n", "k3s-arm-demo"]
        subprocess.check_call(scaleUpPodPin5)
        print(scaleUpPodPin5)

@buttonshim.on_hold(buttonshim.BUTTON_C, hold_time=2)
def button_C_hold(button):
    global buttonC_was_held
    buttonC_was_held = True
    scaleDownPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "scale", "--replicas=" + str(downScale()), "deployment/white-pod", "-n", "k3s-arm-demo"]
    subprocess.check_call(scaleDownPodPin5)
    print(scaleDownPodPin5)

##############
# Button D
##############
buttonD_was_held = False
deployAudioJobMaster = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/audio-job.yaml"]
undeployAudioJobMaster = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/audio-job.yaml"]

@buttonshim.on_press(buttonshim.BUTTON_D)
def button_D_press(button, pressed):
    global buttonD_was_held
    buttonshim.set_pixel(0xff, 0xff, 0x00)
    buttonD_was_held = False

@buttonshim.on_release(buttonshim.BUTTON_D)
def button_D_release(button, pressed):
    global buttonD_was_held
    if not buttonD_was_held:
        subprocess.check_call(deployAudioJobMaster)
        print(deployAudioJobMaster)

@buttonshim.on_hold(buttonshim.BUTTON_D, hold_time=2)
def button_D_hold(button):
    global buttonD_was_held
    buttonD_was_held = True
    subprocess.check_call(undeployAudioJobMaster)
    print(undeployAudioJobMaster)

##############
# Button E
##############

buttonE_was_held = False
# Currently not deploying or undeploying the powerpod
#deployPowerPod = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/power-pod.yaml"]
#undeployPowerPod = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "deployment", "power-pod", "-n", "k3s-arm-demo"]

E_scale=1
def E_upScale():
    global E_scale
    E_scale=E_scale+1
    return E_scale

def E_downScale():
    global E_scale
    E_scale=E_scale-1
    return E_scale

deployFindWorker1 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/find-worker1.yaml"]
deployFindWorker2 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/find-worker2.yaml"]
undeployFindWorker1 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/find-worker1.yaml"]
undeployFindWorker2 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/find-worker2.yaml"]


# delete the tc-enable-activated file process
deployResetDS = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/reset-tc.yaml"]
undeployResetDS = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/reset-tc.yaml"]
undeployScout = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/scout.yaml"]

def E_single_press():
    print ("E_single_press")
    subprocess.check_call(deployFindWorker1)
    subprocess.check_call(deployFindWorker2)

# Setup a timer to run when the button is pressed the first time
# cancel the timer it it's pressed within the alloted time
E_timer = None
# track how many times E is pressed 
E_count = 0

@buttonshim.on_press(buttonshim.BUTTON_E)
def button_E_press(button, pressed):
    global buttonE_was_held
    global E_count
    buttonshim.set_pixel(0xff, 0x00, 0x00)
    buttonE_was_held = False
    E_count = E_count + 1
    if E_count > 2:
        E_count = 0
    print ("E_press E_count=", E_count)

@buttonshim.on_release(buttonshim.BUTTON_E)
def button_E_release(button, pressed):
    global buttonE_was_held
    global E_count
    global E_timer
    print("button released")
    if not buttonE_was_held:
        if E_count == 1:
            print("starting timer E_count is 1")
            E_timer = None
            E_timer = threading.Timer(1.0, E_single_press)
            E_timer.start()
        if E_count == 2:
            print("cancelling timer E_count is 2")
            E_timer.cancel()
            subprocess.check_call(undeployFindWorker1)
            subprocess.check_call(undeployFindWorker2)
            print("reset E_count to 0")
            E_count = 0


@buttonshim.on_hold(buttonshim.BUTTON_E, hold_time=2)
def button_E_hold(button):
    global buttonE_was_held
    global E_count
    buttonE_was_held = True
    print("E_count is:", E_count)
    E_count = 0

    l_scale = str(E_upScale())
    scaleFindWorker1 = ["kubectl", "scale", "--kubeconfig=/home/pi/kubeconfig.yaml", "--replicas=" + l_scale, "-f", "/home/pi/workloads/find-worker1.yaml"]
    scaleFindWorker2 = ["kubectl", "scale", "--kubeconfig=/home/pi/kubeconfig.yaml", "--replicas=" + l_scale, "-f", "/home/pi/workloads/find-worker2.yaml"]

    subprocess.check_call(scaleFindWorker1)
    subprocess.check_call(scaleFindWorker2)


signal.pause()