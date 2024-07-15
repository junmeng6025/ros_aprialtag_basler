# BASLER Setup
## Install and setup
followed the official Document: https://zh.docs.baslerweb.com/software-installation-(linux)
### Check our BASLER camera type:
`acA1920-40gc`
### Download and setup `pylon`
Download:  
https://zh.docs.baslerweb.com/software-installation-(linux)#:~:text=Suite%20Linux%20%E7%89%88%E3%80%82-,%E5%AE%89%E8%A3%85,-%23  
Build and install:  
```
Installation using tar.gz files
===============================

This installation procedure assumes that you are going to install the
pylon Camera Software Suite in the /opt/pylon directory. If you choose
to install in a different directory, you'll have to modify the 
directory names accordingly.
Note: Root permissions are needed to write to /opt.

To install the pylon 6 Camera Software Suite in /opt/pylon
follow these steps:
```

- 1. Change to the directory that contains the pylon setup tar.gz archive that
     you downloaded from the Basler website.
- 2. Extract the setup tar.gz archive into a directory of your choice (replace
     ./pylon_setup if you want to extract into a different directory):
```bash
mkdir ./pylon_setup
tar -C ./pylon_setup -xzf ./pylon*_setup.tar.gz
```
- 3. Change to the directory into which you extracted the setup tar.gz:
```bash
cd ./pylon_setup
```
- 4. Defaultly we build the pylon to /opt/pylon
```bash
# FIRE UP A NEW TERMINAL
cd /opt
sudo mkdir pylon
```
- 5. Extract the pylon SDK into /opt/pylon:
```bash
# BAKC TO THE TERMINAL BEFORE, i.e. in the directory /pylon_setup
sudo tar -C /opt/pylon -xzf ./pylon*.tar.gz
```
- 6. Change access rights of the pylon folder:
```bash
sudo chmod 755 /opt/pylon
```
Have any confuse, chech this step-by-step tutorial: https://www.forecr.io/blogs/connectivity/pylon-installation-for-basler-camera
### Check the connection
Connect the cam to the laptop with Ethernet cable, and make sure the power cable also connected.
```bash
cd /opt/pylon/bin
sudo ./PylonGigEConfigurator auto-all
```
it should return
```bash
******************************************************************
*  PylonGigEConfigurator 1.0.0.0 - Copyright (c) 2022 Basler AG  *
******************************************************************
Optimizes system and network settings for Basler GigE cameras.
Note: Before using this tool, make sure only cameras are connected to your network adapter(s).


Auto configuration is looking for network adapters and cameras ...
Adapter "docker0" (172.17.0.1) has no camera attached. Excluding adapter from optimization.
Adapter "wlo1" (10.181.82.41) (RTL8822CE 802.11ac PCIe Wireless Network Adapter) has no camera attached. Excluding adapter from optimization.
Adapter "eno1" (192.168.3.2) (RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller):
Found device: Basler acA1920-40gc (00:30:53:33:46:07)
Optimizing adapter eno1: Setting packet size to 9000.
*** Optimize system settings ***
Adjusted rtprio to 99 in /etc/security/limits.conf.
Disabled rp_filter for network eno1.
Added 'net.ipv4.conf.eno1.rp_filter=0' to /etc/sysctl.conf.
Disabled rp_filter for network all.
Added 'net.ipv4.conf.all.rp_filter=0' to /etc/sysctl.conf.
Adjusted net.core.rmem_max value to 32 MB.
Added 'net.core.rmem_max=33554432' to /etc/sysctl.conf.
ethtool isn't installed. Further configuration not possible.
Install the ethtool package: 'sudo apt-get install ethtool'.
IP address already assigned to adapter "eno1". IP: 192.168.3.2, Mask: 255.255.255.0 [24]. No changes required.
IP address already assigned to device "Basler acA1920-40gc (00:30:53:33:46:07)". IP: 192.168.3.3, Mask: 255.255.255.0 [24]. No changes required.
Reboot the system to make the parameter change permanent.
```
this message might vary due to pylon versions, but should NOT show any content about "error"  

### View the capture:
```bash
cd /opt/pylon/bin
sudo ./pylonviewer 
```
Follow the [official document](https://www.forecr.io/blogs/connectivity/pylon-installation-for-basler-camera#:~:text=Then%20the%20user%20interface%20window%20opens.%20Click%20the%20%22Basler%20acA2440%2D35um%22%20option%20under%20USB%20title.)  
Since we connect the BASLER cam via Ethernet cable instead of USB, our cam should be under the category `GigE`  

If the pylonviewer failes to diaplay, try the python script below:

### Write a test script
Refered to the github repo: https://github.com/basler/pypylon
OpenCV script: https://github.com/basler/pypylon/blob/master/samples/opencv.py
```python
'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(
        5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        cv2.namedWindow('title', cv2.WINDOW_NORMAL)
        cv2.imshow('title', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()

# Releasing the resource
camera.StopGrabbing()

cv2.destroyAllWindows()

```
### Run the OpenCV test
Just connect Ethernet cable and power cable for the camera before running the .py script
