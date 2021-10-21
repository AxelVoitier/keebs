EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "SU120 Yakitori Keyboard"
Date ""
Rev "8"
Comp "@e3w2q"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:D D1
U 1 1 5B465AE7
P 6400 1950
F 0 "D1" H 6400 2050 50  0000 C CNN
F 1 "D" H 6400 1850 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 6400 1950 50  0001 C CNN
F 3 "" H 6400 1950 50  0001 C CNN
	1    6400 1950
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D2
U 1 1 5B4657D8
P 7450 1950
F 0 "D2" H 7450 2050 50  0000 C CNN
F 1 "D" H 7450 1850 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 7450 1950 50  0001 C CNN
F 3 "" H 7450 1950 50  0001 C CNN
	1    7450 1950
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D3
U 1 1 5B465834
P 8550 1950
F 0 "D3" H 8550 2050 50  0000 C CNN
F 1 "D" H 8550 1850 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 8550 1950 50  0001 C CNN
F 3 "" H 8550 1950 50  0001 C CNN
	1    8550 1950
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D4
U 1 1 5B465930
P 9600 1950
F 0 "D4" H 9600 2050 50  0000 C CNN
F 1 "D" H 9600 1850 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 9600 1950 50  0001 C CNN
F 3 "" H 9600 1950 50  0001 C CNN
	1    9600 1950
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D6
U 1 1 5B465C74
P 6400 2550
F 0 "D6" H 6400 2650 50  0000 C CNN
F 1 "D" H 6400 2450 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 6400 2550 50  0001 C CNN
F 3 "" H 6400 2550 50  0001 C CNN
	1    6400 2550
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D7
U 1 1 5B465C80
P 7450 2550
F 0 "D7" H 7450 2650 50  0000 C CNN
F 1 "D" H 7450 2450 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 7450 2550 50  0001 C CNN
F 3 "" H 7450 2550 50  0001 C CNN
	1    7450 2550
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D8
U 1 1 5B465C8C
P 8550 2550
F 0 "D8" H 8550 2650 50  0000 C CNN
F 1 "D" H 8550 2450 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 8550 2550 50  0001 C CNN
F 3 "" H 8550 2550 50  0001 C CNN
	1    8550 2550
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D9
U 1 1 5B465C98
P 9600 2550
F 0 "D9" H 9600 2650 50  0000 C CNN
F 1 "D" H 9600 2450 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 9600 2550 50  0001 C CNN
F 3 "" H 9600 2550 50  0001 C CNN
	1    9600 2550
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8550 2100 8750 2100
Wire Wire Line
	8550 2700 8750 2700
$Comp
L Sofle:SW_PUSH_LED SW1
U 1 1 5C43B1D6
P 6200 1700
F 0 "SW1" H 6200 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 1894 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 6200 1900 50  0001 C CNN
F 3 "" H 6200 1900 50  0001 C CNN
	1    6200 1700
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW5
U 1 1 5C43B248
P 7250 1700
F 0 "SW5" H 7250 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 1894 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 7250 1900 50  0001 C CNN
F 3 "" H 7250 1900 50  0001 C CNN
	1    7250 1700
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW9
U 1 1 5C43B29E
P 8350 1700
F 0 "SW9" H 8350 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 1894 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 8350 1900 50  0001 C CNN
F 3 "" H 8350 1900 50  0001 C CNN
	1    8350 1700
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW13
U 1 1 5C43B2EA
P 9400 1700
F 0 "SW13" H 9400 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 1894 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 9400 1900 50  0001 C CNN
F 3 "" H 9400 1900 50  0001 C CNN
	1    9400 1700
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW2
U 1 1 5C43B33A
P 6200 2300
F 0 "SW2" H 6200 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 2494 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 6200 2500 50  0001 C CNN
F 3 "" H 6200 2500 50  0001 C CNN
	1    6200 2300
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW6
U 1 1 5C43B3A2
P 7250 2300
F 0 "SW6" H 7250 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 2494 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 7250 2500 50  0001 C CNN
F 3 "" H 7250 2500 50  0001 C CNN
	1    7250 2300
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW10
U 1 1 5C43B3F4
P 8350 2300
F 0 "SW10" H 8350 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 2494 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 8350 2500 50  0001 C CNN
F 3 "" H 8350 2500 50  0001 C CNN
	1    8350 2300
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW14
U 1 1 5C43B44C
P 9400 2300
F 0 "SW14" H 9400 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 2494 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 9400 2500 50  0001 C CNN
F 3 "" H 9400 2500 50  0001 C CNN
	1    9400 2300
	-1   0    0    -1  
$EndComp
$Comp
L Device:D D5
U 1 1 5C485046
P 10650 1950
F 0 "D5" H 10650 2050 50  0000 C CNN
F 1 "D" H 10650 1850 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 10650 1950 50  0001 C CNN
F 3 "" H 10650 1950 50  0001 C CNN
	1    10650 1950
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D10
U 1 1 5C48504D
P 6400 3750
F 0 "D10" H 6400 3850 50  0000 C CNN
F 1 "D" H 6400 3650 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 6400 3750 50  0001 C CNN
F 3 "" H 6400 3750 50  0001 C CNN
	1    6400 3750
	0    -1   -1   0   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW17
U 1 1 5C485058
P 10450 1700
F 0 "SW17" H 10450 1850 50  0000 C CNN
F 1 "SW_PUSH_LED" H 10450 1894 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 10450 1900 50  0001 C CNN
F 3 "" H 10450 1900 50  0001 C CNN
	1    10450 1700
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW4
U 1 1 5C485061
P 6200 3500
F 0 "SW4" H 6200 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 3694 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 6200 3700 50  0001 C CNN
F 3 "" H 6200 3700 50  0001 C CNN
	1    6200 3500
	-1   0    0    -1  
$EndComp
Text GLabel 5600 2100 0    39   Input ~ 0
Y1
Text GLabel 5600 2700 0    39   Input ~ 0
Y2
$Comp
L Connector:TestPoint H23
U 1 1 5C480499
P 8150 2250
F 0 "H23" V 8150 2500 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 2255 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 2250 50  0001 C CNN
F 3 "~" H 8150 2250 50  0001 C CNN
	1    8150 2250
	0    -1   -1   0   
$EndComp
Connection ~ 6400 2700
$Comp
L Connector:TestPoint H8
U 1 1 5C488E99
P 8150 1950
F 0 "H8" V 8150 2200 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 1955 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 1950 50  0001 C CNN
F 3 "~" H 8150 1950 50  0001 C CNN
	1    8150 1950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8150 1950 8150 2250
$Comp
L Connector:TestPoint H3
U 1 1 5C488EF9
P 8150 1650
F 0 "H3" V 8150 1900 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 1655 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 1650 50  0001 C CNN
F 3 "~" H 8150 1650 50  0001 C CNN
	1    8150 1650
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H28
U 1 1 5C488F59
P 8150 2550
F 0 "H28" V 8150 2800 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 2555 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 2550 50  0001 C CNN
F 3 "~" H 8150 2550 50  0001 C CNN
	1    8150 2550
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H15
U 1 1 5C489A90
P 8350 2100
F 0 "H15" H 8250 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 8450 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8350 2100 50  0001 C CNN
F 3 "~" H 8350 2100 50  0001 C CNN
	1    8350 2100
	1    0    0    -1  
$EndComp
Connection ~ 8350 2100
Wire Wire Line
	8350 2100 8550 2100
$Comp
L Connector:TestPoint H16
U 1 1 5C489B2D
P 8750 2100
F 0 "H16" H 8650 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 8850 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8750 2100 50  0001 C CNN
F 3 "~" H 8750 2100 50  0001 C CNN
	1    8750 2100
	1    0    0    -1  
$EndComp
Connection ~ 8750 2100
$Comp
L Connector:TestPoint H35
U 1 1 5C489B99
P 8350 2700
F 0 "H35" H 8250 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 8450 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8350 2700 50  0001 C CNN
F 3 "~" H 8350 2700 50  0001 C CNN
	1    8350 2700
	1    0    0    -1  
$EndComp
Connection ~ 8350 2700
Wire Wire Line
	8350 2700 8550 2700
$Comp
L Connector:TestPoint H36
U 1 1 5C489C05
P 8750 2700
F 0 "H36" H 8650 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 8850 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8750 2700 50  0001 C CNN
F 3 "~" H 8750 2700 50  0001 C CNN
	1    8750 2700
	1    0    0    -1  
$EndComp
Connection ~ 8750 2700
$Comp
L Connector:TestPoint H2
U 1 1 5C495146
P 7050 1650
F 0 "H2" V 7050 1900 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 1655 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 1650 50  0001 C CNN
F 3 "~" H 7050 1650 50  0001 C CNN
	1    7050 1650
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H7
U 1 1 5C4951C4
P 7050 1950
F 0 "H7" V 7050 2200 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 1955 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 1950 50  0001 C CNN
F 3 "~" H 7050 1950 50  0001 C CNN
	1    7050 1950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7050 1950 7050 2250
$Comp
L Connector:TestPoint H22
U 1 1 5C495230
P 7050 2250
F 0 "H22" V 7050 2500 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 2255 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 2250 50  0001 C CNN
F 3 "~" H 7050 2250 50  0001 C CNN
	1    7050 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H27
U 1 1 5C49529C
P 7050 2550
F 0 "H27" V 7050 2800 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 2555 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 2550 50  0001 C CNN
F 3 "~" H 7050 2550 50  0001 C CNN
	1    7050 2550
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H26
U 1 1 5C495304
P 6000 2550
F 0 "H26" V 6000 2800 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 2555 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 2550 50  0001 C CNN
F 3 "~" H 6000 2550 50  0001 C CNN
	1    6000 2550
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H21
U 1 1 5C49537C
P 6000 2250
F 0 "H21" V 6000 2500 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 2255 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 2250 50  0001 C CNN
F 3 "~" H 6000 2250 50  0001 C CNN
	1    6000 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H6
U 1 1 5C4953F0
P 6000 1950
F 0 "H6" V 6000 2200 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 1955 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 1950 50  0001 C CNN
F 3 "~" H 6000 1950 50  0001 C CNN
	1    6000 1950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6000 1950 6000 2250
$Comp
L Connector:TestPoint H1
U 1 1 5C495462
P 6000 1650
F 0 "H1" V 6000 1900 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 1655 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 1650 50  0001 C CNN
F 3 "~" H 6000 1650 50  0001 C CNN
	1    6000 1650
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H13
U 1 1 5C487CA7
P 7250 2100
F 0 "H13" H 7150 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 7350 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7250 2100 50  0001 C CNN
F 3 "~" H 7250 2100 50  0001 C CNN
	1    7250 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 2100 7450 2100
$Comp
L Connector:TestPoint H14
U 1 1 5C487D31
P 7650 2100
F 0 "H14" H 7550 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 7750 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7650 2100 50  0001 C CNN
F 3 "~" H 7650 2100 50  0001 C CNN
	1    7650 2100
	1    0    0    -1  
$EndComp
Connection ~ 8550 2100
Connection ~ 8550 2700
Wire Wire Line
	6400 2100 6600 2100
Connection ~ 7250 2100
Wire Wire Line
	7450 2100 7650 2100
Connection ~ 7450 2100
Connection ~ 7650 2100
Wire Wire Line
	7650 2100 8350 2100
Wire Wire Line
	8750 2100 9400 2100
Connection ~ 9600 2100
Wire Wire Line
	9600 2100 9800 2100
Wire Wire Line
	8750 2700 9400 2700
Connection ~ 9600 2700
Wire Wire Line
	9600 2700 9800 2700
Wire Wire Line
	6400 2700 6600 2700
Connection ~ 7450 2700
Wire Wire Line
	7450 2700 7650 2700
Connection ~ 6400 2100
$Comp
L Connector:TestPoint H11
U 1 1 5C4A4E75
P 6200 2100
F 0 "H11" H 6100 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 6300 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6200 2100 50  0001 C CNN
F 3 "~" H 6200 2100 50  0001 C CNN
	1    6200 2100
	1    0    0    -1  
$EndComp
Connection ~ 6200 2100
Wire Wire Line
	6200 2100 6400 2100
$Comp
L Connector:TestPoint H31
U 1 1 5C4A4EF9
P 6200 2700
F 0 "H31" H 6100 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 6300 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6200 2700 50  0001 C CNN
F 3 "~" H 6200 2700 50  0001 C CNN
	1    6200 2700
	1    0    0    -1  
$EndComp
Connection ~ 6200 2700
Wire Wire Line
	6200 2700 6400 2700
$Comp
L Connector:TestPoint H32
U 1 1 5C4A4F7F
P 6600 2700
F 0 "H32" H 6500 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 6700 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6600 2700 50  0001 C CNN
F 3 "~" H 6600 2700 50  0001 C CNN
	1    6600 2700
	1    0    0    -1  
$EndComp
Connection ~ 6600 2700
Wire Wire Line
	6600 2700 7250 2700
$Comp
L Connector:TestPoint H12
U 1 1 5C4A5005
P 6600 2100
F 0 "H12" H 6500 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 6700 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6600 2100 50  0001 C CNN
F 3 "~" H 6600 2100 50  0001 C CNN
	1    6600 2100
	1    0    0    -1  
$EndComp
Connection ~ 6600 2100
Wire Wire Line
	6600 2100 7250 2100
$Comp
L Connector:TestPoint H34
U 1 1 5C4A7D52
P 7650 2700
F 0 "H34" H 7550 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 7750 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7650 2700 50  0001 C CNN
F 3 "~" H 7650 2700 50  0001 C CNN
	1    7650 2700
	1    0    0    -1  
