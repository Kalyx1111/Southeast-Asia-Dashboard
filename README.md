# Southeast Asia Dashboard

A locally hosted **OSINT and Geospatial Intelligence Platform** for monitoring Southeast Asia, the South China Sea, Hainan and regional strategic developments.

***

#### 🌏 Regional Coverage

- **11 Southeast Asian states:** Myanmar, Thailand, Cambodia, Laos, Vietnam, Malaysia, Singapore, Indonesia, Philippines, Brunei and Timor-Leste.
- **Strategic geography:** South China Sea, Hainan and Taiwan Strait.
- **India exclusion:** India is shown only as a plain outline. No Indian towns, airports, ports, rivers or installations are plotted.
- **Map infrastructure:** 156 towns, 1,212 civil airports, 36 military-named airfields, 45 ports and 11 sea labels.
- **Strategic sites:** 93 sourced entries, each carrying status, date and source information.

***

#### 🧭 15 Intelligence Categories

1. Geopolitical & Diplomatic
2. Military Operations & Force Posture
3. Strategic Arms & Nuclear Program
4. Naval & Maritime Security
5. Air Force & Aviation
6. Space Tech & Aerospace
7. Critical Tech & AI Governance
8. Cyber Espionage & APTs
9. Darkweb & Threat Intel
10. Economic & Trade
11. Internal Security & Intelligence Operations
12. Social Pulse & Public Sentiment
13. Happiness & Wellbeing Indices
14. Natural Hazards & Environmental Risks
15. Regional Strategic Developments

***

#### 🛰️ Strategic Map Layers

- **Naval and submarine facilities:** selected bases in Vietnam, Indonesia, Malaysia, Singapore, Thailand and Cambodia.
- **Philippines:** nine EDCA sites, Batanes forward base and BrahMos missile deployment references.
- **South China Sea:** Mischief Reef, Subi Reef, Fiery Cross Reef, Antelope Reef, Scarborough Shoal, Spratly Islands and Paracel Islands.
- **Hainan:** East Yulin submarine base and Wenchang space launch site.
- **Nuclear facilities:** Vietnam's planned Ninh Thuan plants, the Dalat research reactor and two Chinese coastal nuclear plants referenced in the build.
- **Cybercrime hubs:** KK Park, Shwe Kokko and Sihanoukville casino compounds.
- **Regional infrastructure:** airports, military-named airfields, ports, towns and maritime geography.

Facility locations may be approximate. Unverified facilities are excluded or explicitly labelled as unverified.

***

#### 📰 News & Intelligence Sources

- 22 verified news feeds, plus eight Google News search feeds.
- GDELT and RSS/Atom-based news monitoring.
- Public Telegram source configuration.
- Optional X, Facebook and Instagram connectors requiring the user's own credentials or tokens.
- Reuses selected regional feeds and site references from the earlier Myanmar, China and Indian Ocean builds.

**Source limitations:** Telegram channels carried over from earlier builds have not been verified for Southeast Asia. Social-media connectors require user configuration. Live news retrieval was not verified because the build environment had no internet access.

***

#### 🛡️ Geographic and Verification Rules

- India-specific sites and infrastructure are excluded.
- China and Taiwan appear as plain outlines except for explicitly included regional map references such as Hainan and South China Sea features.
- Each of the 93 strategic site entries includes a status, date and source.
- Unconfirmed facilities are not presented as verified facts.
- No operating nuclear power plant is identified in the eleven Southeast Asian states in the supplied build findings.

***

#### ⚙️ Installation & Launch

**Local dashboard URL:** http://127.0.0.1:8815

1. Extract `southeastasia-dashboard-v1.zip`.
2. Open the extracted project folder.
3. Run the supplied startup script.
4. Open `http://127.0.0.1:8815` in your browser.

Use the startup script and configuration files included with the project.

***

#### 🧪 Testing

- 36 Python tests passed.
- Three browser test suites passed in a clean rebuild.
- Map layers, category panels, server startup and connector error handling were checked.
- Live external news retrieval remains unverified in the offline build environment.

***

#### ⚠️ Known Limitations

- Some national air bases, naval facilities, research reactors and missile deployments could not be verified.
- Indonesia's proposed Biak spaceport remains unverified.
- State cyber commands and several army headquarters are not included as verified sites.
- Telegram sources need regional verification.
- Positions of some facilities are approximate.
- Live feed availability depends on internet connectivity and source availability.

***

#### 🔐 Responsible Use

This dashboard organizes publicly sourced information for research and situational awareness. Site entries should be assessed against their cited sources and verification status; mapped positions are not guaranteed to represent exact facility boundaries.

***
