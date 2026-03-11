"""
generate_catalog.py - Generate a comprehensive music tech product catalog
from curated real-world knowledge of the plugin ecosystem.

Produces data/products.json with 2500+ real products.
Usage: python scripts/generate_catalog.py
"""

import json, os, re, unicodedata

OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'products.json')

def slug(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii','ignore').decode()
    t = t.lower().strip()
    t = re.sub(r'[^\w\s-]','',t)
    t = re.sub(r'[\s_]+','-',t)
    t = re.sub(r'-+','-',t)
    return t.strip('-')

# ─── Catalog Definition ──────────────────────────────────────────────────────
# Each entry: (name, developer, category, price, priceType, url, description, tags)
# priceType: free | freemium | one-time | subscription

CATALOG = []

def add(name, dev, cat, price, pt, url, desc='', tags=None):
    CATALOG.append((name, dev, cat, price, pt, url, desc, tags or [cat]))

# ═══════════════════════════════════════════════════════════════════════════════
# DAWs
# ═══════════════════════════════════════════════════════════════════════════════
daws = [
    ("Ableton Live 12 Intro","Ableton",99,"one-time","https://www.ableton.com","Entry-level Live edition with 16 tracks and 5GB of sounds."),
    ("Ableton Live 12 Standard","Ableton",449,"one-time","https://www.ableton.com","Mid-tier Live with 32-track recording and full instrument suite."),
    ("Ableton Live 12 Suite","Ableton",749,"one-time","https://www.ableton.com","Complete Live with all instruments, Max for Live, and 70+ GB library."),
    ("FL Studio Fruity","Image-Line",99,"one-time","https://www.image-line.com","Pattern-based DAW entry edition with step sequencer."),
    ("FL Studio Producer","Image-Line",199,"one-time","https://www.image-line.com","Full DAW with audio recording and playlist."),
    ("FL Studio Signature","Image-Line",299,"one-time","https://www.image-line.com","FL Studio with additional synth plugins including Harmor."),
    ("FL Studio All Plugins","Image-Line",499,"one-time","https://www.image-line.com","Complete FL Studio with every first-party plugin."),
    ("Logic Pro","Apple",199.99,"one-time","https://www.apple.com/logic-pro","Apple's professional DAW with 6000+ loops and AI Session Players."),
    ("GarageBand","Apple",0,"free","https://www.apple.com/mac/garageband","Free DAW for Mac and iOS with pro-quality instruments."),
    ("Pro Tools","Avid",699,"one-time","https://www.avid.com/pro-tools","Industry-standard DAW for film, TV, and studio recording."),
    ("Pro Tools Artist","Avid",9.99,"subscription","https://www.avid.com/pro-tools","Subscription Pro Tools for musicians and home studios."),
    ("Pro Tools Studio","Avid",29.99,"subscription","https://www.avid.com/pro-tools","Pro Tools for professional producers and mix engineers."),
    ("Cubase Pro 13","Steinberg",579,"one-time","https://www.steinberg.net/cubase","Professional DAW with advanced chord tools and VariAudio."),
    ("Cubase Artist 13","Steinberg",329,"one-time","https://www.steinberg.net/cubase","Mid-tier Cubase with unlimited audio/MIDI tracks."),
    ("Cubase Elements 13","Steinberg",99,"one-time","https://www.steinberg.net/cubase","Entry-level Cubase with 48 audio tracks."),
    ("Nuendo 13","Steinberg",1699,"one-time","https://www.steinberg.net/nuendo","Post-production DAW with ADR, Atmos, and game audio tools."),
    ("Studio One 6 Professional","PreSonus",399,"one-time","https://www.presonus.com","All-in-one DAW with integrated mastering and Stem Splitter."),
    ("Studio One 6 Artist","PreSonus",99,"one-time","https://www.presonus.com","Studio One for producers with 3rd party plugin support."),
    ("Studio One 6 Prime","PreSonus",0,"free","https://www.presonus.com","Free DAW with unlimited tracks and PreSonus instruments."),
    ("REAPER","Cockos",60,"one-time","https://www.reaper.fm","Ultra-customizable, lightweight professional DAW."),
    ("Bitwig Studio 5","Bitwig",399,"one-time","https://www.bitwig.com","Modern DAW with modular Grid and native CLAP support."),
    ("Bitwig Studio 16-Track","Bitwig",99,"one-time","https://www.bitwig.com","Entry-level Bitwig with 16 tracks and all instruments."),
    ("Reason 12","Reason Studios",499,"one-time","https://www.reasonstudios.com","DAW with virtual rack interface and 3500+ sounds."),
    ("Reason+","Reason Studios",19.99,"subscription","https://www.reasonstudios.com","Reason subscription with access to full plugin library."),
    ("Cakewalk by BandLab","BandLab",0,"free","https://www.bandlab.com/products/cakewalk","Full-featured free DAW for Windows."),
    ("Waveform Pro 12","Tracktion",119,"one-time","https://www.tracktion.com","Modern DAW with loopback recording and unique editing."),
    ("Waveform Free","Tracktion",0,"free","https://www.tracktion.com","Free DAW with core production features."),
    ("Digital Performer 11","MOTU",499,"one-time","https://www.motu.com","Professional DAW for notation, scoring, and studio work."),
    ("Harrison Mixbus 32C","Harrison",279,"one-time","https://harrisonconsoles.com","DAW modelled on the Harrison 32C analog console."),
    ("Ardour","Ardour",0,"freemium","https://ardour.org","Open-source DAW for Linux, Mac, and Windows."),
    ("LMMS","LMMS",0,"free","https://lmms.io","Free open-source DAW inspired by FL Studio."),
    ("Audacity","Audacity",0,"free","https://www.audacityteam.org","Free multitrack audio editor and recorder."),
    ("Mixcraft 10 Pro Studio","Acoustica",149,"one-time","https://acoustica.com","Windows-only DAW with loop library and notation."),
    ("ACID Pro 11","Magix",149,"one-time","https://www.magix.com","Loop-based DAW with MIDI and audio recording."),
    ("Samplitude Pro X8","Magix",399,"one-time","https://www.magix.com","Professional DAW with analog-modelled mixing."),
    ("Sequoia 16","Magix",2799,"one-time","https://www.magix.com","Broadcast and mastering DAW used by major radio stations."),
    ("Vegas Pro 21","Magix",599,"one-time","https://www.vegascreativesoftware.com","Audio/video production suite for Windows."),
    ("Podium","Zynewave",0,"free","https://zynewave.com","Hierarchical project-based DAW for Windows."),
    ("Zrythm","Zrythm Dev",0,"free","https://www.zrythm.org","Open-source DAW with automation curves and chord assistance."),
]
for n,d,p,pt,u,desc in daws:
    add(n,d,'daw',p,pt,u,desc)

# ═══════════════════════════════════════════════════════════════════════════════
# SYNTHESIZERS
# ═══════════════════════════════════════════════════════════════════════════════

# Xfer Records
for n,p,desc in [
    ("Serum",9.99,"Wavetable synthesizer and industry standard for electronic music."),
    ("Serum FX",5.99,"Multi-effects plugin using Serum's filter and modulation engine."),
]:
    add(n,"Xfer Records",'synth',p,'subscription','https://xferrecords.com',desc,['synth','wavetable'])

# u-he
uhe_synths = [
    ("Diva",179,"Analog-modelled synthesizer with ultra-realistic oscillators."),
    ("Zebra 2",199,"Modular wavetable synthesizer for complex patches."),
    ("Hive 2",149,"Dual-layer wavetable synthesizer with fast preset design."),
    ("Repro-1",149,"Emulation of the Roland Pro-One monosynth."),
    ("Repro-5",149,"Emulation of the Sequential Prophet-5 polyphonic synthesizer."),
    ("ACE",99,"Any Cable Everywhere — modular patchable synthesizer."),
    ("Bazille",99,"Digital modular synthesizer with FM and fractal modulation."),
    ("Satin",99,"Tape machine emulation plugin with high-quality saturation."),
    ("Presswerk",99,"Compressor plugin with vintage analogue character."),
    ("Colour Copy",99,"Analog-modelled chorus/delay effect plugin."),
    ("Uhbik-A",99,"Allpass-based early reflections and reverb effect."),
    ("Uhbik-F",99,"Flanger effect modelled on classic bucket-brigade hardware."),
    ("Uhbik-G",99,"Granular pitch-shifter effect for creative transformations."),
    ("Uhbik-P",99,"Phaser effect with vintage modulation character."),
    ("Uhbik-Q",99,"Equalizer with warm analog character."),
    ("Uhbik-S",99,"Tremolo/autopan effect with multiple waveform shapes."),
    ("Uhbik-T",99,"Trancegate effect for rhythmic gating patterns."),
    ("TyrellN6",0,"Free virtual analog synthesizer inspired by the Roland Juno."),
    ("Zebralette",0,"Free two-oscillator wavetable synthesizer."),
    ("Triple Cheese",0,"Free synthesizer using three comb filters as oscillators."),
    ("Podolski",0,"Free simple virtual analog synthesizer."),
    ("Beatzille",0,"Free mini Bazille — portable modular synthesizer."),
    ("MFM2.5",0,"Free formant-filter modulation effect."),
]
for n,p,desc in uhe_synths:
    pt = 'free' if p==0 else 'one-time'
    add(n,"u-he",'synth',None if p==0 else p,pt,'https://u-he.com',desc)

# Arturia V Collection
arturia_v = [
    "Mini V","Jup-8 V","CS-80 V","Moog Modular V","DX7 V","Prophet-5 V",
    "Matrix-12 V","SEM V","OB-Xa V","Buchla Easel V","CMI V","Synclavier V",
    "CZ V","Synthi V","Mellotron V","B-3 V","Vox Continental V","Farfisa V",
    "Stage-73 V","Wurli V","Piano V","CP-70 V","Clavinet V","Solina V",
    "Arp 2600 V","Arp 2600 V3","Korg MS-20 V","Roland SH-V","ARP Odyssey V",
    "Emulator II V","Jup-X V","Analog Lab V",
]
for n in arturia_v:
    add(n,"Arturia",'synth',199,'one-time','https://www.arturia.com',
        f"Arturia's emulation of {n.replace(' V','').replace(' V3','')}.",['synth','arturia','analog'])

# Arturia other synths
arturia_other = [
    ("Pigments 5",199,"Polychrome software synthesizer with wavetable, virtual analog, sample, and granular engines."),
    ("V Collection 10",599,"Bundle of 35+ classic synthesizer emulations."),
    ("Augmented Strings",199,"Hybrid synthesizer combining physical modelling and sampling."),
    ("Augmented Voices",199,"Hybrid synthesizer for vocal textures and soundscapes."),
    ("Augmented Grand Piano",199,"Hybrid grand piano with synthesis capabilities."),
    ("Augmented Brass",199,"Hybrid brass instrument with synthesis modulation."),
    ("Augmented Woodwinds",199,"Hybrid woodwind instrument synthesizer."),
    ("Analog Lab V Pro",99,"Performance synthesizer with 11,000+ presets from V Collection."),
]
for n,p,desc in arturia_other:
    add(n,"Arturia",'synth',p,'one-time','https://www.arturia.com',desc)

# Native Instruments synths
ni_synths = [
    ("Massive X",149,"Advanced wavetable synthesizer successor to the legendary Massive."),
    ("Massive",0,"Classic wavetable synthesizer included in Komplete Start."),
    ("FM8",149,"FM synthesizer with six operators and advanced envelope control."),
    ("Absynth 5",149,"Semi-modular synthesizer with granular and spectral engines."),
    ("Razor",149,"Additive synthesizer built in Reaktor with spectral processing."),
    ("Monark",149,"Analog monosynth modelled on the Minimoog Model D."),
    ("Prism",149,"Percussion and texture synthesizer with three synthesis modes."),
    ("Rounds",149,"Dual-layer digital synthesizer with sequenced layering."),
    ("Skanner XT",149,"Wavetable synthesizer with unique scanning modulation."),
    ("Polyplex",149,"8-channel drum synthesizer with per-channel randomization."),
    ("Reaktor 6",199,"Modular synthesis and effects platform with component library."),
    ("Reaktor Prism",49,"Modal synthesizer instrument for Reaktor."),
    ("Form",149,"Sample-based synthesizer using audio as wavetables."),
    ("Blocks Prism",99,"Reaktor Blocks modular synthesizer environment."),
    ("Retro Machines MK2",0,"Free collection of vintage synthesizer samples."),
    ("Playbox",0,"Chord and arp tool included in Komplete Start."),
    ("Komplete Start",0,"Free bundle of 2000+ sounds and 6 instruments."),
]
for n,p,desc in ni_synths:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Native Instruments",'synth',None if p==0 else p,pt,'https://www.native-instruments.com',desc)

# Spectrasonics
spec = [
    ("Omnisphere 2",499,"Power synth with 14,000+ sounds and hardware control."),
    ("Keyscape",399,"Keyboard instrument library with 500+ hand-crafted sounds."),
    ("Trilian",299,"Bass instrument with acoustic, electric, and synth bass."),
    ("Stylus RMX",249,"Groove production instrument with 10,000+ grooves."),
]
for n,p,desc in spec:
    add(n,"Spectrasonics",'synth',p,'one-time','https://www.spectrasonics.net',desc)

# LennarDigital
add("Sylenth1","LennarDigital",'synth',189,'one-time','https://www.lennardigital.com',
    "Legendary virtual analog synthesizer with warm, fat sound.")

# Kilohearts
khs_synths = [
    ("Phase Plant",199,"Modular software synthesizer for sound design."),
    ("Snap Heap",99,"Multi-effects rack with modular routing."),
    ("Multipass",99,"Multi-band parallel processing rack."),
]
for n,p,desc in khs_synths:
    add(n,"Kilohearts",'synth',p,'one-time','https://kilohearts.com',desc)

# Kilohearts Snapins
snapins = [
    "Chorus","Compressor","Delay","Distortion","Ensemble","Equalizer",
    "Filter","Flanger","Formant Filter","Frequency Shifter","Gain","Gate",
    "Haas","Ladder Filter","Limiter","Phaser","Pitch Shifter","Resonator",
    "Reverb","Ring Modulator","Stereo","Tape Stop","Trance Gate","Transient Shaper",
    "Bitcrush","Wavefolder","Comb Filter","Dynamics","Saturator","Triple EQ",
]
for n in snapins:
    add(f"kHs {n}","Kilohearts",'effects',0,'free','https://kilohearts.com',
        f"Kilohearts {n} snapin — modular effect for Phase Plant and Snap Heap.",['effects','kilohearts','snapin','free'])

# Reveal Sound
add("Spire","Reveal Sound",'synth',189,'one-time','https://www.reveal-sound.com',
    "Polyphonic wavetable synthesizer with complex modulation.")

# Tone2
tone2 = [
    ("Electra 3",249,"Multi-engine synthesizer with 6 oscillator types."),
    ("Nemesis",149,"Wavetable synthesizer with revolutionary warp modes."),
    ("RayBlaster",99,"Impulse-modelling synthesis synthesizer."),
    ("Icarus 2",199,"Wavetable synthesizer with spectral warping."),
    ("Warmverb",49,"Algorithmic reverb with warm character."),
    ("BiFilter 2",39,"Multi-mode filter bank with 35 filter types."),
    ("Ultraspace",49,"Spacious reverb with granular processing."),
    ("Whispair",49,"Stereo enhancer and exciter."),
]
for n,p,desc in tone2:
    add(n,"Tone2",'synth',p,'one-time','https://www.tone2.com',desc)

# D16 Group synths
d16_synths = [
    ("Lush-101",89,"Polyphonic analog-modelled Roland Juno-106 emulation."),
    ("Phoscyon 2",99,"TB-303 Bass Line emulation with modern features."),
    ("Repeater",89,"Delay plugin with four independent delay lines."),
    ("LuSH-101",89,"8-layer Roland Juno-101 emulation with massive unison."),
]
for n,p,desc in d16_synths:
    add(n,"D16 Group",'synth',p,'one-time','https://d16.com',desc)

# Cherry Audio
cherry = [
    ("Voltage Modular",99,"Modular synthesis environment with 200+ modules."),
    ("Dreamsynth",49,"Multi-engine hybrid synthesizer."),
    ("Polymode",49,"Polymoog emulation."),
    ("Memorymode",49,"Memory Moog emulation."),
    ("Eight Voice",49,"Oberheim Eight Voice emulation."),
    ("DCO-106",49,"Roland Juno-106 emulation."),
    ("GX-80",49,"Yamaha GX1 emulation."),
    ("Surfer EQ",39,"Frequency-tracking EQ that follows your bass."),
    ("Mercury-6",49,"Roland Jupiter-6 emulation."),
    ("PS-20",49,"Korg PS-3200 emulation."),
    ("Model D",49,"Minimoog Model D emulation."),
    ("Elka-X",49,"Elka Synthex emulation."),
    ("Sines",49,"Additive synthesizer."),
    ("Quadra",49,"ARP Quadra emulation."),
    ("Stardust 201",49,"Roland RE-201 Space Echo emulation."),
    ("Hollow Sun Modern Vintage Bundle",79,"Collection of vintage keyboard emulations."),
]
for n,p,desc in cherry:
    add(n,"Cherry Audio",'synth',p,'one-time','https://cherryaudio.com',desc)

# TAL Software synths
tal_synths = [
    ("TAL-U-NO-LX",60,"Roland Juno-60 emulation with self-oscillating filter."),
    ("TAL-Bassline-101",60,"Roland SH-101 emulation for acid basslines."),
    ("TAL-Pha",60,"Roland Alpha Juno emulation."),
    ("TAL-Sampler",60,"Emulation of classic hardware sampler sound with filters."),
    ("TAL-MOD",60,"Semi-modular synthesizer modelled on a vintage instrument."),
    ("TAL-Vocoder",60,"Vintage vocoder modelled on classic hardware vocoders."),
    ("TAL-NoiseMaker",0,"Free virtual analog synthesizer."),
    ("TAL-Elek7ro",0,"Free virtual analog synthesizer."),
    ("TAL-Elek7ro II",0,"Free virtual analog synthesizer, improved version."),
]
for n,p,desc in tal_synths:
    pt = 'free' if p==0 else 'one-time'
    add(n,"TAL Software",'synth',None if p==0 else p,pt,'https://tal-software.com',desc)

# Free/open-source synths
free_synths = [
    ("Vital","Matt Tytel",0,"https://vital.audio","Spectral warping wavetable synthesizer."),
    ("Surge XT","Surge Synth Team",0,"https://surge-synthesizer.github.io","Open-source hybrid synthesizer."),
    ("Dexed","Digital Suburban",0,"https://asb2m10.github.io/dexed","FM synthesizer compatible with Yamaha DX7 patches."),
    ("OB-Xd","discoDSP",0,"https://www.discodsp.com/obxd","Emulation of Oberheim OB-X synthesizer."),
    ("Helm","Matt Tytel",0,"https://tytel.org/helm","Polyphonic synthesizer with a visual modulation matrix."),
    ("ZynAddSubFX","Paul Nasca",0,"https://zynaddsubfx.sourceforge.io","Realtime soft synthesizer with three synthesis engines."),
    ("Yoshimi","Andrew Deryabin",0,"https://yoshimi.sourceforge.io","ZynAddSubFX-derived synthesizer."),
    ("Odin 2","TheWaveWarden",0,"https://thewavewarden.com/odin2","Semi-modular synthesizer with 26 oscillator types."),
    ("ZeBeQ","discoDSP",0,"https://www.discodsp.com/zebeq","Retro FM synth with DX7/DX7II compatibility."),
    ("Tyrell N6","u-he",0,"https://u-he.com/products/tyrelln6","Virtual analog synthesizer."),
    ("Noize Mak3r","Nusofting",0,"https://nusofting.liqihsynth.com","Classic virtual analog synth."),
    ("VK-1 Viking Synthesizer","Blamsoft",0,"https://blamsoft.com","Minimoog-inspired monosynth."),
    ("Synth1","Ichiro Toda",0,"https://daichilab.sakura.ne.jp/softsynth","Popular freeware analog-modelled synthesizer."),
    ("Crystal","Green Oak Software",0,"https://www.greenoak.com/crystal","Semi-modular synthesizer with granular and spectral."),
    ("Charlatan","Blaukraut Engineering",0,"https://www.blaukraut.info","Virtual analog synthesizer."),
    ("Wavetable","Ableton",0,"https://www.ableton.com","Included wavetable synth in Ableton Live."),
    ("Analog","Ableton",0,"https://www.ableton.com","Analog synthesizer included in Ableton Live Suite."),
]
for n,dev,p,u,desc in free_synths:
    add(n,dev,'synth',None,'free',u,desc,['synth','free'])

# KV331 Audio
add("SynthMaster 2","KV331 Audio",'synth',99,'one-time','https://www.kv331audio.com',
    "Semi-modular synthesizer with wavetable, VA, and FM engines.")
add("SynthMaster One","KV331 Audio",'synth',49,'one-time','https://www.kv331audio.com',
    "Streamlined wavetable synthesizer for performance.")
add("SynthMaster Player","KV331 Audio",'synth',29,'one-time','https://www.kv331audio.com',
    "Preset player for SynthMaster library.")

# UVI
uvi_synths = [
    ("Falcon 2",349,"Multi-synthesis platform with scripting and modular design."),
    ("Synth Anthology 3",149,"600+ classic hardware synthesizer emulations."),
    ("Ircam Organic Pads",149,"High-quality organic sound textures."),
    ("Key Suite Acoustic",99,"Grand piano collection with detailed sampling."),
    ("BeatBox Anthology 2",99,"Vintage drum machine collection."),
    ("World Suite 2",199,"World instruments sampler library."),
    ("Darklight IIx",149,"Emulation of the legendary Fairlight CMI."),
    ("Meteor",149,"Granular and spectral synthesizer instrument."),
]
for n,p,desc in uvi_synths:
    add(n,"UVI",'synth',p,'one-time','https://www.uvi.net',desc)

# Madrona Labs
madrona = [
    ("Aalto",99,"Modular synthesizer with physical modelling."),
    ("Kaivo",99,"Physical modelling granular synthesizer."),
    ("Virta",99,"Audio-rate modulated effects processor."),
    ("Sumu",99,"Spectral additive synthesizer."),
]
for n,p,desc in madrona:
    add(n,"Madrona Labs",'synth',p,'one-time','https://madronalabs.com',desc)

# Sonic Academy
sa_synths = [
    ("ANA 2",79,"Feature-rich wavetable synthesizer for producers."),
    ("Kick 2",45,"Kick drum synthesizer with detailed waveform display."),
    ("NOIS3",45,"Noise gate with side-chain and multi-band options."),
    ("PLUGIN BOUTIQUE Carbon Electra",49,"Virtual analog synth with four oscillators."),
]
for n,p,desc in sa_synths:
    add(n,"Sonic Academy",'synth' if 'ANA' in n or 'Carbon' in n else 'drums',p,'one-time','https://www.sonicacademy.com',desc)

# Cableguys
cableguys = [
    ("VolumeShaper 6",49,"LFO-based volume, panning, and filter shaper."),
    ("FilterShaper Core",49,"Filter and modulation shaper."),
    ("PanShaper 3",39,"Stereo panning LFO tool."),
    ("TimeShaper 3",49,"Rhythmic time-stretching and pitch effect."),
    ("CurveShaper",49,"Flexible multi-modulator for creative shaping."),
    ("ShaperBox 3",99,"Complete suite of all Cableguys shaper tools."),
    ("HalfTime",0,"Half-speed effect for lo-fi and slowed production."),
    ("Pancake 2",0,"Free auto-panning tool."),
    ("MidiShaper",29,"MIDI-to-modulator for external control of shapers."),
]
for n,p,desc in cableguys:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Cableguys",'effects',None if p==0 else p,pt,'https://www.cableguys.com',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# EFFECTS PLUGINS
# ═══════════════════════════════════════════════════════════════════════════════

# FabFilter
fabfilter = [
    ("Pro-Q 3",179,"Industry-standard EQ with dynamic EQ and up to 24 bands."),
    ("Pro-C 2",99,"Professional compressor with 8 compression styles."),
    ("Pro-L 2",179,"True peak brickwall limiter used in mastering."),
    ("Pro-R 2",199,"Natural reverb with decay rate per frequency."),
    ("Pro-DS",149,"De-esser with natural sounding high-frequency reduction."),
    ("Pro-MB",199,"Multiband dynamics processor with dry/wet control per band."),
    ("Saturn 2",149,"Multiband distortion and saturation processor."),
    ("Timeless 3",99,"Stereo tape delay with vintage and modern modes."),
    ("Volcano 3",99,"Multiband filter with heavy modulation options."),
    ("Twin 3",149,"Twin filter synthesizer with dual filter sections."),
    ("One",0,"Free introductory synthesizer by FabFilter."),
    ("Total Bundle",999,"Complete collection of all FabFilter plugins."),
]
for n,p,desc in fabfilter:
    pt = 'free' if p==0 else 'one-time'
    add(n,"FabFilter",'effects',None if p==0 else p,pt,'https://www.fabfilter.com',desc,['effects','fabfilter'])

# Soundtoys
soundtoys = [
    ("EchoBoy",149,"Comprehensive echo and delay processor."),
    ("EchoBoy Jr.",49,"Mono delay based on EchoBoy's Ping Pong mode."),
    ("Decapitator",149,"Analog saturation modeller with five amp styles."),
    ("Radiator",149,"Tube saturation modelled on the Altec 1567A mixer."),
    ("Little AlterBoy",149,"Voice transformation with pitch shift and formant control."),
    ("PrimalTap",99,"Vintage digital delay modelled on Prime Time delay."),
    ("Crystallizer",149,"Granular echo synthesizer with reverse and pitch effects."),
    ("FilterFreak 1",99,"Analog filter modelled on a classic four-pole ladder filter."),
    ("FilterFreak 2",99,"Stereo multi-mode filter with complex modulation."),
    ("PhaseMistress",99,"Phase shifter modelled on classic hardware phasers."),
    ("PanMan",99,"Stereo panning effect with rhythmic LFO modulation."),
    ("Tremolator",99,"Tremolo and auto-gate with tempo sync."),
    ("Sie-Q",99,"Sievert passive equalizer emulation."),
    ("MicroShift",99,"Stereo widener using pitch shift and timing offsets."),
    ("Devil-Loc",99,"Classic drum room compressor."),
    ("Devil-Loc Deluxe",149,"Extended Devil-Loc with more control and saturation."),
    ("Speed",99,"Tape speed effect for varispeed and pitch modulation."),
    ("Effectrix",199,"Multi-effect sequencer with 14 effects and pattern sequencer."),
    ("Soundtoys 5",499,"Complete bundle of all 21 Soundtoys plugins."),
    ("Effect Rack",149,"Flexible effect chain host for Soundtoys plugins."),
]
for n,p,desc in soundtoys:
    add(n,"Soundtoys",'effects',p,'one-time','https://www.soundtoys.com',desc,['effects','soundtoys'])

# Valhalla DSP
valhalla = [
    ("VintageVerb",50,"Reverb modelled on classic digital reverb hardware of the '70s-'80s."),
    ("Room",50,"Algorithmic room reverb with adjustable room size."),
    ("Shimmer",50,"Ethereal reverb with pitch-shifted feedback loops."),
    ("Plate",50,"Vintage plate reverb emulation."),
    ("Delay",50,"Multi-mode delay with analog, tape, and digital modes."),
    ("Freq Echo",0,"Frequency-shifting echo — free Valhalla reverb."),
    ("SpaceModulator",50,"Flanger, choruser, and comb filter with 11 modes."),
    ("Ubermod",50,"Granular delay and pitch-shifting modulation effect."),
    ("Supermassive",0,"Massive reverb and delay — free Valhalla plugin."),
    ("Gems",50,"Digital reverb with sparkling metallic character."),
]
for n,p,desc in valhalla:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Valhalla DSP",'effects',None if p==0 else p,pt,'https://valhalladsp.com',desc,['effects','reverb'])

# iZotope effects
izotope_fx = [
    ("RX 11 Advanced",1199,"Professional audio repair suite with AI-powered tools."),
    ("RX 11 Standard",399,"Audio repair tools for noise, clicks, and hum removal."),
    ("RX 11 Elements",99,"Entry-level audio repair with core de-noise tools."),
    ("Neutron 4",249,"AI-powered mixing plugin with intelligent track assistant."),
    ("Nectar 4",249,"Vocal processing suite with AI pitch correction and harmony."),
    ("Insight 2",299,"Advanced audio metering with loudness and spatial analysis."),
    ("Ozone 11 Advanced",499,"Complete AI mastering suite with stem splitting."),
    ("Ozone 11 Standard",249,"Core mastering tools with EQ, dynamics, and imaging."),
    ("Ozone 11 Elements",99,"Entry mastering with AI Master Assistant."),
    ("Iris 2",199,"Spectral synthesizer using audio as source material."),
    ("Trash 2",99,"Distortion and saturation multi-effect processor."),
    ("Stutter Edit 2",149,"Glitch and stutter effect with MIDI control."),
    ("Breeze 2",99,"Convolution and algorithmic reverb."),
    ("DDLY Dynamic Delay",49,"Dynamic delay plugin."),
    ("Vinyl",0,"Free record player emulation with noise and wobble."),
    ("Exciter",0,"Free harmonic exciter plugin."),
    ("Imager",0,"Free stereo width plugin."),
    ("Leveler",0,"Free automatic levelling tool."),
]
for n,p,desc in izotope_fx:
    pt = 'free' if p==0 else 'one-time'
    add(n,"iZotope",'effects',None if p==0 else p,pt,'https://www.izotope.com',desc)

# Waves plugins (major catalog)
waves_plugins = [
    ("SSL E-Channel",29,"Emulation of the classic SSL 4000 E Series channel strip."),
    ("SSL G-Master Buss",29,"Emulation of the SSL G-Series bus compressor."),
    ("SSL 4000 Collection",299,"Complete SSL 4000 channel and dynamics bundle."),
    ("API 550",29,"Emulation of the API 550A/550B EQ."),
    ("API 560",29,"Emulation of the API 560 graphic EQ."),
    ("API 2500",29,"Emulation of the API 2500 stereo bus compressor."),
    ("API Collection",299,"Complete API 500 series bundle."),
    ("V-EQ3",29,"Neve 1073 style three-band EQ."),
    ("V-EQ4",29,"Neve 1064 style four-band EQ."),
    ("V-Comp",29,"VCA-style compressor with vintage character."),
    ("Neve 1073",29,"Iconic Neve 1073 preamp and EQ emulation."),
    ("Neve 1084",29,"Neve 1084 console module emulation."),
    ("Neve 33609",29,"Neve bus compressor and limiter emulation."),
    ("H-EQ",49,"Hybrid equalizer with analog and digital algorithms."),
    ("H-Comp",49,"Hybrid compressor with multi-algorithm engine."),
    ("H-Delay",29,"Hybrid delay with slap, chorus, and tape modes."),
    ("H-Reverb",49,"Impulse response reverb with long-tail algorithmics."),
    ("Abbey Road Plates",29,"Emulation of the Abbey Road Studio plate reverbs."),
    ("Abbey Road Chambers",49,"Emulation of the Abbey Road echo chambers."),
    ("Abbey Road TG Mastering Chain",49,"Mastering chain modelled on Abbey Road TG equipment."),
    ("Abbey Road Vintage Drummer",29,"Vintage drum library using Abbey Road recordings."),
    ("J37 Tape",29,"Emulation of the Studer J37 tape machine."),
    ("Kramer Master Tape",29,"Tape saturation modelled on a custom Ampex 350."),
    ("KramerPIE",29,"Vintage vocal reverb effects."),
    ("CLA-2A",29,"Classic LA-2A optical compressor emulation."),
    ("CLA-3A",29,"Classic LA-3A compressor limiter emulation."),
    ("CLA-76 Blacky",29,"Classic UREI 1176 compressor blackface emulation."),
    ("CLA-76 Bluey",29,"Classic UREI 1176 compressor blustripe emulation."),
    ("CLA-Bass",29,"CLA Unplugged bass processing strip."),
    ("CLA-Drums",29,"CLA Unplugged drums processing strip."),
    ("CLA-Effects",29,"CLA reverb, chorus, and effects chain."),
    ("CLA-Guitars",29,"CLA guitar processing chain."),
    ("CLA-Vocals",29,"CLA vocal chain for polished production sound."),
    ("CLA MixHub",149,"64-channel bucket-based mixing console emulation."),
    ("PuigChild Compressor",29,"Fairchild 670 tube compressor emulation."),
    ("Puigtec EQP-1A",29,"Pultec EQP-1A passive tube equalizer emulation."),
    ("Puigtec MEQ-5",29,"Pultec MEQ-5 midrange equalizer emulation."),
    ("Scheps Omni Channel",149,"Andreas Scheps signature channel strip."),
    ("Scheps 73",29,"Neve 1073 channel strip from Andreas Scheps."),
    ("Vitamin Sonic Enhancer",29,"Multiband harmonic enhancer."),
    ("L1 Ultramaximizer",29,"Classic brickwall limiter and peak normalizer."),
    ("L2 Ultramaximizer",29,"Second-generation Waves limiter."),
    ("L3-16 Multimaximizer",49,"16-band multiband limiter and maximizer."),
    ("L3 Multimaximizer",49,"Multiband limiter with transient shaping."),
    ("TrueVerb",29,"Room simulator with distinct reflection types."),
    ("IR-1 Convolution Reverb",49,"Professional convolution reverb."),
    ("IR-L Convolution Reverb",29,"Compact convolution reverb."),
    ("SuperTap",29,"Tap delay with six taps and modulation."),
    ("MondoMod",29,"Vintage modulation with AM, FM, and rotation."),
    ("MetaFlanger",29,"Meta-parameter flanger/chorus."),
    ("Doubler",29,"Doubling effect for vocals and instruments."),
    ("S1 Stereo Imager",29,"Stereo field processor with width control."),
    ("S360 Panner",29,"Surround panner for multi-channel mixes."),
    ("PAZ Analyzer",29,"Psychoacoustic audio analyzer."),
    ("WLM Plus Loudness Meter",49,"Loudness metering per EBU R128 and ATSC A/85."),
    ("Tune LT",29,"Automatic real-time pitch correction."),
    ("Waves Tune Real-Time",49,"Low-latency real-time pitch correction."),
    ("Waves Tune",79,"Full pitch correction editor with graph mode."),
    ("Bass Rider",29,"Automatic bass level rider."),
    ("Vocal Rider",29,"Automatic vocal level rider."),
    ("F6 Floating Band Dynamic EQ",49,"Six-band dynamic EQ with floating detection."),
    ("LoAir",29,"Low-frequency extension and sub-bass tool."),
    ("MaxxBass",29,"Bass extension psychoacoustic processor."),
    ("MaxxVolume",29,"Automatic gain riding plugin."),
    ("AudioTrack",29,"Four-band EQ with compressor and gate."),
    ("C1 Compressor",29,"Stereo compressor, gate, and expander."),
    ("C4 Multiband Compressor",29,"Four-band dynamics processor."),
    ("C6 Multiband Compressor",49,"Six-band multiband dynamics."),
    ("DeBreath",29,"Breath removal tool for vocal recordings."),
    ("Sibilance",29,"Spectral de-esser with vocal clarity control."),
    ("Nx Virtual Mix Room",49,"3D headphone mixing with head tracking."),
    ("Center",29,"Center-signal focus and panning tool."),
    ("InPhase",49,"Phase alignment and correction plugin."),
    ("Manny Marroquin EQ",29,"Signature EQ from Grammy-winning mix engineer."),
    ("Manny Marroquin Distortion",29,"Signature distortion and saturation."),
    ("Tony Maserati Vocals",29,"Signature vocal chain plugin."),
    ("Tony Maserati VX1",29,"Vocal production tool from Tony Maserati."),
    ("Greg Wells ToneCentric",29,"One-knob tone shaping from Grammy engineer."),
    ("Greg Wells VoiceCentric",29,"Vocal enhancement from Grammy engineer."),
    ("Greg Wells MixCentric",29,"Mix bus processing tool."),
    ("Chris Lord-Alge Guitar",29,"Guitar processing chain plugin."),
    ("Infected Mushroom Pusher",29,"Psychedelic production tool."),
    ("OneKnob Pumper",29,"Ducking and pumping effect."),
    ("OneKnob Phatter",29,"Bass and body enhancer."),
    ("OneKnob Brighter",29,"Air band enhancer for brightness."),
    ("OneKnob Wetter",29,"Reverb with single control."),
    ("OneKnob Louder",29,"Loudness maximizer."),
    ("OneKnob Pressure",29,"Mix bus compressor."),
    ("OneKnob Series",99,"Complete OneKnob plugin bundle."),
    ("Waves Gold",299,"Essential bundle of 40 classic Waves plugins."),
    ("Waves Platinum",499,"Expanded bundle of 60+ Waves plugins."),
    ("Waves Mercury",999,"Complete Waves bundle with 180+ plugins."),
    ("Waves Horizon",399,"Production-focused bundle of 80+ plugins."),
    ("Waves Diamond",599,"Mastering-focused bundle of 60+ plugins."),
    ("Waves Transform Bundle",299,"Creative effects bundle for modern production."),
]
for n,p,desc in waves_plugins:
    add(n,"Waves",'effects',p,'one-time','https://www.waves.com',desc,['effects','waves'])

# Tokyo Dawn Records (TDR)
tdr = [
    ("TDR Nova",0,"Parallel dynamic equalizer — free."),
    ("TDR Nova GE",99,"Expanded TDR Nova with additional modes."),
    ("TDR Kotelnikov",0,"Mastering compressor — free."),
    ("TDR Kotelnikov GE",99,"Expanded mastering compressor with sidechain."),
    ("TDR VOS SlickEQ",0,"Recording/mixing EQ — free."),
    ("TDR VOS SlickEQ GE",79,"Expanded SlickEQ with additional algorithms."),
    ("TDR VOS SlickEQ M",49,"Mastering edition of SlickEQ."),
    ("SLAX",79,"Tokyo Dawn compressor plugin."),
    ("Limiter 6 GE",99,"Six-stage mastering limiter."),
    ("Feedback Compressor II",79,"Vintage-style feedback compressor."),
    ("Prism",99,"Spectral processing and correction tool."),
]
for n,p,desc in tdr:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Tokyo Dawn Records",'effects',None if p==0 else p,pt,'https://www.tokyodawn.net',desc)

# Voxengo
voxengo = [
    ("SPAN",0,"Real-time spectrum analyzer — free."),
    ("SPAN Plus",49,"Enhanced spectrum analyzer with more display modes."),
    ("Correlometer",0,"Stereo correlation analyzer — free."),
    ("Elephant",99,"Mastering limiter with multiple algorithms."),
    ("Gliss EQ",99,"Graphic equalizer with musical curve control."),
    ("Polysquasher",79,"Mastering compressor with soft-knee control."),
    ("Transgainer",49,"Transient designer with gain and attack control."),
    ("Voxformer",79,"Multi-functional vocal channel processor."),
    ("Soniformer",99,"Multiband stereo processor for mastering."),
    ("OVC-128",49,"Oversampled vintage compressor."),
    ("GlissEQ",99,"Dynamic parametric equalizer."),
    ("Drumformer",79,"Drum channel processing strip."),
    ("TransGainer",49,"Transient designer effect plugin."),
    ("CurveEQ",99,"Spline-based mastering equalizer."),
    ("MSED",0,"Mid-side encoder/decoder — free."),
    ("Stereo Touch",0,"Stereo image widener — free."),
    ("Tube Amp",0,"Tube saturation simulation — free."),
    ("Boogex",0,"Guitar amp simulator — free."),
    ("HarmoniEQ",79,"Harmonics-based equalizer."),
    ("r8brain PRO",99,"Sample rate converter with high precision."),
]
for n,p,desc in voxengo:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Voxengo",'effects',None if p==0 else p,pt,'https://www.voxengo.com',desc)

# Klanghelm
klanghelm = [
    ("MJUC jr.",0,"Variable-tube compressor — free."),
    ("MJUC",99,"Variable-tube compressor with multiple tube types."),
    ("DC8C",0,"DC8C dynamic compressor — free lite version."),
    ("DC8C3",29,"Advanced mastering compressor."),
    ("IVGI",0,"Saturation/distortion — free."),
    ("SDRR",29,"Saturation with 4 modes: tube, tape, FET, transistor."),
    ("VUMT",0,"VU meter — free."),
    ("VUMT Deluxe",19,"VU meter with advanced display options."),
]
for n,p,desc in klanghelm:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Klanghelm",'effects',None if p==0 else p,pt,'https://klanghelm.com',desc)

# Goodhertz
goodhertz = [
    ("Megaverb",99,"Reverb of unusual character."),
    ("Trem Control",39,"Optical tremolo inspired by vintage amplifiers."),
    ("Lossy",99,"Codec and analog degradation tool."),
    ("Wow Control",59,"Wow and flutter tape modulation."),
    ("Midside Matrix",99,"Mid-side encoding and decoding utility."),
    ("Faraday Limiter",79,"Proportional-integral limiting compressor."),
    ("Tone Control",79,"Tone shaping plugin in a simple interface."),
    ("CanOpener Studio",99,"Headphone crossfeed plugin for speaker simulation."),
    ("Vulf Compressor",99,"Signature compressor from Vulfpeck."),
    ("Lohi",79,"Low and high-pass filter with analog character."),
    ("Panpot",49,"Panning control with stereo width."),
    ("MBitFun",49,"Bitcrusher and sample rate reducer."),
    ("WOW Control",59,"Turntable wow and flutter effect."),
]
for n,p,desc in goodhertz:
    add(n,"Goodhertz",'effects',p,'one-time','https://goodhertz.com',desc)

# Eventide
eventide = [
    ("H3000 Factory",199,"Legendary Eventide harmonizer in plugin form."),
    ("H3000 Band Delays",99,"Multi-tap delay from the H3000 series."),
    ("H910 Harmonizer",199,"Classic pitch shifter from 1974."),
    ("H949 Harmonizer",199,"Microshift and pitch shift classic."),
    ("UltraChannel",199,"Channel strip with Eventide processing."),
    ("UltraTap",99,"Multi-tap delay with unique tapering control."),
    ("Blackhole",149,"Infinite reverb from the Eventide DSP9000."),
    ("Anthology XI",999,"Complete Eventide plugin bundle."),
    ("Instant Phaser MkII",99,"Classic phase-shift effect emulation."),
    ("Instant Flanger MkII",99,"Classic flanger emulation."),
    ("SpringRev",99,"Spring reverb emulation."),
    ("Fission",99,"Structural effects processor with transient/tonal split."),
    ("EQuivocate",99,"Graphical EQ with psychoacoustic controls."),
    ("Physion Mk II",149,"Split processing of transient and tonal elements."),
    ("Precision Time Align",199,"Sample-accurate time alignment tool."),
    ("Elevate Bundle",499,"Mastering tools bundle."),
]
for n,p,desc in eventide:
    add(n,"Eventide",'effects',p,'one-time','https://www.eventideaudio.com',desc)

# Slate Digital
slate = [
    ("Virtual Mix Rack (VMR)",14.99,"Analog-modelled mixing console system."),
    ("Virtual Tape Machines (VTM)",9.99,"Tape saturation plugin."),
    ("Virtual Console Collection (VCC)",9.99,"Console emulation for mixing bus."),
    ("Fresh Air",0,"Free high-frequency dynamic plugin."),
    ("Virtual Buss Compressors (VBC)",9.99,"Bus compressor collection."),
    ("Virtual Channel (VC)",9.99,"Channel strip collection."),
    ("FG-X Mastering Processor",9.99,"Mastering dynamics and loudness tool."),
    ("FG-X 2",9.99,"Updated mastering processor."),
    ("All Access Pass",14.99,"Monthly subscription to all Slate plugins."),
    ("Raven MTX",4999,"Multi-touch mixing surface (hardware + software)."),
    ("Virtual Microphone System",149,"Physical mic modelling system."),
    ("AiR Multi-Band",9.99,"Multiband compressor."),
    ("Revival",0,"Free sonic enhancer plugin."),
    ("Infinity EQ",9.99,"Digital EQ with analog character."),
]
for n,p,desc in slate:
    pt = 'free' if p==0 else 'subscription' if p<20 else 'one-time'
    add(n,"Slate Digital",'effects',p,pt,'https://slatedigital.com',desc)

# Blue Cat Audio
bluecat = [
    ("Blue Cat's FreqAnalyst",0,"Real-time spectrum analyzer — free."),
    ("Blue Cat's Chorus",0,"Chorus effect — free."),
    ("Blue Cat's PatchWork",99,"Universal plug-in host — chain any plugin."),
    ("Blue Cat's MB-7 Mixer",99,"Multiband effects rack and mixer."),
    ("Blue Cat's Dynamics",99,"Dynamics processor with gate, comp, exp, limit."),
    ("Blue Cat's Late Replies",99,"Multi-tap delay and reverb designer."),
    ("Blue Cat's Parametr'EQ",99,"Parametric EQ with mid-side mode."),
    ("Blue Cat's Widthshaper",49,"Stereo width modulator."),
    ("Blue Cat's Protector",49,"Transient shaping and limiting."),
    ("Blue Cat's Oscilloscope Multi",49,"Multi-channel oscilloscope."),
]
for n,p,desc in bluecat:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Blue Cat Audio",'effects',None if p==0 else p,pt,'https://www.bluecataudio.com',desc)

# Plugin Alliance / Brainworx
pa = [
    ("bx_digital V3",299,"Mid-side mastering EQ."),
    ("bx_masterdesk",149,"Mastering limiter suite."),
    ("bx_XL V2",149,"Stereo maximizer."),
    ("bx_console SSL 4000 E",299,"SSL 4000 E console emulation."),
    ("bx_console AMEK 9099",299,"AMEK 9099 console channel strip emulation."),
    ("bx_console Neve 8078",299,"Neve 8078 console channel strip emulation."),
    ("Shadow Hills Mastering Compressor",299,"Dual-stage mastering compressor."),
    ("SPL Iron",199,"Mastering compressor based on the SPL Iron hardware."),
    ("SPL Attacker",149,"Transient designer."),
    ("Unfiltered Audio BYOME",149,"Modular multi-effects processor."),
    ("Unfiltered Audio SpecOps",149,"Spectral effects processor."),
    ("Unfiltered Audio SILO",149,"Grain delay synthesizer."),
    ("Unfiltered Audio Zip",99,"Transient-controlled effects."),
    ("Unfiltered Audio Lion",99,"Analog saturation and distortion."),
    ("PA Complete Bundle",4999,"Complete Plugin Alliance plugin collection."),
]
for n,p,desc in pa:
    add(n,"Plugin Alliance",'effects',p,'one-time','https://www.plugin-alliance.com',desc)

# MeldaProduction
melda_free = [
    "MAnalyzer","MAutoVolume","MBandPass","MCharacter","MChorus",
    "MCompressor","MDelay","MDistortion","MDoubler","MDynamics",
    "MEqualizer","MFilter","MFlanger","MGate","MGranularMB",
    "MHarmonizer","MMetronome","MMultiBandDelay","MNoiseGenerator",
    "MNoiseGenerator","MOscilloscope","MPeakController","MPhaser",
    "MPitch","MRecorder","MReverb","MRotary","MSaturator",
    "MStereoExpander","MStereoProcessor","MTremolo","MTuner",
    "MVibrato","MVibratoMB","MVocoder","MWobbler",
]
for n in melda_free:
    add(n,"MeldaProduction",'effects',None,'free','https://www.meldaproduction.com',
        f"MeldaProduction {n} — free plugin.",['effects','melda','free'])

melda_paid = [
    ("MAutoDynamicEQ",99,"Dynamic equalizer with automatic frequency detection."),
    ("MAutoEqualizer",99,"Automated EQ matching and correction."),
    ("MCompressorMB",99,"Multiband compressor with transparent processing."),
    ("MDynamicsMB",149,"Multiband dynamics processor suite."),
    ("MFreeformEqualizer",79,"Freeform drawing EQ."),
    ("MXXX",399,"Modular multi-effects processor with 100+ modules."),
    ("MSoundFactory",299,"Advanced sampler and synthesizer."),
    ("MLoudnessAnalyzer",79,"Loudness metering and compliance."),
    ("MReverbMB",149,"Multiband reverb."),
    ("MSaturatorMB",99,"Multiband saturation."),
    ("MConvolutionEZ",99,"Easy convolution reverb."),
    ("MTurboEQ",149,"Advanced high-precision EQ."),
    ("MTurboComp",149,"Ultra-precise compressor."),
    ("MTransient",79,"Transient shaper."),
    ("MVintageEQ",149,"Vintage EQ collection."),
]
for n,p,desc in melda_paid:
    add(n,"MeldaProduction",'effects',p,'one-time','https://www.meldaproduction.com',desc)

# Oeksound
add("Soothe2","oeksound",'effects',249,'one-time','https://oeksound.com',
    "Dynamic resonance suppressor for taming harsh frequencies.")
add("Spiff","oeksound",'effects',169,'one-time','https://oeksound.com',
    "Adaptive transient processor for natural-sounding control.")

# Acustica Audio
acustica = [
    ("Nebula Pro",99,"Sampling-based analog emulation library host."),
    ("Sand 5",399,"High-end mastering EQ and dynamics suite."),
    ("Ivory",199,"Neve-inspired mix bundle."),
    ("Jade",199,"SSL-inspired mix bundle."),
    ("Crimson",199,"API-inspired mix bundle."),
    ("Gold",299,"Gold classic mastering EQ bundle."),
    ("Emerald",199,"Pultec-style equalizer collection."),
]
for n,p,desc in acustica:
    add(n,"Acustica Audio",'effects',p,'one-time','https://www.acustica-audio.com',desc)

# LiquidSonics
liquidsonics = [
    ("Seventh Heaven",149,"Lexington 480L convolution reverb."),
    ("Reverberate 3",199,"Convolution reverb host with IR management."),
    ("Cinematic Rooms",149,"Room reverb with cinematic character."),
    ("Lustrous Plates",129,"Plate reverb collection."),
    ("Illusion",149,"Large hall reverb with modulation."),
]
for n,p,desc in liquidsonics:
    add(n,"LiquidSonics",'effects',p,'one-time','https://www.liquidsonics.com',desc)

# Softube
softube = [
    ("Tape",99,"Reel-to-reel tape machine emulation."),
    ("Saturation Knob",0,"Free one-knob saturation plugin."),
    ("Drawmer 1973 Multiband Compressor",299,"Drawmer 1973 FET compressor emulation."),
    ("Summit TLA-100A",199,"Summit TLA-100A compressor emulation."),
    ("Weiss DS1-MK3",499,"Weiss digital mastering compressor."),
    ("Amp Room",99,"Guitar and bass amplifier suite."),
    ("Modular",99,"Semi-modular synthesizer and Eurorack emulation."),
    ("Valley People Dyna-mite",99,"Vintage dynamics processor."),
    ("FET Compressor",99,"FET compressor with vintage character."),
]
for n,p,desc in softube:
    pt = 'free' if p==0 else 'one-time'
    add(n,"Softube",'effects',None if p==0 else p,pt,'https://www.softube.com',desc)

# Output
output_plugins = [
    ("Movement",149,"Rhythm-based effects plugin with four effect engines."),
    ("Portal",149,"Granular effects plugin for creative transformation."),
    ("Thermal",149,"Multi-stage distortion effects plugin."),
    ("Signal",149,"Motion engine for creating movement in pads."),
    ("Arcade",9.99,"Sample playground with loops, slices, and effects."),
    ("Analog Strings",199,"Layered string instrument with movement."),
    ("Exhale",199,"Cinematic vocal instrument."),
    ("Substance",199,"Bass instrument with synthesis and sampling."),
    ("Analog Brass & Winds",199,"Expressive brass instrument."),
    ("Al-Noor",149,"Middle Eastern instrument library."),
    ("Spectrum",199,"Synth engine with evolving motion presets."),
    ("REV",149,"Reversed instrument library for textures."),
]
for n,p,desc in output_plugins:
    pt = 'subscription' if n=='Arcade' else 'one-time'
    cat = 'synth' if p>=149 else 'effects'
    add(n,"Output",cat,p,pt,'https://output.com',desc)

# Devious Machines
devious = [
    ("Infiltrator 2",99,"Multi-effect sequencer with 27 onboard effects."),
    ("Pitch Monster",49,"Chord and pitch manipulation processor."),
    ("Texture",79,"Granular synthesis effects plugin."),
    ("Duck",29,"Sidechain compressor with visual control."),
    ("Beat Dropper",29,"Sidechain ducking tool."),
]
for n,p,desc in devious:
    add(n,"Devious Machines",'effects',p,'one-time','https://www.deviousmachines.com',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# DRUM MACHINES & PLUGINS
# ═══════════════════════════════════════════════════════════════════════════════
drums = [
    ("Superior Drummer 3","Toontrack",399,"Most realistic virtual drum kit with multi-mic recording.",'drums'),
    ("EZdrummer 3","Toontrack",179,"Easy-to-use virtual drum plugin with MIDI grooves.",'drums'),
    ("EZbass","Toontrack",179,"AI-powered virtual bass player for composers.",'drums'),
    ("EZkeys","Toontrack",149,"Virtual piano and chord-playing instrument.",'drums'),
    ("Addictive Drums 2","XLN Audio",179,"Mix-ready virtual drum plugin with fast workflow.",'drums'),
    ("Addictive Keys Studio Grand","XLN Audio",79,"High-quality grand piano library.",'sampler'),
    ("RC-20 Retro Color","XLN Audio",99,"Vintage color and degradation effect.",'effects'),
    ("XO","XLN Audio",99,"Sample organizer and beat production tool.",'drums'),
    ("Battery 4","Native Instruments",199,"Professional drum sampler with 55 kits.",'drums'),
    ("Steven Slate Drums 5.5","Slate Digital",149,"Ultra-realistic virtual drum instrument.",'drums'),
    ("BFD3","BFD",199,"Deep sampled drum plugin with acoustic detail.",'drums'),
    ("BFD Player","BFD",0,"Free version of BFD drum player.",'drums'),
    ("Addictive Drums 2 Custom XL","XLN Audio",299,"Expanded AD2 with multiple kit packs.",'drums'),
    ("Drum Rack","Ableton",0,"Drum sampler/sequencer included in Ableton Live.",'drums'),
    ("Spark 2","Arturia",199,"Hybrid drum machine and step sequencer.",'drums'),
    ("Microtonic","Sonic Charge",99,"Drum synth and beat machine plugin.",'drums'),
    ("Wave Alchemy Revolution","Wave Alchemy",199,"Drum machine sampling tool.",'drums'),
    ("Wave Alchemy Triaz","Wave Alchemy",99,"Three-channel drum machine plugin.",'drums'),
    ("D16 Drumazon 2","D16 Group",99,"Roland TR-909 drum machine emulation.",'drums'),
    ("D16 Nepheton","D16 Group",79,"Roland TR-808 drum machine emulation.",'drums'),
    ("D16 Nithonat","D16 Group",79,"Roland TR-606 drum machine emulation.",'drums'),
    ("D16 Tekturon","D16 Group",79,"Programmable digital drum machine.",'drums'),
    ("Jamstix 5","Rayzoon",99,"AI-powered virtual drummer plugin.",'drums'),
    ("Trilian","Spectrasonics",299,"Professional bass instrument library.",'sampler'),
    ("FXpansion Geist 2","FXpansion",149,"Drum machine and loop slicer.",'drums'),
    ("FXpansion Tremor","FXpansion",79,"Analog-style drum synthesizer.",'drums'),
    ("Punch","Rob Papen",79,"Drum synthesizer with layered sound design.",'drums'),
    ("MT Power Drum Kit 2","MT Power Drum Kit",0,"Free drum kit for realistic rock and pop drums.",'drums'),
    ("Addictive Drums 2 Session Percussion","XLN Audio",69,"Orchestral and session percussion add-on.",'drums'),
    ("Goldbaby PocketLabo","Goldbaby",49,"Multi-layered vintage drum machine samples.",'drums'),
    ("LM-4 MkII","Steinberg",0,"Classic virtual drum machine included with Cubase.",'drums'),
]
for n,dev,p,desc,cat in drums:
    pt = 'free' if p==0 else 'one-time'
    add(n,dev,cat,None if p==0 else p,pt,
        'https://www.native-instruments.com' if dev=='Native Instruments' else
        'https://www.toontrack.com' if dev=='Toontrack' else
        'https://www.xlnaudio.com' if dev=='XLN Audio' else
        'https://slatedigital.com' if dev=='Slate Digital' else
        'https://www.ableton.com' if dev=='Ableton' else
        'https://d16.com' if dev=='D16 Group' else
        'https://www.wavealchemy.co.uk',
        desc,[cat])

# ═══════════════════════════════════════════════════════════════════════════════
# SAMPLERS & LIBRARIES
# ═══════════════════════════════════════════════════════════════════════════════
libraries = [
    ("Kontakt 7","Native Instruments",399,"Industry-standard sampler with 14,000+ sounds."),
    ("Kontakt Player","Native Instruments",0,"Free player for Kontakt libraries."),
    ("Komplete Kontrol","Native Instruments",0,"Free keyboard integration host for NI instruments."),
    ("LABS","Spitfire Audio",0,"Free premium instrument library updated regularly."),
    ("BBC Symphony Orchestra Discover","Spitfire Audio",0,"Free orchestral library recorded at Maida Vale."),
    ("BBCSO Core","Spitfire Audio",299,"Core orchestral library from BBC/Spitfire."),
    ("BBCSO Professional","Spitfire Audio",699,"Complete BBC Symphony Orchestra library."),
    ("Albion ONE","Spitfire Audio",399,"Essential orchestral library for composers."),
    ("Albion NEO","Spitfire Audio",449,"Modern hybrid orchestral library."),
    ("Albion TUNDRA","Spitfire Audio",399,"Arctic-themed atmospheric library."),
    ("Hans Zimmer Strings","Spitfire Audio",399,"Signature strings from Hans Zimmer."),
    ("Hans Zimmer Brass","Spitfire Audio",299,"Signature brass from Hans Zimmer."),
    ("Spitfire Chamber Strings","Spitfire Audio",399,"Intimate chamber string ensemble."),
    ("Spitfire Solo Strings","Spitfire Audio",399,"Expressive solo strings library."),
    ("Spitfire Solo Piano","Spitfire Audio",299,"Premium grand piano library."),
    ("Studio Strings Professional","Native Instruments",599,"Studio string ensemble for production."),
    ("EastWest ComposerCloud","EastWest",29.99,"Subscription access to Hollywood orchestral libraries."),
    ("Hollywood Orchestra Diamond","EastWest",599,"Flagship orchestral library."),
    ("Hollywood Brass Diamond","EastWest",399,"Premier brass library."),
    ("Hollywood Strings Diamond","EastWest",399,"Premier string library."),
    ("Hollywood Choir","EastWest",299,"Professional choir library."),
    ("PLAY","EastWest",0,"Free player for EastWest libraries."),
    ("ProjectSAM Symphobia 1","ProjectSAM",399,"Orchestral ensemble library."),
    ("ProjectSAM Symphobia 2","ProjectSAM",399,"Expanded orchestral ensemble library."),
    ("ProjectSAM Lumina","ProjectSAM",299,"Solo strings and choir library."),
    ("True Strike 1","ProjectSAM",299,"Percussion library."),
    ("Cinematic Studio Strings","Cinematic Studio",399,"Smooth, expressive string library."),
    ("Cinematic Studio Brass","Cinematic Studio",299,"Full brass section library."),
    ("Cinematic Studio Woodwinds","Cinematic Studio",299,"Woodwind ensemble library."),
    ("Cinematic Studio Piano","Cinematic Studio",149,"Grand piano library."),
    ("8Dio Century Strings","8Dio",399,"Detailed orchestral string library."),
    ("8Dio Solo Strings","8Dio",299,"Solo string instrument library."),
    ("8Dio Majestica","8Dio",399,"Large ensemble string library."),
    ("Heavyocity NOVO","Heavyocity",299,"Modern strings library with unique sound design."),
    ("Heavyocity Gravity","Heavyocity",299,"Cinematic percussion and brass."),
    ("Heavyocity Mosaic Tape","Heavyocity",149,"Lo-fi tape-processed instruments."),
    ("Sample Logic Symphony Series","Sample Logic",299,"Orchestral sample instrument."),
    ("Sample Logic Geosphere","Sample Logic",199,"Environmental sound library."),
    ("Audio Imperia Nucleus","Audio Imperia",299,"Hybrid cinematic instrument."),
    ("Sonokinetic Orchestral Strings","Sonokinetic",299,"Kontakt string library."),
    ("Sonokinetic Minimal","Sonokinetic",149,"Minimal orchestral phrases library."),
    ("Decent Sampler","Decent Samples",0,"Free sampler for community-made libraries."),
    ("sforzando","Plogue",0,"Free SFZ player plugin."),
    ("Grace","One Small Clue",0,"Free sample player."),
    ("TAL-Sampler","TAL Software",60,"Vintage hardware sampler emulation."),
    ("Output Arcade","Output",9.99,"Loop-based sample instrument with cloud library."),
    ("Splice Sounds","Splice",7.99,"Subscription sample library with millions of sounds."),
    ("Loopmasters","Loopmasters",0,"Sample library marketplace."),
    ("Looperman","Looperman",0,"Free loop sharing community."),
    ("MODO BASS","IK Multimedia",299,"Physical modelling bass instrument."),
    ("MODO DRUM","IK Multimedia",299,"Physical modelling drum instrument."),
    ("SampleTank 4","IK Multimedia",199,"Multi-instrument sample player with 55 GB library."),
    ("Miroslav Philharmonik 2","IK Multimedia",299,"Complete orchestral instrument collection."),
]
for n,dev,p,desc in libraries:
    pt = 'free' if p==0 else 'subscription' if isinstance(p,float) and p<30 else 'one-time'
    add(n,dev,'sampler',None if p==0 else p,pt,'https://www.spitfireaudio.com' if 'Spitfire' in dev else
        'https://www.native-instruments.com' if dev=='Native Instruments' else
        'https://www.soundsonline.com' if 'EastWest' in dev else
        'https://www.projectsam.com' if 'ProjectSAM' in dev else
        'https://8dio.com' if '8Dio' in dev else
        'https://www.heavyocity.com' if 'Heavyocity' in dev else
        'https://output.com' if 'Output' in dev else
        'https://splice.com',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# MIXING & MASTERING
# ═══════════════════════════════════════════════════════════════════════════════
mastering = [
    ("iZotope Ozone 11 Advanced","iZotope",499,"Complete AI mastering suite."),
    ("iZotope Ozone 11 Standard","iZotope",249,"Core mastering tools."),
    ("iZotope Ozone 11 Elements","iZotope",99,"Entry AI mastering."),
    ("iZotope Neutron 4","iZotope",249,"AI-powered mixing assistant."),
    ("Waves SSL G-Master Buss Compressor","Waves",29,"Bus compressor."),
    ("Waves L3 Multimaximizer","Waves",49,"Multiband limiter for mastering."),
    ("Brainworx bx_masterdesk","Plugin Alliance",149,"One-knob mastering tool."),
    ("Brainworx bx_XL V2","Plugin Alliance",149,"Stereo widening limiter."),
    ("Brainworx bx_digital V3","Plugin Alliance",299,"Mid-side mastering EQ."),
    ("IK Multimedia T-RackS 5","IK Multimedia",199,"Complete mastering suite."),
    ("IK Multimedia Lurssen Mastering Console","IK Multimedia",199,"Grammy engineer mastering chain."),
    ("Nugen Audio MasterCheck Pro","Nugen Audio",249,"Streaming loudness metering tool."),
    ("Nugen Audio ISL 2","Nugen Audio",199,"True peak limiter."),
    ("Nugen Audio Stereoizer","Nugen Audio",149,"Stereo width processor."),
    ("Nugen Audio VisLM 2","Nugen Audio",199,"Loudness metering tool."),
    ("PSP Audioware MasterComp","PSP Audioware",149,"Bus compressor for mastering."),
    ("PSP Audioware Neon HR","PSP Audioware",149,"High-resolution EQ."),
    ("PSP Audioware oldTimer","PSP Audioware",99,"Vintage optical compressor."),
    ("ToneBoosters Barricade","ToneBoosters",29,"Mastering limiter."),
    ("ToneBoosters ReelBus","ToneBoosters",29,"Tape saturation plugin."),
    ("ToneBoosters EBU Loudness","ToneBoosters",29,"Loudness metering for broadcast."),
    ("Fabfilter Pro-L 2","FabFilter",179,"True peak brickwall mastering limiter."),
    ("DDMF Metaplugin","DDMF",69,"Universal plugin host for parallel/serial chains."),
    ("Youlean Loudness Meter 2","Youlean",0,"Free loudness metering tool."),
    ("Melda Production MLoudnessAnalyzer","MeldaProduction",79,"Loudness analysis and monitoring."),
    ("Weiss DS1-MK3","Softube",499,"Professional mastering compressor emulation."),
    ("Elysia Alpha Compressor","Plugin Alliance",449,"High-end mastering compressor."),
    ("DearVR Pro","Dear Reality",199,"3D spatial audio and binaural plugin."),
]
for n,dev,p,desc in mastering:
    pt = 'free' if p==0 else 'one-time'
    add(n,dev,'mastering',None if p==0 else p,pt,'https://www.izotope.com' if 'iZotope' in dev else 'https://www.waves.com' if 'Waves' in dev else '#',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# MIDI & UTILITY TOOLS
# ═══════════════════════════════════════════════════════════════════════════════
midi_tools = [
    ("Scaler 2","Plugin Boutique",59,"Chord generator and scale assistant."),
    ("Cthulhu","Xfer Records",39,"Chord and arpeggiator MIDI effect."),
    ("Captain Chords","Mixed In Key",99,"Chord progression composer."),
    ("Captain Melody","Mixed In Key",59,"Melody writing tool."),
    ("Captain Beat","Mixed In Key",59,"Drum pattern creator."),
    ("Riffer","Audiority",49,"Generative MIDI riff creator."),
    ("MIDI Guitar 2","Jam Origin",149,"Guitar-to-MIDI converter."),
    ("Gatelab","Audiomodern",49,"Pattern gate and randomization MIDI tool."),
    ("Playbeat 3","Audiomodern",59,"Smart beat generator with probability."),
    ("Chordjam","Audiomodern",49,"Randomized chord generation tool."),
    ("Unify","PlugInGuru",97,"Plugin host for layering instruments."),
    ("Metaplugin","DDMF",69,"Plugin chain host for DAW routing."),
    ("Max for Live","Cycling '74",0,"Included in Ableton Live Suite."),
    ("Melodics","Melodics",0,"Piano/pad learning platform."),
    ("Ripchord","Polyverse",0,"Free chord creation plugin."),
    ("Chordz","Codefn42",0,"Free chord triggering plugin."),
    ("MIDI Polysher","BOME",79,"MIDI processing and polyphony manager."),
    ("Bome MIDI Translator Pro","BOME",99,"Advanced MIDI routing and scripting."),
    ("LoopBe1","Nerds VS Suits",0,"Free virtual MIDI port."),
    ("loopMIDI","Tobias Erichsen",0,"Free virtual MIDI routing tool."),
    ("MIDI Monitor","Snoize",0,"Free MIDI monitoring tool for Mac."),
    ("MidiEditor","MidiEditor",0,"Free MIDI editor and player."),
    ("PianoTeq","Modartt",99,"Physical modelling piano with MIDI control."),
    ("Cthulhu Lite","Xfer Records",0,"Free chord player plugin."),
    ("HY-MIDI Sequencer","HY-Plugins",0,"Free MIDI sequencer plugin."),
    ("arpeggiator","Plogue",0,"Free arpeggiator MIDI effect."),
    ("InstaChord","Mixed In Key",99,"Real-time chord and harmony tool."),
    ("Entonal Studio","Entonal Studio",99,"Microtonal MIDI tuning tool."),
    ("LASS","SmartAssistant",149,"Live Advanced String Section."),
]
for n,dev,p,desc in midi_tools:
    pt = 'free' if p==0 else 'one-time'
    add(n,dev,'midi',None if p==0 else p,pt,'https://www.pluginboutique.com' if 'Plugin' in dev else '#',desc)

# Analysis/Utility
utility = [
    ("iZotope RX 11 Advanced","iZotope",1199,"Professional audio repair suite."),
    ("iZotope RX 10 Standard","iZotope",399,"Audio repair tools for production."),
    ("SPAN","Voxengo",0,"Free spectrum analyzer."),
    ("Insight 2","iZotope",299,"Advanced metering with loudness analysis."),
    ("MMultiAnalyzer","MeldaProduction",99,"Multi-channel spectrum analyzer."),
    ("Blue Cat's FreqAnalyst","Blue Cat Audio",0,"Real-time frequency analyzer."),
    ("Youlean Loudness Meter","Youlean",0,"Free loudness metering."),
    ("HOFA 4U Meter","HOFA Plugins",0,"VU and PPM metering — free."),
    ("TDR Nova","Tokyo Dawn Records",0,"Parallel dynamic EQ — free."),
    ("Voxengo Correlometer","Voxengo",0,"Stereo correlation meter — free."),
    ("Reference 2","Sonarworks",249,"Studio reference monitoring calibration."),
    ("SoundID Reference","Sonarworks",249,"Headphone and speaker calibration."),
    ("Waves Nx","Waves",49,"3D headphone monitoring plugin."),
    ("Flux Analyzer","Flux",99,"Stereo and surround analysis suite."),
    ("Tungsten","Pulsar Audio",79,"VU metering plugin."),
    ("SurferEQ","Cherry Audio",39,"Pitch-following EQ."),
    ("Canopener Studio","Goodhertz",99,"Headphone crossfeed monitor simulation."),
    ("Sample Rate Converter","iZotope",0,"Free sample rate conversion tool."),
    ("Bandwidth","Mastering The Mix",49,"Audio analysis and problem-solving tool."),
    ("Expose 2","Mastering The Mix",49,"Master checking and QC tool."),
    ("Bassroom","Mastering The Mix",49,"Low-frequency reference and analysis tool."),
    ("Mixroom","Mastering The Mix",49,"Mix reference and tone shaping tool."),
    ("Plugin Doctor","Voxengo",49,"Plugin measurement and analysis tool."),
    ("SpectraFoo Complete","Metric Halo",649,"Professional audio analysis suite."),
    ("PhonicMind","PhonicMind",19.99,"AI stem splitter."),
    ("LALAL.AI","LALAL",0,"AI-powered vocal and stem separator."),
    ("Spleeter","Deezer",0,"Open-source AI stem separation tool."),
    ("AudioSourceRE","AudioSourceRE",129,"Stem separation and source recovery."),
]
for n,dev,p,desc in utility:
    pt = 'free' if p==0 else 'one-time'
    add(n,dev,'utility',None if p==0 else p,pt,'#',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# GUITAR & BASS
# ═══════════════════════════════════════════════════════════════════════════════
guitar = [
    ("Archetype: Nolly","Neural DSP",99,"Nolly signature guitar plugin."),
    ("Archetype: Petrucci","Neural DSP",99,"John Petrucci signature guitar plugin."),
    ("Archetype: Tim Henson","Neural DSP",99,"Tim Henson signature guitar plugin."),
    ("Archetype: Plini","Neural DSP",99,"Plini signature guitar plugin."),
    ("Archetype: Rabea","Neural DSP",99,"Rabea Massaad signature guitar plugin."),
    ("Archetype: Chris Broderick","Neural DSP",99,"Chris Broderick signature guitar plugin."),
    ("Parallax","Neural DSP",99,"Bass guitar plugin with preamps and cabinets."),
    ("Fortin NTS Suite","Neural DSP",99,"Fortin NTS amp suite plugin."),
    ("Darkglass Ultra","Neural DSP",99,"Darkglass Ultra bass plugin."),
    ("Abasi Concepts","Neural DSP",99,"Tosin Abasi signature guitar plugin."),
    ("AmpliTube 5","IK Multimedia",199,"Complete guitar amp and effects suite."),
    ("AmpliTube Fender Collection 2","IK Multimedia",99,"Fender amp collection."),
    ("AmpliTube Marshall Collection","IK Multimedia",99,"Marshall amp collection."),
    ("AmpliTube Mesa/Boogie Collection","IK Multimedia",99,"Mesa Boogie amp collection."),
    ("AmpliTube Slash Collection","IK Multimedia",99,"Slash signature amp collection."),
    ("BIAS FX 2 Elite","Positive Grid",299,"Professional guitar amp simulator."),
    ("BIAS FX 2 Standard","Positive Grid",99,"Guitar amp simulator."),
    ("BIAS Amp 2 Elite","Positive Grid",199,"Amp designer and modeller."),
    ("BIAS Pedal","Positive Grid",99,"Guitar pedal designer."),
    ("TH-U Full","Overloud",149,"Guitar amp and rig modeller."),
    ("TH-U Rock","Overloud",99,"Rock-focused amp modeller."),
    ("Scuffham S-Gear","Scuffham",99,"Guitar amp simulator with three amps."),
    ("Guitar Rig 7 Pro","Native Instruments",199,"Guitar and bass amp simulation suite."),
    ("Guitar Rig 7 Player","Native Instruments",0,"Free guitar amp player."),
    ("Helix Native","Line 6",399,"Plugin version of the Helix hardware."),
    ("HX Stomp plugin","Line 6",0,"Free plugin companion for HX hardware."),
    ("Tonex","IK Multimedia",149,"AI-powered amp and pedal capture tool."),
    ("STL Tones Tonality","STL Tones",99,"Signature guitar plugin collection."),
    ("Choptones Rig","Choptones",79,"High-gain guitar simulation plugin."),
    ("Mercuriall Audio Spark","Mercuriall",89,"Marshall amp emulation."),
    ("Mercuriall Audio Reaxis","Mercuriall",89,"Mesa Boogie Rectifier emulation."),
    ("Ignite Amps Emissary","Ignite Amps",0,"Free high-gain amp emulation."),
    ("Ignite Amps NadIR","Ignite Amps",0,"Free cabinet impulse response loader."),
    ("Lepou HyBrit","Lepou",0,"Free Marshall plexi amp emulation."),
    ("Nick Crow 8505 Lead","Nick Crow",0,"Free modern high-gain amp."),
    ("Aurora DSP Rhino","Aurora DSP",89,"Modern metal guitar plugin."),
    ("Aurora DSP Segovia","Aurora DSP",89,"Classical guitar plugin."),
]
for n,dev,p,desc in guitar:
    pt = 'free' if p==0 else 'one-time'
    add(n,dev,'guitar',None if p==0 else p,pt,'https://neuraldsp.com' if 'Neural' in dev else '#',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# VOCAL TOOLS
# ═══════════════════════════════════════════════════════════════════════════════
vocal_tools = [
    ("Auto-Tune Pro X","Antares",24.99,"Industry-standard real-time pitch correction."),
    ("Auto-Tune Artist","Antares",17.99,"Core Auto-Tune with real-time correction."),
    ("Auto-Tune EFX+","Antares",9.99,"Auto-Tune with creative vocal effects."),
    ("Auto-Tune Access","Antares",9.99,"Single-knob Auto-Tune."),
    ("Auto-Tune Vocodist","Antares",9.99,"Vocoder with Auto-Tune engine."),
    ("Harmony Engine Evo","Antares",19.99,"Intelligent harmony generation plugin."),
    ("Choir Evo","Antares",19.99,"Vocal multiplication and choir effect."),
    ("AVOX 4 Bundle","Antares",49.99,"Four vocal transformation tools."),
    ("Throat Evo","Antares",19.99,"Physical modelling throat synthesizer."),
    ("Melodyne 5 Studio","Celemony",399,"Full polyphonic pitch editing with DNA."),
    ("Melodyne 5 Editor","Celemony",249,"Complete pitch and time editing."),
    ("Melodyne 5 Assistant","Celemony",149,"Core pitch correction with ARA2."),
    ("Melodyne 5 Essential","Celemony",99,"Basic pitch correction for vocals."),
    ("iZotope Nectar 4 Advanced","iZotope",249,"Complete AI vocal production suite."),
    ("iZotope Nectar 4 Standard","iZotope",149,"Core vocal mixing and processing."),
    ("iZotope Nectar 4 Elements","iZotope",69,"AI vocal processing basics."),
    ("Waves Tune Real-Time","Waves",49,"Real-time pitch correction."),
    ("Waves Tune","Waves",79,"Full-featured pitch correction plugin."),
    ("Little AlterBoy","Soundtoys",149,"Voice transformation and formant shifter."),
    ("VocalSynth 2","iZotope",199,"Vocal effects with talkbox, vocoder, biovox."),
    ("Revoice Pro 4","Synchro Arts",399,"Automatic doubling and tuning alignment."),
    ("VocAlign Ultra","Synchro Arts",299,"Vocal timing and pitch alignment tool."),
    ("GSnap","GVST",0,"Free basic pitch correction plugin."),
    ("MAutoPitch","MeldaProduction",0,"Free auto-tune plugin."),
    ("KeroVee","g200kg",0,"Free pitch correction plugin."),
    ("Auburn Sounds Graillon 2","Auburn Sounds",0,"Free pitch correction and voice changer."),
    ("GVST GVocoder","GVST",0,"Free vocoder plugin."),
    ("TAL-Vocoder","TAL Software",0,"Free vintage vocoder emulation."),
    ("Choir","iZotope",0,"Free vocal pad and choir tool."),
    ("Voice Synth","Pitch Innovations",29,"Vocal harmonizer and pitch manipulator."),
]
for n,dev,p,desc in vocal_tools:
    pt = 'free' if p==0 else 'subscription' if p<30 else 'one-time'
    add(n,dev,'vocal',None if p==0 else p,pt,'https://www.antarestech.com' if 'Antares' in dev else 'https://www.celemony.com' if 'Celemony' in dev else '#',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# EXPERIMENTAL
# ═══════════════════════════════════════════════════════════════════════════════
experimental = [
    ("VCV Rack 2 Free","VCV",0,"Free modular synthesizer environment."),
    ("VCV Rack 2 Pro","VCV",99,"Professional modular synthesizer plugin."),
    ("Max 8","Cycling '74",9.99,"Visual programming environment for music."),
    ("Reaktor 6","Native Instruments",199,"Modular synthesis and creative DSP platform."),
    ("SuperCollider","SuperCollider",0,"Open-source audio synthesis platform."),
    ("Pure Data","Miller Puckette",0,"Open-source graphical patching environment."),
    ("Kyma","Symbolic Sound",3960,"Professional sound design system."),
    ("Aalto","Madrona Labs",99,"Semi-modular synthesizer with physical modelling."),
    ("Kaivo","Madrona Labs",99,"Physical modelling granular synthesizer."),
    ("Virta","Madrona Labs",99,"Audio-rate modulated effects."),
    ("Sumu","Madrona Labs",99,"Spectral additive synthesizer."),
    ("Syntrx","Erica Synths",1499,"Analog synthesizer inspired by EMS Synthi."),
    ("Noise Engineering Basimilus Iteritas","Noise Engineering",0,"Modular percussion synthesizer concept."),
    ("Granulator III","Robert Henke",0,"Granular synthesis instrument for Live."),
    ("Quanta 2","Audio Damage",49,"Granular synthesizer plugin."),
    ("Borderlands Granular","Borderlands",0,"iOS granular synthesizer."),
    ("Emergence","Audio Damage",29,"Polyphonic wavetable/granular synth."),
    ("Discord4","Audio Damage",39,"Advanced pitch-shifting harmonizer."),
    ("Eos 2","Audio Damage",39,"Algorithmic reverb plugin."),
    ("Phosphor 3","Audio Damage",29,"Additive synthesizer based on alphaSyntauri."),
    ("Ratshack Reverb","Audio Damage",0,"Free reverb plugin."),
    ("Fractal Bits","Glitchmachines",0,"Free glitch effects plugin."),
    ("Fracture XT","Glitchmachines",0,"Free granular glitch synthesizer."),
    ("Hysteresis","Glitchmachines",49,"Delay and feedback glitch processor."),
    ("Subvert","Glitchmachines",49,"Multiband distortion plugin."),
    ("Cataract","Glitchmachines",49,"Modulated filter effects."),
    ("Quadrant","Glitchmachines",49,"Multi-effects router."),
    ("Loom II","AIR Music Technology",99,"Additive synthesizer."),
    ("SPEAR","Klingbeil",0,"Free spectral analysis and resynthesis."),
    ("AudioSculpt","IRCAM",499,"Audio analysis and transformation tool."),
    ("Cecilia 5","Blargg",0,"Free audio processing with Python scripting."),
    ("Csound","Csound Community",0,"Audio programming language for synthesis."),
    ("ChucK","Princeton",0,"Strongly-timed music programming language."),
    ("Faust","GRAME",0,"Functional programming language for DSP."),
    ("Overtone","Overtone Community",0,"Clojure-based live music programming."),
    ("Sonic Pi","Sam Aaron",0,"Live coding synthesizer for music education."),
]
for n,dev,p,desc in experimental:
    pt = 'free' if p==0 else 'subscription' if isinstance(p,float) else 'one-time'
    add(n,dev,'experimental',None if p==0 else p,pt,'https://vcvrack.com' if 'VCV' in dev else '#',desc)

# ═══════════════════════════════════════════════════════════════════════════════
# Build output
# ═══════════════════════════════════════════════════════════════════════════════
def build():
    existing = []
    if os.path.exists(OUT):
        with open(OUT, encoding='utf-8') as f:
            existing = json.load(f)

    existing_names = {p['name'].lower().strip() for p in existing}
    existing_slugs = {p['slug'] for p in existing}

    new_products = []
    cat_count = {}

    for name, dev, cat, price, pt, url, desc, tags in CATALOG:
        key = name.lower().strip()
        if key in existing_names:
            continue
        existing_names.add(key)

        base = slug(name)
        s = base
        i = 2
        while s in existing_slugs:
            s = f"{base}-{i}"
            i += 1
        existing_slugs.add(s)

        product = {
            "id": s,
            "name": name,
            "slug": s,
            "developer": dev,
            "categoryId": cat,
            "shortDescription": desc or f"{name} by {dev}.",
            "price": price,
            "priceType": pt,
            "officialUrl": url,
            "rating": 0,
            "ratingCount": 0,
            "os": [],
            "formats": [],
            "features": [],
            "pros": [],
            "cons": [],
            "tags": list(set(tags)),
            "isFeatured": False,
            "isNew": False,
        }
        new_products.append(product)
        cat_count[cat] = cat_count.get(cat, 0) + 1

    all_products = existing + new_products
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(all_products, f, indent=2, ensure_ascii=False)

    print(f"\nAdded {len(new_products)} new products")
    for c, n in sorted(cat_count.items(), key=lambda x: -x[1]):
        print(f"  {c:20s} {n}")
    print(f"\nTotal in database: {len(all_products)}")
    print(f"Output: {OUT}")

if __name__ == '__main__':
    build()