$EndComp
Connection ~ 7650 2700
Wire Wire Line
	7650 2700 8350 2700
$Comp
L Connector:TestPoint H33
U 1 1 5C4A7DEA
P 7250 2700
F 0 "H33" H 7150 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 7350 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7250 2700 50  0001 C CNN
F 3 "~" H 7250 2700 50  0001 C CNN
	1    7250 2700
	1    0    0    -1  
$EndComp
Connection ~ 7250 2700
Wire Wire Line
	7250 2700 7450 2700
$Comp
L Connector:TestPoint H37
U 1 1 5C4A8698
P 9400 2700
F 0 "H37" H 9300 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 9500 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9400 2700 50  0001 C CNN
F 3 "~" H 9400 2700 50  0001 C CNN
	1    9400 2700
	1    0    0    -1  
$EndComp
Connection ~ 9400 2700
Wire Wire Line
	9400 2700 9600 2700
$Comp
L Connector:TestPoint H17
U 1 1 5C4A8722
P 9400 2100
F 0 "H17" H 9300 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 9500 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9400 2100 50  0001 C CNN
F 3 "~" H 9400 2100 50  0001 C CNN
	1    9400 2100
	1    0    0    -1  
$EndComp
Connection ~ 9400 2100
Wire Wire Line
	9400 2100 9600 2100
$Comp
L Connector:TestPoint H18
U 1 1 5C4A87BA
P 9800 2100
F 0 "H18" H 9700 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 9900 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9800 2100 50  0001 C CNN
F 3 "~" H 9800 2100 50  0001 C CNN
	1    9800 2100
	1    0    0    -1  
$EndComp
Connection ~ 9800 2100
Wire Wire Line
	9800 2100 10450 2100
$Comp
L Connector:TestPoint H38
U 1 1 5C4A8848
P 9800 2700
F 0 "H38" H 9700 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 9900 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9800 2700 50  0001 C CNN
F 3 "~" H 9800 2700 50  0001 C CNN
	1    9800 2700
	1    0    0    -1  
$EndComp
Connection ~ 9800 2700
$Comp
L Connector:TestPoint H19
U 1 1 5C4A900B
P 10450 2100
F 0 "H19" H 10350 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 10550 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10450 2100 50  0001 C CNN
F 3 "~" H 10450 2100 50  0001 C CNN
	1    10450 2100
	1    0    0    -1  
$EndComp
Connection ~ 10450 2100
Wire Wire Line
	10450 2100 10650 2100
$Comp
L Connector:TestPoint H39
U 1 1 5C4A90A3
P 6200 3900
F 0 "H39" H 6100 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 6300 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6200 3900 50  0001 C CNN
F 3 "~" H 6200 3900 50  0001 C CNN
	1    6200 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H40
U 1 1 5C4A913B
P 6600 3900
F 0 "H40" H 6500 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 6700 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6600 3900 50  0001 C CNN
F 3 "~" H 6600 3900 50  0001 C CNN
	1    6600 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H20
U 1 1 5C4A91D1
P 10850 2100
F 0 "H20" H 10750 2300 50  0000 L CNN
F 1 "MountingHole_Pad" H 10950 2060 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10850 2100 50  0001 C CNN
F 3 "~" H 10850 2100 50  0001 C CNN
	1    10850 2100
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H4
U 1 1 5C4A98DB
P 9200 1650
F 0 "H4" V 9200 1900 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 1655 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 1650 50  0001 C CNN
F 3 "~" H 9200 1650 50  0001 C CNN
	1    9200 1650
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H9
U 1 1 5C4A9981
P 9200 1950
F 0 "H9" V 9200 2200 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 1955 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 1950 50  0001 C CNN
F 3 "~" H 9200 1950 50  0001 C CNN
	1    9200 1950
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9200 1950 9200 2250
$Comp
L Connector:TestPoint H24
U 1 1 5C4A9A19
P 9200 2250
F 0 "H24" V 9200 2500 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 2255 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 2250 50  0001 C CNN
F 3 "~" H 9200 2250 50  0001 C CNN
	1    9200 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H29
U 1 1 5C4A9AB1
P 9200 2550
F 0 "H29" V 9200 2800 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 2555 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 2550 50  0001 C CNN
F 3 "~" H 9200 2550 50  0001 C CNN
	1    9200 2550
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H5
U 1 1 5C4A9F79
P 10250 1650
F 0 "H5" V 10250 1900 50  0000 C CNN
F 1 "MountingHole_Pad" V 10396 1655 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 10250 1650 50  0001 C CNN
F 3 "~" H 10250 1650 50  0001 C CNN
	1    10250 1650
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H10
U 1 1 5C4AA027
P 10250 1950
F 0 "H10" V 10250 2200 50  0000 C CNN
F 1 "MountingHole_Pad" V 10396 1955 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 10250 1950 50  0001 C CNN
F 3 "~" H 10250 1950 50  0001 C CNN
	1    10250 1950
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H25
U 1 1 5C4AA0C7
P 6000 3450
F 0 "H25" V 6000 3700 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 3455 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 3450 50  0001 C CNN
F 3 "~" H 6000 3450 50  0001 C CNN
	1    6000 3450
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H30
U 1 1 5C4AA169
P 6000 3750
F 0 "H30" V 6000 4000 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 3755 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 3750 50  0001 C CNN
F 3 "~" H 6000 3750 50  0001 C CNN
	1    6000 3750
	0    -1   -1   0   
$EndComp
Wire Wire Line
	10650 2100 10850 2100
Connection ~ 10650 2100
Connection ~ 8150 1950
Connection ~ 7050 1950
Connection ~ 6000 1950
Connection ~ 9200 1950
$Comp
L Device:D D16
U 1 1 5C71DC1E
P 10650 2550
F 0 "D16" H 10650 2650 50  0000 C CNN
F 1 "D" H 10650 2450 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 10650 2550 50  0001 C CNN
F 3 "" H 10650 2550 50  0001 C CNN
	1    10650 2550
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D17
U 1 1 5C71DC2A
P 9600 3750
F 0 "D17" H 9600 3850 50  0000 C CNN
F 1 "D" H 9600 3650 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 9600 3750 50  0001 C CNN
F 3 "" H 9600 3750 50  0001 C CNN
	1    9600 3750
	0    -1   -1   0   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW16
U 1 1 5C71DC44
P 9400 3500
F 0 "SW16" H 9400 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 3694 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 9400 3700 50  0001 C CNN
F 3 "" H 9400 3700 50  0001 C CNN
	1    9400 3500
	-1   0    0    -1  
$EndComp
Text GLabel 5600 3900 0    39   Input ~ 0
Y4
Wire Wire Line
	6000 2550 6000 2850
$Comp
L Connector:TestPoint H41
U 1 1 5C71DC7E
P 10250 2250
F 0 "H41" V 10250 2500 50  0000 C CNN
F 1 "MountingHole_Pad" V 10396 2255 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 10250 2250 50  0001 C CNN
F 3 "~" H 10250 2250 50  0001 C CNN
	1    10250 2250
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H43
U 1 1 5C71DC86
P 10250 2550
F 0 "H43" V 10250 2800 50  0000 C CNN
F 1 "MountingHole_Pad" V 10396 2555 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 10250 2550 50  0001 C CNN
F 3 "~" H 10250 2550 50  0001 C CNN
	1    10250 2550
	0    -1   -1   0   
$EndComp
Connection ~ 9600 3900
Wire Wire Line
	9600 3900 9800 3900
$Comp
L Connector:TestPoint H46
U 1 1 5C71DCB6
P 10850 2700
F 0 "H46" H 10750 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 10950 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10850 2700 50  0001 C CNN
F 3 "~" H 10850 2700 50  0001 C CNN
	1    10850 2700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H45
U 1 1 5C71DCBE
P 10350 2700
F 0 "H45" H 10250 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 10450 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10350 2700 50  0001 C CNN
F 3 "~" H 10350 2700 50  0001 C CNN
	1    10350 2700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H47
U 1 1 5C71DCC6
P 9400 3900
F 0 "H47" H 9300 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 9500 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9400 3900 50  0001 C CNN
F 3 "~" H 9400 3900 50  0001 C CNN
	1    9400 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 3900 9600 3900
$Comp
L Connector:TestPoint H48
U 1 1 5C71DCCE
P 9800 3900
F 0 "H48" H 9700 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 9900 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9800 3900 50  0001 C CNN
F 3 "~" H 9800 3900 50  0001 C CNN
	1    9800 3900
	1    0    0    -1  
$EndComp
Wire Wire Line
	9200 2550 9200 2850
$Comp
L Connector:TestPoint H42
U 1 1 5C71DCE5
P 9200 3450
F 0 "H42" V 9200 3700 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 3455 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 3450 50  0001 C CNN
F 3 "~" H 9200 3450 50  0001 C CNN
	1    9200 3450
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H44
U 1 1 5C71DCED
P 9200 3750
F 0 "H44" V 9200 4000 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 3755 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 3750 50  0001 C CNN
F 3 "~" H 9200 3750 50  0001 C CNN
	1    9200 3750
	0    -1   -1   0   
$EndComp
Connection ~ 9200 2550
Connection ~ 6000 2550
$Comp
L #library:MJ-4PP-9 J1
U 1 1 5CE190C3
P 1050 4300
F 0 "J1" H 1080 4718 50  0000 C CNN
F 1 "MJ-4PP-9" H 1080 4627 50  0000 C CNN
F 2 "#footprint:MJ-4PP-9" H 1325 4475 50  0001 C CNN
F 3 "" H 1325 4475 50  0001 C CNN
	1    1050 4300
	1    0    0    -1  
$EndComp
Text GLabel 1800 750  1    50   Input ~ 0
led
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
P 5500 4750
F 0 "SW22" H 5500 5035 50  0000 C CNN
F 1 "SW_Push" H 5500 4944 50  0000 C CNN
F 2 "#footprint:ResetSW" H 5500 4950 50  0001 C CNN
F 3 "" H 5500 4950 50  0001 C CNN
	1    5500 4750
	1    0    0    -1  
$EndComp
Text GLabel 5300 4750 0    50   Input ~ 0
reset1
$Comp
L Connector_Generic:Conn_01x03 J2
U 1 1 5CE3FF01
P 3200 4250
F 0 "J2" H 3280 4292 50  0000 L CNN
F 1 "Conn_01x03" H 3280 4201 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 3200 4250 50  0001 C CNN
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
Text GLabel 3800 4250 2    50   Input ~ 0
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
Connection ~ 6000 2250
Connection ~ 7050 2250
Connection ~ 8150 2250
Connection ~ 9200 2250
$Comp
L Device:D D11
U 1 1 5CE4CCBF
P 6400 3150
F 0 "D11" H 6400 3250 50  0000 C CNN
F 1 "D" H 6400 3050 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 6400 3150 50  0001 C CNN
F 3 "" H 6400 3150 50  0001 C CNN
	1    6400 3150
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D12
U 1 1 5CE4CCC5
P 7450 3150
F 0 "D12" H 7450 3250 50  0000 C CNN
F 1 "D" H 7450 3050 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 7450 3150 50  0001 C CNN
F 3 "" H 7450 3150 50  0001 C CNN
	1    7450 3150
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D13
U 1 1 5CE4CCCB
P 8550 3150
F 0 "D13" H 8550 3250 50  0000 C CNN
F 1 "D" H 8550 3050 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 8550 3150 50  0001 C CNN
F 3 "" H 8550 3150 50  0001 C CNN
	1    8550 3150
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D14
U 1 1 5CE4CCD1
P 9600 3150
F 0 "D14" H 9600 3250 50  0000 C CNN
F 1 "D" H 9600 3050 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 9600 3150 50  0001 C CNN
F 3 "" H 9600 3150 50  0001 C CNN
	1    9600 3150
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8550 3300 8750 3300
$Comp
L Sofle:SW_PUSH_LED SW3
U 1 1 5CE4CCD8
P 6200 2900
F 0 "SW3" H 6200 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 6200 3094 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 6200 3100 50  0001 C CNN
F 3 "" H 6200 3100 50  0001 C CNN
	1    6200 2900
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW7
U 1 1 5CE4CCDE
P 7250 2900
F 0 "SW7" H 7250 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 3094 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 7250 3100 50  0001 C CNN
F 3 "" H 7250 3100 50  0001 C CNN
	1    7250 2900
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW11
U 1 1 5CE4CCE4
P 8350 2900
F 0 "SW11" H 8350 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 3094 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 8350 3100 50  0001 C CNN
F 3 "" H 8350 3100 50  0001 C CNN
	1    8350 2900
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW15
U 1 1 5CE4CCEA
P 9400 2900
F 0 "SW15" H 9400 3050 50  0000 C CNN
F 1 "SW_PUSH_LED" H 9400 3094 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 9400 3100 50  0001 C CNN
F 3 "" H 9400 3100 50  0001 C CNN
	1    9400 2900
	-1   0    0    -1  
$EndComp
$Comp
L Device:D D15
U 1 1 5CE4CCF0
P 7450 3750
F 0 "D15" H 7450 3850 50  0000 C CNN
F 1 "D" H 7450 3650 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 7450 3750 50  0001 C CNN
F 3 "" H 7450 3750 50  0001 C CNN
	1    7450 3750
	0    -1   -1   0   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW8
U 1 1 5CE4CCF6
P 7250 3500
F 0 "SW8" H 7250 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 7250 3694 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 7250 3700 50  0001 C CNN
F 3 "" H 7250 3700 50  0001 C CNN
	1    7250 3500
	-1   0    0    -1  
$EndComp
Text GLabel 5600 3300 0    39   Input ~ 0
Y3
Connection ~ 6000 3000
Wire Wire Line
	6000 3000 6000 3150
