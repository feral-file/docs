# Running FF1 OS on Mac with QEMU

This guide explains how to use QEMU to emulate the FF1 OS on a Mac. It is intended for technical users familiar with the command line.

It's just for testing purpose.

Note: This guide assumes you are comfortable with the terminal and basic Unix commands. For further help, consult the FF1 OS community or documentation.

## Prerequisites

- macOS
- Homebrew package manager installed
- Install qemu via brew

    ```bash
    brew install qemu
    ```

## Usage

1. Clone the Repository

    - Clone the FF1 OS repository to your local machine:

    ```bash
    git clone https://github.com/feral-file/ffos.git
    cd ffos/qemu/MacOS
    ```

2. Download the FF1 OS QEMU ISO
    - Download the QEMU-specific ISO image for FF1 OS from the official distribution site: <https://ff1.feral-file.workers.dev/>
    - Download the QEMU iso file
    - Place the ISO file in the `ffos/qemu/MacOS`
3. Install the QEMU Script
    - The repository provides a script to automate QEMU setup and launch.

    ```bash
    ./install.sh FF1-other-qemu-0.0.1.iso
    ```

    The script will:

    - Check for Homebrew and QEMU, and install QEMU if missing
    - Copy required firmware files
    - Create a virtual disk image (ff1.qcow2)
    - Launch QEMU with recommended settings for FF1 OS
    - Install FF1 OS and shutdown the virtual machine
4. Run the QEMU VM
    - Run the script to start running the installed FF1 OS.

    ```bash
    ./run.sh
    ```

5. Accessing the Virtual Machine
    - The VM will open in a new window using QEMU's Cocoa display.
    - SSH access is forwarded to localhost:2222

    ```bash
    ssh -p 2222 feralfile@localhost
    ```

6. Troubleshooting
    - Ensure the ISO path is correct and the file exists.
    - If you encounter permission issues, try `chmod +x install.sh run.sh`.
