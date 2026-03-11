"""
Programmatically generated product entries covering:
- Vienna Symphonic Library / VSL
- Reason Rack Extensions
- Ableton Live built-in instruments
- Korg / Roland / Yamaha software
- Cinesamples + boutique orchestral libraries
- Impact Soundworks
- Soundiron
- AudioImperia
- Strezov Sampling
- Plugin Alliance extended
- Vocal / choir sample libraries
- Film/game audio tools
- Loopmasters genre packs
- More free VSTs
"""

def _p(name, slug, dev, cat, price, ptype, desc, url, rating, rc):
    return {
        "name": name, "slug": slug, "developer": dev,
        "category": cat, "price": price, "priceType": ptype,
        "description": desc, "url": url,
        "rating": float(rating), "ratingCount": int(rc)
    }

PRODUCTS = [
    # ─── VIENNA SYMPHONIC LIBRARY ─────────────────────────────────────────────
    _p("Vienna Symphonic Library Synchron Elite Strings","vsl-synchron-elite-strings","Vienna Symphonic Library","sampler","$845","paid","Premium orchestral string library recorded in VSL's purpose-built Synchron Stage Vienna.","https://www.vsl.co.at/en/Strings/Synchron_Elite_Strings",4.9,834),
    _p("VSL Synchron Brass","vsl-synchron-brass","Vienna Symphonic Library","sampler","$675","paid","Full brass ensemble library with solo and section instruments recorded at Synchron Stage.","https://www.vsl.co.at/en/Brass/Synchron_Brass",4.9,712),
    _p("VSL Synchron Woodwinds","vsl-synchron-woodwinds","Vienna Symphonic Library","sampler","$575","paid","Comprehensive woodwind library with all standard orchestral woodwind instruments.","https://www.vsl.co.at/en/Woodwinds/Synchron_Woodwinds",4.8,634),
    _p("VSL Synchron Percussion","vsl-synchron-percussion","Vienna Symphonic Library","drums","$345","paid","Orchestral percussion library with timpani, pitched, and unpitched instruments.","https://www.vsl.co.at/en/Percussion/Synchron_Percussion",4.8,534),
    _p("VSL Dimension Strings","vsl-dimension-strings","Vienna Symphonic Library","sampler","$845","paid","Positional string library with 7 players independently controllable in stereo.","https://www.vsl.co.at/en/Strings/Dimension_Strings",4.9,712),
    _p("VSL Vienna Special Edition","vsl-vienna-special-edition","Vienna Symphonic Library","sampler","$295","paid","Entry-level orchestral library with strings, brass, woodwinds, and percussion.","https://www.vsl.co.at/en/Orchestral_Strings/Vienna_Special_Edition",4.7,623),
    _p("VSL Synchron-ized Harp","vsl-synchron-harp","Vienna Symphonic Library","sampler","$195","paid","Concert harp library recorded at Synchron Stage with glissando and arpeggio phrases.","https://www.vsl.co.at/en/Keyboards/Synchron_Harp",4.8,423),
    _p("VSL Big Bang Orchestra Venus","vsl-bbo-venus","Vienna Symphonic Library","sampler","$145","paid","Intimate strings expansion for the Big Bang Orchestra series.","https://www.vsl.co.at/en/Big_Bang_Orchestra/Venus",4.7,312),
    _p("VSL Vienna MIR Pro 3D","vsl-mir-pro-3d","Vienna Symphonic Library","effects","$375","paid","Convolution reverb with 3D room simulation based on Vienna's concert halls.","https://www.vsl.co.at/en/Vienna_Software_Package/MIR_Pro_3D",4.8,456),
    _p("VSL Synchron Piano","vsl-synchron-piano","Vienna Symphonic Library","sampler","$295","paid","Bösendorfer Imperial piano captured at Synchron Stage with multiple mic positions.","https://www.vsl.co.at/en/Keyboards/Synchron_Piano",4.9,634),
    _p("VSL Vienna Ensemble Pro 7","vsl-ensemble-pro-7","Vienna Symphonic Library","utility","$295","paid","Networked plugin host for running large orchestral templates across multiple computers.","https://www.vsl.co.at/en/Vienna_Software_Package/Vienna_Ensemble_Pro_7",4.8,534),

    # ─── CINESAMPLES ──────────────────────────────────────────────────────────
    _p("CineStrings CORE","cinesamples-cinestrings-core","Cinesamples","sampler","$399","paid","Intimate Hollywood string library with detailed legato and expressive articulations.","https://cinesamples.com/product/cinestrings-core",4.8,623),
    _p("CineBrass CORE","cinesamples-cinebrass-core","Cinesamples","sampler","$399","paid","Powerful Hollywood brass library recorded in Los Angeles with 5 mic positions.","https://cinesamples.com/product/cinebrass-core",4.8,534),
    _p("CineWinds CORE","cinesamples-cinewinds-core","Cinesamples","sampler","$299","paid","Complete woodwind library for film and media composers.","https://cinesamples.com/product/cinewinds-core",4.7,423),
    _p("CinePerc CORE","cinesamples-cineperc-core","Cinesamples","drums","$299","paid","Cinematic percussion library with orchestral, ethnic, and electronic elements.","https://cinesamples.com/product/cineperc-core",4.7,389),
    _p("CineHarps","cinesamples-cineharps","Cinesamples","sampler","$149","paid","Intimate orchestral harp library with extensive glissando and effect phrases.","https://cinesamples.com/product/cineharps",4.7,312),
    _p("CinePiano","cinesamples-cinepiano","Cinesamples","sampler","$149","paid","Cinematic piano with intimate character suitable for film and TV scoring.","https://cinesamples.com/product/cinepiano",4.7,356),
    _p("CineChoir","cinesamples-cinechoir","Cinesamples","sampler","$299","paid","Professional vocal ensemble with wordbuilder-style phoneme control.","https://cinesamples.com/product/cinechoir",4.7,423),
    _p("Cinesamples Piano in Blue","cinesamples-piano-in-blue","Cinesamples","sampler","$149","paid","Intimate Yamaha C7 concert grand captured in a small Paris recording studio.","https://cinesamples.com/product/piano-in-blue",4.8,534),

    # ─── IMPACT SOUNDWORKS ────────────────────────────────────────────────────
    _p("Juggernaut","impact-soundworks-juggernaut","Impact Soundworks","sampler","$149","paid","Epic hybrid cinematic toolkit with 11 NKI instruments for massive productions.","https://impactsoundworks.com/product/juggernaut/",4.7,423),
    _p("Shreddage 3 Stratus","impact-shreddage-3-stratus","Impact Soundworks","sampler","$199","paid","Electric guitar sample library with realistic strumming, picking, and muting.","https://impactsoundworks.com/product/shreddage-3-stratus/",4.7,534),
    _p("Shreddage 3 Hydra","impact-shreddage-3-hydra","Impact Soundworks","sampler","$249","paid","7-string and 8-string electric guitar library for extreme metal production.","https://impactsoundworks.com/product/shreddage-3-hydra/",4.7,456),
    _p("Shreddage 3 Bass","impact-shreddage-3-bass","Impact Soundworks","sampler","$149","paid","Bass guitar sample library with slap, pick, finger, and chordal techniques.","https://impactsoundworks.com/product/shreddage-3-bass/",4.7,489),
    _p("Super Audio Cart","impact-super-audio-cart","Impact Soundworks","sampler","$99","paid","Retro video game sample library covering NES, SNES, Genesis, and more systems.","https://impactsoundworks.com/product/super-audio-cart/",4.7,534),
    _p("Lorelei","impact-lorelei","Impact Soundworks","sampler","$149","paid","Solo female vocalist instrument with breathtaking phrasing and lush harmonics.","https://impactsoundworks.com/product/lorelei/",4.7,345),
    _p("Percussion Collective","impact-percussion-collective","Impact Soundworks","drums","$149","paid","World and orchestral percussion library with taiko, frame drums, and metals.","https://impactsoundworks.com/product/percussion-collective/",4.6,312),

    # ─── SOUNDIRON ────────────────────────────────────────────────────────────
    _p("Mercury Elements","soundiron-mercury-elements","Soundiron","sampler","$399","paid","Modern epic choir library with full ensemble and solo voice articulations.","https://soundiron.com/products/mercury-elements",4.8,423),
    _p("Olympus Elements","soundiron-olympus-elements","Soundiron","sampler","$199","paid","Intimate choir library with professional adult ensemble in a concert hall.","https://soundiron.com/products/olympus-elements",4.7,389),
    _p("Requiem Light","soundiron-requiem-light","Soundiron","sampler","$149","paid","Dark, emotive choir library designed for requiem-style composition.","https://soundiron.com/products/requiem-light",4.7,312),
    _p("Voices of Wind","soundiron-voices-of-wind","Soundiron","sampler","$99","paid","Ethereal breathy choir textures and vocal pads for atmospheric scoring.","https://soundiron.com/products/voices-of-wind",4.6,267),
    _p("Iron Pack","soundiron-iron-pack","Soundiron","drums","$99","paid","Industrial and hybrid percussion library with metal textures and impacts.","https://soundiron.com/products/iron-pack",4.6,234),
    _p("Steinway Model B","soundiron-steinway-model-b","Soundiron","sampler","$99","paid","Intimate Steinway Model B grand piano with natural room ambience.","https://soundiron.com/products/steinway-model-b",4.7,345),

    # ─── AUDIO IMPERIA ────────────────────────────────────────────────────────
    _p("Audio Imperia Jaeger","audio-imperia-jaeger","Audio Imperia","sampler","$249","paid","Essential orchestral toolkit with strings, brass, woodwinds, and percussion phrases.","https://www.audioimperia.com/products/jaeger",4.8,534),
    _p("Audio Imperia Nucleus","audio-imperia-nucleus","Audio Imperia","sampler","$249","paid","Hybrid orchestral instrument combining live ensemble with modern synthesis.","https://www.audioimperia.com/products/nucleus",4.7,423),
    _p("Audio Imperia Areia","audio-imperia-areia","Audio Imperia","sampler","$149","paid","Desert-inspired world percussion and texture library for cinematic scoring.","https://www.audioimperia.com/products/areia",4.6,312),

    # ─── STREZOV SAMPLING ────────────────────────────────────────────────────
    _p("Storm Choir Ultimate","strezov-storm-choir-ultimate","Strezov Sampling","sampler","$499","paid","Massive epic choir library with aggressive performances and massive dynamics.","https://strezovsampling.com/product/storm-choir-2/",4.9,623),
    _p("Storm Choir 2","strezov-storm-choir-2","Strezov Sampling","sampler","$299","paid","Epic choral library with full ensemble SATB voices and solo performances.","https://strezovsampling.com/product/storm-choir-2/",4.8,534),
    _p("Wotan - Taiko & War Drums","strezov-wotan","Strezov Sampling","drums","$299","paid","Epic taiko and war drum library for cinematic action sequences.","https://strezovsampling.com/product/wotan/",4.8,456),
    _p("Freyja Female Choir","strezov-freyja","Strezov Sampling","sampler","$249","paid","Beautiful female choir library with Nordic and classical influences.","https://strezovsampling.com/product/freyja/",4.8,423),

    # ─── MUSICAL SAMPLING ─────────────────────────────────────────────────────
    _p("Bohemian Violin Pizzicato","musical-sampling-bohemian-pizzicato","Musical Sampling","sampler","$149","paid","Expressive solo violin pizzicato library with multiple performance techniques.","https://www.musicalsampling.com/",4.7,267),
    _p("Trailer Strings","musical-sampling-trailer-strings","Musical Sampling","sampler","$149","paid","Cinematic string phrases perfect for trailer and action music production.","https://www.musicalsampling.com/",4.7,312),

    # ─── KORG SOFTWARE ────────────────────────────────────────────────────────
    _p("Korg Gadget 3","korg-gadget-3","Korg","daw","$49","paid","Award-winning collection of synthesizers and drum machines for music production.","https://www.korg.com/us/products/software/korg_gadget_3/",4.7,712),
    _p("Korg Legacy Collection","korg-legacy-collection","Korg","synth","$299","paid","Classic Korg synthesizer emulations including MS-20, Polysix, and Wavestation.","https://www.korg.com/us/products/software/korg_legacy_collection/",4.8,834),
    _p("Korg M1","korg-m1-plugin","Korg","synth","$39","paid","Digital emulation of the iconic Korg M1 workstation synthesizer from 1988.","https://www.korg.com/us/products/software/m1/",4.8,923),
    _p("Korg Wavestation","korg-wavestation","Korg","synth","$39","paid","Emulation of the legendary Korg Wavestation advanced vector synthesis keyboard.","https://www.korg.com/us/products/software/wavestation/",4.7,712),
    _p("Korg Triton","korg-triton","Korg","synth","$49","paid","Digital emulation of the Korg Triton workstation synthesizer.","https://www.korg.com/us/products/software/triton/",4.7,634),
    _p("Korg ARP Odyssei","korg-arp-odyssei","Korg","synth","$39","paid","Authentic recreation of the classic ARP Odyssey analog synthesizer.","https://www.korg.com/us/products/software/arp_odyssei/",4.8,712),
    _p("Korg iPolysix","korg-ipolysix","Korg","synth","$15","paid","iOS version of the classic Korg Polysix polyphonic analog synthesizer.","https://www.korg.com/us/products/software/ipolysix/",4.5,356),
    _p("Korg MS-20","korg-ms-20-plugin","Korg","synth","$39","paid","Semi-modular analog synthesizer emulation of the legendary Korg MS-20.","https://www.korg.com/us/products/software/ms20/",4.8,823),

    # ─── ROLAND CLOUD ─────────────────────────────────────────────────────────
    _p("Roland Cloud Subscription","roland-cloud-subscription","Roland","synth","Subscription","subscription","Access to 100+ Roland synthesizers, drum machines, and instruments via subscription.","https://www.roland.com/us/categories/apps/roland-cloud/",4.7,712),
    _p("Roland Zenology","roland-zenology","Roland","synth","$7","subscription","ZEN-Core synthesizer engine with Supernatural acoustic and modeled synthesis.","https://www.roland.com/us/products/zenology/",4.7,534),
    _p("Roland TR-808 Rhythm Composer (Cloud)","roland-tr-808-cloud","Roland","drums","Subscription","subscription","Official Roland TR-808 drum machine software emulation via Roland Cloud.","https://www.roland.com/us/products/tr-808/",4.8,712),
    _p("Roland TR-909 (Cloud)","roland-tr-909-cloud","Roland","drums","Subscription","subscription","Official Roland TR-909 drum machine emulation via Roland Cloud.","https://www.roland.com/us/products/tr-909/",4.8,634),
    _p("Roland Jupiter-8 (Cloud)","roland-jupiter-8-cloud","Roland","synth","Subscription","subscription","Official Roland Jupiter-8 polyphonic synthesizer emulation via Roland Cloud.","https://www.roland.com/us/products/jupiter-8/",4.8,712),
    _p("Roland Juno-106 (Cloud)","roland-juno-106-cloud","Roland","synth","Subscription","subscription","Official Roland Juno-106 synthesizer emulation via Roland Cloud.","https://www.roland.com/us/products/juno-106/",4.8,823),
    _p("Roland Juno-60 (Cloud)","roland-juno-60-cloud","Roland","synth","Subscription","subscription","Official Roland Juno-60 chorus synthesizer emulation via Roland Cloud.","https://www.roland.com/us/products/juno-60/",4.8,712),
    _p("Roland SH-101 (Cloud)","roland-sh-101-cloud","Roland","synth","Subscription","subscription","Official Roland SH-101 monosynth emulation via Roland Cloud.","https://www.roland.com/us/products/sh-101/",4.7,534),
    _p("Roland D-50 Linear Synth (Cloud)","roland-d-50-cloud","Roland","synth","Subscription","subscription","Official Roland D-50 linear arithmetic synthesis keyboard emulation.","https://www.roland.com/us/products/d-50/",4.8,634),
    _p("Roland SH-2 (Cloud)","roland-sh-2-cloud","Roland","synth","Subscription","subscription","Official Roland SH-2 two-oscillator monosynth emulation.","https://www.roland.com/us/products/sh-2/",4.6,312),
    _p("Roland System-8 (Cloud)","roland-system-8-cloud","Roland","synth","Subscription","subscription","ACB-based programmable synthesizer with Jupiter-8 and Juno-106 plug-out capability.","https://www.roland.com/us/products/system-8/",4.7,423),

    # ─── ABLETON LIVE INSTRUMENTS ─────────────────────────────────────────────
    _p("Ableton Drift","ableton-drift","Ableton","synth","Included with Live 11 Suite","paid","FM and wavetable hybrid synthesizer with dual oscillator engines in Live 11 Suite.","https://www.ableton.com/en/packs/drift/",4.7,534),
    _p("Ableton Meld","ableton-meld","Ableton","synth","Included with Live 11 Suite","paid","Polyphonic synthesizer with frequency modulation and wavetable oscillators.","https://www.ableton.com/en/packs/meld/",4.7,423),
    _p("Ableton Analog","ableton-analog","Ableton","synth","Included with Live Suite","paid","Classic analog synthesizer emulation built into Ableton Live Suite.","https://www.ableton.com/en/packs/analog/",4.7,634),
    _p("Ableton Collision","ableton-collision","Ableton","synth","Included with Live Suite","paid","Physical modeling percussion synthesizer using modal synthesis.","https://www.ableton.com/en/packs/collision/",4.6,423),
    _p("Ableton Electric","ableton-electric","Ableton","synth","Included with Live Suite","paid","Electric piano instrument based on physical models of tine and reed pianos.","https://www.ableton.com/en/packs/electric/",4.7,534),
    _p("Ableton Tension","ableton-tension","Ableton","synth","Included with Live Suite","paid","Physical modeling string synthesizer with realistic string resonance.","https://www.ableton.com/en/packs/tension/",4.5,312),
    _p("Ableton Operator","ableton-operator","Ableton","synth","Included with Live Suite","paid","FM synthesizer with 4 operators and flexible modulation routing.","https://www.ableton.com/en/packs/operator/",4.7,823),
    _p("Ableton Sampler","ableton-sampler","Ableton","sampler","Included with Live Suite","paid","Advanced multisampler with real-time warping, filters, and LFO modulation.","https://www.ableton.com/en/packs/sampler/",4.7,712),
    _p("Ableton Wavetable","ableton-wavetable","Ableton","synth","Included with Live Suite","paid","Wavetable synthesizer with two oscillators, dual filters, and LFO modulation.","https://www.ableton.com/en/packs/wavetable/",4.8,834),
    _p("Ableton Drum Rack","ableton-drum-rack","Ableton","drums","Included with Live","paid","Pad-based drum sampler for building custom drum kits with 128 pads.","https://www.ableton.com/en/manual/instrument-drum-and-effect-racks/",4.7,1023),
    _p("Ableton Max for Live Granulator II","ableton-granulator-ii","Ableton","experimental","Included with Live Suite","paid","Granular synthesizer based on real-time audio granulation and looping.","https://www.ableton.com/en/packs/granulator-ii/",4.8,712),
    _p("Ableton Orchestral Strings","ableton-orchestral-strings","Ableton","sampler","$49","paid","String library expansion for Ableton Live with multiple articulations.","https://www.ableton.com/en/packs/orchestral-strings/",4.5,312),
    _p("Ableton Orchestral Brass","ableton-orchestral-brass","Ableton","sampler","$49","paid","Brass section expansion pack for Ableton Live with section and solo instruments.","https://www.ableton.com/en/packs/orchestral-brass/",4.5,289),

    # ─── REASON RACK EXTENSIONS ───────────────────────────────────────────────
    _p("Reason Thor Polyphonic Synthesizer","reason-thor","Reason Studios","synth","Included with Reason","paid","Semi-modular polyphonic synthesizer combining 6 oscillator types in Reason.","https://www.reasonstudios.com/shop/rack-extension/thor-polyphonic-synthesizer/",4.8,712),
    _p("Reason Kong Drum Designer","reason-kong","Reason Studios","drums","Included with Reason","paid","Drum machine with 16 pads, each with its own signal chain and synth module.","https://www.reasonstudios.com/shop/rack-extension/kong-drum-designer/",4.7,534),
    _p("Reason Neptune Pitch Adjuster","reason-neptune","Reason Studios","vocal","Included with Reason","paid","Real-time pitch correction and voice tuning module in Reason's rack.","https://www.reasonstudios.com/shop/rack-extension/neptune-pitch-adjuster-voice-synth/",4.5,345),
    _p("Reason Radical Piano","reason-radical-piano","Reason Studios","sampler","Included with Reason","paid","Piano instrument module with 3 distinct piano models and dynamic layers.","https://www.reasonstudios.com/shop/rack-extension/radical-piano/",4.6,423),
    _p("Reason Europa","reason-europa","Reason Studios","synth","Included with Reason","paid","Spectral wavetable synthesizer with three unique synthesis engines.","https://www.reasonstudios.com/shop/rack-extension/europa-shapeshifting-synthesizer/",4.8,712),
    _p("Reason Grain","reason-grain","Reason Studios","synth","Included with Reason","paid","Granular synthesizer for creating evolving textures and unique timbres.","https://www.reasonstudios.com/shop/rack-extension/grain-sample-manipulator/",4.7,534),
    _p("Reason Mimic Creative Sampler","reason-mimic","Reason Studios","sampler","Included with Reason","paid","Creative sampler with loop slicing, envelope shaping, and granular features.","https://www.reasonstudios.com/shop/rack-extension/mimic-creative-sampler/",4.6,423),
    _p("Reason Monotone","reason-monotone","Reason Studios","synth","Included with Reason","paid","Mono bass synthesizer inspired by classic analog bassline machines.","https://www.reasonstudios.com/shop/rack-extension/monotone-bass-synthesizer/",4.5,312),
    _p("Reason Rytmik","reason-rytmik","Reason Studios","drums","$49","paid","Retro drum machine rack extension with analog and sample-based engines.","https://www.reasonstudios.com/shop/rack-extension/rytmik-retrobuzz/",4.5,267),
    _p("Reason Parsec 2","reason-parsec-2","Reason Studios","synth","$79","paid","Spectral synthesizer with additive and subtractive spectrum engines.","https://www.reasonstudios.com/shop/rack-extension/parsec-spectral-synthesizer/",4.6,312),
    _p("Reason A-List Acoustic Guitarist","reason-acoustic-guitarist","Reason Studios","sampler","$79","paid","Realistic acoustic guitar instrument with chord detection and auto-strumming.","https://www.reasonstudios.com/shop/rack-extension/a-list-acoustic-guitarist/",4.6,378),
    _p("Reason Radical Keys","reason-radical-keys","Reason Studios","sampler","$49","paid","Vintage keyboard collection including Rhodes, Wurly, and clavinet sounds.","https://www.reasonstudios.com/shop/rack-extension/radical-keys/",4.6,345),
    _p("Reason Algorave Synth","reason-algorave","Reason Studios","experimental","$49","paid","Algorithmic and generative synthesizer for evolving textures and sequences.","https://www.reasonstudios.com/",4.4,189),

    # ─── STEINBERG INSTRUMENTS ────────────────────────────────────────────────
    _p("Steinberg HALion 7","steinberg-halion-7","Steinberg","sampler","$349","paid","Professional software sampler and synthesizer with 4,500+ sounds included.","https://www.steinberg.net/halion/",4.7,712),
    _p("Steinberg HALion Sonic 7","steinberg-halion-sonic-7","Steinberg","sampler","$99","paid","Multi-timbral sound module with 3,000+ sounds from HALion's library.","https://www.steinberg.net/halion-sonic/",4.6,534),
    _p("Steinberg Padshop 2","steinberg-padshop-2","Steinberg","synth","$49","paid","Granular/spectral synthesizer with over 500 presets for ambient textures.","https://www.steinberg.net/padshop/",4.6,423),
    _p("Steinberg Retrologue 2","steinberg-retrologue-2","Steinberg","synth","$49","paid","Classic analog synthesizer emulation with virtual analog sound engine.","https://www.steinberg.net/retrologue/",4.6,389),
    _p("Steinberg SpectraLayers Pro 11","steinberg-spectralayers-pro-11","Steinberg","utility","$399","paid","Spectral audio editing and unmixing tool with AI stem separation.","https://www.steinberg.net/spectralayers/",4.7,534),
    _p("Steinberg WaveLab Pro 12","steinberg-wavelab-pro-12","Steinberg","mastering","$499","paid","Professional audio mastering and restoration workstation.","https://www.steinberg.net/wavelab/",4.8,712),
    _p("Steinberg The Grand 3","steinberg-the-grand-3","Steinberg","sampler","$99","paid","Acoustic piano instrument with 7 premium grand pianos and room modeling.","https://www.steinberg.net/the-grand/",4.7,534),

    # ─── FREE PLUGINS (additional) ────────────────────────────────────────────
    _p("PaulXStretch","paulxstretch","Xenakios","experimental","Free","free","Extreme time-stretching plugin for creating drone and ambient textures.","https://sonosaurus.com/paulxstretch/",4.7,934),
    _p("T-Force Alpha Plus","t-force-alpha-plus","Mastrcode Music","synth","Free","free","Free FM synthesizer with 6 FM operators and 256 preset patches.","https://www.mmastrcode-music.de/",4.5,534),
    _p("Synth1","synth1","Ichiro Toda","synth","Free","free","Free 32-voice polyphonic software synthesizer with 35,000+ user presets.","http://www.geocities.jp/daichi1969/softsynth/",4.6,1456),
    _p("Noize2","noize2","Jeroen Breebaart","synth","Free","free","Free additive/subtractive synthesizer with modular signal path.","https://www.jeroenb.com/noize/",4.3,234),
    _p("Charlatan","charlatan","Blaukraut Engineering","synth","Free","free","Free virtual analog synthesizer with unison and stereo spread.","https://blaukraut.de/charlatan/",4.4,456),
    _p("Digits","digits","Extent of the Jam","synth","Free","free","Free phase modulation synthesizer inspired by the Casio CZ series.","https://www.extentofthejam.com/",4.5,356),
    _p("Spiro","spiro","Nusofting","synth","Free","free","Free virtual analog synthesizer with 4 oscillators and flexible modulation.","https://nusofting.com/",4.4,267),
    _p("VSCO 2 Community Edition","vsco-2-community","Versilian Studios","sampler","Free","free","Free orchestral sample library covering all standard orchestral instruments.","https://vis.versilstudios.com/vsco-community.html",4.5,812),
    _p("Spitfire Audio LABS Peel Guitar","spitfire-labs-peel-guitar","Spitfire Audio","sampler","Free","free","Free intimate acoustic guitar with unique palm-muted and open string samples.","https://www.spitfireaudio.com/labs",4.6,634),
    _p("Spitfire Audio LABS Amplified Cello Quartet","spitfire-labs-amplified-cello","Spitfire Audio","sampler","Free","free","Free amplified cello quartet with electric and acoustic tones blended.","https://www.spitfireaudio.com/labs",4.7,712),
    _p("Native Instruments Komplete Start","ni-komplete-start","Native Instruments","sampler","Free","free","Free bundle of instruments, samples, and effects — over 2,000 sounds.","https://www.native-instruments.com/en/products/komplete/bundles/komplete-start/",4.7,1789),
    _p("Arturia Analog Lab Play","arturia-analog-lab-play","Arturia","synth","Free","free","Free version of Analog Lab with 500 sounds from Arturia's V Collection.","https://www.arturia.com/products/software-instruments/analoglab/overview",4.6,923),
    _p("Waveform Free","waveform-free","Tracktion","daw","Free","free","Fully-featured DAW with unlimited tracks and built-in plugins.","https://www.tracktion.com/products/waveform-free",4.3,534),
    _p("BandLab","bandlab-daw","BandLab Technologies","daw","Free","free","Free cloud-based DAW with collaboration features and virtual instruments.","https://www.bandlab.com/",4.3,712),
    _p("Audacity","audacity","Audacity Team","utility","Free","free","Free open-source audio editor and recorder for Windows, macOS, and Linux.","https://www.audacityteam.org/",4.4,2000),
    _p("ocenaudio","ocenaudio","ocenaudio team","utility","Free","free","Free cross-platform audio editor with real-time preview and VST plugin support.","https://www.ocenaudio.com/",4.2,456),
    _p("TyrellN6","tyrelln6-vst","u-he","synth","Free","free","Free virtual analog synthesizer originally published in Computer Music magazine.","https://u-he.com/products/tyrelln6/",4.5,712),
    _p("Podolski","podolski-vst","u-he","synth","Free","free","Free simple, CPU-friendly virtual analog synthesizer by u-he.","https://u-he.com/products/podolski/",4.4,534),
    _p("GVST GDelay","gvst-gdelay","GVST","effects","Free","free","Free simple stereo delay plugin with tempo-sync and feedback controls.","https://www.gvst.co.uk/",4.2,345),
    _p("GVST GSnap","gvst-gsnap","GVST","vocal","Free","free","Free pitch correction plugin for vocals and melodic instruments.","https://www.gvst.co.uk/gsnap.htm",4.2,567),
    _p("mda Delay","mda-delay","MDA","effects","Free","free","Free simple stereo delay plugin from the classic MDA plugin collection.","http://mda.smartelectronix.com/",4.2,312),
    _p("mda Ambience","mda-ambience","MDA","effects","Free","free","Free reverb plugin with small and large room algorithms.","http://mda.smartelectronix.com/",4.2,289),
    _p("ReaFIR","reafir","Cockos","utility","Free","free","Free FFT-based EQ, compressor, and noise reduction from Cockos.","https://www.reaper.fm/reaplugs/",4.5,712),
    _p("ReaComp","reacomp","Cockos","effects","Free","free","Free compressor plugin from the ReaPlugs suite by Cockos/REAPER.","https://www.reaper.fm/reaplugs/",4.5,634),
    _p("ReaEQ","reaeq","Cockos","effects","Free","free","Free parametric equalizer plugin from Cockos/REAPER with unlimited bands.","https://www.reaper.fm/reaplugs/",4.5,712),
    _p("ReaGate","reagate","Cockos","effects","Free","free","Free gate/expander plugin from the Cockos ReaPlugs suite.","https://www.reaper.fm/reaplugs/",4.4,423),
    _p("ReaXcomp","reaxcomp","Cockos","mastering","Free","free","Free unlimited band multiband compressor from Cockos/REAPER.","https://www.reaper.fm/reaplugs/",4.5,456),
    _p("Tal Chorus LX","tal-chorus-lx","TAL Software","effects","Free","free","Free Roland Juno-60 chorus emulation plugin with warm, lush character.","https://tal-software.com/products/tal-chorus-lx",4.7,1123),
    _p("OrilRiver","orilriver","Denis Tihanov","effects","Free","free","Free algorithmic stereo reverb plugin covering hall, room, and special modes.","https://www.kvraudio.com/product/orilriver-by-denis-tihanov",4.6,712),
    _p("Ambience","ambience-silverspike","Silverspike","effects","Free","free","Free reverb plugin with warm, dense reverberation and small-to-large spaces.","https://www.silverspike.com/",4.4,356),
    _p("Glitchmachines Hysteresis","glitchmachines-hysteresis","Glitchmachines","experimental","Free","free","Free glitch delay plugin with feedback destruction and modulation.","https://glitchmachines.com/products/hysteresis/",4.6,534),
    _p("Glitchmachines Fracture","glitchmachines-fracture","Glitchmachines","experimental","Free","free","Free buffer-effect plugin for real-time stuttering, repeating, and reversing.","https://glitchmachines.com/products/fracture/",4.6,623),
    _p("Boogex","boogex-audio-damage","Audio Damage","guitar","Free","free","Free guitar amplifier plugin with cabinet IR loading capability.","https://www.audiodamage.com/",4.3,345),

    # ─── AUDIO DAMAGE ─────────────────────────────────────────────────────────
    _p("Audio Damage Quanta 2","audio-damage-quanta-2","Audio Damage","synth","$99","paid","Granular synthesizer with up to 32 grain voices and deep modulation.","https://www.audiodamage.com/pages/current",4.7,423),
    _p("Audio Damage Phosphor 3","audio-damage-phosphor-3","Audio Damage","synth","$49","paid","Additive FM synthesizer inspired by the Casio CZ series phase distortion.","https://www.audiodamage.com/pages/current",4.5,312),
    _p("Audio Damage Kombinat Dva","audio-damage-kombinat-dva","Audio Damage","effects","$49","paid","Distortion plugin with 3 distortion units and a 3-band EQ.","https://www.audiodamage.com/pages/current",4.4,267),
    _p("Audio Damage Eos 2","audio-damage-eos-2","Audio Damage","effects","$79","paid","Algorithmic reverb with Hall, Chamber, and Plate algorithms.","https://www.audiodamage.com/pages/current",4.6,345),
    _p("Audio Damage Filterstation 2","audio-damage-filterstation-2","Audio Damage","effects","$49","paid","Dual-filter plugin with 10 filter types and modulation options.","https://www.audiodamage.com/pages/current",4.5,289),
    _p("Audio Damage Discord 4","audio-damage-discord-4","Audio Damage","effects","$79","paid","Pitch shifter and delay combining detuning, harmonization, and modulation.","https://www.audiodamage.com/pages/current",4.5,312),

    # ─── GLITCHMACHINES ──────────────────────────────────────────────────────
    _p("Glitchmachines Palindrome","glitchmachines-palindrome","Glitchmachines","experimental","$39","paid","Granular gate effect for rhythmic glitch and fragmented audio manipulation.","https://glitchmachines.com/products/palindrome/",4.6,312),
    _p("Glitchmachines Quadrant","glitchmachines-quadrant","Glitchmachines","experimental","$39","paid","4-module effects system for advanced glitch and experimental processing.","https://glitchmachines.com/products/quadrant/",4.6,289),
    _p("Glitchmachines Subvert","glitchmachines-subvert","Glitchmachines","experimental","$39","paid","Circuit-bent inspired effects processor for digital destruction and glitch art.","https://glitchmachines.com/products/subvert/",4.5,267),

    # ─── INSTRUMENT / SOUND DESIGN ────────────────────────────────────────────
    _p("Spitfire Hans Zimmer Percussion","spitfire-hans-zimmer-percussion","Spitfire Audio","drums","$349","paid","Massive ensemble percussion library from Hans Zimmer's LA percussion sessions.","https://www.spitfireaudio.com/hans-zimmer-percussion",4.9,834),
    _p("Spitfire Tundra","spitfire-tundra","Spitfire Audio","sampler","$149","paid","Intimate Nordic chamber strings recorded in a converted Danish barn.","https://www.spitfireaudio.com/tundra",4.8,534),
    _p("Spitfire BT Phobos","spitfire-bt-phobos","Spitfire Audio","experimental","$149","paid","Complex evolving textures and sound design tool developed with artist BT.","https://www.spitfireaudio.com/bt-phobos",4.7,423),
    _p("Spitfire Albion II Loegria","spitfire-albion-ii-loegria","Spitfire Audio","sampler","$299","paid","Second Albion installment with cinematic strings and hybrid electronics.","https://www.spitfireaudio.com/albion-ii",4.7,534),
    _p("Spitfire Albion V Tundra","spitfire-albion-v-tundra","Spitfire Audio","sampler","$299","paid","Nordic chamber orchestra with organic textures and intimate recording.","https://www.spitfireaudio.com/albion-v",4.8,612),
    _p("EastWest Quantum Leap Ministry of Rock 2","ew-ministry-rock-2","EastWest","sampler","$295","paid","Essential rock sample library with guitars, bass, drums, and vocals.","https://www.soundsonline.com/ministry-of-rock-2",4.7,534),
    _p("EastWest Voices of the Empire","ew-voices-of-empire","EastWest","sampler","$295","paid","Male and female epic choir with legato phrases and staccato syllables.","https://www.soundsonline.com/voices-of-the-empire",4.7,456),
    _p("EastWest Ghostwriter","ew-ghostwriter","EastWest","sampler","$195","paid","Dark and cinematic hybrid instrument for supernatural and horror scoring.","https://www.soundsonline.com/ghostwriter",4.6,345),
    _p("8Dio Studio Strings","8dio-studio-strings","8Dio","sampler","$299","paid","Close-mic studio string library with intimate chamber character.","https://8dio.com/product/studio-strings/",4.7,389),
    _p("8Dio Claire Solo Violin","8dio-claire-solo-violin","8Dio","sampler","$149","paid","Solo violin instrument with extensive vibrato, portamento, and expressive techniques.","https://8dio.com/product/claire/",4.7,345),
    _p("8Dio 1928 Bosendorfer","8dio-bosendorfer-1928","8Dio","sampler","$149","paid","1928 Bösendorfer Imperial grand piano with vintage tone and room ambience.","https://8dio.com/product/1928-bosendorfer/",4.8,456),
    _p("8Dio Anthology Brass","8dio-anthology-brass","8Dio","sampler","$399","paid","Premier brass ensemble library with dense, powerful recordings.","https://8dio.com/product/anthology-brass/",4.8,423),

    # ─── MINIMAL AUDIO ────────────────────────────────────────────────────────
    _p("Minimal Audio Rift","minimal-audio-rift","Minimal Audio","effects","$89","paid","Modular multi-effects system with 6 effect types and wavetable modulation.","https://www.minimal.audio/products/rift",4.8,534),
    _p("Minimal Audio Current","minimal-audio-current","Minimal Audio","synth","$149","paid","Subtractive wavetable synthesizer with unique Spectral Modifier system.","https://www.minimal.audio/products/current",4.8,456),
    _p("Minimal Audio Cluster Delay","minimal-audio-cluster-delay","Minimal Audio","effects","$79","paid","Granular delay plugin with cluster and spread modes for unique delay effects.","https://www.minimal.audio/products/cluster-delay",4.7,312),

    # ─── CYMATICS / PRODUCER TOOLS ───────────────────────────────────────────
    _p("Cymatics Signature Bundle","cymatics-signature-bundle","Cymatics","sampler","$49","paid","Premium producer sample pack with loops, one-shots, and presets.","https://cymatics.fm/collections/bundles",4.6,534),
    _p("Splice Sounds Bundle","splice-sounds-bundle","Splice","sampler","$7","subscription","Monthly subscription for unlimited access to millions of royalty-free samples.","https://splice.com/sounds",4.7,1789),
    _p("KSHMR Sample Library","kshmr-sample-library","KSHMR","sampler","$49","paid","Producer sample pack from chart-topping EDM artist KSHMR.","https://splice.com/sounds/kshmr",4.6,456),
    _p("Loopmasters Deep House Essentials","loopmasters-deep-house","Loopmasters","sampler","$29","paid","Deep house loops, one-shots, and synth patches for DJ and producer use.","https://www.loopmasters.com/",4.5,345),
    _p("Loopmasters Drum and Bass Arsenal","loopmasters-dnb-arsenal","Loopmasters","sampler","$29","paid","Drum and bass sample pack with breaks, bass loops, and synth hits.","https://www.loopmasters.com/",4.5,312),
    _p("Loopmasters Trap Essentials","loopmasters-trap-essentials","Loopmasters","sampler","$29","paid","Modern trap production sample pack with 808s, hats, and melodic loops.","https://www.loopmasters.com/",4.5,389),
    _p("Black Octopus Leviathan 3","black-octopus-leviathan-3","Black Octopus Sound","sampler","$79","paid","Massive EDM sample pack with basses, leads, pads, and drum loops.","https://blackoctopus-sound.com/",4.7,456),
    _p("Black Octopus Skully Drum Kit","black-octopus-skully","Black Octopus Sound","drums","$39","paid","Hip-hop and trap drum kit with crispy 808s, snares, and hi-hats.","https://blackoctopus-sound.com/",4.6,345),

    # ─── ADDITIONAL MIDI TOOLS ────────────────────────────────────────────────
    _p("Scaler EQ","scaler-eq","Plugin Boutique","midi","$49","paid","Adaptive EQ that learns from Scaler 2 to EQ based on scale and key.","https://www.pluginboutique.com/products/6756",4.6,312),
    _p("HY-MPS2","hy-mps2","HY-Plugins","midi","$49","paid","MIDI pattern sequencer with step sequencer and random variation options.","https://www.hy-plugins.com/",4.5,267),
    _p("Mozaic Beats Xequence 2","mozaic-xequence-2","Mozaic Beats","midi","$19","paid","Full-featured MIDI sequencer app for iPad with clips and timeline editing.","https://apps.apple.com/us/app/xequence-2/",4.7,312),
    _p("Streambyter","streambyter","AudioCentralMagazine","midi","$12","paid","MIDI transformation tool for complex routing and processing rules.","https://audiocentral.com/",4.4,189),
    _p("ChordPotion","chordpotion","Prometheansound","midi","$49","paid","Harmonic chord generator with smart voicing and progression tools.","https://prometheansound.com/chordpotion/",4.5,267),
    _p("Chordz","chordz","Tino Leiotardi","midi","Free","free","Free chord trigger plugin that generates chords from single MIDI notes.","https://www.vstplanet.com/News/2012/12/chordz-free-midi-chord-plugin",4.4,534),
    _p("Helio Workstation","helio-workstation","Peter Rudenko","daw","Free","free","Free open-source MIDI sequencer and composition tool with linear layout.","https://helio.fm/",4.4,345),

    # ─── SOUND DESIGN / FX LIBRARIES ─────────────────────────────────────────
    _p("Boom Library Cinematic Bundle","boom-library-cinematic","Boom Library","sampler","$399","paid","Professional cinematic SFX library with designed and pure sounds for film.","https://www.boomlibrary.com/collections/cinematic-bundle",4.8,312),
    _p("Soundsnap Pro","soundsnap-pro","Soundsnap","sampler","Subscription","subscription","Subscription sound effects library with 300,000+ royalty-free SFX.","https://www.soundsnap.com/",4.6,234),
    _p("Zapsplat","zapsplat","ZapSplat","sampler","Free","free","Free sound effects library with 100,000+ royalty-free sounds for media.","https://www.zapsplat.com/",4.5,489),
    _p("Freesound","freesound","Freesound Project","sampler","Free","free","Community-based repository of Creative Commons licensed sound recordings.","https://freesound.org/",4.5,1234),

    # ─── POST-PRODUCTION / BROADCAST ─────────────────────────────────────────
    _p("Nugen Loudness Toolkit 2","nugen-loudness-toolkit-2","Nugen Audio","mastering","$499","paid","Professional loudness metering and management suite for broadcast delivery.","https://nugenaudio.com/loudness-toolkit/",4.8,345),
    _p("Nugen MasterCheck Pro","nugen-mastercheck-pro","Nugen Audio","mastering","$99","paid","Streaming loudness and codec simulation tool for modern masters.","https://nugenaudio.com/mastercheck/",4.7,489),
    _p("Nugen VisLM 2","nugen-vislm-2","Nugen Audio","utility","$199","paid","Comprehensive loudness and True Peak metering with timeline view.","https://nugenaudio.com/vislm/",4.7,345),
    _p("Nugen Stereoizer Evolution","nugen-stereoizer","Nugen Audio","effects","$149","paid","Stereo field processor for mono-to-stereo conversion with artifact-free widening.","https://nugenaudio.com/stereoizer/",4.6,267),
    _p("Orban Loudness Meter","orban-loudness-meter","Orban","utility","Free","free","Free professional loudness metering plugin following BS.1770 standards.","https://www.orban.com/meter/",4.6,456),
    _p("Dolby Atmos Production Suite","dolby-atmos-production","Dolby","utility","Subscription","subscription","Professional immersive audio authoring tools for Dolby Atmos mixing.","https://professional.dolby.com/content-creation/dolby-atmos-production-suite/",4.8,345),
    _p("Blackmagic DaVinci Resolve","davinci-resolve","Blackmagic Design","daw","Free","free","Professional video editing and color grading software with Fairlight audio.","https://www.blackmagicdesign.com/products/davinciresolve",4.7,1567),
    _p("Pro Tools First","pro-tools-first","Avid","daw","Free","free","Free entry-level version of Pro Tools with 16 tracks and basic editing.","https://www.avid.com/resource-center/pro-tools-first",4.3,712),

    # ─── MIDI CONTROLLERS SOFTWARE ────────────────────────────────────────────
    _p("Native Instruments Maschine 2","ni-maschine-2","Native Instruments","drums","$199","paid","Beat production studio with hardware-style workflow and extensive drum kits.","https://www.native-instruments.com/en/products/maschine/production-systems/maschine/",4.8,1234),
    _p("Native Instruments Maschine Plus","ni-maschine-plus","Native Instruments","drums","$1299","paid","Standalone Maschine with built-in Komplete content and WiFi streaming.","https://www.native-instruments.com/en/products/maschine/production-systems/maschine-plus/",4.8,712),
    _p("iZotope Trash","izotope-trash","iZotope","effects","$49","paid","Reimagined distortion plugin with flexible signal chain and multiband drive.","https://www.izotope.com/en/products/trash.html",4.6,423),
    _p("Soundtheory Gullfoss Live","soundtheory-gullfoss-live","Soundtheory","effects","$99","paid","Real-time intelligent EQ for live performance and broadcast applications.","https://www.soundtheory.com/",4.6,289),
    _p("Sonible frei:raum","sonible-freiraum","Sonible","effects","$149","paid","Spatial audio mastering equalizer with Proximity EQ and stereo enhancement.","https://www.sonible.com/freiraum/",4.6,312),
    _p("Sonnox Oxford DeBuzzer","sonnox-oxford-debuzzer","Sonnox","utility","$149","paid","Targeted noise removal plugin for buzz, hum, and continuous tonal interference.","https://www.sonnox.com/plugin/oxford-debuzzer",4.6,234),
    _p("Sonnox Oxford DeClipper","sonnox-oxford-declipper","Sonnox","utility","$149","paid","Intelligent clip restoration plugin for recovering overloaded audio recordings.","https://www.sonnox.com/plugin/oxford-declipper",4.6,267),
    _p("Sonnox Oxford DeNoise","sonnox-oxford-denoise","Sonnox","utility","$149","paid","Adaptive noise reduction plugin for continuous broadband noise reduction.","https://www.sonnox.com/plugin/oxford-denoise",4.6,289),
    _p("Sonnox Oxford Claro","sonnox-oxford-claro","Sonnox","mastering","$249","paid","Mastering equalizer based on perceptual hearing models for natural balance.","https://www.sonnox.com/plugin/oxford-claro",4.7,312),
    _p("Eiosis AirEQ Premium","eiosis-aireq-premium","Eiosis","effects","$299","paid","Air EQ with a unique 10-band equalizer for adding air without harshness.","https://eiosis.com/aireq.htm",4.7,423),
    _p("Eiosis e2deesser","eiosis-e2deesser","Eiosis","effects","$149","paid","De-esser with high-resolution spectral analysis and transparent processing.","https://eiosis.com/e2deesser.htm",4.7,356),
    _p("Leapwing Audio StageOne","leapwing-stageone","Leapwing Audio","effects","$99","paid","Spatial enhancement plugin for natural stereo widening and depth.","https://www.leapwingaudio.com/stageone/",4.6,289),
    _p("Leapwing Audio RootOne","leapwing-rootone","Leapwing Audio","effects","$99","paid","Sub-bass enhancement plugin for adding weight and presence to low end.","https://www.leapwingaudio.com/rootone/",4.6,267),
    _p("Leapwing Audio CenterOne","leapwing-centerone","Leapwing Audio","effects","$99","paid","Intelligent center channel extraction and manipulation plugin.","https://www.leapwingaudio.com/centerone/",4.6,234),
    _p("Leapwing Audio Al Schmitt","leapwing-al-schmitt","Leapwing Audio","effects","$149","paid","Vintage high-end console character plugin designed with legendary engineer Al Schmitt.","https://www.leapwingaudio.com/alschmitt/",4.7,312),

    # ─── NICHE / SPECIALTY ────────────────────────────────────────────────────
    _p("Audioease Altiverb 8 XL","audioease-altiverb-8-xl","Audio Ease","effects","$695","paid","Industry-standard convolution reverb with 4K impulse responses from famous venues.","https://www.audioease.com/altiverb/",4.9,823),
    _p("AudioEase 360pan Suite","audioease-360pan-suite","Audio Ease","utility","$495","paid","Surround and 3D audio panning plugin for immersive audio production.","https://www.audioease.com/360pan/",4.7,267),
    _p("Audio Ease Speakerphone 3","audioease-speakerphone-3","Audio Ease","effects","$395","paid","Speaker emulation plugin covering telephones, radios, and vintage speakers.","https://www.audioease.com/speakerphone/",4.7,345),
    _p("Focusrite Red 2 EQ","focusrite-red-2-eq","Focusrite","effects","$99","paid","Emulation of the Focusrite Red 2 equalizer with transformer-balanced circuits.","https://focusritepro.com/",4.6,312),
    _p("Focusrite Red 3 Compressor","focusrite-red-3-compressor","Focusrite","effects","$99","paid","Emulation of the Focusrite Red 3 dual-section compressor/limiter.","https://focusritepro.com/",4.6,289),
    _p("Empirical Labs Arousor","empirical-labs-arousor","Empirical Labs","effects","$199","paid","Official software version of the legendary Distressor compressor.","https://www.empiricallabs.com/arousor/",4.8,534),
    _p("Lindell Audio PEX-500","lindell-pex-500","Lindell Audio","effects","$99","paid","Passive pultec-style equalizer emulation for smooth frequency shaping.","https://www.lindelludio.com/",4.6,289),
    _p("Kush Audio UBK-1","kush-audio-ubk-1","Kush Audio","effects","$149","paid","Compressor with three saturation modes and smooth optical-style detection.","https://www.kush.audio/products/ubk-1",4.7,345),
    _p("Kush Audio Omega Series","kush-audio-omega-series","Kush Audio","effects","$149","paid","Class A transformer saturation plugin for adding analog color and warmth.","https://www.kush.audio/",4.7,312),
    _p("Infected Mushroom Manipulator","infected-mushroom-manipulator","Waves","effects","$99","paid","Real-time pitch and vocal effect manipulator from Infected Mushroom and Waves.","https://www.waves.com/plugins/infected-mushroom-manipulator",4.6,423),
    _p("Sinevibes Droplet","sinevibes-droplet","Sinevibes","effects","$29","paid","Granular delay plugin with scatter, size, and position controls.","https://www.sinevibes.com/droplet/",4.5,234),
    _p("Sinevibes Grid","sinevibes-grid","Sinevibes","effects","$29","paid","Step-filtered gate effect with 16-step pattern and tempo synchronization.","https://www.sinevibes.com/grid/",4.5,212),
    _p("Sinevibes Turbine","sinevibes-turbine","Sinevibes","effects","$29","paid","Rotary speaker simulator inspired by Leslie cabinet with spring reverb.","https://www.sinevibes.com/turbine/",4.5,245),
]