$Comp
L Connector:TestPoint H115
U 1 1 5CE4CD00
P 8150 2850
F 0 "H115" V 8150 3150 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 2855 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 2850 50  0001 C CNN
F 3 "~" H 8150 2850 50  0001 C CNN
	1    8150 2850
	0    -1   -1   0   
$EndComp
Connection ~ 6400 3300
Wire Wire Line
	8150 2550 8150 2850
$Comp
L Connector:TestPoint H120
U 1 1 5CE4CD09
P 8150 3150
F 0 "H120" V 8150 3450 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 3155 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 3150 50  0001 C CNN
F 3 "~" H 8150 3150 50  0001 C CNN
	1    8150 3150
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H127
U 1 1 5CE4CD11
P 8350 3300
F 0 "H127" H 8250 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 8450 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8350 3300 50  0001 C CNN
F 3 "~" H 8350 3300 50  0001 C CNN
	1    8350 3300
	1    0    0    -1  
$EndComp
Connection ~ 8350 3300
Wire Wire Line
	8350 3300 8550 3300
$Comp
L Connector:TestPoint H128
U 1 1 5CE4CD19
P 8750 3300
F 0 "H128" H 8650 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 8850 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8750 3300 50  0001 C CNN
F 3 "~" H 8750 3300 50  0001 C CNN
	1    8750 3300
	1    0    0    -1  
$EndComp
Connection ~ 8750 3300
Wire Wire Line
	7050 2550 7050 2850
$Comp
L Connector:TestPoint H114
U 1 1 5CE4CD21
P 7050 2850
F 0 "H114" V 7050 3150 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 2855 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 2850 50  0001 C CNN
F 3 "~" H 7050 2850 50  0001 C CNN
	1    7050 2850
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H119
U 1 1 5CE4CD28
P 7050 3150
F 0 "H119" V 7050 3450 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 3155 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 3150 50  0001 C CNN
F 3 "~" H 7050 3150 50  0001 C CNN
	1    7050 3150
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H118
U 1 1 5CE4CD2E
P 6000 3150
F 0 "H118" V 6000 3450 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 3155 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 3150 50  0001 C CNN
F 3 "~" H 6000 3150 50  0001 C CNN
	1    6000 3150
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H113
U 1 1 5CE4CD34
P 6000 2850
F 0 "H113" V 6000 3150 50  0000 C CNN
F 1 "MountingHole_Pad" V 6146 2855 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6000 2850 50  0001 C CNN
F 3 "~" H 6000 2850 50  0001 C CNN
	1    6000 2850
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6000 2850 6000 3000
Connection ~ 8550 3300
Wire Wire Line
	8750 3300 9400 3300
Connection ~ 9600 3300
Wire Wire Line
	9600 3300 9800 3300
Wire Wire Line
	6400 3300 6600 3300
Connection ~ 7450 3300
Wire Wire Line
	7450 3300 7650 3300
$Comp
L Connector:TestPoint H123
U 1 1 5CE4CD46
P 6200 3300
F 0 "H123" H 6100 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 6300 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6200 3300 50  0001 C CNN
F 3 "~" H 6200 3300 50  0001 C CNN
	1    6200 3300
	1    0    0    -1  
$EndComp
Connection ~ 6200 3300
Wire Wire Line
	6200 3300 6400 3300
$Comp
L Connector:TestPoint H124
U 1 1 5CE4CD4E
P 6600 3300
F 0 "H124" H 6500 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 6700 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 6600 3300 50  0001 C CNN
F 3 "~" H 6600 3300 50  0001 C CNN
	1    6600 3300
	1    0    0    -1  
$EndComp
Connection ~ 6600 3300
Wire Wire Line
	6600 3300 7250 3300
$Comp
L Connector:TestPoint H126
U 1 1 5CE4CD57
P 7650 3300
F 0 "H126" H 7550 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 7750 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7650 3300 50  0001 C CNN
F 3 "~" H 7650 3300 50  0001 C CNN
	1    7650 3300
	1    0    0    -1  
$EndComp
Connection ~ 7650 3300
Wire Wire Line
	7650 3300 8350 3300
$Comp
L Connector:TestPoint H125
U 1 1 5CE4CD5F
P 7250 3300
F 0 "H125" H 7150 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 7350 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7250 3300 50  0001 C CNN
F 3 "~" H 7250 3300 50  0001 C CNN
	1    7250 3300
	1    0    0    -1  
$EndComp
Connection ~ 7250 3300
Wire Wire Line
	7250 3300 7450 3300
$Comp
L Connector:TestPoint H129
U 1 1 5CE4CD67
P 9400 3300
F 0 "H129" H 9300 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 9500 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9400 3300 50  0001 C CNN
F 3 "~" H 9400 3300 50  0001 C CNN
	1    9400 3300
	1    0    0    -1  
$EndComp
Connection ~ 9400 3300
Wire Wire Line
	9400 3300 9600 3300
$Comp
L Connector:TestPoint H130
U 1 1 5CE4CD6F
P 9800 3300
F 0 "H130" H 9700 3500 50  0000 L CNN
F 1 "MountingHole_Pad" H 9900 3260 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9800 3300 50  0001 C CNN
F 3 "~" H 9800 3300 50  0001 C CNN
	1    9800 3300
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H131
U 1 1 5CE4CD77
P 7250 3900
F 0 "H131" H 7150 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 7350 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7250 3900 50  0001 C CNN
F 3 "~" H 7250 3900 50  0001 C CNN
	1    7250 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H132
U 1 1 5CE4CD7F
P 7650 3900
F 0 "H132" H 7550 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 7750 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 7650 3900 50  0001 C CNN
F 3 "~" H 7650 3900 50  0001 C CNN
	1    7650 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H116
U 1 1 5CE4CD86
P 9200 2850
F 0 "H116" V 9200 3150 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 2855 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 2850 50  0001 C CNN
F 3 "~" H 9200 2850 50  0001 C CNN
	1    9200 2850
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H121
U 1 1 5CE4CD8D
P 9200 3150
F 0 "H121" V 9200 3450 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 3155 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 3150 50  0001 C CNN
F 3 "~" H 9200 3150 50  0001 C CNN
	1    9200 3150
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H117
U 1 1 5CE4CD94
P 7050 3450
F 0 "H117" V 7050 3750 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 3455 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 3450 50  0001 C CNN
F 3 "~" H 7050 3450 50  0001 C CNN
	1    7050 3450
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H122
U 1 1 5CE4CD9B
P 7050 3750
F 0 "H122" V 7050 4050 50  0000 C CNN
F 1 "MountingHole_Pad" V 7196 3755 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7050 3750 50  0001 C CNN
F 3 "~" H 7050 3750 50  0001 C CNN
	1    7050 3750
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9200 3150 9200 3450
Connection ~ 9200 3150
Connection ~ 6000 2850
Connection ~ 7050 2850
Connection ~ 8150 2850
Connection ~ 9200 2850
Connection ~ 7050 2550
Connection ~ 8150 2550
Connection ~ 9200 3450
$Comp
L Device:D D18
U 1 1 5CE5B1E1
P 9600 5350
F 0 "D18" H 9600 5450 50  0000 C CNN
F 1 "D" H 9600 5250 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 9600 5350 50  0001 C CNN
F 3 "" H 9600 5350 50  0001 C CNN
	1    9600 5350
	0    -1   -1   0   
$EndComp
$Comp
L Device:D D19
U 1 1 5CE5B200
P 10650 5350
F 0 "D19" H 10650 5450 50  0000 C CNN
F 1 "D" H 10650 5250 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 10650 5350 50  0001 C CNN
F 3 "" H 10650 5350 50  0001 C CNN
	1    10650 5350
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
Text GLabel 9200 4800 1    39   Input ~ 0
X4
Text GLabel 10250 4800 1    39   Input ~ 0
X5
Connection ~ 9600 5500
Wire Wire Line
	9600 5500 9800 5500
$Comp
L Connector:TestPoint H137
U 1 1 5CE5B292
P 9400 5500
F 0 "H137" H 9300 5700 50  0000 L CNN
F 1 "MountingHole_Pad" H 9500 5460 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9400 5500 50  0001 C CNN
F 3 "~" H 9400 5500 50  0001 C CNN
	1    9400 5500
	1    0    0    -1  
$EndComp
Connection ~ 9400 5500
Wire Wire Line
	9400 5500 9600 5500
$Comp
L Connector:TestPoint H138
U 1 1 5CE5B29A
P 9800 5500
F 0 "H138" H 9700 5700 50  0000 L CNN
F 1 "MountingHole_Pad" H 9900 5460 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9800 5500 50  0001 C CNN
F 3 "~" H 9800 5500 50  0001 C CNN
	1    9800 5500
	1    0    0    -1  
$EndComp
Connection ~ 9800 5500
Wire Wire Line
	9800 5500 10450 5500
$Comp
L Connector:TestPoint H139
U 1 1 5CE5B2A2
P 10450 5500
F 0 "H139" H 10350 5700 50  0000 L CNN
F 1 "MountingHole_Pad" H 10550 5460 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10450 5500 50  0001 C CNN
F 3 "~" H 10450 5500 50  0001 C CNN
	1    10450 5500
	1    0    0    -1  
$EndComp
Connection ~ 10450 5500
Wire Wire Line
	10450 5500 10650 5500
$Comp
L Connector:TestPoint H140
U 1 1 5CE5B2AA
P 10850 5500
F 0 "H140" H 10750 5700 50  0000 L CNN
F 1 "MountingHole_Pad" H 10950 5460 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10850 5500 50  0001 C CNN
F 3 "~" H 10850 5500 50  0001 C CNN
	1    10850 5500
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H133
U 1 1 5CE5B2B0
P 9200 5050
F 0 "H133" V 9200 5350 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 5055 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 5050 50  0001 C CNN
F 3 "~" H 9200 5050 50  0001 C CNN
	1    9200 5050
	0    -1   -1   0   
$EndComp
Connection ~ 9200 5050
$Comp
L Connector:TestPoint H135
U 1 1 5CE5B2B8
P 9200 5350
F 0 "H135" V 9200 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 5355 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 5350 50  0001 C CNN
F 3 "~" H 9200 5350 50  0001 C CNN
	1    9200 5350
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H134
U 1 1 5CE5B2BF
P 10250 5050
F 0 "H134" V 10250 5350 50  0000 C CNN
F 1 "MountingHole_Pad" V 10396 5055 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 10250 5050 50  0001 C CNN
F 3 "~" H 10250 5050 50  0001 C CNN
	1    10250 5050
	0    -1   -1   0   
$EndComp
Connection ~ 10250 5050
$Comp
L Connector:TestPoint H136
U 1 1 5CE5B2C7
P 10250 5350
F 0 "H136" V 10250 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 10396 5355 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 10250 5350 50  0001 C CNN
F 3 "~" H 10250 5350 50  0001 C CNN
	1    10250 5350
	0    -1   -1   0   
$EndComp
Wire Wire Line
	10650 5500 10850 5500
Connection ~ 10650 5500
Connection ~ 6000 1650
Connection ~ 7050 1650
Connection ~ 8150 1650
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
F 2 "#footprint:PinHeader_1x08_P2.54mm_Vertical_rev2" H 3900 3250 50  0001 C CNN
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
F 2 "#footprint:PinHeader_1x08_P2.54mm_Vertical_rev2" H 1750 3250 50  0001 C CNN
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
F 2 "#footprint:MJ-4PP-9" H 2325 4475 50  0001 C CNN
F 3 "" H 2325 4475 50  0001 C CNN
	1    2050 4300
	1    0    0    -1  
$EndComp
NoConn ~ 2250 4100
Connection ~ 9400 3900
$Comp
L Device:D D20
U 1 1 5D04CD16
P 8550 3750
F 0 "D20" H 8550 3850 50  0000 C CNN
F 1 "D" H 8550 3650 50  0001 C CNN
F 2 "#footprint:diode_TH_SMD_rev2" H 8550 3750 50  0001 C CNN
F 3 "" H 8550 3750 50  0001 C CNN
	1    8550 3750
	0    -1   -1   0   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW12
U 1 1 5D04CD1C
P 8350 3500
F 0 "SW12" H 8350 3650 50  0000 C CNN
F 1 "SW_PUSH_LED" H 8350 3694 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 8350 3700 50  0001 C CNN
F 3 "" H 8350 3700 50  0001 C CNN
	1    8350 3500
	-1   0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H212
U 1 1 5D04CD24
P 8350 3900
F 0 "H212" H 8250 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 8450 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8350 3900 50  0001 C CNN
F 3 "~" H 8350 3900 50  0001 C CNN
	1    8350 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H213
U 1 1 5D04CD2B
P 8750 3900
F 0 "H213" H 8650 4100 50  0000 L CNN
F 1 "MountingHole_Pad" H 8850 3860 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 8750 3900 50  0001 C CNN
F 3 "~" H 8750 3900 50  0001 C CNN
	1    8750 3900
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H210
U 1 1 5D04CD31
P 8150 3450
F 0 "H210" V 8150 3750 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 3455 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 3450 50  0001 C CNN
F 3 "~" H 8150 3450 50  0001 C CNN
	1    8150 3450
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H211
U 1 1 5D04CD38
P 8150 3750
F 0 "H211" V 8150 4050 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 3755 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 3750 50  0001 C CNN
F 3 "~" H 8150 3750 50  0001 C CNN
	1    8150 3750
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5600 3900 6200 3900
Wire Wire Line
	5600 3300 6200 3300
Wire Wire Line
	5600 2700 6200 2700
Wire Wire Line
	5600 2100 6200 2100
Wire Wire Line
	5600 5500 9400 5500
