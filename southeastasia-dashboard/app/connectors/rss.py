"""RSS aggregator - free, no key. English-language feeds only.

Feed URLs are either confirmed from a publisher's own feed (SpaceNews returned
live items during verification), or listed in a feed directory (FeedSpot)
pending the connector's own live check. Each feed reports its own status and
fails independently. World-wide feeds keep only region-relevant headlines.
"""
from __future__ import annotations
import re
from .base import Item, ConnectorResult
from ..classify import classify

NAME = "rss"

FEEDS = [
    {"url": "http://myanmargazette.net/feed", "source": "Myanmar Gazette News Media Forum Network"},
    {"url": "http://www.dvb.no/feed", "source": "Democratic Voice of Burma (DVB)"},
    {"url": "http://www.thithtoolwin.com/feeds/posts/default", "source": "Thit Htoo Lwin (Myanmar)"},
    {"url": "https://www.bangkokpost.com/rss/data/most-recent.xml", "source": "Bangkok Post (Thailand)"},
    {"url": "https://www.bangkokpost.com/rss/data/thailand.xml", "source": "Bangkok Post - Thailand"},
    {"url": "https://thailandnews.co/feed/", "source": "Thailand News"},
    {"url": "https://www.antaranews.com/en/rss/news", "source": "ANTARA News (Indonesia, English)"},
    {"url": "https://www.straitstimes.com/news/asia/rss.xml", "source": "The Straits Times (Asia)"},
    {"url": "http://www.channelnewsasia.com/rss/latest_cna_sg_rss.xml", "source": "CNA (Channel NewsAsia, latest)"},
    {"url": "http://www.channelnewsasia.com/rss/latest_cna_biz_rss.xml", "source": "CNA (business)"},
    {"url": "https://feeds.bbci.co.uk/news/world/asia/rss.xml", "source": "BBC News - Asia"},
    {"url": "https://www.aljazeera.com/xml/rss/all.xml", "source": "Al Jazeera"},
    {"url": "https://www.scmp.com/rss/5/feed", "source": "SCMP - World"},
    {"url": "https://www.scmp.com/rss/318198/feed", "source": "SCMP - China Military"},
    {"url": "https://www.taipeitimes.com/xml/index.rss", "source": "Taipei Times (Taiwan, English)"},
    {"url": "https://news.ltn.com.tw/rss/all.xml", "source": "Liberty Times (Taiwan)"},
    {"url": "https://news.usni.org/feed", "source": "USNI News (naval, Indo-Pacific)"},
    {"url": "https://blog.usni.org/feed", "source": "USNI Blog (naval analysis)"},
    {"url": "https://breakingdefense.com/feed", "source": "Breaking Defense"},
    {"url": "https://spacenews.com/feed/", "source": "SpaceNews"},
    {"url": "https://www.space.com/feeds.xml", "source": "Space.com"},
    {"url": "https://therecord.media/feed", "source": "The Record (cyber)"},
    {"url": "https://news.google.com/rss/search?q=Philippines+West+Philippine+Sea&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Philippines and the West Philippine Sea"},
    {"url": "https://news.google.com/rss/search?q=Vietnam+South+China+Sea&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Vietnam and the South China Sea"},
    {"url": "https://news.google.com/rss/search?q=Malaysia+Indonesia+navy&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Malaysia and Indonesia navies"},
    {"url": "https://news.google.com/rss/search?q=Myanmar+junta&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Myanmar"},
    {"url": "https://news.google.com/rss/search?q=Cambodia+Thailand+border&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Cambodia and Thailand"},
    {"url": "https://news.google.com/rss/search?q=KK+Park+scam+Myawaddy&hl=en-US&gl=US&ceid=US:en", "source": "Google News: scam compounds (Myanmar, Cambodia)"},
    {"url": "https://news.google.com/rss/search?q=Ream+naval+base+Cambodia&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Ream naval base"},
    {"url": "https://news.google.com/rss/search?q=Ninh+Thuan+nuclear+Vietnam&hl=en-US&gl=US&ceid=US:en", "source": "Google News: Vietnam nuclear"},
]

WORLD_WIDE_SOURCES = ('BBC News - Asia', 'Al Jazeera', 'SCMP - World', 'SCMP - China Military', 'Taipei Times (Taiwan, English)', 'Liberty Times (Taiwan)', 'USNI News (naval, Indo-Pacific)', 'USNI Blog (naval analysis)', 'Breaking Defense', 'SpaceNews', 'Space.com', 'The Record (cyber)')
REGION_TERMS = ["vietnam", "vietnamese", "hanoi", "ho chi minh", "philippine", "filipino", "manila", "luzon", "mindanao", "palawan", "indonesia", "indonesian", "jakarta", "surabaya", "malaysia", "malaysian", "kuala lumpur", "sabah", "sarawak", "singapore", "thailand", "thai ", "bangkok", "cambodia", "cambodian", "phnom penh", "sihanoukville", "ream naval", "laos", "laotian", "vientiane", "myanmar", "burma", "burmese", "naypyidaw", "yangon", "mandalay", "rakhine", "kachin", "karen state", "karen national", "brunei", "timor", "asean", "south china sea", "west philippine sea", "spratly", "paracel", "scarborough", "malacca", "hainan", "taiwan strait", "kk park", "shwe kokko", "myawaddy", "scam", "edca", "balikatan", "brahmos", "ninh thuan", "cam ranh", "natuna", "biak", "papua"]


def configured() -> bool:
    return True


def _looks_english(text: str) -> bool:
    if not text:
        return False
    latin = sum(1 for c in text if c.isascii() and c.isalpha())
    letters = sum(1 for c in text if c.isalpha())
    if letters == 0:
        return True
    return (latin / letters) > 0.6


def _relevant(title: str, source: str) -> bool:
    if not source.startswith(WORLD_WIDE_SOURCES):
        return True
    t = title.lower()
    return any(re.search(r'\b' + re.escape(term) + r'\b', t) for term in REGION_TERMS)


def fetch(per_feed_limit: int = 15) -> ConnectorResult:
    from .. import safe_http
    import feedparser
    all_items, errors, ok_feeds = [], [], 0
    for feed in FEEDS:
        try:
            r = safe_http.safe_get(feed["url"])
            if r.status_code != 200:
                errors.append(f"{feed['source']}: HTTP {r.status_code}")
                continue
            parsed = feedparser.parse(r.content)
            if parsed.bozo and not parsed.entries:
                errors.append(f"{feed['source']}: not a readable feed")
                continue
            ok_feeds += 1
            count = 0
            for entry in parsed.entries:
                title = getattr(entry, "title", "").strip()
                if not title or not _looks_english(title) or not _relevant(title, feed["source"]):
                    continue
                all_items.append(Item(
                    category=classify(title), label=title[:90] if len(title) > 90 else title,
                    text=title, source=feed["source"],
                    date=getattr(entry, "published", "") or getattr(entry, "updated", ""),
                    url=getattr(entry, "link", None), connector=NAME,
                ).to_dict())
                count += 1
                if count >= per_feed_limit:
                    break
        except safe_http.FetchError as e:
            errors.append(f"{feed['source']}: blocked ({e})")
        except Exception as e:
            errors.append(f"{feed['source']}: {type(e).__name__}")
    if not all_items and errors:
        return ConnectorResult(NAME, True, False, "; ".join(errors)[:300])
    msg = f"{len(all_items)} items from {ok_feeds} of {len(FEEDS)} feeds"
    if errors:
        msg += f" ({len(errors)} failed: {'; '.join(errors)[:200]})"
    return ConnectorResult(NAME, True, True, msg, all_items)
