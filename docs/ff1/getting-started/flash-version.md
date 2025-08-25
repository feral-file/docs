# **Installing the Feral File System**

This guide will walk you through the process of flashing the Feral File system image to a USB drive and installing it on your device.

## **Part 1: Preparing the Bootable USB Drive**

First, you will need to download the necessary software and the system image, then flash the image onto a USB drive.

1. **Download and Install BalenaEtcher:** If you don't already have it, download and install BalenaEtcher, a tool for flashing OS images.  
2. **Download the System Image:**  
   * **URL:** [https://ff1.feral-file.workers.dev](https://ff1.feral-file.workers.dev){target="_blank"}
   * **Account/password:** feralfile/portal
   * Download the latest image on the branch `release`
3. **Flash the Image:**  
   * Open BalenaEtcher.  
   * Click **“Flash from file”** and select the .zip image file you just downloaded.  
   * Under **“Select target,”** choose your USB drive. Be careful to select the correct drive, as this process will erase all data on it.  
   * Click **“Flash\!”** and wait for the process to complete and verify.

## **Part 2: Installing the System**

Now you will boot your device from the USB drive to begin the installation.

1. **Insert the USB Drive:** Plug the newly flashed USB drive into your device.  
2. **Boot into Selection Menu:** Power on the device and repeatedly press the **F7** key during startup until a blue boot selection screen appears.  
3. **Select Boot Device:** From the menu, select your USB drive as the boot device.  
4. **Complete Installation:** Follow the installation wizard to complete the setup. The device will automatically shut down once finished.  
5. **Final Step:** Remove the USB drive from the device.  
6. **First Boot:** Power on the device again to start using your new system.