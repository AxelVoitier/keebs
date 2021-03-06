EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Lergo modular PCB"
Date "2021-11-15"
Rev "v1.A"
Comp "Axel Voitier"
Comment1 "SPDX-License-Identifier: CERN-OHL-W-2.0"
Comment2 "Derived from SU120 of @e3w2q, under MIT license"
Comment3 "Also reuse some symbols from Sofle (Choc v2 RGB variant), under MIT license"
Comment4 ""
$EndDescr
$Comp
L Sofle:SW_PUSH_LED SW9
U 1 1 5C43B29E
P 8350 1700
F 0 "SW9" H 8350 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 1894 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 8350 1900 50  0001 C CNN
F 3 "" H 8350 1900 50  0001 C CNN
	1    8350 1700
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW13
U 1 1 5C43B2EA
P 9400 1700
F 0 "SW13" H 9400 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 1894 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 9400 1900 50  0001 C CNN
F 3 "" H 9400 1900 50  0001 C CNN
	1    9400 1700
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW2
U 1 1 5C43B33A
P 6200 2300
F 0 "SW2" H 6200 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 2494 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 6200 2500 50  0001 C CNN
F 3 "" H 6200 2500 50  0001 C CNN
	1    6200 2300
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW6
U 1 1 5C43B3A2
P 7250 2300
F 0 "SW6" H 7250 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 2494 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 7250 2500 50  0001 C CNN
F 3 "" H 7250 2500 50  0001 C CNN
	1    7250 2300
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW10
U 1 1 5C43B3F4
P 8350 2300
F 0 "SW10" H 8350 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 2494 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 8350 2500 50  0001 C CNN
F 3 "" H 8350 2500 50  0001 C CNN
	1    8350 2300
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW14
U 1 1 5C43B44C
P 9400 2300
F 0 "SW14" H 9400 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 2494 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 9400 2500 50  0001 C CNN
F 3 "" H 9400 2500 50  0001 C CNN
	1    9400 2300
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW17
U 1 1 5C485058
P 10450 1700
F 0 "SW17" H 10450 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 10450 1894 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 10450 1900 50  0001 C CNN
F 3 "" H 10450 1900 50  0001 C CNN
	1    10450 1700
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW4
U 1 1 5C485061
P 6200 3500
F 0 "SW4" H 6200 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 3694 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 6200 3700 50  0001 C CNN
F 3 "" H 6200 3700 50  0001 C CNN
	1    6200 3500
	1    0    0    -1  
$EndComp
Text GLabel 5600 2000 0    39   Input ~ 0
Y1
Text GLabel 5600 2600 0    39   Input ~ 0
Y2
$Comp
L Sofle:SW_PUSH_LED SW16
U 1 1 5C71DC44
P 9400 3500
F 0 "SW16" H 9400 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 3694 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 9400 3700 50  0001 C CNN
F 3 "" H 9400 3700 50  0001 C CNN
	1    9400 3500
	1    0    0    -1  
$EndComp
Text GLabel 5600 3800 0    39   Input ~ 0
Y4
$Comp
L #library:MJ-4PP-9 J1
U 1 1 5CE190C3
P 1050 4300
F 0 "J1" H 1080 4718 50  0000 C CNN
F 1 "MJ-4PP-9" H 1080 4627 50  0000 C CNN
F 2 "Lergo Footprints:MJ-4PP-9" H 1325 4475 50  0001 C CNN
F 3 "" H 1325 4475 50  0001 C CNN
	1    1050 4300
	1    0    0    -1  
$EndComp
Text GLabel 1800 750  1    50   Input ~ 0
led_
Text GLabel 3450 2000 2    50   Input ~ 0
Y1
Text GLabel 3450 2100 2    50   Input ~ 0
Y2
Text GLabel 3450 2200 2    50   Input ~ 0
Y3
Text GLabel 3450 2300 2    50   Input ~ 0
Y4
Text GLabel 3450 2500 2    50   Input ~ 0
Y6
Text GLabel 3450 2400 2    50   Input ~ 0
Y5
Text GLabel 1550 2950 0    50   Input ~ 0
X1
Text GLabel 1550 3050 0    50   Input ~ 0
X2
Text GLabel 1550 3150 0    50   Input ~ 0
X3
Text GLabel 1550 3250 0    50   Input ~ 0
X4
Text GLabel 1550 3350 0    50   Input ~ 0
X5
Text GLabel 1550 3450 0    50   Input ~ 0
X6
Text GLabel 1550 3550 0    50   Input ~ 0
X7
Text GLabel 1550 3650 0    50   Input ~ 0
X8
Text GLabel 4100 2950 2    50   Input ~ 0
X9
Text GLabel 4100 3050 2    50   Input ~ 0
X10
Text GLabel 4100 3150 2    50   Input ~ 0
Y1
Text GLabel 4100 3250 2    50   Input ~ 0
Y2
Text GLabel 4100 3350 2    50   Input ~ 0
Y3
Text GLabel 4100 3450 2    50   Input ~ 0
Y4
Text GLabel 4100 3650 2    50   Input ~ 0
Y6
Text GLabel 4100 3550 2    50   Input ~ 0
Y5
$Comp
L power:GND #PWR0101
U 1 1 5CE3BEE4
P 4750 4300
F 0 "#PWR0101" H 4750 4050 50  0001 C CNN
F 1 "GND" H 4750 4150 50  0000 C CNN
F 2 "" H 4750 4300 50  0001 C CNN
F 3 "" H 4750 4300 50  0001 C CNN
	1    4750 4300
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 5CE3BEEA
P 4750 4150
F 0 "#FLG0101" H 4750 4225 50  0001 C CNN
F 1 "PWR_FLAG" H 4750 4300 50  0000 C CNN
F 2 "" H 4750 4150 50  0001 C CNN
F 3 "" H 4750 4150 50  0001 C CNN
	1    4750 4150
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG0102
U 1 1 5CE3BEF0
P 4150 4300
F 0 "#FLG0102" H 4150 4375 50  0001 C CNN
F 1 "PWR_FLAG" H 4150 4450 50  0000 C CNN
F 2 "" H 4150 4300 50  0001 C CNN
F 3 "" H 4150 4300 50  0001 C CNN
	1    4150 4300
	-1   0    0    1   
$EndComp
Wire Wire Line
	4750 4150 4750 4200
Wire Wire Line
	4150 4150 4150 4250
$Comp
L power:VCC #PWR0102
U 1 1 5CE3E880
P 4150 4150
F 0 "#PWR0102" H 4150 4000 50  0001 C CNN
F 1 "VCC" H 4167 4323 50  0000 C CNN
F 2 "" H 4150 4150 50  0001 C CNN
F 3 "" H 4150 4150 50  0001 C CNN
	1    4150 4150
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW22
U 1 1 5CE3F474
P 5300 4850
F 0 "SW22" H 5300 5135 50  0000 C CNN
F 1 "SW_Push" H 5300 5044 50  0000 C CNN
F 2 "Lergo Footprints:ResetSW" H 5300 5050 50  0001 C CNN
F 3 "" H 5300 5050 50  0001 C CNN
	1    5300 4850
	1    0    0    -1  
$EndComp
Text GLabel 5100 4850 0    50   Input ~ 0
reset1
$Comp
L Connector_Generic:Conn_01x03 J2
U 1 1 5CE3FF01
P 3200 4250
F 0 "J2" H 3280 4292 50  0000 L CNN
F 1 "Conn_01x03" H 3280 4201 50  0000 L CNN
F 2 "Lergo Footprints:PinHeader_1x03_P2.54mm_Vertical" H 3200 4250 50  0001 C CNN
F 3 "~" H 3200 4250 50  0001 C CNN
	1    3200 4250
	-1   0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0107