Wire Wire Line
	10250 4800 10250 5050
Wire Wire Line
	9200 4800 9200 5050
Wire Wire Line
	8150 800  8150 1650
Wire Wire Line
	7050 800  7050 1650
Wire Wire Line
	6000 800  6000 1650
$Comp
L Connector:TestPoint H50
U 1 1 5D363A98
P 10750 2700
F 0 "H50" H 10650 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 10850 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10750 2700 50  0001 C CNN
F 3 "~" H 10750 2700 50  0001 C CNN
	1    10750 2700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H49
U 1 1 5D363BD2
P 10450 2700
F 0 "H49" H 10350 2900 50  0000 L CNN
F 1 "MountingHole_Pad" H 10550 2660 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10450 2700 50  0001 C CNN
F 3 "~" H 10450 2700 50  0001 C CNN
	1    10450 2700
	1    0    0    -1  
$EndComp
Wire Wire Line
	9200 5050 9200 5200
Wire Wire Line
	10250 5050 10250 5200
$Comp
L Device:Rotary_Encoder_Switch SW20
U 1 1 5D659111
P 9500 4900
F 0 "SW20" V 9454 4670 50  0000 R CNN
F 1 "Rotary_Encoder_Switch" V 9545 4670 50  0001 R CNN
F 2 "#footprint:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_rev2" H 9350 5060 50  0001 C CNN
F 3 "~" H 9500 5160 50  0001 C CNN
	1    9500 4900
	0    -1   1    0   
$EndComp
$Comp
L Device:Rotary_Encoder_Switch SW21
U 1 1 5D6595AB
P 10550 4900
F 0 "SW21" V 10504 4670 50  0000 R CNN
F 1 "Rotary_Encoder_Switch" V 10595 4670 50  0001 R CNN
F 2 "#footprint:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm_rev2" H 10400 5060 50  0001 C CNN
F 3 "~" H 10550 5160 50  0001 C CNN
	1    10550 4900
	0    -1   1    0   
$EndComp
Wire Wire Line
	9400 5200 9200 5200
Connection ~ 9200 5200
Wire Wire Line
	9200 5200 9200 5350
Wire Wire Line
	10450 5200 10250 5200
Connection ~ 10250 5200
Wire Wire Line
	10250 5200 10250 5350
Text GLabel 9500 4150 1    50   Input ~ 0
GND
Text GLabel 10550 4150 1    50   Input ~ 0
GND
Text GLabel 9200 800  1    39   Input ~ 0
X4
Text GLabel 10250 800  1    39   Input ~ 0
X5
Wire Wire Line
	10250 800  10250 1650
Connection ~ 10250 1650
Wire Wire Line
	9200 800  9200 1650
Connection ~ 9200 1650
Text GLabel 10700 4350 2    50   Input ~ 0
X7
Text GLabel 10450 4300 1    50   Input ~ 0
X8
$Comp
L Mechanical:MountingHole_Pad H57
U 1 1 5E0F561B
P 900 2150
F 0 "H57" H 900 2350 50  0000 C CNN
F 1 "MountingHole_Pad" V 1046 2155 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 900 2150 50  0001 C CNN
F 3 "~" H 900 2150 50  0001 C CNN
	1    900  2150
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J8
U 1 1 5E124F08
P 10050 4450
F 0 "J8" H 10100 4867 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 10100 4776 50  0001 C CNN
F 2 "#footprint:IDC-Header_2x05_P2.54mm_Vertical" H 10050 4450 50  0001 C CNN
F 3 "~" H 10050 4450 50  0001 C CNN
	1    10050 4450
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J7
U 1 1 5E113B23
P 9000 4450
F 0 "J7" H 9050 4867 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 9050 4776 50  0001 C CNN
F 2 "#footprint:IDC-Header_2x05_P2.54mm_Vertical" H 9000 4450 50  0001 C CNN
F 3 "~" H 9000 4450 50  0001 C CNN
	1    9000 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 4300 9400 4550
Wire Wire Line
	9500 4150 9500 4250
Wire Wire Line
	10450 4300 10450 4550
Wire Wire Line
	10550 4150 10550 4250
Wire Wire Line
	9300 4350 9600 4350
Wire Wire Line
	9600 4350 9600 4600
Wire Wire Line
	9300 4450 9500 4450
Connection ~ 9500 4450
Wire Wire Line
	9500 4450 9500 4600
Wire Wire Line
	9300 4550 9400 4550
Connection ~ 9400 4550
Wire Wire Line
	9400 4550 9400 4600
Wire Wire Line
	10350 4350 10650 4350
Connection ~ 10650 4350
Wire Wire Line
	10650 4350 10650 4600
Wire Wire Line
	10350 4450 10550 4450
Connection ~ 10550 4450
Wire Wire Line
	10550 4450 10550 4600
Wire Wire Line
	10350 4550 10450 4550
Connection ~ 10450 4550
Wire Wire Line
	10450 4550 10450 4600
Wire Wire Line
	6000 1650 6000 1800
Wire Wire Line
	6300 1800 6400 1800
Wire Wire Line
	6100 1800 6000 1800
Connection ~ 6000 1800
Wire Wire Line
	6000 1800 6000 1950
$Comp
L power:VDD #PWR0105
U 1 1 61694F35
P 4400 4150
F 0 "#PWR0105" H 4400 4000 50  0001 C CNN
F 1 "VDD" H 4415 4323 50  0000 C CNN
F 2 "" H 4400 4150 50  0001 C CNN
F 3 "" H 4400 4150 50  0001 C CNN
	1    4400 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 4250 4300 4250
Wire Wire Line
	4400 4250 4400 4150
Connection ~ 4150 4250
Wire Wire Line
	4150 4250 4150 4300
Wire Wire Line
	6000 2250 6000 2400
Wire Wire Line
	6300 2400 6400 2400
Wire Wire Line
	6100 2400 6000 2400
Connection ~ 6000 2400
Wire Wire Line
	6000 2400 6000 2550
$Comp
L Sofle:SW_PUSH_LED SW2
U 2 1 616DEF13
P 1300 6100
F 0 "SW2" H 1300 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 6303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1330 6300 50  0001 C CNN
F 3 "" H 1300 6200 50  0001 C CNN
	2    1300 6100
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW1
U 2 1 61623882
P 1300 5600
F 0 "SW1" H 1300 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 5803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1330 5800 50  0001 C CNN
F 3 "" H 1300 5700 50  0001 C CNN
	2    1300 5600
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1500 5850 1100 5850
Wire Wire Line
	1100 5850 1100 5900
Wire Wire Line
	6100 3000 6000 3000
Wire Wire Line
	6300 3000 6400 3000
$Comp
L Sofle:SW_PUSH_LED SW3
U 2 1 6174F456
P 1300 6600
F 0 "SW3" H 1300 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 6803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1330 6800 50  0001 C CNN
F 3 "" H 1300 6700 50  0001 C CNN
	2    1300 6600
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1500 6200 1500 6300
Wire Wire Line
	1500 6350 1100 6350
Wire Wire Line
	1100 6350 1100 6400
Wire Wire Line
	7050 1650 7050 1800
Wire Wire Line
	7050 2250 7050 2400
Wire Wire Line
	7050 2850 7050 3000
Wire Wire Line
	7350 3000 7450 3000
Wire Wire Line
	7150 3000 7050 3000
Connection ~ 7050 3000
Wire Wire Line
	7050 3000 7050 3150
Wire Wire Line
	7150 2400 7050 2400
Connection ~ 7050 2400
Wire Wire Line
	7050 2400 7050 2550
Wire Wire Line
	7350 2400 7450 2400
Wire Wire Line
	7350 1800 7450 1800
Wire Wire Line
	7150 1800 7050 1800
Connection ~ 7050 1800
Wire Wire Line
	7050 1800 7050 1950
Wire Wire Line
	1500 6700 1500 6800
Wire Wire Line
	1500 5700 1500 5800
Wire Wire Line
	1700 6850 1700 6800
Wire Wire Line
	2100 6850 1700 6850
Wire Wire Line
	4000 6200 4000 6300
Wire Wire Line
	1700 5850 1700 5800
Wire Wire Line
	2100 5850 1700 5850
Wire Wire Line
	2100 6000 2100 5900
Wire Wire Line
	1700 6350 1700 6300
Wire Wire Line
	2100 6350 1700 6350
Wire Wire Line
	2100 6500 2100 6400
$Comp
L Sofle:SW_PUSH_LED SW7
U 2 1 617FB0D7
P 1900 6600
F 0 "SW7" H 1900 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 6803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1930 6800 50  0001 C CNN
F 3 "" H 1900 6700 50  0001 C CNN
	2    1900 6600
	-1   0    0    1   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW6
U 2 1 617FAB8F
P 1900 6100
F 0 "SW6" H 1900 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 6303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1930 6300 50  0001 C CNN
F 3 "" H 1900 6200 50  0001 C CNN
	2    1900 6100
	-1   0    0    1   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW5
U 2 1 617EE3B8
P 1900 5600
F 0 "SW5" H 1900 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 5803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1930 5800 50  0001 C CNN
F 3 "" H 1900 5700 50  0001 C CNN
	2    1900 5600
	-1   0    0    1   
$EndComp
Connection ~ 1500 5800
Wire Wire Line
	1500 5800 1500 5850
$Comp
L Connector:TestPoint H53
U 1 1 618C9AF1
P 1100 5900
F 0 "H53" V 1100 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 5900 50  0001 C CNN
F 3 "~" H 1100 5900 50  0001 C CNN
	1    1100 5900
	0    1    1    0   
$EndComp
Connection ~ 1100 5900
Wire Wire Line
	1100 5900 1100 6000
$Comp
L Connector:TestPoint H59
U 1 1 618B212E
P 1500 5800
F 0 "H59" V 1500 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 5800 50  0001 C CNN
F 3 "~" H 1500 5800 50  0001 C CNN
	1    1500 5800
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H61
U 1 1 618D8964
P 1500 6300
F 0 "H61" V 1500 6550 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 6305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 6300 50  0001 C CNN
F 3 "~" H 1500 6300 50  0001 C CNN
	1    1500 6300
	0    -1   -1   0   
$EndComp
Connection ~ 1500 6300
Wire Wire Line
	1500 6300 1500 6350
$Comp
L Connector:TestPoint H63
U 1 1 618D8B7D
P 1500 6800
F 0 "H63" V 1500 7050 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 6805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 6800 50  0001 C CNN
F 3 "~" H 1500 6800 50  0001 C CNN
	1    1500 6800
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H55
U 1 1 618D9214
P 1100 6400
F 0 "H55" V 1100 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 6405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 6400 50  0001 C CNN
F 3 "~" H 1100 6400 50  0001 C CNN
	1    1100 6400
	0    1    1    0   
$EndComp
Connection ~ 1100 6400
Wire Wire Line
	1100 6400 1100 6500
$Comp
L Connector:TestPoint H51
U 1 1 618D958F
P 1100 5400
F 0 "H51" V 1100 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 5405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 5400 50  0001 C CNN
F 3 "~" H 1100 5400 50  0001 C CNN
	1    1100 5400
	0    1    1    0   
$EndComp
Wire Wire Line
	1100 5400 1100 5500
$Comp
L Connector:TestPoint H69
U 1 1 618E8C84
P 1700 6800
F 0 "H69" V 1700 7050 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 6805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 6800 50  0001 C CNN
F 3 "~" H 1700 6800 50  0001 C CNN
	1    1700 6800
	0    1    1    0   
$EndComp
Connection ~ 1700 6800
Wire Wire Line
	1700 6800 1700 6700
$Comp
L Connector:TestPoint H71
U 1 1 618E8F32
P 3600 5900
F 0 "H71" V 3600 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 3746 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3600 5900 50  0001 C CNN
F 3 "~" H 3600 5900 50  0001 C CNN
	1    3600 5900
	0    1    -1   0   
$EndComp
$Comp
L Connector:TestPoint H67
U 1 1 618E9233
P 1700 6300
F 0 "H67" V 1700 6550 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 6305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 6300 50  0001 C CNN
F 3 "~" H 1700 6300 50  0001 C CNN
	1    1700 6300
	0    1    1    0   
$EndComp
Connection ~ 1700 6300
Wire Wire Line
	1700 6300 1700 6200
$Comp
L Connector:TestPoint H65
U 1 1 618E945A
P 1700 5800
F 0 "H65" V 1700 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 5800 50  0001 C CNN
F 3 "~" H 1700 5800 50  0001 C CNN
	1    1700 5800
	0    1    1    0   
$EndComp
Connection ~ 1700 5800
Wire Wire Line
	1700 5800 1700 5700
$Comp
L Connector:TestPoint H78
U 1 1 618E978B
P 4000 6300
F 0 "H78" V 4000 6550 50  0000 C CNN
F 1 "MountingHole_Pad" V 4146 6305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 4000 6300 50  0001 C CNN
F 3 "~" H 4000 6300 50  0001 C CNN
	1    4000 6300
	0    -1   1    0   
$EndComp
$Comp
L Connector:TestPoint H76
U 1 1 618E9C71
P 2100 6400
F 0 "H76" V 2100 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 6405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 6400 50  0001 C CNN
F 3 "~" H 2100 6400 50  0001 C CNN
	1    2100 6400
	0    -1   -1   0   
$EndComp
Connection ~ 2100 6400
Wire Wire Line
	2100 6400 2100 6350
$Comp
L Connector:TestPoint H74
U 1 1 618E9F7D
P 2100 5900
F 0 "H74" V 2100 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 5900 50  0001 C CNN
F 3 "~" H 2100 5900 50  0001 C CNN
	1    2100 5900
	0    -1   -1   0   
