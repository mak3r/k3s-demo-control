#!/usr/bin/python3

import signal
import buttonshim
import os
import subprocess

print("""
Control the k3s-arm-demo
Press Ctrl+C to exit.
""")

buttonA_was_held = False
deployDSPin4 = ["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "apply", "-f", "/home/pi/workloads/blue-ds.yaml"]
undeployDSPin4 =["kubectl", "--kubeconfig=/home/pi/kubeconfig.yaml", "delete", "-f", "/home/pi/workloads/blue-ds.yaml"]


@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a_press(button, pressed):
    global buttonA_was_held
    buttonshim.set_pixel(0x94, 0x00, 0xd3)
    buttonA_was_held = False
    print("on_press A", buttonA_was_held)

@buttonshim.on_release(buttonshim.BUTTON_A)
def button_a_release(button, pressed):
    if not buttonA_was_held:
        subprocess.check_call(deployDSPin4)
    print("on_release A", buttonA_was_held)

@buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
def button_a_hold(button):
    global buttonA_was_held
    subprocess.check_call(undeployDSPin4)
    buttonA_was_held = True
    print("on_hold A", buttonA_was_held)

buttonBHold = False
deployPodPin5 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml apply -f /home/pi/workloads/white-pod.yaml'
undeployPodPin5 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml delete -f /home/pi/workloads/white-pod.yaml'
scaleUpPodPin5 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml scale --replicas=3 pod/white-pod'

@buttonshim.on_release(buttonshim.BUTTON_B)
def button_b_release(button, released):
    global buttonBHold
    if buttonBHold == False:
        os.system(deployPodPin5)
    buttonBHold = False

@buttonshim.on_hold(buttonshim.BUTTON_B)
def button_b_hold(button):
    global buttonBHold
    os.system(undeployPodPin5)
    buttonBHold = True


buttonCHold = False
deployPodPin5 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml apply -f /home/pi/workloads/white-pod.yaml'
undeployPodPin5 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml delete -f /home/pi/workloads/white-pod.yaml'
scaleUpPodPin5 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml scale --replicas=3 pod/white-pod'

@buttonshim.on_release(buttonshim.BUTTON_C)
def button_c_release(button, released):
    global buttonCHold
    if buttonCHold == False:
        os.system(scaleUpPodPin5)
    buttonCHold = False

@buttonshim.on_hold(buttonshim.BUTTON_C)
def button_c_hold(button):
    global buttonCHold
    os.system(undeployPodPin5)
    buttonCHold = True


# On press default pimoroni actions

@buttonshim.on_press(buttonshim.BUTTON_B)
def button_b(button, pressed):
    buttonshim.set_pixel(0x00, 0x00, 0xff)


@buttonshim.on_press(buttonshim.BUTTON_C)
def button_c(button, pressed):
    buttonshim.set_pixel(0x00, 0xff, 0x00)


@buttonshim.on_press(buttonshim.BUTTON_D)
def button_d(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)


@buttonshim.on_press(buttonshim.BUTTON_E)
def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)


signal.pause()