U 1 1 5CE5249C
P 3600 4000
F 0 "#PWR0107" H 3600 3850 50  0001 C CNN
F 1 "VCC" H 3617 4173 50  0000 C CNN
F 2 "" H 3600 4000 50  0001 C CNN
F 3 "" H 3600 4000 50  0001 C CNN
	1    3600 4000
	-1   0    0    -1  
$EndComp
Text GLabel 2900 3550 2    50   Input ~ 0
led
Text GLabel 1250 4400 2    50   Input ~ 0
data
$Comp
L power:GND #PWR0109
U 1 1 5CE6AB53
P 1550 4450
F 0 "#PWR0109" H 1550 4200 50  0001 C CNN
F 1 "GND" H 1550 4300 50  0000 C CNN
F 2 "" H 1550 4450 50  0001 C CNN
F 3 "" H 1550 4450 50  0001 C CNN
	1    1550 4450
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0110
U 1 1 5CE6AC90
P 1550 4050
F 0 "#PWR0110" H 1550 3900 50  0001 C CNN
F 1 "VCC" H 1567 4223 50  0000 C CNN
F 2 "" H 1550 4050 50  0001 C CNN
F 3 "" H 1550 4050 50  0001 C CNN
	1    1550 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1250 4300 1550 4300
Wire Wire Line
	1550 4300 1550 4450
Wire Wire Line
	1250 4200 1550 4200
Wire Wire Line
	1550 4200 1550 4050
NoConn ~ 1250 4100
$Comp
L Sofle:SW_PUSH_LED SW7
U 1 1 5CE4CCDE
P 7250 2900
F 0 "SW7" H 7250 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 3094 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 7250 3100 50  0001 C CNN
F 3 "" H 7250 3100 50  0001 C CNN
	1    7250 2900
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW11
U 1 1 5CE4CCE4
P 8350 2900
F 0 "SW11" H 8350 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 3094 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 8350 3100 50  0001 C CNN
F 3 "" H 8350 3100 50  0001 C CNN
	1    8350 2900
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW15
U 1 1 5CE4CCEA
P 9400 2900
F 0 "SW15" H 9400 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 3094 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 9400 3100 50  0001 C CNN
F 3 "" H 9400 3100 50  0001 C CNN
	1    9400 2900
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW8
U 1 1 5CE4CCF6
P 7250 3500
F 0 "SW8" H 7250 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 3694 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 7250 3700 50  0001 C CNN
F 3 "" H 7250 3700 50  0001 C CNN
	1    7250 3500
	1    0    0    -1  
$EndComp
Text GLabel 5600 3200 0    39   Input ~ 0
Y3
$Comp
L Device:D D18
U 1 1 5CE5B200
P 9600 5350
F 0 "D18" H 9600 5450 50  0000 C CNN
F 1 "D" H 9600 5250 50  0001 C CNN
F 2 "Lergo Footprints:diode_TH_SMD_rev3" H 9600 5350 50  0001 C CNN
F 3 "" H 9600 5350 50  0001 C CNN
	1    9600 5350
	0    -1   -1   0   
$EndComp
Text GLabel 5600 5500 0    39   Input ~ 0
Y6
Text GLabel 6000 800  1    39   Input ~ 0
X1
Text GLabel 7050 800  1    39   Input ~ 0
X2
Text GLabel 8150 800  1    39   Input ~ 0
X3
$Comp
L Connector:TestPoint H138
U 1 1 5CE5B2AA
P 9800 5500
F 0 "H138" H 9700 5700 50  0000 L CNN
F 1 "MountingHole_Pad" H 9900 5460 50  0001 L CNN
F 2 "Lergo Footprints:1pin_rect_conn" H 9800 5500 50  0001 C CNN
F 3 "~" H 9800 5500 50  0001 C CNN
	1    9800 5500
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H135
U 1 1 5CE5B2BF
P 9200 5050
F 0 "H135" V 9200 5350 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 5055 50  0001 C CNN
F 2 "Lergo Footprints:1pin_rect_conn" H 9200 5050 50  0001 C CNN
F 3 "~" H 9200 5050 50  0001 C CNN
	1    9200 5050
	0    -1   -1   0   
$EndComp
Connection ~ 9200 5050
Wire Wire Line
	9600 5500 9800 5500
$Comp
L power:GND #PWR0106
U 1 1 5CE5189D
P 3600 4400
F 0 "#PWR0106" H 3600 4150 50  0001 C CNN
F 1 "GND" H 3600 4250 50  0000 C CNN
F 2 "" H 3600 4400 50  0001 C CNN
F 3 "" H 3600 4400 50  0001 C CNN
	1    3600 4400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3600 4400 3600 4350
Wire Wire Line
	3600 4350 3400 4350
Wire Wire Line
	3400 4150 3600 4150
Wire Wire Line
	3600 4150 3600 4000
$Comp
L Connector_Generic:Conn_01x08 J3
U 1 1 5CE5F218
P 3900 3250
F 0 "J3" H 3980 3242 50  0000 L CNN
F 1 "Conn_01x08" H 3980 3151 50  0000 L CNN
F 2 "Lergo Footprints:PinHeader_1x08_P2.54mm_Vertical_rev2" H 3900 3250 50  0001 C CNN
F 3 "~" H 3900 3250 50  0001 C CNN
	1    3900 3250
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J4
U 1 1 5CE5F3DE
P 1750 3250
F 0 "J4" H 1670 3767 50  0000 C CNN
F 1 "Conn_01x08" H 1670 3676 50  0000 C CNN
F 2 "Lergo Footprints:PinHeader_1x08_P2.54mm_Vertical_rev2" H 1750 3250 50  0001 C CNN
F 3 "~" H 1750 3250 50  0001 C CNN
	1    1750 3250
	1    0    0    -1  
$EndComp
$Comp
L #library:MJ-4PP-9 J6
U 1 1 5CF7DFCF
P 2050 4300
F 0 "J6" H 2080 4718 50  0000 C CNN
F 1 "MJ-4PP-9" H 2080 4627 50  0000 C CNN
F 2 "Lergo Footprints:MJ-4PP-9" H 2325 4475 50  0001 C CNN
F 3 "" H 2325 4475 50  0001 C CNN
	1    2050 4300
	1    0    0    -1  
$EndComp
NoConn ~ 2250 4100
$Comp
L Sofle:SW_PUSH_LED SW12
U 1 1 5D04CD1C
P 8350 3500
F 0 "SW12" H 8350 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 3694 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 8350 3700 50  0001 C CNN
F 3 "" H 8350 3700 50  0001 C CNN
	1    8350 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	9200 4800 9200 5050
Wire Wire Line
	9200 5050 9200 5200
$Comp
L Device:Rotary_Encoder_Switch SW20
U 1 1 5D6595AB
P 9500 4900
F 0 "SW20" V 9454 4670 50  0000 R CNN
F 1 "Rotary_Encoder_Switch" V 9545 4670 50  0001 R CNN
F 2 "Lergo Footprints:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_rev2" H 9350 5060 50  0001 C CNN
F 3 "~" H 9500 5160 50  0001 C CNN
	1    9500 4900
	0    -1   1    0   
$EndComp
Wire Wire Line
	9400 5200 9200 5200