$EndComp
Connection ~ 2100 5900
Wire Wire Line
	2100 5900 2100 5850
$Comp
L Connector:TestPoint H72
U 1 1 618EA20E
P 2100 5400
F 0 "H72" V 2100 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 5405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 5400 50  0001 C CNN
F 3 "~" H 2100 5400 50  0001 C CNN
	1    2100 5400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2100 5400 2100 5500
Wire Wire Line
	3600 5900 3600 6000
$Comp
L Connector:TestPoint H58
U 1 1 6190B0C7
P 1500 5500
F 0 "H58" H 1500 5450 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 5505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 5500 50  0001 C CNN
F 3 "~" H 1500 5500 50  0001 C CNN
	1    1500 5500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H60
U 1 1 6190BE91
P 1500 6000
F 0 "H60" H 1500 5950 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 6005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 6000 50  0001 C CNN
F 3 "~" H 1500 6000 50  0001 C CNN
	1    1500 6000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H62
U 1 1 6190C758
P 1500 6500
F 0 "H62" H 1500 6450 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 6505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 6500 50  0001 C CNN
F 3 "~" H 1500 6500 50  0001 C CNN
	1    1500 6500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H70
U 1 1 6190CA8E
P 3600 6200
F 0 "H70" H 3600 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 3746 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3600 6200 50  0001 C CNN
F 3 "~" H 3600 6200 50  0001 C CNN
	1    3600 6200
	-1   0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H68
U 1 1 6190CE36
P 1700 6500
F 0 "H68" H 1700 6450 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 6505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 6500 50  0001 C CNN
F 3 "~" H 1700 6500 50  0001 C CNN
	1    1700 6500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H66
U 1 1 6190D18E
P 1700 6000
F 0 "H66" H 1700 5950 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 6005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 6000 50  0001 C CNN
F 3 "~" H 1700 6000 50  0001 C CNN
	1    1700 6000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H64
U 1 1 6190D4F8
P 1700 5500
F 0 "H64" H 1700 5450 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 5505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 5500 50  0001 C CNN
F 3 "~" H 1700 5500 50  0001 C CNN
	1    1700 5500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H52
U 1 1 6192D1EE
P 1100 5700
F 0 "H52" H 1100 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 5705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 5700 50  0001 C CNN
F 3 "~" H 1100 5700 50  0001 C CNN
	1    1100 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H54
U 1 1 6192D58C
P 1100 6200
F 0 "H54" H 1100 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 6200 50  0001 C CNN
F 3 "~" H 1100 6200 50  0001 C CNN
	1    1100 6200
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H56
U 1 1 6192D811
P 1100 6700
F 0 "H56" H 1100 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 6705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 6700 50  0001 C CNN
F 3 "~" H 1100 6700 50  0001 C CNN
	1    1100 6700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H73
U 1 1 6192DDFA
P 2100 5700
F 0 "H73" H 2100 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 5705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 5700 50  0001 C CNN
F 3 "~" H 2100 5700 50  0001 C CNN
	1    2100 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H75
U 1 1 6192E134
P 2100 6200
F 0 "H75" H 2100 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 6200 50  0001 C CNN
F 3 "~" H 2100 6200 50  0001 C CNN
	1    2100 6200
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H77
U 1 1 6192E370
P 2100 6700
F 0 "H77" H 2100 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 6705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 6700 50  0001 C CNN
F 3 "~" H 2100 6700 50  0001 C CNN
	1    2100 6700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H79
U 1 1 6192E721
P 4000 6000
F 0 "H79" H 4000 5950 50  0000 C CNN
F 1 "MountingHole_Pad" V 4146 6005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 4000 6000 50  0001 C CNN
F 3 "~" H 4000 6000 50  0001 C CNN
	1    4000 6000
	1    0    0    1   
$EndComp
Wire Wire Line
	10250 1650 10250 1800
Wire Wire Line
	8150 1650 8150 1800
Wire Wire Line
	8150 2250 8150 2400
Wire Wire Line
	9200 2250 9200 2400
Wire Wire Line
	9200 3450 9200 3600
Wire Wire Line
	8150 2850 8150 3000
Wire Wire Line
	9200 2850 9200 3000
Wire Wire Line
	7050 3450 7050 3600
Wire Wire Line
	8150 3450 8150 3600
Wire Wire Line
	8250 1800 8150 1800
Connection ~ 8150 1800
Wire Wire Line
	8150 1800 8150 1950
Wire Wire Line
	8450 1800 8550 1800
Wire Wire Line
	9200 1650 9200 1800
Wire Wire Line
	9300 1800 9200 1800
Connection ~ 9200 1800
Wire Wire Line
	9200 1800 9200 1950
Wire Wire Line
	9500 1800 9600 1800
Wire Wire Line
	10350 1800 10250 1800
Connection ~ 10250 1800
Wire Wire Line
	10250 1800 10250 1950
Wire Wire Line
	10550 1800 10650 1800
Wire Wire Line
	9600 2400 9500 2400
Wire Wire Line
	9300 2400 9200 2400
Connection ~ 9200 2400
Wire Wire Line
	9200 2400 9200 2550
Wire Wire Line
	8550 2400 8450 2400
Wire Wire Line
	8250 2400 8150 2400
Connection ~ 8150 2400
Wire Wire Line
	8150 2400 8150 2550
Wire Wire Line
	8250 3000 8150 3000
Connection ~ 8150 3000
Wire Wire Line
	8150 3000 8150 3150
Wire Wire Line
	8450 3000 8550 3000
Wire Wire Line
	9300 3000 9200 3000
Connection ~ 9200 3000
Wire Wire Line
	9200 3000 9200 3150
Wire Wire Line
	9500 3000 9600 3000
Wire Wire Line
	7150 3600 7050 3600
Connection ~ 7050 3600
Wire Wire Line
	7050 3600 7050 3750
Wire Wire Line
	7350 3600 7450 3600
Wire Wire Line
	8250 3600 8150 3600
Connection ~ 8150 3600
Wire Wire Line
	8150 3600 8150 3750
Wire Wire Line
	8450 3600 8550 3600
Wire Wire Line
	9500 3600 9600 3600
Wire Wire Line
	9300 3600 9200 3600
Connection ~ 9200 3600
Wire Wire Line
	9200 3600 9200 3750
NoConn ~ 8800 4250
NoConn ~ 8800 4350
NoConn ~ 8800 4450
NoConn ~ 8800 4550
NoConn ~ 8800 4650
NoConn ~ 9300 4650
NoConn ~ 9300 4250
NoConn ~ 9850 4250
NoConn ~ 9850 4350
NoConn ~ 9850 4450
NoConn ~ 9850 4550
NoConn ~ 9850 4650
NoConn ~ 10350 4650
NoConn ~ 10350 4250
$Comp
L Sofle:SW_PUSH_LED SW10
U 2 1 61D0453F
P 2550 6100
F 0 "SW10" H 2550 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2550 6303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 2580 6300 50  0001 C CNN
F 3 "" H 2550 6200 50  0001 C CNN
	2    2550 6100
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW9
U 2 1 61D04A09
P 2550 5600
F 0 "SW9" H 2550 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2550 5803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 2580 5800 50  0001 C CNN
F 3 "" H 2550 5700 50  0001 C CNN
	2    2550 5600
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2750 5850 2350 5850
Wire Wire Line
	2350 5850 2350 5900
$Comp
L Sofle:SW_PUSH_LED SW11
U 2 1 61D04A15
P 2550 6600
F 0 "SW11" H 2550 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2550 6803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 2580 6800 50  0001 C CNN
F 3 "" H 2550 6700 50  0001 C CNN
	2    2550 6600
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2750 6200 2750 6300
Wire Wire Line
	2750 6350 2350 6350
Wire Wire Line
	2350 6350 2350 6400
Wire Wire Line
	2750 6700 2750 6800
Wire Wire Line
	2750 5700 2750 5800
Wire Wire Line
	2950 6850 2950 6800
Wire Wire Line
	3350 6850 2950 6850
Wire Wire Line
	3350 7000 3350 6900
$Comp
L Sofle:SW_PUSH_LED SW16
U 2 1 61D04A28
P 3150 7100
F 0 "SW16" H 3150 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3150 7303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 3180 7300 50  0001 C CNN
F 3 "" H 3150 7200 50  0001 C CNN
	2    3150 7100
	-1   0    0    1   
$EndComp
Wire Wire Line
	2950 5850 2950 5800
Wire Wire Line
	3350 5850 2950 5850
Wire Wire Line
	3350 6000 3350 5900
Wire Wire Line
	2950 6350 2950 6300
Wire Wire Line
	3350 6350 2950 6350
Wire Wire Line
	3350 6500 3350 6400
$Comp
L Sofle:SW_PUSH_LED SW15
U 2 1 61D04A38
P 3150 6600
F 0 "SW15" H 3150 6600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3150 6803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 3180 6800 50  0001 C CNN
F 3 "" H 3150 6700 50  0001 C CNN
	2    3150 6600
	-1   0    0    1   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW14
U 2 1 61D04A42
P 3150 6100
F 0 "SW14" H 3150 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3150 6303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 3180 6300 50  0001 C CNN
F 3 "" H 3150 6200 50  0001 C CNN
	2    3150 6100
	-1   0    0    1   
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW13
U 2 1 61D04A4C
P 3150 5600
F 0 "SW13" H 3150 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3150 5803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 3180 5800 50  0001 C CNN
F 3 "" H 3150 5700 50  0001 C CNN
	2    3150 5600
	-1   0    0    1   
$EndComp
Connection ~ 2750 5800
Wire Wire Line
	2750 5800 2750 5850
$Comp
L Connector:TestPoint H82
U 1 1 61D04A58
P 2350 5900
F 0 "H82" V 2350 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 5900 50  0001 C CNN
F 3 "~" H 2350 5900 50  0001 C CNN
	1    2350 5900
	0    1    1    0   
$EndComp
Connection ~ 2350 5900
Wire Wire Line
	2350 5900 2350 6000
$Comp
L Connector:TestPoint H87
U 1 1 61D04A64
P 2750 5800
F 0 "H87" V 2750 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 5800 50  0001 C CNN
F 3 "~" H 2750 5800 50  0001 C CNN
	1    2750 5800
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H89
U 1 1 61D04A6E
P 2750 6300
F 0 "H89" V 2750 6550 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 6305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 6300 50  0001 C CNN
F 3 "~" H 2750 6300 50  0001 C CNN
	1    2750 6300
	0    -1   -1   0   
$EndComp
Connection ~ 2750 6300
Wire Wire Line
	2750 6300 2750 6350
$Comp
L Connector:TestPoint H91
U 1 1 61D04A7A
P 2750 6800
F 0 "H91" V 2750 7050 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 6805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 6800 50  0001 C CNN
F 3 "~" H 2750 6800 50  0001 C CNN
	1    2750 6800
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H84
U 1 1 61D04A86
P 2350 6400
F 0 "H84" V 2350 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 6405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 6400 50  0001 C CNN
F 3 "~" H 2350 6400 50  0001 C CNN
	1    2350 6400
	0    1    1    0   
$EndComp
Connection ~ 2350 6400
Wire Wire Line
	2350 6400 2350 6500
$Comp
L Connector:TestPoint H80
U 1 1 61D04A92
P 2350 5400
F 0 "H80" V 2350 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 5405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 5400 50  0001 C CNN
F 3 "~" H 2350 5400 50  0001 C CNN
	1    2350 5400
	0    1    1    0   
$EndComp
Wire Wire Line
	2350 5400 2350 5500
$Comp
L Connector:TestPoint H97
U 1 1 61D04A9D
P 2950 6800
F 0 "H97" V 2950 7050 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 6805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 6800 50  0001 C CNN
F 3 "~" H 2950 6800 50  0001 C CNN
	1    2950 6800
	0    1    1    0   
$EndComp
Connection ~ 2950 6800
Wire Wire Line
	2950 6800 2950 6700
$Comp
L Connector:TestPoint H99
U 1 1 61D04AA9
P 2950 7300
F 0 "H99" V 2950 7550 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 7305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 7300 50  0001 C CNN
F 3 "~" H 2950 7300 50  0001 C CNN
	1    2950 7300
	0    1    1    0   
$EndComp
$Comp
L Connector:TestPoint H95
U 1 1 61D04AB3
P 2950 6300
F 0 "H95" V 2950 6550 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 6305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 6300 50  0001 C CNN
F 3 "~" H 2950 6300 50  0001 C CNN
	1    2950 6300
	0    1    1    0   
$EndComp
Connection ~ 2950 6300
Wire Wire Line
	2950 6300 2950 6200
$Comp
L Connector:TestPoint H93
U 1 1 61D04ABF
P 2950 5800
F 0 "H93" V 2950 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 5800 50  0001 C CNN
F 3 "~" H 2950 5800 50  0001 C CNN
	1    2950 5800
	0    1    1    0   
$EndComp
Connection ~ 2950 5800
Wire Wire Line
	2950 5800 2950 5700
$Comp
L Connector:TestPoint H106
U 1 1 61D04ACB
P 3350 6900
F 0 "H106" V 3350 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 6905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 6900 50  0001 C CNN
F 3 "~" H 3350 6900 50  0001 C CNN
	1    3350 6900
	0    -1   -1   0   
$EndComp
Connection ~ 3350 6900
Wire Wire Line
	3350 6900 3350 6850
$Comp
L Connector:TestPoint H104
U 1 1 61D04AD7
P 3350 6400
F 0 "H104" V 3350 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 6405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 6400 50  0001 C CNN
F 3 "~" H 3350 6400 50  0001 C CNN
	1    3350 6400
	0    -1   -1   0   
