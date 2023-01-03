# DrKnow

This very simple bot uses OpenAI and InstructGPT to run a Discord bot.

The InstructGPT examples are in [DrKnow.py](DrKnow.py), and currently result in a fairly irreverant technology Q&A bot that knows dad jokes.

To use, you will need an OpenAI token and Discord API token.

First, copy the [.env.example](.env.example) file to `.env`:

    cp .env.example .env

Now edit that .env file with the appropriate credentials.

Running the bot should be as simple as running `make`:

    make

Which just runs these docker-compose steps:

    docker-compose build
    docker-compose up --force-recreate -d
    docker-compose logs -f

Enjoy!