Connection ~ 9200 5200
Text GLabel 9500 4150 1    50   Input ~ 0
GND
Text GLabel 9200 800  1    39   Input ~ 0
X4
Text GLabel 10250 800  1    39   Input ~ 0
X5
Text GLabel 9650 4350 2    50   Input ~ 0
X7
Text GLabel 9400 4100 1    50   Input ~ 0
X8
$Comp
L Mechanical:MountingHole_Pad H57
U 1 1 5E0F561B
P 900 2150
F 0 "H57" H 900 2350 50  0000 C CNN
F 1 "MountingHole_Pad" V 1046 2155 50  0001 C CNN
F 2 "Lergo Footprints:1pin_conn" H 900 2150 50  0001 C CNN
F 3 "~" H 900 2150 50  0001 C CNN
	1    900  2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9500 4150 9500 4250
Wire Wire Line
	9600 4350 9600 4450
Wire Wire Line
	9300 4450 9500 4450
Connection ~ 9500 4450
Wire Wire Line
	9500 4450 9500 4600
Wire Wire Line
	4150 4250 4300 4250
Connection ~ 4150 4250
Wire Wire Line
	4150 4250 4150 4300
$Comp
L Sofle:SW_PUSH_LED SW2
U 2 1 616DEF13
P 1300 6100
F 0 "SW2" H 1300 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 6303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1330 6300 50  0001 C CNN
F 3 "" H 1300 6200 50  0001 C CNN
	2    1300 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW3
U 2 1 6174F456
P 1300 6600
F 0 "SW3" H 1300 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 6803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1330 6800 50  0001 C CNN
F 3 "" H 1300 6700 50  0001 C CNN
	2    1300 6600
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW6
U 2 1 617FAB8F
P 1900 6100
F 0 "SW6" H 1900 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 6303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1930 6300 50  0001 C CNN
F 3 "" H 1900 6200 50  0001 C CNN
	2    1900 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW5
U 2 1 617EE3B8
P 1900 5600
F 0 "SW5" H 1900 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 5803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1930 5800 50  0001 C CNN
F 3 "" H 1900 5700 50  0001 C CNN
	2    1900 5600
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW4
U 2 1 61D91426
P 1300 7100
F 0 "SW4" H 1300 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 7303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1330 7300 50  0001 C CNN
F 3 "" H 1300 7200 50  0001 C CNN
	2    1300 7100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW8
U 2 1 61D91BC6
P 1900 7100
F 0 "SW8" H 1900 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 7303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1930 7300 50  0001 C CNN
F 3 "" H 1900 7200 50  0001 C CNN
	2    1900 7100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW18
U 1 1 5C71DC38
P 10450 2300
F 0 "SW18" H 10450 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 10450 2494 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_2u" H 10450 2500 50  0001 C CNN
F 3 "" H 10450 2500 50  0001 C CNN
	1    10450 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 7200 1700 7200
$Comp
L Sofle:LED_SK6812_Mini_E LED1
U 1 1 61796572
P 4950 6100
F 0 "LED1" H 4950 6150 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 4950 6303 25  0001 C CNN
F 2 "Lergo Footprints:SK6812_Mini_E" H 4980 6300 50  0001 C CNN
F 3 "" H 4950 6200 50  0001 C CNN
	1    4950 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:LED_SK6812_Mini_E LED2
U 1 1 61859F12
P 5550 6100
F 0 "LED2" H 5550 6150 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 5550 6303 25  0001 C CNN
F 2 "Lergo Footprints:SK6812_Mini_E" H 5580 6300 50  0001 C CNN
F 3 "" H 5550 6200 50  0001 C CNN
	1    5550 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:LED_SK6812_Mini_E LED3
U 1 1 6188B6CA
P 4950 6950
F 0 "LED3" H 4950 7000 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 4950 7153 25  0001 C CNN
F 2 "Lergo Footprints:SK6812_Mini_E" H 4980 7150 50  0001 C CNN
F 3 "" H 4950 7050 50  0001 C CNN
	1    4950 6950
	1    0    0    -1  
$EndComp
$Comp
L Sofle:LED_SK6812_Mini_E LED4
U 1 1 6188B6EA
P 5550 6950
F 0 "LED4" H 5550 7000 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 5550 7153 25  0001 C CNN
F 2 "Lergo Footprints:SK6812_Mini_E" H 5580 7150 50  0001 C CNN
F 3 "" H 5550 7050 50  0001 C CNN
	1    5550 6950
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_3_Open JP105
U 1 1 617D511C
P 3850 1100
F 0 "JP105" H 3850 1213 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 3850 1214 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 3850 1100 50  0001 C CNN
F 3 "~" H 3850 1100 50  0001 C CNN
	1    3850 1100
	0    1    1    0   
$EndComp
NoConn ~ 3850 900 
Text GLabel 3850 1300 3    50   Input ~ 0
led_
$Comp
L Jumper:SolderJumper_3_Open JP106
U 1 1 618D09E4
P 4350 1100
F 0 "JP106" H 4350 1213 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 4350 1214 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 4350 1100 50  0001 C CNN
F 3 "~" H 4350 1100 50  0001 C CNN
	1    4350 1100
	0    1    1    0   
$EndComp
Text GLabel 4350 1300 3    50   Input ~ 0
data
$Comp
L Jumper:SolderJumper_3_Open JP107
U 1 1 618D1B46
P 4900 1100
F 0 "JP107" H 4900 1213 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 4900 1214 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 4900 1100 50  0001 C CNN
F 3 "~" H 4900 1100 50  0001 C CNN
	1    4900 1100
	0    1    1    0   
$EndComp
Text GLabel 4900 900  1    50   Input ~ 0
reset1
$Comp
L Jumper:SolderJumper_3_Open JP108
U 1 1 618D2207
P 5500 1100
F 0 "JP108" H 5500 1213 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 5500 1214 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 5500 1100 50  0001 C CNN
F 3 "~" H 5500 1100 50  0001 C CNN
	1    5500 1100
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0103
U 1 1 618D27FA
P 5500 900
F 0 "#PWR0103" H 5500 750 50  0001 C CNN
F 1 "VCC" H 5517 1073 50  0000 C CNN
F 2 "" H 5500 900 50  0001 C CNN
F 3 "" H 5500 900 50  0001 C CNN
	1    5500 900 
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 618D3156
P 4350 900
F 0 "#PWR0104" H 4350 650 50  0001 C CNN
F 1 "GND" H 4350 750 50  0000 C CNN
F 2 "" H 4350 900 50  0001 C CNN
F 3 "" H 4350 900 50  0001 C CNN
	1    4350 900 
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0108
U 1 1 618D37CE
P 4900 1300
F 0 "#PWR0108" H 4900 1050 50  0001 C CNN
F 1 "GND" H 4900 1150 50  0000 C CNN
F 2 "" H 4900 1300 50  0001 C CNN
F 3 "" H 4900 1300 50  0001 C CNN
	1    4900 1300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0111
U 1 1 618D3D03
P 5500 1300
F 0 "#PWR0111" H 5500 1050 50  0001 C CNN
F 1 "GND" H 5500 1150 50  0000 C CNN
F 2 "" H 5500 1300 50  0001 C CNN
F 3 "" H 5500 1300 50  0001 C CNN
	1    5500 1300
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_3_Open JP104
U 1 1 61928023
P 1800 950
F 0 "JP104" H 1800 1063 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 1800 1064 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 1800 950 50  0001 C CNN
F 3 "~" H 1800 950 50  0001 C CNN
	1    1800 950 
	0    -1   1    0   
$EndComp
NoConn ~ 1800 1150
$Comp
L Jumper:SolderJumper_3_Open JP103
U 1 1 619A29B2
P 1450 950
F 0 "JP103" H 1450 1063 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 1450 1064 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 1450 950 50  0001 C CNN
F 3 "~" H 1450 950 50  0001 C CNN
	1    1450 950 
	0    -1   1    0   