$EndComp
Connection ~ 3350 6400
Wire Wire Line
	3350 6400 3350 6350
$Comp
L Connector:TestPoint H102
U 1 1 61D04AE3
P 3350 5900
F 0 "H102" V 3350 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 5900 50  0001 C CNN
F 3 "~" H 3350 5900 50  0001 C CNN
	1    3350 5900
	0    -1   -1   0   
$EndComp
Connection ~ 3350 5900
Wire Wire Line
	3350 5900 3350 5850
$Comp
L Connector:TestPoint H100
U 1 1 61D04AEF
P 3350 5400
F 0 "H100" V 3350 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 5405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 5400 50  0001 C CNN
F 3 "~" H 3350 5400 50  0001 C CNN
	1    3350 5400
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3350 5400 3350 5500
Wire Wire Line
	2950 7300 2950 7200
$Comp
L Connector:TestPoint H86
U 1 1 61D04AFC
P 2750 5500
F 0 "H86" H 2750 5450 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 5505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 5500 50  0001 C CNN
F 3 "~" H 2750 5500 50  0001 C CNN
	1    2750 5500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H88
U 1 1 61D04B06
P 2750 6000
F 0 "H88" H 2750 5950 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 6005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 6000 50  0001 C CNN
F 3 "~" H 2750 6000 50  0001 C CNN
	1    2750 6000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H90
U 1 1 61D04B10
P 2750 6500
F 0 "H90" H 2750 6450 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 6505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 6500 50  0001 C CNN
F 3 "~" H 2750 6500 50  0001 C CNN
	1    2750 6500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H98
U 1 1 61D04B1A
P 2950 7000
F 0 "H98" H 2950 6950 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 7005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 7000 50  0001 C CNN
F 3 "~" H 2950 7000 50  0001 C CNN
	1    2950 7000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H96
U 1 1 61D04B24
P 2950 6500
F 0 "H96" H 2950 6450 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 6505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 6500 50  0001 C CNN
F 3 "~" H 2950 6500 50  0001 C CNN
	1    2950 6500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H94
U 1 1 61D04B2E
P 2950 6000
F 0 "H94" H 2950 5950 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 6005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 6000 50  0001 C CNN
F 3 "~" H 2950 6000 50  0001 C CNN
	1    2950 6000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H92
U 1 1 61D04B38
P 2950 5500
F 0 "H92" H 2950 5450 50  0000 C CNN
F 1 "MountingHole_Pad" V 3096 5505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2950 5500 50  0001 C CNN
F 3 "~" H 2950 5500 50  0001 C CNN
	1    2950 5500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H81
U 1 1 61D04B42
P 2350 5700
F 0 "H81" H 2350 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 5705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 5700 50  0001 C CNN
F 3 "~" H 2350 5700 50  0001 C CNN
	1    2350 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H83
U 1 1 61D04B4C
P 2350 6200
F 0 "H83" H 2350 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 6200 50  0001 C CNN
F 3 "~" H 2350 6200 50  0001 C CNN
	1    2350 6200
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H85
U 1 1 61D04B56
P 2350 6700
F 0 "H85" H 2350 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 6705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 6700 50  0001 C CNN
F 3 "~" H 2350 6700 50  0001 C CNN
	1    2350 6700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H101
U 1 1 61D04B60
P 3350 5700
F 0 "H101" H 3350 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 5705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 5700 50  0001 C CNN
F 3 "~" H 3350 5700 50  0001 C CNN
	1    3350 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H103
U 1 1 61D04B6A
P 3350 6200
F 0 "H103" H 3350 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 6200 50  0001 C CNN
F 3 "~" H 3350 6200 50  0001 C CNN
	1    3350 6200
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H105
U 1 1 61D04B74
P 3350 6700
F 0 "H105" H 3350 6650 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 6705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 6700 50  0001 C CNN
F 3 "~" H 3350 6700 50  0001 C CNN
	1    3350 6700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H107
U 1 1 61D04B7E
P 3350 7200
F 0 "H107" H 3350 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 3496 7205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3350 7200 50  0001 C CNN
F 3 "~" H 3350 7200 50  0001 C CNN
	1    3350 7200
	1    0    0    -1  
$EndComp
Wire Wire Line
	2100 5400 2350 5400
Connection ~ 2100 5400
Connection ~ 2350 5400
$Comp
L Sofle:SW_PUSH_LED SW4
U 2 1 61D91426
P 1300 7100
F 0 "SW4" H 1300 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1300 7303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1330 7300 50  0001 C CNN
F 3 "" H 1300 7200 50  0001 C CNN
	2    1300 7100
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW17
U 2 1 61D91BBA
P 3800 5600
F 0 "SW17" H 3800 5600 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3800 5803 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 3830 5800 50  0001 C CNN
F 3 "" H 3800 5700 50  0001 C CNN
	2    3800 5600
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1500 6850 1100 6850
Wire Wire Line
	1100 6850 1100 6900
$Comp
L Sofle:SW_PUSH_LED SW8
U 2 1 61D91BC6
P 1900 7100
F 0 "SW8" H 1900 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 1900 7303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 1930 7300 50  0001 C CNN
F 3 "" H 1900 7200 50  0001 C CNN
	2    1900 7100
	-1   0    0    1   
$EndComp
Wire Wire Line
	1500 7200 1500 7300
Wire Wire Line
	2100 7000 2100 6900
Wire Wire Line
	4000 5700 4000 5800
Wire Wire Line
	1500 6800 1500 6850
$Comp
L Connector:TestPoint H110
U 1 1 61D91BD7
P 1100 6900
F 0 "H110" V 1100 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 6905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 6900 50  0001 C CNN
F 3 "~" H 1100 6900 50  0001 C CNN
	1    1100 6900
	0    1    1    0   
$EndComp
Connection ~ 1100 6900
Wire Wire Line
	1100 6900 1100 7000
$Comp
L Connector:TestPoint H145
U 1 1 61D91BE3
P 4000 5800
F 0 "H145" V 4000 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 4146 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 4000 5800 50  0001 C CNN
F 3 "~" H 4000 5800 50  0001 C CNN
	1    4000 5800
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H147
U 1 1 61D91BED
P 1500 7300
F 0 "H147" V 1500 7550 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 7305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 7300 50  0001 C CNN
F 3 "~" H 1500 7300 50  0001 C CNN
	1    1500 7300
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H149
U 1 1 61D91BF9
P 2100 6900
F 0 "H149" V 2100 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 6905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 6900 50  0001 C CNN
F 3 "~" H 2100 6900 50  0001 C CNN
	1    2100 6900
	0    -1   1    0   
$EndComp
$Comp
L Connector:TestPoint H112
U 1 1 61D91C05
P 1700 7300
F 0 "H112" V 1700 7550 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 7305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 7300 50  0001 C CNN
F 3 "~" H 1700 7300 50  0001 C CNN
	1    1700 7300
	0    1    -1   0   
$EndComp
Wire Wire Line
	1700 7300 1700 7200
$Comp
L Connector:TestPoint H108
U 1 1 61D91C11
P 3600 5400
F 0 "H108" V 3600 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 3746 5405 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3600 5400 50  0001 C CNN
F 3 "~" H 3600 5400 50  0001 C CNN
	1    3600 5400
	0    1    1    0   
$EndComp
Wire Wire Line
	3600 5400 3600 5500
$Comp
L Connector:TestPoint H144
U 1 1 61D91C1C
P 4000 5500
F 0 "H144" H 4000 5450 50  0000 C CNN
F 1 "MountingHole_Pad" V 4146 5505 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 4000 5500 50  0001 C CNN
F 3 "~" H 4000 5500 50  0001 C CNN
	1    4000 5500
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H146
U 1 1 61D91C26
P 1500 7000
F 0 "H146" H 1500 6950 50  0000 C CNN
F 1 "MountingHole_Pad" V 1646 7005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1500 7000 50  0001 C CNN
F 3 "~" H 1500 7000 50  0001 C CNN
	1    1500 7000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H148
U 1 1 61D91C30
P 2100 7200
F 0 "H148" H 2100 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2246 7205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2100 7200 50  0001 C CNN
F 3 "~" H 2100 7200 50  0001 C CNN
	1    2100 7200
	-1   0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H109
U 1 1 61D91C3A
P 3600 5700
F 0 "H109" H 3600 5650 50  0000 C CNN
F 1 "MountingHole_Pad" V 3746 5705 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 3600 5700 50  0001 C CNN
F 3 "~" H 3600 5700 50  0001 C CNN
	1    3600 5700
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H111
U 1 1 61D91C44
P 1100 7200
F 0 "H111" H 1100 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 1246 7205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1100 7200 50  0001 C CNN
F 3 "~" H 1100 7200 50  0001 C CNN
	1    1100 7200
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H141
U 1 1 61D91C4E
P 1700 7000
F 0 "H141" H 1700 6950 50  0000 C CNN
F 1 "MountingHole_Pad" V 1846 7005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 1700 7000 50  0001 C CNN
F 3 "~" H 1700 7000 50  0001 C CNN
	1    1700 7000
	1    0    0    1   
$EndComp
Wire Wire Line
	3350 5400 3600 5400
Connection ~ 3600 5400
Connection ~ 3350 5400
$Comp
L Sofle:SW_PUSH_LED SW12
U 2 1 61E0AFBC
P 2550 7100
F 0 "SW12" H 2550 7100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 2550 7303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 2580 7300 50  0001 C CNN
F 3 "" H 2550 7200 50  0001 C CNN
	2    2550 7100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2750 6850 2350 6850
Wire Wire Line
	2350 6850 2350 6900
Wire Wire Line
	2750 7200 2750 7300
Wire Wire Line
	2100 6900 2100 6850
$Comp
L Connector:TestPoint H151
U 1 1 61E0B796
P 2750 7300
F 0 "H151" V 2750 7550 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 7305 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 7300 50  0001 C CNN
F 3 "~" H 2750 7300 50  0001 C CNN
	1    2750 7300
	0    -1   -1   0   
$EndComp
$Comp
L Connector:TestPoint H142
U 1 1 61E0B7A0
P 2350 6900
F 0 "H142" V 2350 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 6905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 6900 50  0001 C CNN
F 3 "~" H 2350 6900 50  0001 C CNN
	1    2350 6900
	0    1    1    0   
$EndComp
Connection ~ 2350 6900
Wire Wire Line
	2350 6900 2350 7000
$Comp
L Connector:TestPoint H150
U 1 1 61E0B7AC
P 2750 7000
F 0 "H150" H 2750 6950 50  0000 C CNN
F 1 "MountingHole_Pad" V 2896 7005 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2750 7000 50  0001 C CNN
F 3 "~" H 2750 7000 50  0001 C CNN
	1    2750 7000
	-1   0    0    1   
$EndComp
$Comp
L Connector:TestPoint H143
U 1 1 61E0B7B6
P 2350 7200
F 0 "H143" H 2350 7150 50  0000 C CNN
F 1 "MountingHole_Pad" V 2496 7205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 2350 7200 50  0001 C CNN
F 3 "~" H 2350 7200 50  0001 C CNN
	1    2350 7200
	1    0    0    -1  
$EndComp
Connection ~ 2100 6900
Connection ~ 6400 3900
Wire Wire Line
	6400 3900 6600 3900
Connection ~ 6200 3900
Wire Wire Line
	6200 3900 6400 3900
Connection ~ 6600 3900
Wire Wire Line
	6000 3150 6000 3450
Wire Wire Line
	9800 2700 10350 2700
Connection ~ 6000 3150
Wire Wire Line
	6000 3450 6000 3600
Connection ~ 6000 3450
Wire Wire Line
	6100 3600 6000 3600
Connection ~ 6000 3600
Wire Wire Line
	6000 3600 6000 3750
Wire Wire Line
	6300 3600 6400 3600
$Comp
L Sofle:SW_PUSH_LED SW18
U 2 1 61823C35
P 3800 6100
F 0 "SW18" H 3800 6100 50  0000 C CNN
F 1 "SW_PUSH_LED" H 3800 6303 25  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 3830 6300 50  0001 C CNN
F 3 "" H 3800 6200 50  0001 C CNN
	2    3800 6100
	-1   0    0    -1  
$EndComp
$Comp
L Sofle:SW_PUSH_LED SW18
U 1 1 5C71DC38
P 10450 2300
F 0 "SW18" H 10450 2450 50  0000 C CNN
F 1 "SW_PUSH_LED" H 10450 2494 50  0001 C CNN
F 2 "#footprint:CherryMX_MidHeight_RGB_Hotswap" H 10450 2500 50  0001 C CNN
F 3 "" H 10450 2500 50  0001 C CNN
	1    10450 2300
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6600 3900 7250 3900
Connection ~ 7250 3900
Wire Wire Line
	7250 3900 7450 3900
Connection ~ 7450 3900
Wire Wire Line
	7450 3900 7650 3900
Connection ~ 7650 3900
Wire Wire Line
	7650 3900 8350 3900
Wire Wire Line
	7050 3150 7050 3450
Connection ~ 7050 3150
Connection ~ 7050 3450
Connection ~ 8350 3900
Wire Wire Line
	8350 3900 8550 3900
Connection ~ 8550 3900
Wire Wire Line
	8550 3900 8750 3900
Connection ~ 8750 3900
Wire Wire Line
	8750 3900 9400 3900
Wire Wire Line
	8150 3150 8150 3450
Connection ~ 8150 3150
Connection ~ 8150 3450
Connection ~ 1500 6800
Wire Wire Line
	1500 7300 1700 7300
Connection ~ 1500 7300
Connection ~ 1700 7300
Wire Wire Line
	2750 6850 2750 6800
Connection ~ 2750 6800
Wire Wire Line
	2750 7300 2950 7300
