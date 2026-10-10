# SouthEast Asia Dashboard - v1

Covers the eleven South-East Asian states (Myanmar, Thailand, Cambodia, Laos, Vietnam, Malaysia, Singapore, Indonesia, the
Philippines, Brunei and Timor-Leste), the South China Sea and its reefs, Hainan, the Taiwan Strait, and the Malacca and
Sunda approaches. It uses the China Dashboard v6 architecture: Flask with waitress, a supervisor with automatic restart,
AES-256-GCM key storage, the same 15 headings, layer toggles and live connectors.

**India is not plotted.** Its towns, airports, ports, rivers and installations are left out of the map, and its outline is
drawn plain. Bangladesh, China and Taiwan are also outlines only, apart from the South China Sea features and Hainan
listed below.

## Start

Windows: double-click `start.bat`. The dashboard runs at **http://127.0.0.1:8815/** (the port is set in `run.py` and
`start.bat`). The first pass of the news connectors takes a few minutes, because GDELT is paced at six seconds per query.

## The 15 headings (China v6's set)

Geopolitical & Diplomatic - Military Operations & Force Posture - Strategic Arms & Nuclear Program - Naval & Maritime
Security - South China Sea & Maritime Chokepoints - Air Force & Aviation - Space Tech & Aerospace - Critical Tech & AI
Governance - Cyber Espionage & APTs - Darkweb & Threat Intel - Economic & Trade - Internal Security & Intelligence
Operations - Social Pulse & Public Sentiment - Happiness & Wellbeing Indices - Natural Hazards & Environmental Risks.

Routing is rule-based (`app/classify.py`). The rules run in order: darkweb, cyber (including scam and cybercrime
reports), hazards, armed groups (Arakan Army, Kachin Independence Army, Karen National Army and others), internal security,
naval, maritime chokepoints, air, space, weapons and nuclear, military operations, technology, economy, social, wellbeing,
and geopolitics by default.

## The map

- **Frame:** longitude 92.0 to 141.5 and latitude -11.5 to 28.6. It covers the eleven states, the South China Sea, Hainan
  and the Taiwan Strait.
- **Shaded:** the eleven states. **Outlined:** China, India, Bangladesh and Taiwan, with no details plotted in them.
- **Rivers:** 89 segments from Natural Earth, with none inside India.
- **Towns and capitals:** 156 towns from Natural Earth (200,000 or more people, and capitals), plus Chinese cities of
  one million or more on the South China Sea coast.
- **Civil airports:** 1,212 from OurAirports (public domain, CC0).
- **Military-named airfields:** 36, chosen by name ("air base", "air force" and similar). A name is a clue, not a
  confirmation of use, and the perimeter is not published.
- **Seaports:** 45 Natural Earth port points, plus named sites from the reporting.
- **Sea labels:** the Andaman Sea, Gulf of Thailand, South China Sea, Sulu, Celebes, Java, Banda, Arafura, Philippine,
  Gulf of Tonkin and Malacca.

## What is plotted: 93 sites, each with its status, date and source

Each tooltip gives the source. "Not verified in this build" marks public knowledge that this build's searches did not
confirm. Positions are approximate unless the note says otherwise.

- **US access (9 EDCA sites, Philippines):** Antonio Bautista (Palawan), Basa (Pampanga), Fort Magsaysay (Nueva Ecija),
  Lumbia (Cagayan de Oro), Mactan-Benito Ebuen (Cebu), Naval Base Camilo Osias (Cagayan), Camp Melchor dela Cruz (Isabela),
  Balabac (Palawan) and Lal-lo (Cagayan). The DND said on 2 March 2026 that they remain Philippine installations.
- **Navies and submarines:** Cam Ranh Bay (the 189th Submarine Brigade and six Kilo-class boats); Surabaya (Indonesia's
  2nd Fleet and Type 209 boats, and PT PAL building two Scorpene Evolved boats from 7 August 2026); Teluk Sepanggar (two
  Scorpenes; the Malaysian principal submarine base); Lumut (RMN Fleet HQ); Changi Naval Base (Invincible and Archer-class
  submarines); Sattahip (Royal Thai Navy Fleet HQ; no submarine in service yet); Ream (Cambodia; PLAN access disputed);
  Subic Bay (former US base); Kota Kinabalu (third-party listing); East Yulin (Hainan; China's only ballistic-missile
  submarine base); Zhanjiang (fleet HQ).
- **Air bases:** Halim Perdanakusuma (Jakarta; the National Air Operations Command), Iswahjudi (fighters), Sultan Hasanuddin
  (Su-30s), Manuhua (Biak), Raden Sadjad (Natuna), Roesmin Nurjadin (Pekanbaru) and Mingaladon (Myanmar), plus the 36
  military-named airfields.
- **Missile batteries:** the first BrahMos battery in Western Luzon (Zambales), and a base planned for northern Luzon.
- **Nuclear:** Ninh Thuan 1 (planned; Russian agreement of 23 March 2026, approved by Vietnam's parliament on 24 August
  2026) and Ninh Thuan 2 (planned; Korean talks accelerated 9 September 2026); the Dalat research reactor (Vietnam);
  Bataan (never operated; not verified in this build); and the two WRI-listed plants on Hainan and the Guangxi coast
  (Changjiang and Fangchenggang; the WRI data dates from 2018).
- **Defence industry and shipyards:** PT PAL (Surabaya), the X52 shipyard (Cam Ranh), Lumut Naval Shipyard and the
  Mahidol Adulyadej Naval Dockyard (Sattahip).
- **South China Sea features:** Mischief, Subi and Fiery Cross reefs (occupied and militarised: airstrips, radar, hangars,
  missile systems); Antelope Reef in the Paracels (a new artificial island, first phase completed per Reuters, August 2026);
  Itu Aba and Second Thomas Shoal (not verified in this build); and the Spratly, Paracel and Scarborough flashpoints.
