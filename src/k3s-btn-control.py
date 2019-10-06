#!/usr/bin/python3

import signal
import buttonshim
import os
import subprocess

print("""
Control the k3s-arm-demo
Press Ctrl+C to exit.
""")

scale=1
def upScale():
    global scale
    scale=scale+1
    return scale

def downScale():
    global scale
    scale=scale-1
    return scale

buttonA_was_held = False
deployDSPin4 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/blue-ds.yaml"]
undeployDSPin4 =["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/blue-ds.yaml"]

buttonB_was_held = False
deployPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/white-pod.yaml"]
undeployPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/white-pod.yaml"]

buttonC_was_held = False
scaleUpPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "scale", "--replicas=" + str(upScale()), "deployment/white-pod", "-n", "k3s-arm-demo"]
scaleDownPodPin5 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "scale", "--replicas=" + str(downScale()), "deployment/white-pod", "-n", "k3s-arm-demo"]

buttonD_was_held = False

buttonE_was_held = False


# Button A
@buttonshim.on_press(buttonshim.BUTTON_A)
def button_A_press(button, pressed):
    global buttonA_was_held
    buttonshim.set_pixel(0x94, 0x00, 0xd3)
    buttonA_was_held = False
    print("on_press A", buttonA_was_held)

@buttonshim.on_release(buttonshim.BUTTON_A)
def button_A_release(button, pressed):
    global buttonA_was_held
    print("on_release A", buttonA_was_held)
    if not buttonA_was_held:
        subprocess.check_call(deployDSPin4)

@buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
def button_A_hold(button):
    global buttonA_was_held
    print("begin on_hold A", buttonA_was_held)
    buttonA_was_held = True
    subprocess.check_call(undeployDSPin4)
    print("end on_hold A", buttonA_was_held)

# Button B
@buttonshim.on_press(buttonshim.BUTTON_B)
def button_B_press(button, pressed):
    global buttonB_was_held
    buttonshim.set_pixel(0x00, 0x00, 0xff)
    buttonB_was_held = False
    print("on_press B", buttonB_was_held)

@buttonshim.on_release(buttonshim.BUTTON_B)
def button_B_release(button, pressed):
    global buttonB_was_held
    print("on_release B", buttonB_was_held)
    if not buttonB_was_held:
        subprocess.check_call(deployPodPin5)

@buttonshim.on_hold(buttonshim.BUTTON_B, hold_time=2)
def button_B_hold(button):
    global buttonB_was_held
    print("begin on_hold B", buttonB_was_held)
    buttonB_was_held = True
    subprocess.check_call(undeployPodPin5)
    print("end on_hold B", buttonB_was_held)

# Button C
@buttonshim.on_press(buttonshim.BUTTON_C)
def button_C_press(button, pressed):
    global buttonC_was_held
    buttonshim.set_pixel(0x00, 0xff, 0x00)
    buttonC_was_held = False
    print("on_press C", buttonC_was_held)

@buttonshim.on_release(buttonshim.BUTTON_C)
def button_C_release(button, pressed):
    global buttonC_was_held
    print("on_release C", buttonC_was_held)
    if not buttonC_was_held:
        subprocess.check_call(scaleUpPodPin5)

@buttonshim.on_hold(buttonshim.BUTTON_C, hold_time=2)
def button_C_hold(button):
    global buttonC_was_held
    print("begin on_hold C", buttonC_was_held)
    buttonC_was_held = True
    subprocess.check_call(scaleDownPodPin5)
    print("end on_hold C", buttonC_was_held)

# Button D
@buttonshim.on_press(buttonshim.BUTTON_D)
def button_D_press(button, pressed):
    global buttonD_was_held
    buttonshim.set_pixel(0xff, 0xff, 0x00)
    buttonD_was_held = False
    print("on_press D", buttonD_was_held)

@buttonshim.on_release(buttonshim.BUTTON_D)
def button_D_release(button, pressed):
    global buttonD_was_held
    print("on_release D", buttonD_was_held)
    if not buttonD_was_held:
        subprocess.check_call(deployDSPin4)

@buttonshim.on_hold(buttonshim.BUTTON_D, hold_time=2)
def button_D_hold(button):
    global buttonD_was_held
    print("begin on_hold D", buttonD_was_held)
    buttonD_was_held = True
    subprocess.check_call(undeployDSPin4)
    print("end on_hold D", buttonD_was_held)

# Button E
@buttonshim.on_press(buttonshim.BUTTON_E)
def button_E_press(button, pressed):
    global buttonE_was_held
    buttonshim.set_pixel(0xff, 0x00, 0x00)
    buttonE_was_held = False
    print("on_press E", buttonE_was_held)

@buttonshim.on_release(buttonshim.BUTTON_E)
def button_E_release(button, pressed):
    global buttonE_was_held
    print("on_release E", buttonE_was_held)
    if not buttonE_was_held:
        subprocess.check_call(deployDSPin4)

@buttonshim.on_hold(buttonshim.BUTTON_E, hold_time=2)
def button_E_hold(button):
    global buttonE_was_held
    print("begin on_hold E", buttonE_was_held)
    buttonE_was_held = True
    subprocess.check_call(undeployDSPin4)
    print("end on_hold E", buttonE_was_held)






signal.pause()