Connection ~ 2750 7300
Connection ~ 2950 7300
Wire Wire Line
	4000 5800 4000 5850
Wire Wire Line
	4000 5850 3600 5850
Wire Wire Line
	3600 5850 3600 5900
Connection ~ 4000 5800
Connection ~ 3600 5900
Connection ~ 10650 2700
Wire Wire Line
	10650 2700 10750 2700
Connection ~ 10450 2700
Wire Wire Line
	10450 2700 10650 2700
Wire Wire Line
	10250 1950 10250 2250
Connection ~ 10250 1950
Connection ~ 10250 2250
Wire Wire Line
	10350 2400 10250 2400
Connection ~ 10250 2400
Wire Wire Line
	10250 2400 10250 2550
Wire Wire Line
	10550 2400 10650 2400
$Comp
L Device:C_Small C1
U 1 1 61C218E5
P 4500 5850
F 0 "C1" H 4592 5896 50  0000 L CNN
F 1 "100n" H 4592 5805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4500 5850 50  0001 C CNN
F 3 "~" H 4500 5850 50  0001 C CNN
	1    4500 5850
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C5
U 1 1 61C2A62B
P 4900 5850
F 0 "C5" H 4992 5896 50  0000 L CNN
F 1 "100n" H 4992 5805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4900 5850 50  0001 C CNN
F 3 "~" H 4900 5850 50  0001 C CNN
	1    4900 5850
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C9
U 1 1 61C2B50F
P 5300 5850
F 0 "C9" H 5392 5896 50  0000 L CNN
F 1 "100n" H 5392 5805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5300 5850 50  0001 C CNN
F 3 "~" H 5300 5850 50  0001 C CNN
	1    5300 5850
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C13
U 1 1 61C2C39B
P 5700 5850
F 0 "C13" H 5792 5896 50  0000 L CNN
F 1 "100n" H 5792 5805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5700 5850 50  0001 C CNN
F 3 "~" H 5700 5850 50  0001 C CNN
	1    5700 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 5950 5500 5950
Connection ~ 5300 5950
Connection ~ 4900 5950
Wire Wire Line
	4900 5950 4500 5950
Wire Wire Line
	5700 5750 5300 5750
Connection ~ 4900 5750
Wire Wire Line
	4900 5750 4500 5750
Connection ~ 5300 5750
$Comp
L power:VCC #PWR02
U 1 1 61C8B58E
P 5100 5750
F 0 "#PWR02" H 5100 5600 50  0001 C CNN
F 1 "VCC" H 5117 5923 50  0000 C CNN
F 2 "" H 5100 5750 50  0001 C CNN
F 3 "" H 5100 5750 50  0001 C CNN
	1    5100 5750
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 61C8D239
P 5500 5950
F 0 "#PWR06" H 5500 5700 50  0001 C CNN
F 1 "GND" H 5500 5800 50  0000 C CNN
F 2 "" H 5500 5950 50  0001 C CNN
F 3 "" H 5500 5950 50  0001 C CNN
	1    5500 5950
	-1   0    0    -1  
$EndComp
$Comp
L Device:C_Small C17
U 1 1 61C8E1E6
P 6100 5850
F 0 "C17" H 6192 5896 50  0000 L CNN
F 1 "100n" H 6192 5805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 6100 5850 50  0001 C CNN
F 3 "~" H 6100 5850 50  0001 C CNN
	1    6100 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 5750 6100 5750
Connection ~ 5700 5750
Wire Wire Line
	6100 5950 5700 5950
Connection ~ 5700 5950
Wire Wire Line
	4900 5950 5300 5950
Wire Wire Line
	4900 5750 5100 5750
Connection ~ 5100 5750
Wire Wire Line
	5100 5750 5300 5750
Connection ~ 5500 5950
Wire Wire Line
	5500 5950 5300 5950
$Comp
L Device:C_Small C2
U 1 1 61CF9C71
P 4500 6300
F 0 "C2" H 4592 6346 50  0000 L CNN
F 1 "100n" H 4592 6255 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4500 6300 50  0001 C CNN
F 3 "~" H 4500 6300 50  0001 C CNN
	1    4500 6300
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C6
U 1 1 61CF9C77
P 4900 6300
F 0 "C6" H 4992 6346 50  0000 L CNN
F 1 "100n" H 4992 6255 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4900 6300 50  0001 C CNN
F 3 "~" H 4900 6300 50  0001 C CNN
	1    4900 6300
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C10
U 1 1 61CF9C7D
P 5300 6300
F 0 "C10" H 5392 6346 50  0000 L CNN
F 1 "100n" H 5392 6255 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5300 6300 50  0001 C CNN
F 3 "~" H 5300 6300 50  0001 C CNN
	1    5300 6300
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C14
U 1 1 61CF9C83
P 5700 6300
F 0 "C14" H 5792 6346 50  0000 L CNN
F 1 "100n" H 5792 6255 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5700 6300 50  0001 C CNN
F 3 "~" H 5700 6300 50  0001 C CNN
	1    5700 6300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 6400 5500 6400
Connection ~ 5300 6400
Connection ~ 4900 6400
Wire Wire Line
	4900 6400 4500 6400
Wire Wire Line
	5700 6200 5300 6200
Connection ~ 4900 6200
Wire Wire Line
	4900 6200 4500 6200
Connection ~ 5300 6200
$Comp
L power:VCC #PWR03
U 1 1 61CF9C91
P 5100 6200
F 0 "#PWR03" H 5100 6050 50  0001 C CNN
F 1 "VCC" H 5117 6373 50  0000 C CNN
F 2 "" H 5100 6200 50  0001 C CNN
F 3 "" H 5100 6200 50  0001 C CNN
	1    5100 6200
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR07
U 1 1 61CF9C97
P 5500 6400
F 0 "#PWR07" H 5500 6150 50  0001 C CNN
F 1 "GND" H 5500 6250 50  0000 C CNN
F 2 "" H 5500 6400 50  0001 C CNN
F 3 "" H 5500 6400 50  0001 C CNN
	1    5500 6400
	-1   0    0    -1  
$EndComp
$Comp
L Device:C_Small C18
U 1 1 61CF9C9D
P 6100 6300
F 0 "C18" H 6192 6346 50  0000 L CNN
F 1 "100n" H 6192 6255 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 6100 6300 50  0001 C CNN
F 3 "~" H 6100 6300 50  0001 C CNN
	1    6100 6300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 6200 6100 6200
Connection ~ 5700 6200
Wire Wire Line
	6100 6400 5700 6400
Connection ~ 5700 6400
Wire Wire Line
	4900 6400 5300 6400
Wire Wire Line
	4900 6200 5100 6200
Connection ~ 5100 6200
Wire Wire Line
	5100 6200 5300 6200
Connection ~ 5500 6400
Wire Wire Line
	5500 6400 5300 6400
$Comp
L Device:C_Small C3
U 1 1 61D1C130
P 4500 6750
F 0 "C3" H 4592 6796 50  0000 L CNN
F 1 "100n" H 4592 6705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4500 6750 50  0001 C CNN
F 3 "~" H 4500 6750 50  0001 C CNN
	1    4500 6750
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C7
U 1 1 61D1C136
P 4900 6750
F 0 "C7" H 4992 6796 50  0000 L CNN
F 1 "100n" H 4992 6705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4900 6750 50  0001 C CNN
F 3 "~" H 4900 6750 50  0001 C CNN
	1    4900 6750
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C11
U 1 1 61D1C13C
P 5300 6750
F 0 "C11" H 5392 6796 50  0000 L CNN
F 1 "100n" H 5392 6705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5300 6750 50  0001 C CNN
F 3 "~" H 5300 6750 50  0001 C CNN
	1    5300 6750
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C15
U 1 1 61D1C142
P 5700 6750
F 0 "C15" H 5792 6796 50  0000 L CNN
F 1 "100n" H 5792 6705 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5700 6750 50  0001 C CNN
F 3 "~" H 5700 6750 50  0001 C CNN
	1    5700 6750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 6850 5500 6850
Connection ~ 5300 6850
Connection ~ 4900 6850
Wire Wire Line
	4900 6850 4500 6850
Wire Wire Line
	5700 6650 5300 6650
Connection ~ 4900 6650
Wire Wire Line
	4900 6650 4500 6650
Connection ~ 5300 6650
$Comp
L power:VCC #PWR04
U 1 1 61D1C150
P 5100 6650
F 0 "#PWR04" H 5100 6500 50  0001 C CNN
F 1 "VCC" H 5117 6823 50  0000 C CNN
F 2 "" H 5100 6650 50  0001 C CNN
F 3 "" H 5100 6650 50  0001 C CNN
	1    5100 6650
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 61D1C156
P 5500 6850
F 0 "#PWR08" H 5500 6600 50  0001 C CNN
F 1 "GND" H 5500 6700 50  0000 C CNN
F 2 "" H 5500 6850 50  0001 C CNN
F 3 "" H 5500 6850 50  0001 C CNN
	1    5500 6850
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4900 6850 5300 6850
Wire Wire Line
	4900 6650 5100 6650
Connection ~ 5100 6650
Wire Wire Line
	5100 6650 5300 6650
Connection ~ 5500 6850
Wire Wire Line
	5500 6850 5300 6850
$Comp
L Device:C_Small C4
U 1 1 61D4048B
P 4500 7200
F 0 "C4" H 4592 7246 50  0000 L CNN
F 1 "100n" H 4592 7155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4500 7200 50  0001 C CNN
F 3 "~" H 4500 7200 50  0001 C CNN
	1    4500 7200
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C8
U 1 1 61D40491
P 4900 7200
F 0 "C8" H 4992 7246 50  0000 L CNN
F 1 "100n" H 4992 7155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 4900 7200 50  0001 C CNN
F 3 "~" H 4900 7200 50  0001 C CNN
	1    4900 7200
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C12
U 1 1 61D40497
P 5300 7200
F 0 "C12" H 5392 7246 50  0000 L CNN
F 1 "100n" H 5392 7155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5300 7200 50  0001 C CNN
F 3 "~" H 5300 7200 50  0001 C CNN
	1    5300 7200
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C16
U 1 1 61D4049D
P 5700 7200
F 0 "C16" H 5792 7246 50  0000 L CNN
F 1 "100n" H 5792 7155 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 5700 7200 50  0001 C CNN
F 3 "~" H 5700 7200 50  0001 C CNN
	1    5700 7200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 7300 5500 7300
Connection ~ 5300 7300
Connection ~ 4900 7300
Wire Wire Line
	4900 7300 4500 7300
Wire Wire Line
	5700 7100 5300 7100
Connection ~ 4900 7100
Wire Wire Line
	4900 7100 4500 7100
Connection ~ 5300 7100
$Comp
L power:VCC #PWR05
U 1 1 61D404AB
P 5100 7100
F 0 "#PWR05" H 5100 6950 50  0001 C CNN
F 1 "VCC" H 5117 7273 50  0000 C CNN
F 2 "" H 5100 7100 50  0001 C CNN
F 3 "" H 5100 7100 50  0001 C CNN
	1    5100 7100
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 61D404B1
P 5500 7300
F 0 "#PWR09" H 5500 7050 50  0001 C CNN
F 1 "GND" H 5500 7150 50  0000 C CNN
F 2 "" H 5500 7300 50  0001 C CNN
F 3 "" H 5500 7300 50  0001 C CNN
	1    5500 7300
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4900 7300 5300 7300
Wire Wire Line
	4900 7100 5100 7100
Connection ~ 5100 7100
Wire Wire Line
	5100 7100 5300 7100
Connection ~ 5500 7300
Wire Wire Line
	5500 7300 5300 7300
Connection ~ 10350 2700
Wire Wire Line
	10350 2700 10450 2700
Connection ~ 10750 2700
Wire Wire Line
	10750 2700 10850 2700
Wire Wire Line
	10250 2250 10250 2400
$Comp
L Device:C_Small C19
U 1 1 61786C7F
P 9550 6000
F 0 "C19" H 9642 6046 50  0000 L CNN
F 1 "100n" H 9642 5955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 9550 6000 50  0001 C CNN
F 3 "~" H 9550 6000 50  0001 C CNN
	1    9550 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C20
U 1 1 61787637
P 9950 6000
F 0 "C20" H 10042 6046 50  0000 L CNN
F 1 "100n" H 10042 5955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 9950 6000 50  0001 C CNN
F 3 "~" H 9950 6000 50  0001 C CNN
	1    9950 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C21
U 1 1 61787641
P 10350 6000
F 0 "C21" H 10442 6046 50  0000 L CNN
F 1 "100n" H 10442 5955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 10350 6000 50  0001 C CNN
F 3 "~" H 10350 6000 50  0001 C CNN
	1    10350 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C22
U 1 1 6178764B
P 10750 6000
F 0 "C22" H 10842 6046 50  0000 L CNN
F 1 "100n" H 10842 5955 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric_Pad1.08x0.95mm_HandSolder" H 10750 6000 50  0001 C CNN
F 3 "~" H 10750 6000 50  0001 C CNN
	1    10750 6000
	1    0    0    -1  
$EndComp
Wire Wire Line
	10750 6100 10550 6100
Connection ~ 10350 6100
Connection ~ 9950 6100
Wire Wire Line
	9950 6100 9550 6100
Wire Wire Line
	10750 5900 10350 5900
Connection ~ 9950 5900
Wire Wire Line
	9950 5900 9550 5900
