import pandas as pd

personal = [
    'thighhighs'
]

# lists below (nude)

fem_masturbation = [
    'baddragon',
    'buttplug',
    'clenching',
    'dildo_gifs',
    'dildothreesomes',
    'doubledildos',
    'edging',
    'femaleorgasmdenial',
    'fingering',
    'fuckingmachines',
    'gettingherselfoff',
    'girlsmasturbating',
    'girlswatchingporn',
    'girlswithtoys',
    'holewreckers',
    'hugedildos',
    'hugetoys',
    'jilling',
    'masturbationgonewild',
    'mmgirls',
    'notadildo',
    'nsfwtoys',
    'orgasmiccontractions',
    'pillowhumping',
    'realjilling',
    'rubbingherpussy',
    'solo_girls',
    'solo_gonewild',
    'solomasturbation'
    'suctiondildos',
    'toysgw'
]

humiliation = [
    'femdomhumiliation',
    'hentaihumiliation',
    'ftmspunished',
    'humiliationbdsm',
    'humiliationexercises',
    'humiliationpose',
    'bodywriting',
    'whorelipstick',
    'whoremouth',
    'womenarethings'
]

misogyny = [
    'fuckdoll',
    'misogynyxxx',
    'misogynygonewild',
    'womensupportsmisogyny',
    'degradethispig',
    'betawomen',
    'misogynisticlife',
    'patriarchyparadise'
]

alternative = [
    'adorableneongirls',
    'alternativebeauty',
    'altgirlnsfw',
    'altgirls',
    'altgonewild',
    'bigassaltgirls',
    'bigbootygothiccgf',
    'bigtiddygothgf',
    'bigtittyaltgirls',
    'chainedpiercings',
    'draculabiscuits',
    'emogirls',
    'emogirlsfuck',
    'fishnets',
    'girlswithneonhairnsfw',
    'girlswithtatsnsfw',
    'gonewildmetal',
    'gothgirlsgw',
    'gothgonewild',
    'gothsluts',
    'hotchickswithtattoos',
    'hotgirlswithtattoos',
    'inkedamatuers',
    'inkedasianwomen',
    'nsfw_altporn',
    'nsfwpunkgirls',
    'piercednipples',
    'piercednsfw',
    'piercedslits',
    'prettyaltgirls',
    'pubic_tattoo',
    'punkgirls',
    'ravegirls',
    'scenegirls',
    'smoltiddygothgf',
    'tattoo_porn',
    'tattooed_girls',
    'tattooed_redheads',
    'tattoogirlmodels',
    'tattoogirls',
    'tattoosporn',
    'tittats',
    'wombtattoos'
]

public = [
    '18pluspublic',
    'exhibitionistfun',
    'exposedinpublic',
    'exposehernature',
    'flashing',
    'flashingandflaunting',
    'flashinggirls',
    'gwpublic',
    'naughtyinpublic',
    'nsfw_outdoors',
    'outdoorbondage',
    'outdoorrecreation',
    'public',
    'publicfetish',
    'publicflashing',
    'publicnudity',
    'realpublicnudity',
    'toplessinpublic',
    'voyeurflash',
    'workgonewild',
    'yolooutdoors'
]

cunnilingus = [
    'aviewfrombelow',
    'camerasquatting',
    'cunnilingus',
    'eating_pussy_gifs',
    'eatingpussy',
    'facesitting',
    'facesittinghub',
    'facesittingporn',
    'hoverpussy',
    'simulingus',
    'tongueinpussy'
]

amateur =[
    'amateur',
    'amateurs',
    'amateurxxx',
    'asianhotties',
    'bad_ass_girlfriends',
    'changingrooms',
    'gifsgonewild',
    'girlsdoingstuffnaked',
    'gonemild',
    'gonewild',
    'gonewild18',
    'gonewildcolor',
    'gonewildscrubs',
    'gonewildsmiles',
    'gwnerdy',
    'gwpublic',
    'homemadensfw',
    'instahotties',
    'labiagw',
    'leggingsgonewild',
    'normalnudes',
    'normalnudesgonewild',
    'nsfw_amateurs',
    'nsfw_girlfriendvideos',
    'nude_selfie',
    'onoff',
    'phgonewild',
    'ratemynudebody',
    'realgirls',
    'repressedgonewild',
    'sundressesgonewild',
    'tallgonewild',
    'workgonewild',
    'workoutgonewild'
]

young = [
    '18_19',
    'barelylegal',
    'barelylegalteens',
    'collegeamateurs',
    'collegensfw',
    'collegesluts',
    'legalteens'
]

# lists below (barely sfw)

breasts = [
    'braless',
    'bralessforever',
    'bralessinmotion',
    'candidpiercedpokies',
    'downblouse',
    'nipple_ripple',
    'nobra',
    'oblivious_pokies',
    'pokies',
    'thinclothing',
    'tshirtsandtanktops'
]

tight_clothes = [
    'bootsandstockings',
    'clothedforprejacs',
    'girlsinleggings',
    'girlsinyogapants',
    'gymgirls',
    'hotgirlsinyogapants',
    'leggings',
    'leggingsandjeansfeet',
    'stockings',
    'tightdresses',
    'tightsandtightclothes',
    'workoutgirls',
    'yogacameltoes',
    'yogapants'
]

# lists below (strictly non-nude)

censors = [
    'armpitsforbetas',
    'betasafeheaven',
    'censoredbellyslut',
    'censoredboobs',
    'censoredfetish',
    'censoredforbetas',
    'censoredforfeet',
    'censoredforhairypits',
    'censoredhannah',
    'censoredloservirgin',
    'censoredsimps',
    'censoredtiktok',
    'pixelpumpers',
    'pussyfreeasians',
    'pussyfreeporn'
]

# dictionary of lists: update after adding new lists in the corresponding dict row

master = {
    'nsfw': [fem_masturbation, humiliation, misogyny, alternative, public, cunnilingus, amateur, young],
    'barely_sfw': [breasts, tight_clothes],
    'non_nude': [censors]
}

# creating pandas dataframe from above dictionary

master_df = pd.DataFrame.from_dict(master, orient='index')
master_df['Count'] = master_df.notnull().sum(axis=1)
