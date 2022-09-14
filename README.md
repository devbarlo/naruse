## naruse
![Python Version](https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor)
![LICENSE](https://img.shields.io/github/license/TeamKillerX/naruse?style=for-the-badge&logo=appveyor)
![Contributors](https://img.shields.io/github/contributors/TeamKillerX/naruse?style=for-the-badge&logo=appveyor)
![Repository Size](https://img.shields.io/github/repo-size/TeamKillerX/naruse?style=for-the-badge&logo=appveyor)
<img src="https://github-readme-stats.vercel.app/api?username=TeamKillerX&show_icons=true" alt="TeamKillerX GitHub Stats">

# Clients
## Importing Telethon
```python3
from naruse import telethn
```
## Importing Pyrogram
```python3
from naruse import pbot
```
## Importing ARQ
```python3
from naruse import arq
```
## Importing aiohttp
```python3
from naruse import aiohttp
```
# DataBase
## Importing Postgres
```python3
from naruse.modules.sql import SESSION
```

### Database

If you wish to use a database-dependent module (eg: locks, notes, userinfo, users, filters, welcomes),
you'll need to have a database installed on your system. I use postgres, so I recommend using it for optimal compatibility.

In the case of postgres, this is how you would set up a the database on a debian/ubuntu system. Other distributions may vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and db name.

## Modules
### Setting load order.

The module load order can be changed via the `LOAD` and `NO_LOAD` configuration settings.
These should both represent lists.

If `LOAD` is an empty list, all modules in `modules/` will be selected for loading by default.

If `NO_LOAD` is not present, or is an empty list, all modules selected for loading will be loaded.

If a module is in both `LOAD` and `NO_LOAD`, the module will not be loaded - `NO_LOAD` takes priority.

### Creating your own modules.

Creating a module has been simplified as much as possible - but do not hesitate to suggest further simplification.

All that is needed is that your .py file be in the modules folder.

To add commands, make sure to import the dispatcher via

`from naruse import dispatcher`.

You can then add commands using the usual

`dispatcher.add_handler()`.

Assigning the `__help__` variable to a string describing this modules' available
commands will allow the bot to load it and add the documentation for
your module to the `/help` command. Setting the `__mod_name__` variable will also allow you to use a nicer, user
friendly name for a module.

The `__migrate__()` function is used for migrating chats - when a chat is upgraded to a supergroup, the ID changes, so 
it is necessary to migrate it in the db.

The `__stats__()` function is for retrieving module statistics, eg number of users, number of chats. This is accessed 
through the `/stats` command, which is only available to the bot owner.

## Support and Help:
We do not provide any support or help or take any questions or queries around this repo, if you want to deploy it you are on your own, learn to read or ask in some python dev group or stalkoverflow, the internet is your learning ground - but do NOT come our support group asking any help around the code or the repo, you will get immediately banned and just cussed at. 

We did not run this bot or this repo to feed every entititled user who demands our dedicated time and attention, we are tired of it and the horrible community around kangs.

## Credits [DEV]
* [TeamKillerX/Randi356](https://github.com/TeamKillerX)
* [PaulSonOfLars](https://github.com/PaulSonOfLars) 
* [Kigyo](https://github.com/AnimeKaizoku/EnterpriseALRobot)
* [TheHamkerCat](https://github.com/TheHamkerCat/WilliamButcherBot)
* [SaitamaRobot](https://github.com/AnimeKaizoku/SaitamaRobot)
* [szsupunma](https://github.com/szsupunma/sz-rose-bot)
* [TeamDaisyX](https://github.com/TeamDaisyX)