$EndComp
Text GLabel 1450 750  1    50   Input ~ 0
data
$Comp
L power:GND #PWR0112
U 1 1 619A2FB2
P 1450 1150
F 0 "#PWR0112" H 1450 900 50  0001 C CNN
F 1 "GND" H 1450 1000 50  0000 C CNN
F 2 "" H 1450 1150 50  0001 C CNN
F 3 "" H 1450 1150 50  0001 C CNN
	1    1450 1150
	-1   0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_3_Open JP102
U 1 1 61AE87EE
P 1100 950
F 0 "JP102" V 1100 1017 50  0000 L CNN
F 1 "SolderJumper_3_Open" H 1100 1064 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 1100 950 50  0001 C CNN
F 3 "~" H 1100 950 50  0001 C CNN
	1    1100 950 
	0    -1   1    0   
$EndComp
$Comp
L #library:ProMicro U1
U 1 1 5CE18F26
P 2750 2150
F 0 "U1" H 2750 3187 60  0000 C CNN
F 1 "ProMicro" H 2750 3081 60  0000 C CNN
F 2 "Lergo Footprints:Arduino_ProMicro_Rivets" H 2850 1100 60  0001 C CNN
F 3 "" H 2850 1100 60  0000 C CNN
	1    2750 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3450 1400 3700 1400
Wire Wire Line
	3700 1400 3700 1100
Wire Wire Line
	3450 1500 4200 1500
Wire Wire Line
	4200 1500 4200 1100
Wire Wire Line
	3450 1600 4750 1600
Wire Wire Line
	4750 1600 4750 1100
Wire Wire Line
	3450 1700 5350 1700
Wire Wire Line
	5350 1700 5350 1100
$Comp
L power:GND #PWR0113
U 1 1 61E4578F
P 1100 750
F 0 "#PWR0113" H 1100 500 50  0001 C CNN
F 1 "GND" H 1100 600 50  0000 C CNN
F 2 "" H 1100 750 50  0001 C CNN
F 3 "" H 1100 750 50  0001 C CNN
	1    1100 750 
	1    0    0    1   
$EndComp
$Comp
L Jumper:SolderJumper_3_Open JP101
U 1 1 61E45C5D
P 700 950
F 0 "JP101" V 700 1017 50  0000 L CNN
F 1 "SolderJumper_3_Open" H 700 1064 50  0001 C CNN
F 2 "Lergo Footprints:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 700 950 50  0001 C CNN
F 3 "~" H 700 950 50  0001 C CNN
	1    700  950 
	0    -1   1    0   
$EndComp
$Comp
L power:GND #PWR0114
U 1 1 61E466C0
P 700 750
F 0 "#PWR0114" H 700 500 50  0001 C CNN
F 1 "GND" H 700 600 50  0000 C CNN
F 2 "" H 700 750 50  0001 C CNN
F 3 "" H 700 750 50  0001 C CNN
	1    700  750 
	1    0    0    1   
$EndComp
Text GLabel 1100 1150 3    50   Input ~ 0
reset1
$Comp
L power:VCC #PWR0115
U 1 1 61E73DFF
P 700 1150
F 0 "#PWR0115" H 700 1000 50  0001 C CNN
F 1 "VCC" H 717 1323 50  0000 C CNN
F 2 "" H 700 1150 50  0001 C CNN
F 3 "" H 700 1150 50  0001 C CNN
	1    700  1150
	1    0    0    1   
$EndComp
Wire Wire Line
	2050 1700 850  1700
Wire Wire Line
	850  1700 850  950 
Wire Wire Line
	2050 1600 1250 1600
Wire Wire Line
	1250 1600 1250 950 
Wire Wire Line
	2050 1500 1600 1500
Wire Wire Line
	1600 1500 1600 950 
Wire Wire Line
	2050 1400 1950 1400
Wire Wire Line
	1950 1400 1950 950 
$Comp
L power:GND #PWR0116
U 1 1 620199E6
P 5600 4950
F 0 "#PWR0116" H 5600 4700 50  0001 C CNN
F 1 "GND" H 5600 4800 50  0000 C CNN
F 2 "" H 5600 4950 50  0001 C CNN
F 3 "" H 5600 4950 50  0001 C CNN
	1    5600 4950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5500 4850 5600 4850
Wire Wire Line
	5600 4850 5600 4950
$Comp
L power:GND #PWR0117
U 1 1 6208C099
P 900 2250
F 0 "#PWR0117" H 900 2000 50  0001 C CNN
F 1 "GND" H 900 2100 50  0000 C CNN
F 2 "" H 900 2250 50  0001 C CNN
F 3 "" H 900 2250 50  0001 C CNN
	1    900  2250
	-1   0    0    -1  
$EndComp
Text GLabel 2250 4400 2    50   Input ~ 0
data
$Comp
L power:GND #PWR0118
U 1 1 620B2CCE
P 2550 4450
F 0 "#PWR0118" H 2550 4200 50  0001 C CNN
F 1 "GND" H 2550 4300 50  0000 C CNN
F 2 "" H 2550 4450 50  0001 C CNN
F 3 "" H 2550 4450 50  0001 C CNN
	1    2550 4450
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0119
U 1 1 620B2CD4
P 2550 4050
F 0 "#PWR0119" H 2550 3900 50  0001 C CNN
F 1 "VCC" H 2567 4223 50  0000 C CNN
F 2 "" H 2550 4050 50  0001 C CNN
F 3 "" H 2550 4050 50  0001 C CNN
	1    2550 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 4300 2550 4300
Wire Wire Line
	2550 4300 2550 4450
Wire Wire Line
	2250 4200 2550 4200
Wire Wire Line
	2550 4200 2550 4050
$Comp
L Device:R_Small R101
U 1 1 62335352
P 2700 3550
F 0 "R101" V 2600 3550 50  0000 C CNN
F 1 "510R" V 2800 3550 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 2700 3550 50  0001 C CNN
F 3 "~" H 2700 3550 50  0001 C CNN
	1    2700 3550
	0    1    1    0   
$EndComp
Wire Wire Line
	2900 3550 2800 3550
Wire Wire Line
	2600 3550 2500 3550
Wire Wire Line
	9650 4350 9600 4350
$Comp
L Connector:TestPoint H170
U 1 1 617E0E69
P 9500 4250
F 0 "H170" H 9350 4450 50  0000 L CNN
F 1 "MountingHole_Pad" H 9600 4210 50  0001 L CNN
F 2 "Lergo Footprints:1pin_rect_conn" H 9500 4250 50  0001 C CNN
F 3 "~" H 9500 4250 50  0001 C CNN
	1    9500 4250
	0    1    1    0   
$EndComp
Connection ~ 9500 4250
Wire Wire Line
	9500 4250 9500 4450
$Comp
L Connector:TestPoint H168
U 1 1 617E13D0
P 4300 4250
F 0 "H168" V 4300 4500 50  0000 C CNN
F 1 "MountingHole_Pad" V 4446 4255 50  0001 C CNN
F 2 "Lergo Footprints:1pad_conn" H 4300 4250 50  0001 C CNN
F 3 "~" H 4300 4250 50  0001 C CNN
	1    4300 4250
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H169
U 1 1 617E23BC
P 4750 4200
F 0 "H169" V 4750 4500 50  0000 C CNN
F 1 "MountingHole_Pad" V 4896 4205 50  0001 C CNN
F 2 "Lergo Footprints:1pad_conn" H 4750 4200 50  0001 C CNN
F 3 "~" H 4750 4200 50  0001 C CNN
	1    4750 4200
	0    1    1    0   
$EndComp
Connection ~ 4750 4200
Wire Wire Line
	4750 4200 4750 4300
