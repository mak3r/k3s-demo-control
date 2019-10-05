#!/usr/bin/python3

import signal
import buttonshim
import os

print("""
Control the k3s-arm-demo
Press Ctrl+C to exit.
""")

deployDSPin4 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml apply -f /home/pi/workloads/blue-ds.yaml'
undeployDSPin4 = 'kubectl --kubeconfig=/home/pi/kubeconfig.yaml delete -f /home/pi/workloads/blue-ds.yaml'

@buttonshim.on_release(buttonshim.BUTTON_A)
def button_a(button, pressed):
    os.system(deployDSPin4)

@buttonshim.on_hold(buttonshim.BUTTON_A)
def button_a(button, pressed):
    os.system(undeployDSPin4)


@buttonshim.on_press(buttonshim.BUTTON_A)
def button_a(button, pressed):
    buttonshim.set_pixel(0x94, 0x00, 0xd3)


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