- **Chokepoints:** Malacca, Singapore Strait, Sabang, Sunda, Lombok, Makassar, Balabac, Taiwan Strait, Bashi Channel and the
  Coco Channel.
- **Pipelines and terminals:** the China-Myanmar pipeline routes, and the Kyaukphyu deep-sea port (reported).
- **Space:** Wenchang Space Launch Site (Hainan).
- **Army and command sites:** the Myanmar military's Naypyidaw headquarters, the Southern Theatre Command at Guangzhou,
  and the Batanes forward base (analysis; not confirmed by the government).
- **Cyber and scam hubs (reported):** KK Park, Shwe Kokko, Yulong Bay Park (Myawaddy) and the T C Capital / Golden Sun Sky
  Casino complex (Sihanoukville). The US Treasury designated several of these in 2025; KK Park was raided in October 2025.
- **Conflict zones (press reporting):** Sittwe, Myitkyina, Laiza, Lashio, Myawaddy, the Coco Islands (Chinese listening
  facilities reported, not officially confirmed), and the Thai-Cambodian border.

## Nuclear power and nuclear storage

No nuclear power plant is operating in South-East Asia. No state in the region has declared nuclear weapons or weapons
storage, and the region is a nuclear-weapon-free zone under the 1995 Bangkok Treaty (public information). The nuclear layer
therefore shows planned plants (Ninh Thuan), the Dalat research reactor, and the plants listed by WRI on Hainan and the
Guangxi coast. Research-reactor fuel is the only nuclear material the sources describe in the region.

## Gaps (not verified in this build)

These are not plotted, or are plotted only where the verified notes say so:
- Vietnamese navy bases other than Cam Ranh (Hai Phong, Da Nang), Vietnamese air bases, and Vietnamese coastal missile batteries.
- Thailand's U-Tapao air base and its Naval Air Division; Malaysia's RMAF Butterworth and other RMAF bases.
- The Malaysian Puspati research reactor, the Thai TRR-1/M1 reactor, Indonesia's GA Siwabessy reactor and the Philippines' PRR-1 reactor.
- Indonesian Navy Western Fleet headquarters (Jakarta) and Natuna naval facilities; the Biak spaceport (no source found).
- The Brunei Muara naval base; Timor-Leste facilities. Laos is landlocked and has no navy.
- Myanmar naval bases (only Mingaladon and the Naypyidaw headquarters are plotted from the verified Myanmar build).
- State cyber commands in Vietnam, Singapore, Thailand and the Philippines.
- Army corps and division headquarters across the region, and missile batteries other than the Philippine BrahMos.
- Chinese bases on the mainland beyond Hainan and Zhanjiang, which lie outside the South-East Asian scope.

## News, social and dark-web sources

- **Verified feeds (22):** Myanmar Gazette, DVB, Thit Htoo Lwin, Bangkok Post (two feeds), Thailand News, ANTARA, The Straits
  Times (Asia), CNA (two feeds), BBC News Asia, Al Jazeera, SCMP (World and China Military), Taipei Times, Liberty Times,
  USNI News and USNI Blog, Breaking Defense, SpaceNews, Space.com and The Record. No India feeds are included.
- **Google News search feeds (8):** for outlets whose own feed addresses were not verified (Philippine, Vietnamese,
  Malaysian and Indonesian press, Myanmar, Cambodia and Thailand, scam compounds, Ream and Vietnam nuclear). These are
  aggregators, so the underlying outlets are not named by the feed.
- **GDELT:** 30 English-language queries on the South China Sea, each state, the navies, the nuclear and scam stories.
- **USGS earthquakes:** events inside the frame.
- **Ransomware.live:** claims filtered to the eleven states' country codes. Group claims are labelled unverified.
- **X (Twitter):** official API v2 recent search with 10 queries. Set `X_BEARER_TOKEN`. Recent search needs a paid tier.
- **Facebook and Instagram:** official Graph and Business Discovery APIs. Set your tokens and list your own pages or accounts.
- **Telegram:** `data/telegram_channels.json` carries the 16-channel public list from the earlier build. It has not been
  verified for South-East Asia, so add the channels you verify.
- **Dark web (Tor):** none configured. Add onion sources you have verified on the outlet's own site.

## Tests

36 Python tests (`python -m pytest tests/`) and three browser suites (`npm test`), which load the shipped page into a real
DOM. The layer test fails the build if any toggle has no data behind it.

## Security

- Keys and tokens are encrypted with AES-256-GCM and never appear in error messages.
- The server listens on 127.0.0.1 only.
- Strict Content-Security-Policy: no third-party scripts, fonts or trackers.
- Headlines and labels are escaped before display; only http and https links become clickable.
- Telegram handles, Instagram usernames and Facebook Page IDs are validated before any URL is built.
- Requests can go through a proxy you choose (`PROXY_URL`).

A dashboard cannot secure your whole PC or phone, and it cannot hide your IP address from the sites it fetches from unless
you route traffic through a VPN, which can still see your traffic.

## Honest limitations

- **Most positions are approximate.** Bases and industrial sites sit at their town or area centre; open sources do not
  publish perimeters. Each tooltip says so.
- **Some items are not verified in this build.** They are marked in their tooltips and listed under Gaps.
- **Events change daily.** The sources are current to reports up to 10 October 2026. Check them before you rely on any event.
- **No live news was fetched in the build sandbox,** which has no internet access. The status panel on your machine shows
  the real results.
- **The map is not a targeting product.** It maps publicly reported locations and events for analysis.
- **Single-user and local.** It runs on your machine while it is open.
