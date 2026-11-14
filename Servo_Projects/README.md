# Raspberry Pi Servo Control System
This is a simple project proofing out how to control a servos from a Raspbery Pi.
The simple_servo_control.py just cycles between 0, 90, and 180 degrees, repeated until you cancel the script.

The updated versionm, `app.py`, controls the servos from a static, locally hosted webpage, accessible from your network.

## 🛠 Hardware Requirements
* Raspberry Pi (I used a Raspberry Pi 3 B+)
* Breadboard
* Basic 9g servo with JR leads
* 330 ohm resistor
* Jumper wires

## 🔌 Wiring Diagram (Breadboard View)
```text
	Raspberry Pi 3 B+         Breadboard				Servo
    +---------------+
    |               |
    | [Ground Pin]--|---------------------------------( Brown Lead )--|
    |               |
    | [5v Pin] -----|-----------------------------------( Red Lead )--|		Servo 1
    |               |
    | [GPIO 7] -----|-------[330 omhm Resistor]------( Orange Lead )--|
    |               |
    |               |
    | [Ground Pin]--|---------------------------------( Brown Lead )--|
    |               |
    | [5v Pin] -----|-----------------------------------( Red Lead )--|		Servo 2
    |               |
    | [GPIO 11] ----|-------[330 omhm Resistor]------( Orange Lead )--|
    |               |
    +---------------+
 ```

## 🚀 Getting Started

### 1. Preparation
* Setup your Raspbery Pi with SSH.
* Install Python on the Raspbery Pi.
* Download all contents of this repository to your local machine.
* Extract/Open the folder.
* Install the Brown Lead to the Ground Pin on the Raspberry Pi.
* Install the Red Lead to the 5v Pin on the Raspberry Pi.
* Install the Orange Lead to the Breadboard, 330 ohm resistor, and then to the GPIO 7 (BCM 4) Pin on the Raspberry Pi.

### 2. Raspberry Pi Connect / Screen Sharing Setup
From the terminal, run these commands:
1. sudo apt update && sudo apt full-upgrade -y
2. sudo apt install rpi-connect
3. rpi-connect on
4. rpi-connect signin
5. On your PC: Go to Raspberry Pi Connect - https://connect.raspberrypi.com/, sign in, and choose Screen Sharing (GUI) or Remote Shell (terminal)

### 3. Install Python
1. sudo apt update && sudo apt upgrade -y
2. sudo apt install -y python3 python3-pip python3-venv
3. sudo apt autoremove

### 4. Install File Sharing Capabilities 
* You must have a username and password on your network share
1. sudo apt install smbclient -y
2. sudo mkdir -p /mnt/nas
3. sudo mount -t cifs //NAS_SHARE /mnt/nas \ -o username=NAS_USER,vers=3.0,sec=ntlmssp,uid=1000,gid=1000
	*	*My config - sudo mount -t cifs //dsXXX/XXXShare /mnt/nas \ -o username=piXXXX,vers=3.0,sec=ntlmssp,uid=1000,gid=1000*
4. sudo nano /etc/samba/credentials
*	*Add*
	*username=YOUR_NETWORK_SHARE_USERNAME*
	*password=YOUR_NETWORK_PASSWORD*
	*Save and Exit*
	*sudo chmod 600 /etc/samba/credentials*
5. Make the share persistent
*	*sudo nano /etc/fstab*
	*Add this line at the bottom:*
		*//dsXXX/XXXShare /mnt/nas cifs credentials=/etc/samba/credentials,vers=3.0,sec=ntlmssp,uid=1000,gid=1000,_netdev,nofail,x-systemd.automount 0 0*
		*Save and Exit*
	*Test Share*
		*sudo systemctl daemon-reload*
		*sudo mount -a*
		*ls -ls /mnt/nas*
		*findmnt /mnt/nas*
		*sudo reboot*
		*After Reboot:*
		*ls -la /mnt/nas*
		*If you see your network files, you're good to go*

### 5. Copy files to the Raspberry Pi
1. SSH to the Raspberry Pi
2. Copy all the files of the repo to the Raspberry Pi

### 6. Simple Servo Control
1. From the Raspberry Pi, navigate to the folder you copied the repo files to
2. python simple_servo_contro.py
3. Servos will cycle between 0, 90, and 180 degrees until you CTRL + C 



### 7. Web Interface Setup
1. On Raspberry Pi, `sudo apt install python3-flask`
2. On Raspberry Pi, `sudo apt install python3-gpiozero`
2.  **Run the app**:
*	*In the folder containing `app.py`, run:*
	*	*`python app.py`*
3.  **Access the page**:
    On any device connected to your network, open a web browser and type:
    `http://<IP_ADDRESS>:5000`
4. Click the corresponding buttons to control the servo position.



## ✨ Features
* simple_servo_control is a looping program that moves the servo from neutral, to 0 degrees, to 180 degrees.
* app.py launches a background application to control the servos via the index.html from your PC on the same network.

## ✨ Other Notes
// To get Raspberry Pi CPU temp
* vcgencmd measure_temp | awk -F "[=']" '{print ($2 * 1.8) + 32 "°F"}'