Text GLabel 3450 1900 2    50   Input ~ 0
X10
Text GLabel 3450 1800 2    50   Input ~ 0
X9
Text GLabel 2050 2500 0    50   Input ~ 0
X8
Text GLabel 2050 2400 0    50   Input ~ 0
X7
Text GLabel 2050 2300 0    50   Input ~ 0
X6
Text GLabel 2050 2200 0    50   Input ~ 0
X5
Text GLabel 2050 2100 0    50   Input ~ 0
X4
Text GLabel 2050 2000 0    50   Input ~ 0
X3
Text GLabel 2050 1900 0    50   Input ~ 0
X2
Text GLabel 2050 1800 0    50   Input ~ 0
X1
$Comp
L Sofle:SW_PUSH_LED SW1
U 1 1 5C43B1D6
P 6200 1700
F 0 "SW1" H 6200 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 1894 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 6200 1900 50  0001 C CNN
F 3 "" H 6200 1900 50  0001 C CNN
	1    6200 1700
	1    0    0    -1  
$EndComp
Connection ~ 6000 1700
Wire Wire Line
	6000 800  6000 1700
$Comp
L Sofle:SW_PUSH_LED SW3
U 1 1 5CE4CCD8
P 6200 2900
F 0 "SW3" H 6200 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 3094 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 6200 3100 50  0001 C CNN
F 3 "" H 6200 3100 50  0001 C CNN
	1    6200 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 800  7050 1700
Wire Wire Line
	6000 1700 6000 2300
Connection ~ 6000 2300
Wire Wire Line
	6000 2300 6000 2900
Connection ~ 6000 2900
Wire Wire Line
	6000 2900 6000 3500
$Comp
L Sofle:SW_PUSH_LED SW1
U 2 1 61623882
P 1300 5600
F 0 "SW1" H 1300 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 5803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1330 5800 50  0001 C CNN
F 3 "" H 1300 5700 50  0001 C CNN
	2    1300 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 5700 1500 5850
Wire Wire Line
	1500 6200 1500 6350
Wire Wire Line
	1500 6700 1500 6850
Wire Wire Line
	1050 5850 1050 6200
Wire Wire Line
	1050 6200 1100 6200
Wire Wire Line
	1050 5850 1500 5850
Wire Wire Line
	1050 6350 1050 6700
Wire Wire Line
	1050 6700 1100 6700
Wire Wire Line
	1050 6350 1500 6350
Wire Wire Line
	1050 6850 1050 7200
Wire Wire Line
	1050 7200 1100 7200
Wire Wire Line
	1050 6850 1500 6850
Wire Wire Line
	1700 5700 1700 5850
Wire Wire Line
	1700 6200 1700 6350
Wire Wire Line
	1700 6700 1700 6850
Wire Wire Line
	2100 7200 2150 7200
Wire Wire Line
	2150 7200 2150 6850
Wire Wire Line
	1700 6850 2150 6850
$Comp
L Sofle:SW_PUSH_LED SW7
U 2 1 617FB0D7
P 1900 6600
F 0 "SW7" H 1900 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 6803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 1930 6800 50  0001 C CNN
F 3 "" H 1900 6700 50  0001 C CNN
	2    1900 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 6700 2150 6700
Wire Wire Line
	2150 6700 2150 6350
Wire Wire Line
	1700 6350 2150 6350
Wire Wire Line
	2100 6200 2150 6200
Wire Wire Line
	2150 6200 2150 5850
Wire Wire Line
	1700 5850 2150 5850
$Comp
L Sofle:SW_PUSH_LED SW10
U 2 1 61CA23AC
P 2600 6100
F 0 "SW10" H 2600 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2600 6303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 2630 6300 50  0001 C CNN
F 3 "" H 2600 6200 50  0001 C CNN
	2    2600 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW11
U 2 1 61CA23B2
P 2600 6600
F 0 "SW11" H 2600 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2600 6803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 2630 6800 50  0001 C CNN
F 3 "" H 2600 6700 50  0001 C CNN
	2    2600 6600
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW14
U 2 1 61CA23B8
P 3200 6100
F 0 "SW14" H 3200 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3200 6303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 3230 6300 50  0001 C CNN
F 3 "" H 3200 6200 50  0001 C CNN
	2    3200 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW13
U 2 1 61CA23BE
P 3200 5600
F 0 "SW13" H 3200 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3200 5803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 3230 5800 50  0001 C CNN
F 3 "" H 3200 5700 50  0001 C CNN
	2    3200 5600
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW12
U 2 1 61CA23C4
P 2600 7100
F 0 "SW12" H 2600 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2600 7303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 2630 7300 50  0001 C CNN
F 3 "" H 2600 7200 50  0001 C CNN
	2    2600 7100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW16
U 2 1 61CA23CA
P 3200 7100
F 0 "SW16" H 3200 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3200 7303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 3230 7300 50  0001 C CNN
F 3 "" H 3200 7200 50  0001 C CNN
	2    3200 7100
	1    0    0    -1  
$EndComp
Wire Wire Line
	2800 7200 3000 7200
$Comp
L Sofle:SW_PUSH_LED SW9
U 2 1 61CA23D1
P 2600 5600
F 0 "SW9" H 2600 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2600 5803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 2630 5800 50  0001 C CNN
F 3 "" H 2600 5700 50  0001 C CNN
	2    2600 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	2800 5700 2800 5850
Wire Wire Line
	2800 6200 2800 6350
Wire Wire Line
	2800 6700 2800 6850
Wire Wire Line
	2350 5850 2350 6200
Wire Wire Line
	2350 6200 2400 6200
Wire Wire Line
	2350 5850 2800 5850
Wire Wire Line
	2350 6350 2350 6700
Wire Wire Line
	2350 6700 2400 6700
Wire Wire Line
	2350 6350 2800 6350
Wire Wire Line
	2350 6850 2350 7200
Wire Wire Line
	2350 7200 2400 7200
Wire Wire Line
	2350 6850 2800 6850
Wire Wire Line
	3000 5700 3000 5850
Wire Wire Line
	3000 6200 3000 6350
Wire Wire Line
	3000 6700 3000 6850
Wire Wire Line
	3400 7200 3450 7200
Wire Wire Line
	3450 7200 3450 6850
Wire Wire Line
	3000 6850 3450 6850
$Comp
L Sofle:SW_PUSH_LED SW15
U 2 1 61CA23E9
P 3200 6600
F 0 "SW15" H 3200 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3200 6803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 3230 6800 50  0001 C CNN
F 3 "" H 3200 6700 50  0001 C CNN
	2    3200 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3400 6700 3450 6700
Wire Wire Line
	3450 6700 3450 6350
Wire Wire Line
	3000 6350 3450 6350
Wire Wire Line
	3400 6200 3450 6200
Wire Wire Line
	3450 6200 3450 5850
Wire Wire Line
	3000 5850 3450 5850
Wire Wire Line
	2100 5700 2400 5700
Wire Wire Line
	4100 5700 4100 5850
$Comp
L Sofle:SW_PUSH_LED SW18
U 2 1 61823C35
P 3900 6100
F 0 "SW18" H 3900 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3900 6303 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_2u" H 3930 6300 50  0001 C CNN
F 3 "" H 3900 6200 50  0001 C CNN
	2    3900 6100
	1    0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW17
U 2 1 61D91BBA
P 3900 5600
F 0 "SW17" H 3900 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3900 5803 25  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 3930 5800 50  0001 C CNN
F 3 "" H 3900 5700 50  0001 C CNN
	2    3900 5600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 5850 3650 6200
Wire Wire Line
	3650 6200 3700 6200
Wire Wire Line
	3650 5850 4100 5850
Wire Wire Line
	3400 5700 3700 5700
Wire Wire Line
	5150 6200 5200 6200
