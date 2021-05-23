![](https://media.discordapp.net/attachments/844185675489607690/845581142701637672/Logo.png)

<!-- Badges -->

[![Donate](https://img.shields.io/badge/$-support-ff69b4.svg?style=flat-square)](https://paypal.me/WalkxCode)

![](https://img.shields.io/github/languages/code-size/WalkxCode/SaladCLI_Plus?style=flat-square) ![](https://img.shields.io/github/downloads/WalkxCode/SaladCLI_Plus/total?style=flat-square) ![](https://img.shields.io/github/license/WalkxCode/SaladCLI_Plus?style=flat-square) ![](https://img.shields.io/github/stars/WalkxCode/SaladCLI_Plus?style=flat-square)
![](https://img.shields.io/github/v/release/WalkxCode/SaladCLI_Plus?style=flat-square) ![](https://img.shields.io/github/v/tag/WalkxCode/SaladCLI_Plus?style=flat-square) [![Website](https://img.shields.io/website?down_color=red&down_message=offline&style=flat-square&up_color=green&up_message=online&url=https%3A%2F%2Fwalkyltd.xyz)](https://walkyltd.xyz/saladcli)

#### Support server
[![Discord Banner 2](https://discordapp.com/api/guilds/836251413544828929/widget.png?style=banner2)](https://discord.gg/D2VBbJDz8c)

<!-- End Badges -->

---

> Salad CLI+ uses your AUTH code to view your balance, lifetime balance, xp and referral code using the Salad API. Devs can not see your code.

---

## Features
- Increased earnings
  + Salad CLI+ can increase your earnings by using different pools and a optimization script. This doesn't mean everyone will get increased earnings, but some users have got more than 2x earnings.

- In-depth View
  + Salad CLI+ gives you an in-depth view of what the miners are doing, by showing you the miner in the fore-ground. You can see your Hashrate, Accepted shares, New jobs. Etc.

- More control
  + In Salad CLI+ you control the miners. You can choose your region and the miner yourself! All in a easy to use Command line interface.



<!-- Install guide -->

## How to install Salad CLI+

#### Getting ready
###### Downloading Salad CLI+
1. Download the [Latest release](https://github.com/WalkxCode/SaladCLI_Plus/releases/latest) of Salad CLI+.

###### Downloading / Installing Python
1. Go to https://www.python.org/ and Download the latest version.
2. Open the installer.
3. **On the first page make sure to click "Install python to PATH".** *If you don't do this Salad CLI+ won't run.*
4. Click install now.
    + If you get a pop-up saying "Disable PATH length." make sure to click and enable it.


#### Configuring

###### How to find your AUTH code? (Skip this step if you're using the Mining only edition.)
1. Go to app.salad.io
2. Login with your Salad account.
3. Click on the Cookies icon ![](https://images-ext-2.discordapp.net/external/307zW6hU-4O2g0TaCN3VXR29D-byDrPOxcvtV7k5fTs/https/i.imgur.com/rCpRXdW.png) on the left side of the Search bar.
4. Click on "Cookies".
5. Open the `app-api.salad.io` folder in the cookies.
6. Open `Salad.Authentication`.
7. **Right-Click** on the **Content** in the `Salad.Authentication` cookie, and click **Select-all**.
8. **Right-Click** and click **Copy**.

###### How to find your wallets?
1. Completely close Salad. (Make sure to close it from the taskbar too.)
2. Re-open Salad and **Mine** for 5 minutes. *This does not include prepping time.*
3. Go to the "Earn" tab.
4. On the left side click "Miner Details" in the menu.
5. Scroll down until you see the "Show Folder" button and click it.
6. Open the main.log file.
7. Press **Ctrl+F** and search for "Wallet".
8. Here you will see "Nicehash Wallet", "Nicehash RigId", "Ethermine wallet", and "Ethermine WorkerID".
9. These are your wallets and RigId's.

###### Generating the config.json
1. Go to the [Salad CLI+ Config Generator](https://tpelaaja.github.io/Configure-CLI/#/asf).
2. Choose the version of Salad CLI+ you're using (eg. v5/6, v7, v7 only mining edition.).
3. Fill in your AUTH code, Wallet(s) and RigID like  shown.
4. Click the "Download" button to download your config.json.
5. Put the config.json file in the Salad CLI+ folder.


---
#### Using Salad CLI+

##### ! Before your first run, make sure to run Setup.bat.

###### Starting Salad CLI+
- To start Salad CLI+, run the Start<span></span>.py file.

###### Selecting a option from the menu
- To select a option from the menu, press the corresponding key on your keyboard and press enter.

###### Quiting Salad CLI+
- To quit Salad CLI+ simply close the program.

---
#### Bugs and Fixes

###### Start<span></span>.py closes directly after running.
- Make sure you have python installed to PATH.
  + [Guide](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows)

- Make sure you've ran Setup.bat.

###### "Python cannot be found"
- Make sure you have python installed to PATH.
  + [Guide](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows)

###### Phoenixminer Kernel error
- Join the [Support Discord Server](https://discord.gg/D2VBbJDz8c). And we will send you a custom Mining<span></span>.py file.

###### Cannot find 'wallet'
- Try refreshing the logs, like shown above.

###### Can't find the Salad AUTH code / Can't open cookies.
- Make sure you're logged in on app.salad.io
- Try another browser. (eg. Chrome / Brave)

###### Salad AUTH code error when launching Start<span></span>.py
- Re-copy the AUTH code.
  + Your AUTH code should be 600+ characters.

- Refresh app.salad.io
- Try another browser. (eg. Chrome / Brave)

- Re-login on app.salad.io

###### The Setup.bat immediately closes after launching / Gives an error.
- Make sure you installed python to PATH. https://datatofish.com/add-python-to-windows-path/


###### Other issues / Bugs.
- Join the [Support Discord Server](https://discord.gg/D2VBbJDz8c)





