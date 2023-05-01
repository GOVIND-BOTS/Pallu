from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "27424332"))
API_HASH = getenv("API_HASH", "cb93e76ed8e78c8081f52cd3aa66f08b")

BOT_TOKEN = getenv("BOT_TOKEN", "6268640520:AAF8YfhXa1hMgQbe9FvwtBoxmyCrrfj1S90")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5348648456"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/5065cd217f3b87e2fd0ac.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/a54d2b44cc241e0f9e231.jpg")

SESSION = getenv("SESSION", "BQCTlX1Ytlra4FSM5aQNuo0HDGiBAuiqRpZeDnpmpaN9QNwI5SfxIzX9OFmMF5BMZHyG5znRmr-JWCfAFJ0epJUO3BTKRGYHLOREJBan2gf2lki9ERwPtDvnO8hHgR38Z3D12ezwCCPsM-jx9sBw7cHqiXJQcu_TvipJpVVuweU3GfLfUbOxASlEgKaFh_Cip07fZPV-JQ_nHANqFox9dugf9U2y7tOKAUSNnEkjA4M0j2ylov8YrtJbl3c3omoReS9vfAOGpxSLOsqi1AxkGns2d0Fq9_ZsMUkGnYhegDKrX35XtJ-C8NzHCVCvOacWk5d7qfk86rDTAcTogrnRemOSAAAAAWuV21wA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_chatting_club_offical")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shayari_ka_tadka")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6008136265").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
