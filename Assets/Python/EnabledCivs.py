from CvPythonExtensions import *
from Consts import *

'''
This file determines if a civ will spawn.
If a civ has a forced spawn, it will allways spawn, regardless of anything. (To avoid conflicts, Rome and Egypt will have a forced collapse when Italy and Mamluks spawn respectively)
If a civ has a conditional spawn, it will only spawn if it meets the conditions. If no special conditions are defined, the forced spawn method is used. This is the default value for most civs.
If a civ has a no spawn, it will not spawn at all.

To change the spawn type, change the value after the : to one of the values below. (Just copy, replace)
Forced spawn	: iForcedSpawn
Never spawn		: iNoSpawn
Conditional Spawn: iConditionalSpawn
'''

dSpawnTypes = {
iEgypt			: iConditionalSpawn,
iBabylonia		: iConditionalSpawn,
iHarappa		: iConditionalSpawn,
iNubia			: iConditionalSpawn,
iChina			: iConditionalSpawn,
iGreece			: iConditionalSpawn,
iIndia			: iConditionalSpawn,
iCarthage		: iConditionalSpawn,
iPolynesia		: iNoSpawn,
iPersia			: iConditionalSpawn,
iRome			: iConditionalSpawn,
iTamils			: iConditionalSpawn,
iEthiopia		: iConditionalSpawn,
iVietnam		: iConditionalSpawn,
iTeotihuacan	: iConditionalSpawn,
iKorea			: iConditionalSpawn,
iMaya			: iConditionalSpawn,
iByzantium		: iConditionalSpawn,
iJapan			: iConditionalSpawn,
iVikings		: iConditionalSpawn,
iTurks			: iConditionalSpawn,
iArabia			: iConditionalSpawn,
iTibet			: iConditionalSpawn,
iIndonesia		: iConditionalSpawn,
iBurma			: iConditionalSpawn,
iKhazars		: iConditionalSpawn,
iChad			: iConditionalSpawn,
iMoors			: iConditionalSpawn,
iSpain			: iConditionalSpawn,
iFrance			: iConditionalSpawn,
iOman			: iConditionalSpawn,
iKhmer			: iConditionalSpawn,
iYemen			: iConditionalSpawn,
iEngland		: iConditionalSpawn,
iHolyRome		: iConditionalSpawn,
iKievanRus		: iConditionalSpawn,
iHungary		: iConditionalSpawn,
iPhilippines	: iConditionalSpawn,
iSwahili		: iConditionalSpawn,
iMamluks		: iConditionalSpawn,
iMali			: iConditionalSpawn,
iPoland			: iConditionalSpawn,
iZimbabwe		: iConditionalSpawn,
iPortugal		: iConditionalSpawn,
iInca			: iConditionalSpawn,
iItaly			: iConditionalSpawn,
iNigeria		: iConditionalSpawn,
iMongolia		: iConditionalSpawn,
iAztecs			: iConditionalSpawn,
iMughals		: iConditionalSpawn,
iOttomans		: iConditionalSpawn,
iRussia			: iConditionalSpawn,
iThailand		: iConditionalSpawn,
iCongo			: iConditionalSpawn,
iSweden			: iConditionalSpawn,
iNetherlands	: iConditionalSpawn,
iManchuria		: iConditionalSpawn,
iGermany		: iConditionalSpawn,
iAmerica		: iConditionalSpawn,
iArgentina		: iConditionalSpawn,
iBrazil			: iConditionalSpawn,
iAustralia		: iConditionalSpawn,
iBoers			: iConditionalSpawn,
iCanada			: iConditionalSpawn,
iIsrael			: iConditionalSpawn,
}