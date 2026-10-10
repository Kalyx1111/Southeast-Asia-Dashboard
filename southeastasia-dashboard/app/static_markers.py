"""
Fixed reference points for the South-East Asia dashboard: the 11 states (Myanmar, Thailand, Cambodia, Laos, Vietnam,
Malaysia, Singapore, Indonesia, Philippines, Brunei, Timor-Leste), the South China Sea and its features, and the Chinese
installations on Hainan and along the Southern Theatre that face the region. India has no entries (per the brief).

Each point carries its status, date and source in `note` and `source`. Points marked "not verified in this build" come from
public knowledge that this build's searches did not confirm; they are shown, but treat them as unconfirmed.
Coordinates for bases are approximate (the base or town centre). Open sources rarely publish base perimeters.
Strike, casualty and occupation items are reported claims unless the source is a government body or an agency.
Nothing here is a targeting product: the dashboard maps publicly reported locations and events only.
"""
import json
import os


def M(id, name, lat, lon, cat, note, source, aliases=()):
    al = list(aliases) or [name.split(":")[0].split(" (")[0].strip().lower()]
    return {"id": id, "name": name, "lat": lat, "lon": lon, "cat": cat, "note": note, "source": source, "aliases": al}


MARKERS = [
    # ---------- Capitals and principal cities ----------
    M("cap_naypyidaw", "Naypyidaw (capital, Myanmar)", 19.7633, 96.0785, "capital", "Capital of Myanmar; seat of the military government since 2005.", "Myanmar dashboard build (public information)"),
    M("cap_bangkok", "Bangkok (capital, Thailand)", 13.7563, 100.5018, "capital", "Capital of Thailand.", "public information"),
    M("cap_phnom_penh", "Phnom Penh (capital, Cambodia)", 11.5564, 104.9282, "capital", "Capital of Cambodia.", "public information"),
    M("cap_vientiane", "Vientiane (capital, Laos)", 17.9757, 102.6331, "capital", "Capital of Laos. Laos is landlocked and has no navy.", "public information"),
    M("cap_hanoi", "Hanoi (capital, Vietnam)", 21.0278, 105.8342, "capital", "Capital of Vietnam.", "public information"),
    M("cap_kuala_lumpur", "Kuala Lumpur (capital, Malaysia)", 3.1390, 101.6869, "capital", "Capital of Malaysia; the administrative capital is Putrajaya.", "public information"),
    M("cap_singapore", "Singapore (city-state)", 1.3521, 103.8198, "capital", "City-state at the southern end of the Malacca Strait.", "public information"),
    M("cap_jakarta", "Jakarta (capital, Indonesia)", -6.2088, 106.8456, "capital", "Capital of Indonesia.", "public information"),
    M("cap_manila", "Manila (capital, Philippines)", 14.5995, 120.9842, "capital", "Capital of the Philippines.", "public information"),
    M("cap_bsb", "Bandar Seri Begawan (capital, Brunei)", 4.9031, 114.9398, "capital", "Capital of Brunei.", "public information"),
    M("cap_dili", "Dili (capital, Timor-Leste)", -8.5569, 125.5603, "capital", "Capital of Timor-Leste (East Timor).", "public information"),
    M("cap_mandalay", "Mandalay (second city, Myanmar)", 21.9588, 96.0891, "capital", "Second city and former royal capital of Myanmar.", "Myanmar dashboard build (public information)"),
    M("cap_taunggyi", "Taunggyi (capital of Shan State, Myanmar)", 20.7892, 97.0347, "capital", "Capital of Shan State.", "Myanmar dashboard build (public information)"),
    M("cap_mawlamyine", "Mawlamyine (capital of Mon State, Myanmar)", 16.4907, 97.6278, "capital", "Capital of Mon State, on the Gulf of Martaban.", "Myanmar dashboard build (public information)"),
    M("port_yangon", "Yangon (Myanmar's main commercial port)", 16.8409, 96.1735, "seaport", "Myanmar's largest city and main commercial port.", "Myanmar dashboard build (public information)"),

    # ---------- US access in the Philippines: nine EDCA sites (2014 agreement; rotational access, Philippine-owned) ----------
    M("edca_bautista", "Antonio Bautista Air Base (Puerto Princesa, Palawan): EDCA site", 9.7392, 118.7585, "us_base",
      "One of nine EDCA sites: US forces may rotate here under the 2014 agreement; the government says the sites remain Philippine installations. Near the West Philippine Sea. Position approximate.",
      "DND / AFP (2 Mar 2026, via Philstar); Inquirer; SCSPI (2026)"),
    M("edca_basa", "Basa Air Base (Pampanga): EDCA site, first EDCA project", 15.0700, 120.6600, "us_base",
      "First EDCA project (a multi-purpose warehouse) was launched in 2023. Runway and facility works were reported as due for completion in 2026 (SCSPI). Position approximate.",
      "SCSPI (2026); Inquirer (2023)"),
    M("edca_magsaysay", "Fort Magsaysay (Nueva Ecija): EDCA site and training base", 15.5500, 121.0500, "us_base",
      "EDCA site since 2016; described by analysts as the largest training base. Position approximate.",
      "Tribune (1 Mar 2026); Modern Diplomacy (Mar 2026, analysis)"),
    M("edca_lumbia", "Lumbia Air Base (Cagayan de Oro, Mindanao): EDCA site", 8.6100, 124.6000, "us_base",
      "EDCA site since 2016. Position approximate.", "Tribune (1 Mar 2026)"),
    M("edca_mactan", "Mactan-Benito Ebuen Air Base (Cebu): EDCA site", 10.3075, 123.9794, "us_base",
      "EDCA site since 2016. A fuel-storage facility was inaugurated here (SCSPI, 2026).", "SCSPI (2026); Tribune (1 Mar 2026)"),
    M("edca_camilo", "Naval Base Camilo Osias (Santa Ana, Cagayan): EDCA site", 18.5100, 122.0800, "us_base",
      "Added to the EDCA list under the Marcos administration (DND, 2026). Position approximate.", "Philstar (2 Mar 2026)"),
    M("edca_melchor", "Camp Melchor dela Cruz (Gamu, Isabela): EDCA site", 16.9300, 121.6000, "us_base",
      "Added to the EDCA list under the Marcos administration. Position approximate.", "Manila Bulletin (2 Mar 2026)"),
    M("edca_balabac", "Balabac Island (Palawan): EDCA site", 7.9700, 117.0300, "us_base",
      "Added to the EDCA list. Analysts say it controls the passage between the South China Sea and the Sulu Sea. Position approximate.",
      "Manila Bulletin (2 Mar 2026); Modern Diplomacy (Mar 2026, analysis)"),
    M("edca_lallo", "Lal-lo Airport (Cagayan): EDCA site", 18.1600, 121.6200, "us_base",
      "Added to the EDCA list. Analysts describe it as close to Taiwan. Position approximate.", "Manila Bulletin (2 Mar 2026); Modern Diplomacy (Mar 2026, analysis)"),

    # ---------- Philippine navy and Subic ----------
    M("subic", "Subic Bay (Zambales): former US naval base, now a freeport", 14.8000, 120.2800, "navy_base",
      "Returned by the US in 1992; now the Subic Bay Freeport Zone. The SCSPI report (2026) says EDCA facilities there must sit inside the Freeport Zone. Analysts report planned ammunition production here; the government has not confirmed it.",
      "SCSPI (2026); Modern Diplomacy (Mar 2026, analysis); public information (1992 handover)"),
    M("batanes_fob", "Batanes Forward Operating Base (Philippines): closest Philippine territory to Taiwan", 20.4500, 121.9700, "cantonment",
      "Analysts report that a forward operating base opened in Batanes in 2025. Not verified against an official source in this build.",
      "Modern Diplomacy (30 Mar 2026, analysis)"),
    M("bataan_npp", "Bataan Nuclear Power Plant (Morong, Bataan): completed, never operated", 14.6600, 120.4600, "nuclear_site",
      "Built in the 1980s but never operated (public information). Not verified in this build; the WRI database does not list it.",
      "public information (not verified in this build)"),

    # ---------- Philippine missile batteries (BrahMos) ----------
    M("brahmos_zambales", "BrahMos coastal battery, Western Luzon (Zambales): Philippine Marine Corps Coastal Defense Regiment", 15.4000, 119.9000, "missile_base",
      "First battery in service. Each battery has two launchers, a radar vehicle and a reload vehicle; the 290 km supersonic anti-ship missile reaches Scarborough Shoal (Janes; Naval News; USNI News; TurDef). Position approximate.",
      "Janes (Nov 2025); Naval News (Oct 2026); USNI News (Jul 2026); TurDef (2025)"),
    M("brahmos_north", "Planned BrahMos base, northwest tip of Luzon (Coastal Defense Regiment, 273rd Marine Company)", 18.4500, 120.6000, "missile_base",
      "Planned to cover the Luzon Strait; Naval News (Mar 2026) reports it from social-media posts. The AFP has not confirmed it. Position approximate.",
      "Naval News (Mar 2026); IDRW (Mar 2026)"),

    # ---------- Nuclear (Vietnam, planned and research) ----------
    M("ninh_thuan_1", "Ninh Thuan 1 (planned): two VVER-1200 units (2,400 MW), Russian intergovernmental agreement (Mar 2026)", 11.7000, 109.0500, "nuclear_site",
      "Phuoc Dinh commune, Thuan Nam district. The intergovernmental agreement with Russia was signed on 23 Mar 2026 (Rosatom; WNN). Vietnam's National Assembly approved the agreement on 24 Aug 2026 (NucNet). Target: commercial operation 2030-2035. Position approximate.",
      "World Nuclear News (23 Mar 2026); NucNet (24 Aug 2026); Sputnik (9 Sep 2026)"),
    M("ninh_thuan_2", "Ninh Thuan 2 (planned): Vinh Hai commune; Korean talks accelerated (Sep 2026)", 11.8500, 109.1000, "nuclear_site",
      "Japan withdrew from this project (reports date the withdrawal to Dec 2025 or Jan 2026). On 9 Sep 2026 PetroVietnam and KEPCO agreed to accelerate talks; PetroVietnam has acquired almost all the land (Nuclear News Network). Position approximate.",
      "Nuclear News Network (Sep 2026); World Nuclear Association (2026)"),
    M("dalat_reactor", "Dalat Nuclear Research Reactor (Vietnam): 500 kW research reactor, Russian-supplied fuel", 11.9400, 108.4580, "nuclear_site",
      "Operating since March 1984 at a nominal 500 kW. Its Russian-supplied fuel is used to produce medical isotopes (WNA; WNN, Mar 2026). Position approximate (city).",
      "World Nuclear Association (2026); World Nuclear News (Mar 2026)"),

    # ---------- Vietnam: submarines and shipyard ----------
    M("cam_ranh_sub", "Cam Ranh Bay: Vietnam People's Navy submarine base (189th Submarine Brigade; six Kilo-class boats)", 11.9500, 109.1500, "submarine_base",
      "Home of the 189th Submarine Brigade (formed 2013) and the six Russian Kilo-class submarines HQ-182 Ha Noi to HQ-187 Ba Ria-Vung Tau. A submarine training centre is here (VietnamPlus; Wikipedia). The 196th Submarine-Commando Brigade is also reported here (Wikipedia). Position approximate.",
      "VietnamPlus (submarine brigade); Wikipedia (Submarine force, Vietnam People's Navy)"),
    M("x52_camranh", "X52 Shipyard, Cam Ranh: navy repair and maintenance of the Kilo submarines", 11.9300, 109.1700, "defense_industry",
      "Navy-owned maintenance, repair and overhaul shipyard that supports the six Kilo-class boats (Indo-Pacific GeoMill, 2018; older source). Position approximate.",
      "Indo-Pacific GeoMill (2018)"),

    # ---------- Indonesia: submarines, shipyard, air bases ----------
    M("surabaya_sub", "Surabaya (East Java): Indonesian Navy 2nd Fleet and submarine base", -7.2575, 112.7521, "submarine_base",
      "Home port of the Type 209 boats KRI Nagapasa, KRI Ardadedali and KRI Alugoro; the 2nd Fleet Command is based here (Wikipedia). Position approximate.",
      "Wikipedia (KRI Ardadedali; KRI Alugoro)"),
    M("pt_pal", "PT PAL Indonesia shipyard (Surabaya): builds two Scorpene Evolved submarines", -7.2200, 112.7450, "defense_industry",
      "State shipbuilder. First steel was cut on 7 Aug 2026 for the lead Scorpene Evolved boat; the Navy expects delivery in 2032-33 (Antara; Navy Leaders). Naval Group provides design support. Position approximate.",
      "Antara (Aug 2026); Navy Leaders (Aug 2026); Army Recognition (Aug 2026)"),
    M("halim_afb", "Halim Perdanakusuma Air Force Base (Jakarta): National Air Operations Command", -6.2661, 106.8922, "air_base",
      "National Air Operations Command (Koopsudnas) is headquartered here. The base hosts transport and VIP squadrons; the civil airport shares the runway (Global Military, Aug 2026; Wikipedia).",
      "Global Military (Aug 2026); Wikipedia (Halim Perdanakusuma International Airport)"),
    M("iswahjudi_afb", "Iswahjudi Air Force Base (Maospati, East Java): fighter base, 32nd Air Wing", -7.6158, 111.4341, "air_base",
      "Home to the 32nd Air Wing and four other units (ICAO WARI; Global Military, Aug 2026).", "Global Military (Aug 2026)"),
    M("hasanuddin_afb", "Sultan Hasanuddin Air Force Base (Makassar): 33rd Air Wing, Su-27/Su-30", -5.0616, 119.5540, "air_base",
      "Su-30MK2 overran the runway on 24 Aug 2026 during a simulated take-off after a major overhaul; the crew was unhurt (migflug, 2026). Position approximate.",
      "migflug (Aug 2026); Wikipedia (Sultan Hasanuddin International Airport)"),
    M("manuhua_afb", "Manuhua Air Force Base (Biak, Papua): 13th Air Wing; 27th Air Squadron (CN235)", -1.1900, 136.1080, "air_base",
      "ICAO WABB; runway 11/29, 3,571 m (migflug, 2026; Wikipedia). Position approximate.", "migflug (2026); Wikipedia (Indonesian Air Force)"),
    M("raden_sadjad_afb", "Raden Sadjad Air Force Base (Ranai, Natuna Islands)", 3.9260, 108.3870, "air_base",
      "ICAO WIDO; runway 18/36, 2,560 m (Wikipedia, Indonesian Air Force listing). The Natuna Islands face the South China Sea. Position approximate.",
      "Wikipedia (Indonesian Air Force)"),
    M("roesmin_afb", "Roesmin Nurjadin Air Force Base (Pekanbaru, Sumatra): fighter base", 0.4600, 101.4400, "air_base",
      "Fighter base on Sumatra (Wikipedia, Indonesian Air Force listing). Position approximate.", "Wikipedia (Indonesian Air Force)"),
    M("sabang", "Sabang (Weh Island, Indonesia): northwestern tip of Sumatra", 5.8945, 95.3220, "chokepoint",
      "Northwestern tip of Sumatra, at the Andaman Sea entrance to the Malacca Strait (public information).", "public information"),

    # ---------- Malaysia: submarines, navy and shipyard ----------
    M("sepanggar_sub", "Teluk Sepanggar (Sabah): Royal Malaysian Navy's principal submarine base", 5.9810, 116.0800, "submarine_base",
      "Two Scorpene boats (KD Tunku Abdul Rahman and KD Tun Abdul Razak, commissioned 2009) are based here. A Submarine Training Centre and shore-support infrastructure are here (NTI, 2020; Global Military, 2026).",
      "NTI (2020); Global Military (2026); Naval Town (2017)"),
    M("lumut_navy", "Lumut (Perak): Royal Malaysian Navy Fleet HQ (KD Malaya) and Western Fleet", 4.2300, 100.6300, "navy_base",
      "Fleet HQ and Western Fleet headquarters; the RMN's naval air unit is based here (Global Military, 2026; Wikipedia). Position approximate.",
      "Global Military (2026); Wikipedia (Lumut Naval Base)"),
    M("lumut_shipyard", "Lumut Naval Shipyard (Malaysia): domestic construction of RMN ships", 4.2250, 100.6200, "defense_industry",
      "Builds RMN ships domestically (Global Military, 2026). The Boustead DCNS Naval Corporation refitted the Scorpenes (NTI, 2020).",
      "Global Military (2026); NTI (2020)"),
    M("kk_eastern", "Kota Kinabalu (Sabah): RMN Eastern Fleet (third-party listing)", 5.9804, 116.0735, "navy_base",
      "Eastern Fleet headquarters according to a 2026 third-party listing; not confirmed against an official source.", "Global Military (2026, third-party)"),

    # ---------- Singapore ----------
    M("changi_naval", "Changi Naval Base (Singapore): RSN submarine base (RSS Singapura)", 1.3320, 103.9900, "submarine_base",
      "RSS Invincible and RSS Impeccable (Invincible class) were commissioned here on 24 Sep 2024; RSS Illustrious arrived on 10 Apr 2026. The Archer-class submarines are also based here (MINDEF; Naval News; Wikipedia). Position approximate.",
      "MINDEF (10 Apr 2026); Naval News (Apr 2026); Wikipedia (Invincible-class submarine)"),

    # ---------- Thailand ----------
    M("sattahip", "Sattahip (Chonburi): Royal Thai Navy Fleet headquarters and Marine Corps HQ", 12.6700, 100.9000, "navy_base",
      "Fleet headquarters and Royal Thai Marine Corps HQ (Global Security; Global Military, 2026). The helicopter carrier HTMS Chakri Naruebet is in the fleet (Global Military, 2026).",
      "Global Security (Royal Thai Navy bases); Global Military (2026)"),
    M("mahidol_dock", "Mahidol Adulyadej Naval Dockyard (Chuk Samet, Sattahip): RTN shipyard; planned submarine home", 12.6100, 100.9500, "defense_industry",
      "Royal Thai Navy shipyard; plans exist to base a submarine here (Wikipedia). The Chinese-built S26T programme resumed in Aug 2025 after a contract amendment to Chinese engines; no submarine is in service yet (Global Military, Sep 2026).",
      "Wikipedia (Mahidol Adulyadej Naval Dockyard); Global Military (Sep 2026)"),
    M("ram_naval_placeholder_skip", "", 0, 0, "navy_base", "", "", ()),

    # ---------- Cambodia ----------
    M("ream", "Ream Naval Base (Sihanoukville, Cambodia): Royal Cambodian Navy base with a Chinese-funded upgrade", 10.5100, 103.6100, "navy_base",
      "Reopened after renovation on 5 Apr 2025 (Global Military). CSIS says about half of the port is for Cambodian and Chinese use. US officials alleged PLAN exclusive access to about one-third for up to 30 years (2019); Cambodia denies it. USS Cincinnati visited on 24 Jan 2026 (Defense News). Position approximate.",
      "Global Military (2026); Defense News (6 Feb 2026); AMTI / CSIS"),

    # ---------- Hainan and China's Southern Theatre (the South China Sea side) ----------
    M("yulin", "East Yulin Naval Base (Sanya, Hainan): China's only ballistic-missile submarine base", 18.2300, 109.5000, "submarine_base",
      "Houses China's only ballistic-missile submarine base; a submarine enters through a cave here (Washington Post, 2024).",
      "Washington Post (2024); FAS / USNI News (China v6 build)"),
    M("zhanjiang", "Zhanjiang Naval Base (Guangdong): PLA Navy fleet headquarters", 21.2000, 110.4000, "navy_base",
      "Fleet headquarters (Global Military, 2026, third-party listing; background in the China v6 build).",
      "Global Military (2026, third-party); China v6 build (background)"),
    M("stc_guangzhou", "Southern Theatre Command (Guangzhou): PLA command for the South China Sea", 23.1300, 113.2600, "cantonment",
      "Southern Theatre Command headquarters (background from the China v6 build).", "China v6 build (background)"),
    M("wenchang", "Wenchang Space Launch Site (Hainan): China's coastal launch centre", 19.6100, 110.9500, "space_site",
      "One of China's main launch sites, on Hainan's coast (Washington Post, 2024; China v6 build; CNSA / Xinhua).",
      "Washington Post (2024); China v6 build (CNSA / Xinhua)"),

    # ---------- South China Sea features (occupied, militarised or contested) ----------
    M("scarborough", "Scarborough Shoal: disputed by China, the Philippines and Taiwan", 15.1300, 117.7500, "flashpoint",
      "Chinese coast guard and Philippine vessels have repeatedly clashed here (press reporting). Position approximate.",
      "CFR (China v6 build); press reporting"),
    M("spratly", "Spratly Islands: China, Vietnam, the Philippines, Malaysia, Brunei and Taiwan claim parts", 10.0000, 114.0000, "flashpoint",
      "China has militarised its seven main features in the Spratlys (AMTI / CSIS; China v6 build). Other claimants occupy their own features.",
      "AMTI / CSIS (China v6 build)"),
    M("paracel", "Paracel Islands: occupied by China; claimed by Vietnam and Taiwan", 16.5000, 112.0000, "flashpoint",
      "China holds the islands; its outposts include radar sites (Geopolitical Futures; ABC, 2025).", "AMTI / CSIS (China v6 build); Geopolitical Futures; ABC (Jul 2025)"),
    M("mischief", "Mischief Reef (Spratlys): China-occupied and militarised", 9.9000, 115.5300, "scs_outpost",
      "China began occupying it in 1994 (Newsweek). It has hangars, radar, missile shelters and an airstrip (CSIS analysis; ABC, Jul 2025; RFA, 2022). Also called Meiji Reef (China) and Panganiban Reef (Philippines). Position approximate.",
      "Newsweek (2024); ABC (Jul 2025); RFA (2022)"),
    M("subi", "Subi Reef (Spratlys): China-occupied and militarised", 10.9200, 114.0900, "scs_outpost",
      "Airstrips, radar domes, missile systems and a deepwater port (Newsweek). The US Indo-Pacific Command said by 2022 that its military infrastructure appeared complete. Position approximate.",
      "Newsweek (2024)"),
    M("fiery_cross", "Fiery Cross Reef (Spratlys): China-occupied and militarised", 9.5500, 112.8900, "scs_outpost",
      "Operational airfield, hangars and radomes; a harbour for China's largest naval vessels (RFA, 2022; Geopolitical Futures). Position approximate.",
      "RFA (2022); Geopolitical Futures"),
    M("antelope", "Antelope Reef (Paracels): new Chinese artificial island under construction", 16.3000, 111.3000, "scs_outpost",
      "Reuters reported that the first construction phase was completed (Aug 2026). Reports describe a deepwater port, a quay and the start of a runway (Yahoo News, 21 Aug 2026). Position approximate.",
      "Reuters (Aug 2026, via chinaglobalsouth); Yahoo News (21 Aug 2026)"),
    M("itu_aba", "Itu Aba (Taiping Island, Spratlys): administered by Taiwan", 10.3700, 114.3600, "scs_outpost",
      "Administered by Taiwan (public information). Not verified in this build.", "public information (not verified in this build)"),
    M("second_thomas", "Second Thomas Shoal (Ayungin): BRP Sierra Madre", 9.7300, 115.8500, "flashpoint",
      "Philippine-occupied shoal with a grounded naval vessel; resupply disputes have been reported (public information). Not verified in this build.",
      "public information (not verified in this build)"),
    M("thai_cam_border", "Thai-Cambodian border (Preah Vihear area): clashes in July 2025; ceasefire 27 Dec 2025", 14.3900, 104.6800, "flashpoint",
      "Reported clash area. The ceasefire of 27 Dec 2025 is carried from the earlier verified Myanmar build; not re-verified in this build. Position approximate.",
      "Earlier verified build reference (Myanmar dashboard); not re-verified in this build"),

    # ---------- Myanmar: conflict, ports and pipelines (from the verified Myanmar build) ----------
    M("naypyidaw_hq", "Defence Services (Tatmadaw) headquarters, Naypyidaw", 19.7000, 96.1000, "cantonment",
      "Seat of the military government. The military seized power on 1 February 2021. Position approximate.",
      "background / press reporting (Myanmar dashboard build)"),
    M("mingaladon", "Mingaladon Air Base (Yangon): Myanmar Air Force base", 16.9073, 96.1332, "air_base",
      "Myanmar Air Force base beside Yangon International Airport (public information). Position approximate.", "public information (approximate position)"),
    M("sittwe", "Sittwe (Rakhine State): Arakan Army contests much of the state", 20.1500, 92.9000, "flashpoint",
      "Rakhine State capital. The Arakan Army contests control of much of the state (press reporting). Front lines change.", "press reporting (front lines change)"),
    M("myitkyina", "Myitkyina (Kachin State): fighting reported around the city", 25.3833, 97.3964, "flashpoint",
      "Kachin State capital. Fighting between the Kachin Independence Army and the military has been reported around the city (press reporting).", "press reporting (front lines change)"),
    M("laiza", "Laiza (Kachin Independence Army headquarters, China border)", 24.6000, 97.6000, "flashpoint",
      "Headquarters of the Kachin Independence Army, on the China border (press reporting). Position approximate.", "press reporting (approximate position)"),
    M("lashio", "Lashio (northern Shan State): control changed hands in 2024 and 2025", 22.9333, 97.7500, "flashpoint",
      "Northern Shan State town. Control changed hands in 2024 and 2025 (press reporting). Position approximate.", "press reporting (approximate position)"),
    M("myawaddy", "Myawaddy (Thai-Myanmar border): border town with scam compounds", 16.6900, 98.5100, "flashpoint",
      "Border town where scam compounds have been reported (press reporting). Thailand cut power to border towns hosting such operations in February 2025.",
      "press reporting; Thai government (Feb 2025, earlier build)"),
    M("coco_islands", "Coco Islands (Myanmar): reported Chinese listening facilities (not officially confirmed)", 14.1000, 93.4000, "flashpoint",
      "Reports of Chinese electronic listening facilities on these islands are press-reported and not officially confirmed by Myanmar or China.",
      "press reporting (not officially confirmed)"),
    M("kyaukphyu", "Kyaukphyu deep-sea port and China-Myanmar pipeline terminus (Rakhine)", 19.4000, 93.5000, "pipeline",
      "China-backed deep-sea port in Rakhine State, reported as the terminus of the China-Myanmar oil and gas pipelines. Status and terms are reported, not verified.",
      "press reporting (Myanmar dashboard build)"),
    M("muse_pipeline", "China-Myanmar gas pipeline, Muse crossing", 23.9000, 97.9000, "pipeline",
      "Gas pipeline route from the China border at Muse towards Mandalay and Yangon (press reporting). Position approximate.",
      "press reporting (Myanmar dashboard build)"),
    M("pipeline_myanmar", "China-Myanmar oil and gas pipeline (Yunnan border route)", 24.9000, 98.6000, "pipeline",
      "Pipeline corridor from Yunnan through northern Myanmar (background; China v6 build).", "China v6 build (background)"),
    M("thilawa", "Thilawa port and special economic zone (south of Yangon)", 16.6667, 96.2833, "seaport",
      "Port and special economic zone south of Yangon (public information). Position approximate.", "public information"),
    M("dawei", "Dawei deep-sea port project (Andaman coast): status not verified", 14.0833, 98.2000, "seaport",
      "Deep-sea port and industrial zone project on the Andaman coast, announced with Thai backing (press reporting). Status not verified.",
      "press reporting (status not verified)"),
    M("coco_channel", "Coco Channel: strait between the Coco Islands and the Andaman Sea approaches", 13.0000, 93.0000, "chokepoint",
      "Channel near the Coco Islands, cited in strategic reporting. Position approximate.", "press reporting (approximate position)"),

    # ---------- Cyber and scam hubs (reported; OFAC designations are public) ----------
    M("kk_park", "KK Park (Myawaddy, Kayin State): scam compound raided in October 2025", 16.7200, 98.5300, "cyber_hub",
      "Raided in October 2025; the junta reported 635 illegal buildings demolished by January 2026. C4ADS found new construction, expansion or renovation at 14 of 21 suspected sites in Myawaddy since January 2026. Position approximate.",
      "PBS (Oct 2025); Prachatai English (2026, citing C4ADS)"),
    M("shwe_kokko", "Shwe Kokko (Kayin State): scam hub under the Karen National Army; US sanctions", 16.8500, 98.4500, "cyber_hub",
      "Headquarters of the Karen National Army, per OFAC. OFAC sanctioned nine targets here, including Yatai New City (2025). A planned 120 km2 zone valued at US$15bn (Mekong Eye, Nov 2025). Position approximate.",
      "US Treasury (sb0237, 2025); Mekong Eye (Nov 2025)"),
    M("yulong_bay", "Yulong Bay Park (Myawaddy): scam compound (reported)", 16.6800, 98.5000, "cyber_hub",
      "Reported scam compound a few kilometres from the official Thai checkpoint at Myawaddy (Mekong Eye, Nov 2025). Position approximate (Myawaddy township).",
      "Mekong Eye (Nov 2025)"),
    M("tc_capital", "T C Capital and Golden Sun Sky Casino (Sihanoukville, Cambodia): scam complex (OFAC designated)", 10.6100, 103.5200, "cyber_hub",
      "OFAC designated T C Capital, which owns the Golden Sun Sky Casino and Hotel, from which virtual-currency scams were run (US Treasury, 2025). Position approximate.",
      "US Treasury (sb0237, 2025)"),

    # ---------- Chokepoints ----------
    M("malacca", "Strait of Malacca: one of the world's busiest shipping lanes", 2.5000, 101.5000, "chokepoint",
      "The EIA describes it as critical for energy bound for China (EIA; SL-ML-IOR build).", "EIA (earlier build reference)"),
    M("singapore_strait", "Singapore Strait: southern exit of the Malacca Strait", 1.2000, 103.9000, "chokepoint",
      "Southern exit of the Malacca Strait (EIA; SL-ML-IOR build).", "EIA (earlier build reference)"),
    M("sunda", "Sunda Strait (Java-Sumatra)", -6.0500, 105.8000, "chokepoint",
      "Strait between Java and Sumatra (public information). Not verified in this build.", "public information (not verified in this build)"),
    M("lombok", "Lombok Strait (Bali-Lombok)", -8.7800, 115.7500, "chokepoint",
      "Deep-water route between the Java Sea and the Indian Ocean (public information). Not verified in this build.", "public information (not verified in this build)"),
    M("makassar", "Makassar Strait (Borneo-Sulawesi)", -2.0000, 118.5000, "chokepoint",
      "Strait between Borneo and Sulawesi (public information). Not verified in this build.", "public information (not verified in this build)"),
    M("balabac_strait", "Balabac Strait (Palawan-Borneo)", 7.5000, 117.0000, "chokepoint",
      "Strait between Palawan and Borneo; the Balabac EDCA site sits here (analysis). Not verified in this build.", "public information; Modern Diplomacy (Mar 2026, analysis)"),
    M("taiwan_strait", "Taiwan Strait", 24.6000, 119.9000, "chokepoint",
      "Strait between Taiwan and the Chinese mainland; the northern edge of the South China Sea approaches (Taiwan MND; China v6 build).",
      "Taiwan MND (China v6 build)"),
    M("bashi", "Bashi Channel (Luzon Strait): between Taiwan and the Philippines' Batanes", 21.5000, 121.0000, "chokepoint",
      "The northern gateway between the South China Sea and the Pacific (China v6 build; background).", "China v6 build (background)"),
]

# Nuclear plants listed in the WRI Global Power Plant Database inside the frame (Hainan and Guangxi coast). Generated by the geodata step.
_WRI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "wri_nuclear_sea.json")
if os.path.exists(_WRI):
    with open(_WRI, encoding="utf-8") as _f:
        for _m in json.load(_f):
            _m.pop("country_iso3", None)
            _m["aliases"] = [_m["name"].split(" (")[0].lower()]
            MARKERS.append(_m)

# Drop the empty placeholder row used while drafting (kept out of the dataset).
MARKERS = [m for m in MARKERS if m["id"] != "ram_naval_placeholder_skip"]
