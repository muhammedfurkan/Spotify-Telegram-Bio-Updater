CLIENT_ID = ""
CLIENT_SECRET = ""
API_ID = 0
API_HASH = ""
INITIAL_TOKEN = ""
INITIAL_BIO = ""
LOG = "me"
# the escaping is necessary since we are testing against a regex pattern with it.
SHUTDOWN_COMMAND = "\/\/stop"
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
KEY = "🎶"
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [
    KEY + " Now Playing: {interpret} - {title} {progress}/{duration}",
    KEY + " Now Playing: {interpret} - {title}",
    KEY + " : {interpret} - {title}",
    KEY + " Now Playing: {title}",
    KEY + " : {title}",
]
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