Connection ~ 10350 5900
$Comp
L power:VCC #PWR014
U 1 1 6178765D
P 10150 5900
F 0 "#PWR014" H 10150 5750 50  0001 C CNN
F 1 "VCC" H 10167 6073 50  0000 C CNN
F 2 "" H 10150 5900 50  0001 C CNN
F 3 "" H 10150 5900 50  0001 C CNN
	1    10150 5900
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR015
U 1 1 61787667
P 10550 6100
F 0 "#PWR015" H 10550 5850 50  0001 C CNN
F 1 "GND" H 10550 5950 50  0000 C CNN
F 2 "" H 10550 6100 50  0001 C CNN
F 3 "" H 10550 6100 50  0001 C CNN
	1    10550 6100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	9950 6100 10350 6100
Wire Wire Line
	9950 5900 10150 5900
Connection ~ 10150 5900
Wire Wire Line
	10150 5900 10350 5900
Connection ~ 10550 6100
Wire Wire Line
	10550 6100 10350 6100
Wire Wire Line
	4000 6300 4000 7600
Wire Wire Line
	4000 7600 6600 7600
Connection ~ 4000 6300
$Comp
L Sofle:LED_SK6812_Mini_E LED1
U 1 1 61796572
P 7000 6000
F 0 "LED1" H 7000 6050 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 7000 6203 25  0001 C CNN
F 2 "#footprint:SK6812_Mini_E" H 7030 6200 50  0001 C CNN
F 3 "" H 7000 6100 50  0001 C CNN
	1    7000 6000
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H154
U 1 1 617A5B60
P 7200 5800
F 0 "H154" H 7200 5750 50  0000 C CNN
F 1 "MountingHole_Pad" V 7346 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7200 5800 50  0001 C CNN
F 3 "~" H 7200 5800 50  0001 C CNN
	1    7200 5800
	0    -1   1    0   
$EndComp
$Comp
L Connector:TestPoint H153
U 1 1 617AC4EE
P 6800 6200
F 0 "H153" H 6800 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 6946 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6800 6200 50  0001 C CNN
F 3 "~" H 6800 6200 50  0001 C CNN
	1    6800 6200
	0    1    -1   0   
$EndComp
$Comp
L Connector:TestPoint H152
U 1 1 617AC83C
P 6800 5900
F 0 "H152" H 6800 5850 50  0000 C CNN
F 1 "MountingHole_Pad" V 6946 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 6800 5900 50  0001 C CNN
F 3 "~" H 6800 5900 50  0001 C CNN
	1    6800 5900
	1    0    0    1   
$EndComp
$Comp
L Connector:TestPoint H155
U 1 1 617ACB7E
P 7200 6100
F 0 "H155" H 7200 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 7346 6105 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7200 6100 50  0001 C CNN
F 3 "~" H 7200 6100 50  0001 C CNN
	1    7200 6100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6800 6100 6800 6200
Wire Wire Line
	7200 5800 7200 5900
Wire Wire Line
	6600 5650 7200 5650
Wire Wire Line
	6600 5650 6600 7600
$Comp
L Sofle:LED_SK6812_Mini_E LED2
U 1 1 61859F12
P 7650 6000
F 0 "LED2" H 7650 6050 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 7650 6203 25  0001 C CNN
F 2 "#footprint:SK6812_Mini_E" H 7680 6200 50  0001 C CNN
F 3 "" H 7650 6100 50  0001 C CNN
	1    7650 6000
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H158
U 1 1 61859F18
P 7850 5800
F 0 "H158" H 7850 5750 50  0000 C CNN
F 1 "MountingHole_Pad" V 7996 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7850 5800 50  0001 C CNN
F 3 "~" H 7850 5800 50  0001 C CNN
	1    7850 5800
	0    -1   1    0   
$EndComp
$Comp
L Connector:TestPoint H157
U 1 1 61859F1E
P 7450 6200
F 0 "H157" H 7450 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 7596 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7450 6200 50  0001 C CNN
F 3 "~" H 7450 6200 50  0001 C CNN
	1    7450 6200
	0    1    -1   0   
$EndComp
$Comp
L Connector:TestPoint H156
U 1 1 61859F24
P 7450 5900
F 0 "H156" H 7450 5850 50  0000 C CNN
F 1 "MountingHole_Pad" V 7596 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7450 5900 50  0001 C CNN
F 3 "~" H 7450 5900 50  0001 C CNN
	1    7450 5900
	1    0    0    1   
$EndComp
$Comp
L Connector:TestPoint H159
U 1 1 61859F2A
P 7850 6100
F 0 "H159" H 7850 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 7996 6105 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 7850 6100 50  0001 C CNN
F 3 "~" H 7850 6100 50  0001 C CNN
	1    7850 6100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7450 6100 7450 6200
Wire Wire Line
	7850 5800 7850 5900
$Comp
L Sofle:LED_SK6812_Mini_E LED3
U 1 1 6188B6CA
P 8350 6000
F 0 "LED3" H 8350 6050 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 8350 6203 25  0001 C CNN
F 2 "#footprint:SK6812_Mini_E" H 8380 6200 50  0001 C CNN
F 3 "" H 8350 6100 50  0001 C CNN
	1    8350 6000
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H162
U 1 1 6188B6D0
P 8550 5800
F 0 "H162" H 8550 5750 50  0000 C CNN
F 1 "MountingHole_Pad" V 8696 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8550 5800 50  0001 C CNN
F 3 "~" H 8550 5800 50  0001 C CNN
	1    8550 5800
	0    -1   1    0   
$EndComp
$Comp
L Connector:TestPoint H161
U 1 1 6188B6D6
P 8150 6200
F 0 "H161" H 8150 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 6200 50  0001 C CNN
F 3 "~" H 8150 6200 50  0001 C CNN
	1    8150 6200
	0    1    -1   0   
$EndComp
$Comp
L Connector:TestPoint H160
U 1 1 6188B6DC
P 8150 5900
F 0 "H160" H 8150 5850 50  0000 C CNN
F 1 "MountingHole_Pad" V 8296 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8150 5900 50  0001 C CNN
F 3 "~" H 8150 5900 50  0001 C CNN
	1    8150 5900
	1    0    0    1   
$EndComp
$Comp
L Connector:TestPoint H163
U 1 1 6188B6E2
P 8550 6100
F 0 "H163" H 8550 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 8696 6105 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8550 6100 50  0001 C CNN
F 3 "~" H 8550 6100 50  0001 C CNN
	1    8550 6100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	8150 6100 8150 6200
Wire Wire Line
	8550 5800 8550 5900
$Comp
L Sofle:LED_SK6812_Mini_E LED4
U 1 1 6188B6EA
P 9000 6000
F 0 "LED4" H 9000 6050 50  0000 C CNN
F 1 "LED_SK6812_Mini_E" H 9000 6203 25  0001 C CNN
F 2 "#footprint:SK6812_Mini_E" H 9030 6200 50  0001 C CNN
F 3 "" H 9000 6100 50  0001 C CNN
	1    9000 6000
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint H166
U 1 1 6188B6F0
P 9200 5800
F 0 "H166" H 9200 5750 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 5805 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 5800 50  0001 C CNN
F 3 "~" H 9200 5800 50  0001 C CNN
	1    9200 5800
	0    -1   1    0   
$EndComp
$Comp
L Connector:TestPoint H165
U 1 1 6188B6F6
P 8800 6200
F 0 "H165" H 8800 6150 50  0000 C CNN
F 1 "MountingHole_Pad" V 8946 6205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8800 6200 50  0001 C CNN
F 3 "~" H 8800 6200 50  0001 C CNN
	1    8800 6200
	0    1    -1   0   
$EndComp
$Comp
L Connector:TestPoint H164
U 1 1 6188B6FC
P 8800 5900
F 0 "H164" H 8800 5850 50  0000 C CNN
F 1 "MountingHole_Pad" V 8946 5905 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 8800 5900 50  0001 C CNN
F 3 "~" H 8800 5900 50  0001 C CNN
	1    8800 5900
	1    0    0    1   
$EndComp
$Comp
L Connector:TestPoint H167
U 1 1 6188B702
P 9200 6100
F 0 "H167" H 9200 6050 50  0000 C CNN
F 1 "MountingHole_Pad" V 9346 6105 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 9200 6100 50  0001 C CNN
F 3 "~" H 9200 6100 50  0001 C CNN
	1    9200 6100
	-1   0    0    -1  
$EndComp
Wire Wire Line
	8800 6100 8800 6200
Wire Wire Line
	9200 5800 9200 5900
Wire Wire Line
	7200 5650 7200 5800
Connection ~ 7200 5800
Wire Wire Line
	6800 6200 6800 6300
Wire Wire Line
	6800 6300 7300 6300
Wire Wire Line
	7300 6300 7300 5650
Wire Wire Line
	7300 5650 7850 5650
Wire Wire Line
	7850 5650 7850 5800
Connection ~ 6800 6200
Connection ~ 7850 5800
Wire Wire Line
	7450 6200 7450 6300
Wire Wire Line
	7450 6300 7950 6300
Wire Wire Line
	7950 6300 7950 5650
Wire Wire Line
	7950 5650 8550 5650
Wire Wire Line
	8550 5650 8550 5800
Connection ~ 7450 6200
Connection ~ 8550 5800
Wire Wire Line
	8150 6200 8150 6300
Wire Wire Line
	8150 6300 8650 6300
Wire Wire Line
	8650 6300 8650 5650
Wire Wire Line
	8650 5650 9200 5650
Wire Wire Line
	9200 5650 9200 5800
Connection ~ 8150 6200
Connection ~ 9200 5800
$Comp
L Jumper:SolderJumper_3_Open JP105
U 1 1 617D511C
P 3850 1100
F 0 "JP105" H 3850 1213 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 3850 1214 50  0001 C CNN
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 3850 1100 50  0001 C CNN
F 3 "~" H 3850 1100 50  0001 C CNN
	1    3850 1100
	0    1    1    0   
$EndComp
NoConn ~ 3850 900 
Text GLabel 3850 1300 3    50   Input ~ 0
led
$Comp
L Jumper:SolderJumper_3_Open JP106
U 1 1 618D09E4
P 4350 1100
F 0 "JP106" H 4350 1213 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 4350 1214 50  0001 C CNN
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 4350 1100 50  0001 C CNN
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
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 4900 1100 50  0001 C CNN
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
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 5500 1100 50  0001 C CNN
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
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 1800 950 50  0001 C CNN
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
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 1450 950 50  0001 C CNN
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
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 1100 950 50  0001 C CNN
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
F 2 "#footprint:ArduinoProMicro-ZigZag_rev5" H 2850 1100 60  0001 C CNN
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
F 2 "#footprint:SolderJumper-3_P1.3mm_Open_TrianglePad1.0x1.5mm_duplex" H 700 950 50  0001 C CNN
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
P 5800 4850
F 0 "#PWR0116" H 5800 4600 50  0001 C CNN
F 1 "GND" H 5800 4700 50  0000 C CNN
F 2 "" H 5800 4850 50  0001 C CNN
F 3 "" H 5800 4850 50  0001 C CNN
	1    5800 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 4750 5800 4750
Wire Wire Line
	5800 4750 5800 4850
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
P 3600 4250
F 0 "R101" V 3550 4250 50  0000 C CNN
F 1 "50R" V 3650 4250 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 3600 4250 50  0001 C CNN
F 3 "~" H 3600 4250 50  0001 C CNN
	1    3600 4250
	0    1    1    0   
$EndComp
Wire Wire Line
	3800 4250 3700 4250
Wire Wire Line
	3500 4250 3400 4250
Connection ~ 9600 4350
Wire Wire Line
	10700 4350 10650 4350
$Comp
L Connector:TestPoint H170
U 1 1 617932EC
P 9500 4250
F 0 "H170" H 9400 4450 50  0000 L CNN
F 1 "MountingHole_Pad" H 9600 4210 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 9500 4250 50  0001 C CNN
F 3 "~" H 9500 4250 50  0001 C CNN
	1    9500 4250
	0    1    1    0   
$EndComp
Connection ~ 9500 4250
Wire Wire Line
	9500 4250 9500 4450
$Comp
L Connector:TestPoint H171
U 1 1 617E0E69
P 10550 4250
F 0 "H171" H 10450 4450 50  0000 L CNN
F 1 "MountingHole_Pad" H 10650 4210 50  0001 L CNN
F 2 "#footprint:1pin_conn" H 10550 4250 50  0001 C CNN
F 3 "~" H 10550 4250 50  0001 C CNN
	1    10550 4250
	0    1    1    0   
$EndComp
Connection ~ 10550 4250
Wire Wire Line
	10550 4250 10550 4450
$Comp
L Connector:TestPoint H168
U 1 1 617E13D0
P 4300 4250
F 0 "H168" V 4300 4500 50  0000 C CNN
F 1 "MountingHole_Pad" V 4446 4255 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 4300 4250 50  0001 C CNN
F 3 "~" H 4300 4250 50  0001 C CNN
	1    4300 4250
	1    0    0    -1  
$EndComp
Connection ~ 4300 4250
Wire Wire Line
	4300 4250 4400 4250
$Comp
L Connector:TestPoint H169
U 1 1 617E23BC
P 4750 4200
F 0 "H169" V 4750 4450 50  0000 C CNN
F 1 "MountingHole_Pad" V 4896 4205 50  0001 C CNN
F 2 "#footprint:1pin_conn" H 4750 4200 50  0001 C CNN
F 3 "~" H 4750 4200 50  0001 C CNN
	1    4750 4200
	0    1    1    0   
$EndComp
Connection ~ 4750 4200
Wire Wire Line
	4750 4200 4750 4300
Wire Wire Line
	9650 4350 9600 4350
Text GLabel 9650 4350 2    50   Input ~ 0
X9
Text GLabel 9400 4300 1    50   Input ~ 0
X10
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
$EndSCHEMATC