Wire Wire Line
	5750 6200 5750 6350
Wire Wire Line
	5750 6350 4700 6350
Wire Wire Line
	5150 7050 5200 7050
Wire Wire Line
	4100 6200 4700 6200
$Comp
L Device:C_Small C19
U 1 1 61E74A3F
P 4950 5850
F 0 "C19" V 4721 5850 50  0000 C CNN
F 1 "100n" V 4812 5850 50  0000 C CNN
F 2 "Lergo Footprints:C_0603_0805_HandSolder" H 4950 5850 50  0001 C CNN
F 3 "~" H 4950 5850 50  0001 C CNN
	1    4950 5850
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C20
U 1 1 61E7576C
P 5550 5850
F 0 "C20" V 5321 5850 50  0000 C CNN
F 1 "100n" V 5412 5850 50  0000 C CNN
F 2 "Lergo Footprints:C_0603_0805_HandSolder" H 5550 5850 50  0001 C CNN
F 3 "~" H 5550 5850 50  0001 C CNN
	1    5550 5850
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C21
U 1 1 61E948CC
P 4950 6700
F 0 "C21" V 4721 6700 50  0000 C CNN
F 1 "100n" V 4812 6700 50  0000 C CNN
F 2 "Lergo Footprints:C_0603_0805_HandSolder" H 4950 6700 50  0001 C CNN
F 3 "~" H 4950 6700 50  0001 C CNN
	1    4950 6700
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C22
U 1 1 61E95195
P 5550 6700
F 0 "C22" V 5321 6700 50  0000 C CNN
F 1 "100n" V 5412 6700 50  0000 C CNN
F 2 "Lergo Footprints:C_0603_0805_HandSolder" H 5550 6700 50  0001 C CNN
F 3 "~" H 5550 6700 50  0001 C CNN
	1    5550 6700
	0    1    1    0   
$EndComp
Wire Wire Line
	4700 7050 4750 7050
Wire Wire Line
	4700 6350 4700 7050
Wire Wire Line
	4750 6850 4750 6700
Wire Wire Line
	4750 6700 4850 6700
Wire Wire Line
	5050 6700 5150 6700
Wire Wire Line
	5150 6700 5150 6850
Wire Wire Line
	5450 6700 5350 6700
Wire Wire Line
	5350 6700 5350 6850
Wire Wire Line
	5650 6700 5750 6700
Wire Wire Line
	5750 6700 5750 6850
Wire Wire Line
	5650 5850 5750 5850
Wire Wire Line
	5450 5850 5350 5850
Wire Wire Line
	5350 5850 5350 6000
Wire Wire Line
	5050 5850 5150 5850
Wire Wire Line
	5150 5850 5150 6000
Wire Wire Line
	4850 5850 4750 5850
Wire Wire Line
	4750 5850 4750 6000
Wire Wire Line
	10250 800  10250 1700
Wire Wire Line
	9200 800  9200 1700
Wire Wire Line
	8150 800  8150 1700
Wire Wire Line
	5600 2600 6400 2600
Wire Wire Line
	5600 3200 6400 3200
Wire Wire Line
	5600 2000 6400 2000
$Comp
L Sofle:SW_PUSH_LED SW5
U 1 1 5C43B248
P 7250 1700
F 0 "SW5" H 7250 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 1894 50  0001 C CNN
F 2 "Lergo Footprints:CherryMX_Lergo_v1_Module_1u" H 7250 1900 50  0001 C CNN
F 3 "" H 7250 1900 50  0001 C CNN
	1    7250 1700
	1    0    0    -1  
$EndComp
Connection ~ 7050 1700
Connection ~ 7050 2300
Connection ~ 7050 2900
Connection ~ 8150 2900
Connection ~ 8150 2300
Connection ~ 8150 1700
Connection ~ 9200 1700
Connection ~ 9200 2300
Connection ~ 9200 2900
Connection ~ 10250 1700
Wire Wire Line
	10250 1700 10250 2300
Wire Wire Line
	9200 2900 9200 3500
Wire Wire Line
	9200 2300 9200 2900
Wire Wire Line
	9200 1700 9200 2300
Wire Wire Line
	8150 1700 8150 2300
Wire Wire Line
	8150 2300 8150 2900
Wire Wire Line
	8150 2900 8150 3500
Wire Wire Line
	7050 2900 7050 3500
Wire Wire Line
	7050 2300 7050 2900
Wire Wire Line
	7050 1700 7050 2300
Connection ~ 6400 2600
Wire Wire Line
	6400 2600 7450 2600
Connection ~ 7450 2600
Wire Wire Line
	7450 2600 8550 2600
Connection ~ 8550 2600
Wire Wire Line
	8550 2600 9600 2600
Connection ~ 9600 2600
Connection ~ 6400 2000
Wire Wire Line
	6400 2000 7450 2000
Connection ~ 7450 2000
Wire Wire Line
	7450 2000 8550 2000
Connection ~ 8550 2000
Wire Wire Line
	8550 2000 9600 2000
Connection ~ 9600 2000
Wire Wire Line
	9600 2000 10650 2000
Connection ~ 6400 3200
Wire Wire Line
	6400 3200 7450 3200
Connection ~ 7450 3200
Wire Wire Line
	7450 3200 8550 3200
Connection ~ 8550 3200
Wire Wire Line
	8550 3200 9600 3200
Connection ~ 6400 3800
Connection ~ 7450 3800
Connection ~ 8550 3800
Wire Wire Line
	5600 3800 6400 3800
Wire Wire Line
	6400 3800 7450 3800
Wire Wire Line
	7450 3800 8550 3800
Wire Wire Line
	8550 3800 9600 3800
Text GLabel 1050 5700 0    50   Input ~ 0
led
Wire Wire Line
	1050 5700 1100 5700
Wire Wire Line
	9600 2600 10650 2600
$Comp
L Connector:TestPoint H152
U 1 1 6179589B
P 4750 5850
F 0 "H152" H 4650 6050 50  0000 L CNN
F 1 "MountingHole_Pad" H 4850 5810 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 4750 5850 50  0001 C CNN
F 3 "~" H 4750 5850 50  0001 C CNN
	1    4750 5850
	1    0    0    -1  
$EndComp
Connection ~ 4750 5850
$Comp
L Connector:TestPoint H155
U 1 1 617A9D73
P 5150 5850
F 0 "H155" H 5050 6050 50  0000 L CNN
F 1 "MountingHole_Pad" H 5250 5810 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 5150 5850 50  0001 C CNN
F 3 "~" H 5150 5850 50  0001 C CNN
	1    5150 5850
	1    0    0    -1  
$EndComp
Connection ~ 5150 5850
$Comp
L Connector:TestPoint H154
U 1 1 617AB121
P 4700 6200
F 0 "H154" H 4600 6400 50  0000 L CNN
F 1 "MountingHole_Pad" H 4800 6160 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 4700 6200 50  0001 C CNN
F 3 "~" H 4700 6200 50  0001 C CNN
	1    4700 6200
	1    0    0    -1  
$EndComp
Connection ~ 4700 6200
Wire Wire Line
	4700 6200 4750 6200
$Comp
L Connector:TestPoint H153
U 1 1 617B3661
P 5200 6200
F 0 "H153" H 5100 6400 50  0000 L CNN
F 1 "MountingHole_Pad" H 5300 6160 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 5200 6200 50  0001 C CNN
F 3 "~" H 5200 6200 50  0001 C CNN
	1    5200 6200
	1    0    0    -1  
$EndComp
Connection ~ 5200 6200
Wire Wire Line
	5200 6200 5300 6200
