## Log your stuff into Discord!

### Main features:
In this project top level logger with name 'app' created and then with separate 
Cog extends it to let sending logs right into Discord channel. Implementation 
via Cog allows to create modular structure of bot and easily add logging to any 
existing bot. Moreover, Cogs can be attached and detached on-the-fly, without 
restarting the bot ([example](https://github.com/noirscape/dynamic-cog-bot-template)).

Custom **DiscordEmbedFormatter** creates Embed messages of usual log records, so they look pretty.

Custom **CreditCardFilter** filters off card numbers of records.

Refer to 
- [custom handler, formatter, filter](/src/cogs/logger)
- [base logger](/src/basic_project_logger.py)
- its settings [yaml file](/src/logging.yaml)

### Installation:
- Clone repository

### How to use:
- Create a new bot ([howto](https://discordpy.readthedocs.io/en/stable/discord.html)), remember bot token!
- Create `.env` file at root folder (rename and fill `.env.example`)
- Run `make up`
- Invite your bot to server ([howto](https://discordjs.guide/preparations/adding-your-bot-to-servers.html#adding-your-bot-to-servers))
- Run `!synchere` command in any channel. It will sync all slash commands on you server and they become available.

### OR
- Consider joining [my test server](https://discord.gg/qNarsbEHgq) with bot running and ready-to-use playground to test all functions.