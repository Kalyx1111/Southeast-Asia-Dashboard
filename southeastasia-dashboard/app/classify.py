"""Routes every headline into one of the China v6 dashboard's 15 headings, applied to South-East Asia and the South China Sea.

Order matters: the most specific headings first (darkweb, cyber, hazard, armed groups, internal security, naval, maritime
chokepoints, air, space, weapons and nuclear programmes, military operations, technology, economy, social, wellbeing), then
geopolitics as the default. Short words match whole words only, so " rat " does not match "rate".
"""
import re

HEADINGS = ["geo", "milops", "arms", "naval", "scs", "air", "space", "tech", "cyber", "darkweb",
            "econ", "mss", "social", "wellbeing", "hazard"]

RULES = [
    ("darkweb", ["dark web", "darknet", "onion", "ransomware", "leak site", "infostealer", "stealer", "data breach",
                 "data leak", "threat intel", "threat intelligence", "initial access broker"]),
    ("cyber", ["cyber", "hacker", "hacked", "hacking", "malware", "vulnerabilit", "intrusion", "phishing", "ddos",
               "zero-day", "cyberattack", "apt30", "apt40", "wiper", "scam", "scam centre", "scam center", "scam compound",
               "cybercrime", "online fraud", "cyber scam", "crypto scam", "kk park", "shwe kokko"]),
    ("hazard", ["earthquake", "tremor", "flood", "floods", "sandstorm", "heatwave", "heat wave", "cyclone", "typhoon",
                "tropical storm", "monsoon", "storm", "drought", "wildfire", "landslide", "tsunami", "volcan", "eruption",
                "haze", "smog"]),
    ("milops", ["hezbollah", "houthi", "houthis", "hamas", "kataib", "arakan army", "kachin independence army",
                "karen national army", "tatmadaw", "junta", "popular mobilization", "quds force"]),
    ("mss", ["mossad", "espionage", "spy", "spying", "sleeper cell", "informant", "intelligence service", "crackdown",
             "executed", "executions", "arrested", "detained", "assassinat", "counterintelligence", "dissident", "interrogation"]),
    ("naval", ["navy", "naval", "submarine", "warship", "frigate", "destroyer", "corvette", "minesweeper", "fifth fleet",
               "kilo-class", "scorpene", "scorpène", "invincible-class", "submarine base", "naval base", "shipyard", "fleet",
               "coast guard", "irin", "irgc navy", "irgc-n", "midget submarine", "sea trial"]),
    ("scs", ["south china sea", "west philippine sea", "spratly", "paracel", "scarborough", "second thomas", "ayungin",
             "mischief reef", "subi", "fiery cross", "antelope reef", "itu aba", "taiping", "strait of malacca", "malacca",
             "sunda strait", "lombok", "makassar strait", "natuna", "tanker", "shipping", "blockade", "sea lane",
             "taiwan strait", "bashi", "luzon strait", "gulf of tonkin", "gulf of thailand", "tiran", "hainan"]),
    ("air", ["air force", "airbase", "air base", "fighter jet", "f-35", "f-15", "f-16", "su-30", "su-27", "airspace",
             "airport", "helicopter", "air defense", "air defence", "interceptor", "patriot", "uav", "cn235"]),
    ("space", ["satellite", "space program", "rocket launch", "launch site", "orbit", "spacecraft", "space agency",
               "wenchang", "space launch"]),
    ("arms", ["nuclear", "enrichment", "enrich", "uranium", "reactor", "iaea", "centrifuge", "ballistic", "warhead",
              "munition", "ammunition", "weapons", "drone production", "shahed", "missile production", "rocket fuel",
              "bunker buster", "bunker-buster", "arms deal", "arms sale", "brahmos", "missile battery", "vver",
              "ninh thuan", "isotope", "bastion"]),
    ("milops", ["drone attack", "drone strike", "strike", "strikes", "airstrike", "attack on", "missile attack",
                "missiles hit", "missiles struck", "troops", "army", "soldier", "soldiers", "offensive", "military operation",
                "military drill", "invasion", "clashes", "clash", "shelling", "edca", "balikatan", "joint drill", "golden dragon",
                "idf", "centcom", "pentagon", "us forces", "u.s. forces", "bases", "base struck", "killed in strike", "kia"]),
    ("tech", [" ai ", "artificial intelligence", "chips", "semiconductor", "export control", "digital", "technology"]),
    ("geo", ["talks", "negotiat", "summit", "mediat", "memorandum", "diplomat", "asean", "code of conduct", "treaty"]),
    ("econ", ["oil", "crude", "lng", "pipeline", "gas prices", "trade", "tariff", "sanctions", "exports", "imports", "inflation",
              "economy", "economic", "energy", "brent", "budget", "investment", "fuel prices", "special economic zone"]),
    ("social", ["protest", "protests", "human rights", "refugee", "refugees", "displaced", "civilians", "humanitarian",
                "famine", "hunger", "aid workers", "students", "women", "trafficking", "trafficked", "rohingya"]),
    ("wellbeing", ["happiness", "wellbeing", "well-being", "life expectancy", "poverty index", "human development index"]),
]

_SHORT = {"spy", "iaea", "kia", "ai", "uav", "subi", "irin", "bases", "oil", "lng", "tiran", "ied", "shahed", "enrich", "uranium"}


def _has(text: str, word: str) -> bool:
    if " " in word or "-" in word or "'" in word or "." in word or "/" in word or "è" in word or "é" in word:
        return word in text
    if word in _SHORT or (len(word) <= 4 and word.isalpha()):
        return re.search(r"\b" + re.escape(word) + r"\b", text) is not None
    return word in text


def classify(text: str) -> str:
    t = " " + (text or "").lower() + " "
    for heading, words in RULES:
        if any(_has(t, w) for w in words):
            return heading
    return "geo"