$Comp
L Connector:TestPoint H156
U 1 1 617B4237
P 5350 5850
F 0 "H156" H 5250 6050 50  0000 L CNN
F 1 "MountingHole_Pad" H 5450 5810 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 5350 5850 50  0001 C CNN
F 3 "~" H 5350 5850 50  0001 C CNN
	1    5350 5850
	1    0    0    -1  
$EndComp
Connection ~ 5350 5850
$Comp
L Connector:TestPoint H159
U 1 1 617B4BE1
P 5750 5850
F 0 "H159" H 5650 6050 50  0000 L CNN
F 1 "MountingHole_Pad" H 5850 5810 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 5750 5850 50  0001 C CNN
F 3 "~" H 5750 5850 50  0001 C CNN
	1    5750 5850
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H158
U 1 1 617B557E
P 5300 6200
F 0 "H158" H 5200 6400 50  0000 L CNN
F 1 "MountingHole_Pad" H 5400 6160 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 5300 6200 50  0001 C CNN
F 3 "~" H 5300 6200 50  0001 C CNN
	1    5300 6200
	1    0    0    -1  
$EndComp
Connection ~ 5300 6200
Wire Wire Line
	5300 6200 5350 6200
$Comp
L Connector:TestPoint H157
U 1 1 617B5AA9
P 5800 6200
F 0 "H157" H 5700 6400 50  0000 L CNN
F 1 "MountingHole_Pad" H 5900 6160 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 5800 6200 50  0001 C CNN
F 3 "~" H 5800 6200 50  0001 C CNN
	1    5800 6200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 6200 5750 6200
Connection ~ 5750 6200
$Comp
L Connector:TestPoint H163
U 1 1 617FBA37
P 5150 6700
F 0 "H163" H 5050 6900 50  0000 L CNN
F 1 "MountingHole_Pad" H 5250 6660 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 5150 6700 50  0001 C CNN
F 3 "~" H 5150 6700 50  0001 C CNN
	1    5150 6700
	1    0    0    -1  
$EndComp
Connection ~ 5150 6700
$Comp
L Connector:TestPoint H160
U 1 1 617FCDC4
P 4750 6700
F 0 "H160" H 4650 6900 50  0000 L CNN
F 1 "MountingHole_Pad" H 4850 6660 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 4750 6700 50  0001 C CNN
F 3 "~" H 4750 6700 50  0001 C CNN
	1    4750 6700
	1    0    0    -1  
$EndComp
Connection ~ 4750 6700
$Comp
L Connector:TestPoint H162
U 1 1 617FE62E
P 4700 7050
F 0 "H162" H 4600 7250 50  0000 L CNN
F 1 "MountingHole_Pad" H 4800 7010 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 4700 7050 50  0001 C CNN
F 3 "~" H 4700 7050 50  0001 C CNN
	1    4700 7050
	0    -1   -1   0   
$EndComp
Connection ~ 4700 7050
$Comp
L Connector:TestPoint H161
U 1 1 61801014
P 5200 7050
F 0 "H161" H 5100 7250 50  0000 L CNN
F 1 "MountingHole_Pad" H 5300 7010 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 5200 7050 50  0001 C CNN
F 3 "~" H 5200 7050 50  0001 C CNN
	1    5200 7050
	1    0    0    -1  
$EndComp
Connection ~ 5200 7050
Wire Wire Line
	5200 7050 5300 7050
$Comp
L Connector:TestPoint H164
U 1 1 61802D8F
P 5350 6700
F 0 "H164" H 5250 6900 50  0000 L CNN
F 1 "MountingHole_Pad" H 5450 6660 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 5350 6700 50  0001 C CNN
F 3 "~" H 5350 6700 50  0001 C CNN
	1    5350 6700
	1    0    0    -1  
$EndComp
Connection ~ 5350 6700
$Comp
L Connector:TestPoint H167
U 1 1 61805FD7
P 5750 6700
F 0 "H167" H 5650 6900 50  0000 L CNN
F 1 "MountingHole_Pad" H 5850 6660 50  0001 L CNN
F 2 "Lergo Footprints:1pin_conn" H 5750 6700 50  0001 C CNN
F 3 "~" H 5750 6700 50  0001 C CNN
	1    5750 6700
	1    0    0    -1  
$EndComp
Connection ~ 5750 6700
$Comp
L Connector:TestPoint H166
U 1 1 618073A5
P 5300 7050
F 0 "H166" H 5200 7250 50  0000 L CNN
F 1 "MountingHole_Pad" H 5400 7010 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 5300 7050 50  0001 C CNN
F 3 "~" H 5300 7050 50  0001 C CNN
	1    5300 7050
	1    0    0    -1  
$EndComp
Connection ~ 5300 7050
Wire Wire Line
	5300 7050 5350 7050
$Comp
L Connector:TestPoint H165
U 1 1 6180A30A
P 5800 7050
F 0 "H165" H 5700 7250 50  0000 L CNN
F 1 "MountingHole_Pad" H 5900 7010 50  0001 L CNN
F 2 "Lergo Footprints:1pad_conn" H 5800 7050 50  0001 C CNN
F 3 "~" H 5800 7050 50  0001 C CNN
	1    5800 7050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5750 7050 5800 7050
Text GLabel 2500 3550 0    50   Input ~ 0
led_
Text GLabel 3400 4250 2    50   Input ~ 0
led
$Comp
L Device:Rotary_Encoder_Switch SW19
U 1 1 617D6B8F
P 9000 4450
F 0 "SW19" V 8954 4220 50  0000 R CNN
F 1 "Rotary_Encoder_Switch" V 9045 4220 50  0001 R CNN
F 2 "Lergo Footprints:RollerEncoder_Panasonic_EVQWGD001_No_Cutout" H 8850 4610 50  0001 C CNN
F 3 "~" H 9000 4710 50  0001 C CNN
	1    9000 4450
	-1   0    0    1   
$EndComp
Wire Wire Line
	8700 4550 8700 5200
Wire Wire Line
	8700 5200 9200 5200
Wire Wire Line
	8700 4350 8700 3900
Wire Wire Line
	8700 3900 9850 3900
Wire Wire Line
	9850 3900 9850 5200
Wire Wire Line
	9850 5200 9600 5200
Connection ~ 9600 5200
$Comp
L Device:R_Small R102
U 1 1 617E22EC
P 2300 3100
F 0 "R102" H 2150 3050 50  0000 C CNN
F 1 "4k7" H 2200 3150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 2300 3100 50  0001 C CNN
F 3 "~" H 2300 3100 50  0001 C CNN
	1    2300 3100
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R103
U 1 1 617F9D27
P 2600 3100
F 0 "R103" H 2450 3050 50  0000 C CNN
F 1 "4k7" H 2500 3150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 2600 3100 50  0001 C CNN
F 3 "~" H 2600 3100 50  0001 C CNN
	1    2600 3100
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R104
U 1 1 617F9F3F
P 2900 3100
F 0 "R104" H 2750 3050 50  0000 C CNN
F 1 "4k7" H 2800 3150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 2900 3100 50  0001 C CNN
F 3 "~" H 2900 3100 50  0001 C CNN
	1    2900 3100
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R105
U 1 1 617FA297
P 3200 3100
F 0 "R105" H 3050 3050 50  0000 C CNN
F 1 "4k7" H 3100 3150 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 3200 3100 50  0001 C CNN
F 3 "~" H 3200 3100 50  0001 C CNN
	1    3200 3100
	-1   0    0    1   
$EndComp
$Comp
L power:VCC #PWR0105
U 1 1 618067A2
P 2700 2950
F 0 "#PWR0105" H 2700 2800 50  0001 C CNN
F 1 "VCC" H 2717 3123 50  0000 C CNN
F 2 "" H 2700 2950 50  0001 C CNN
F 3 "" H 2700 2950 50  0001 C CNN
	1    2700 2950
	-1   0    0    -1  
