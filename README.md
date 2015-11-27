# Telegram Bots
---
The following is a description of requirements and TODO's for our personal bots development. You can fork it or whatever but it's not really intended for public release.
---

## Language
Bots will be written in python using the [Telebot Library](https://github.com/yukuku/telebot)

## Requirements

The bots should have:

* A start/stop mechanism that allows users to control bot's usage

* A helper command with documentation/description of what the different commands do

* Modular functionalities separated by purpose in a way that accurately and explicitly describes it's purpose, eg:
  > games/dice_roll; games/tic-tac-toe;

  > utils/news; utils/git_status; utils/trending;

  > admin/room_status; admin/user_history; admin/user_mute;

* An API that supports expansion and modules written in several programming languages

* Some other stuff i'm forgetting atm
