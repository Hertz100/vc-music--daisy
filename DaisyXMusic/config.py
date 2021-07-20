# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC8Yg1EbZ-wsWo9B43lw1sSbEBgDKEeG8TQlCLUgrmd0cFsR3OxFNs1LiWJ503xDf6Js5BCyAiP5ErJs0EB-L8bpEUDusxON-SjC8Y8Q9fru8o16JDbeS2asZHSe30raTl8CsPCpQ8Ed_fPmyX6b81dpCgZ-B5FYpfICao5tPYzVXqgah5C9SI1ng4EpkEpfrWIb52QSq8wOnWNHH8a71nCWEEKsyBUwkTkmT4CHVtucaL3VjBMyePz4K6UAp95J8QSt7pfsWBjPXRXIwIzpT2yfx8GDTw5tRENxtVEYEUdt7sUOz01rxpL76NZFZBPeiEFkcOMnn0FFxe8hmKygycsAS2AA")
BOT_TOKEN = getenv("BOT_TOKEN", "1622866660:AAFzAap2GH8i6b2JTBDctJztm2QhQunwCfk")
BOT_NAME = getenv("BOT_NAME", "Eliana_Assistant")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "luminous_robot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/08f5b16938ec55dc9cbc7.jpg")
admins = {}
API_ID = int(getenv("API_ID", "7659384"))
API_HASH = getenv("API_HASH", "3b61e8d32b1b6386bf2bc8764504e23e")
BOT_USERNAME = getenv("BOT_USERNAME", "ElianaPro_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Eliana_Assistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "shapphiree")
PROJECT_NAME = getenv("PROJECT_NAME", "Eliana")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamOfDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