$EndComp
Text GLabel 2300 3200 3    50   Input ~ 0
X1
Text GLabel 2600 3200 3    50   Input ~ 0
X2
Wire Wire Line
	2300 3000 2300 2950
Wire Wire Line
	2300 2950 2600 2950
Wire Wire Line
	2700 2950 2900 2950
Wire Wire Line
	3200 2950 3200 3000
Connection ~ 2700 2950
Wire Wire Line
	2900 3000 2900 2950
Connection ~ 2900 2950
Wire Wire Line
	2900 2950 3200 2950
Wire Wire Line
	2600 3000 2600 2950
Connection ~ 2600 2950
Wire Wire Line
	2600 2950 2700 2950
Text GLabel 2900 3200 3    50   Input ~ 0
X9
Text GLabel 3200 3200 3    50   Input ~ 0
X10
$Comp
L #library:5way_switch SW24
U 1 1 618664BD
P 10500 4450
F 0 "SW24" H 10500 4800 50  0000 C CNN
F 1 "5way_switch" H 10500 4700 50  0000 C CNN
F 2 "Lergo Footprints:Five_Way_Switch_Panasonic_EVQQ7" H 10500 4450 50  0001 C CNN
F 3 "" H 10500 4450 50  0001 C CNN
	1    10500 4450
	0    -1   -1   0   
$EndComp
Connection ~ 5750 5850
Wire Wire Line
	5750 5850 5750 6000
$Comp
L power:GND #PWR01
U 1 1 618C1BC5
P 10950 4350
F 0 "#PWR01" H 10950 4100 50  0001 C CNN
F 1 "GND" H 10950 4200 50  0000 C CNN
F 2 "" H 10950 4350 50  0001 C CNN
F 3 "" H 10950 4350 50  0001 C CNN
	1    10950 4350
	0    -1   -1   0   
$EndComp
$Comp
L Device:D_Small D1
U 1 1 618FAEED
P 10400 4950
F 0 "D1" H 10500 5000 50  0000 C CNN
F 1 "D_Small" H 10400 5066 50  0001 C CNN
F 2 "Lergo Footprints:diode_TH_SMD_rev3_alt" V 10400 4950 50  0001 C CNN
F 3 "~" V 10400 4950 50  0001 C CNN
	1    10400 4950
	0    1    1    0   
$EndComp
$Comp
L Device:D_Small D2
U 1 1 61926050
P 10500 4950
F 0 "D2" H 10600 5000 50  0000 C CNN
F 1 "D_Small" H 10500 5066 50  0001 C CNN
F 2 "Lergo Footprints:diode_TH_SMD_rev3_alt" V 10500 4950 50  0001 C CNN
F 3 "~" V 10500 4950 50  0001 C CNN
	1    10500 4950
	0    1    1    0   
$EndComp
$Comp
L Device:D_Small D3
U 1 1 619271A4
P 10600 4950
F 0 "D3" H 10700 5000 50  0000 C CNN
F 1 "D_Small" H 10600 5066 50  0001 C CNN
F 2 "Lergo Footprints:diode_TH_SMD_rev3_alt" V 10600 4950 50  0001 C CNN
F 3 "~" V 10600 4950 50  0001 C CNN
	1    10600 4950
	0    1    1    0   
$EndComp
$Comp
L Device:D_Small D4
U 1 1 6192826E
P 10400 3950
F 0 "D4" H 10500 4000 50  0000 C CNN
F 1 "D_Small" H 10400 4066 50  0001 C CNN
F 2 "Lergo Footprints:diode_TH_SMD_rev3_alt" V 10400 3950 50  0001 C CNN
F 3 "~" V 10400 3950 50  0001 C CNN
	1    10400 3950
	0    1    -1   0   
$EndComp
$Comp
L Device:D_Small D5
U 1 1 6192988F
P 10600 3950
F 0 "D5" H 10700 4000 50  0000 C CNN
F 1 "D_Small" H 10600 4066 50  0001 C CNN
F 2 "Lergo Footprints:diode_TH_SMD_rev3_alt" V 10600 3950 50  0001 C CNN
F 3 "~" V 10600 3950 50  0001 C CNN
	1    10600 3950
	0    1    -1   0   
$EndComp
Wire Wire Line
	10400 4150 10400 4050
Wire Wire Line
	10600 4150 10600 4050
Wire Wire Line
	10400 4750 10400 4850
Wire Wire Line
	10500 4750 10500 4850
Wire Wire Line
	10600 4750 10600 4850
$Comp
L Connector:TestPoint H6
U 1 1 61AECB68
P 10900 4500
F 0 "H6" H 10900 4700 50  0000 C CNN
F 1 "MountingHole_Pad" V 11046 4505 50  0001 C CNN
F 2 "Lergo Footprints:1pin_rect_conn" H 10900 4500 50  0001 C CNN
F 3 "~" H 10900 4500 50  0001 C CNN
	1    10900 4500
	-1   0    0    1   
$EndComp
Wire Wire Line
	10900 4500 10850 4500
Wire Wire Line
	10950 4350 10850 4350
Wire Wire Line
	10400 5150 10400 5050
Wire Wire Line
	10500 5150 10500 5050
Wire Wire Line
	10600 5150 10600 5050
Wire Wire Line
	10600 3850 10600 3750
Wire Wire Line
	10400 3850 10400 3750
Text GLabel 10500 5150 3    39   Input ~ 0
X5
Text GLabel 10400 5150 3    50   Input ~ 0
X7
Text GLabel 10600 5150 3    50   Input ~ 0
X8
Text GLabel 10400 3750 1    50   Input ~ 0
X9
Text GLabel 10600 3750 1    50   Input ~ 0
X10
Text GLabel 9200 4800 1    39   Input ~ 0
X4
Wire Wire Line
	9400 4100 9400 4150
Wire Wire Line
	9300 4550 9600 4550
Connection ~ 9600 4550
Wire Wire Line
	9600 4550 9600 4600
Wire Wire Line
	9300 4350 9400 4350
Connection ~ 9400 4350
Wire Wire Line
	9400 4350 9400 4600
$Comp
L Connector:TestPoint H101
U 1 1 6189071E
P 9400 4150
F 0 "H101" V 9500 4350 50  0000 C CNN
F 1 "MountingHole_Pad" V 9546 4155 50  0001 C CNN
F 2 "Lergo Footprints:1pin_rect_conn" H 9400 4150 50  0001 C CNN
F 3 "~" H 9400 4150 50  0001 C CNN
	1    9400 4150
	0    -1   -1   0   
$EndComp
Connection ~ 9400 4150
Wire Wire Line
	9400 4150 9400 4350
$Comp
L Connector:TestPoint H102
U 1 1 61890DCE
P 9600 4450
F 0 "H102" V 9700 4550 50  0000 C CNN
F 1 "MountingHole_Pad" V 9746 4455 50  0001 C CNN
F 2 "Lergo Footprints:1pin_rect_conn" H 9600 4450 50  0001 C CNN
F 3 "~" H 9600 4450 50  0001 C CNN
	1    9600 4450
	0    1    1    0   
$EndComp
Connection ~ 9600 4450
Wire Wire Line
	9600 4450 9600 4550
Wire Wire Line
	5600 5500 9600 5500
Connection ~ 9600 5500
Wire Wire Line
	9800 5500 11000 5500
Wire Wire Line
	11000 5500 11000 4500
Wire Wire Line
	11000 4500 10900 4500
Connection ~ 9800 5500
Connection ~ 10900 4500
$EndSCHEMATC
