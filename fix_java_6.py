import re

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix missing closing parens from the method calls
replacements = [
    ("getGameType().getPlayingFieldBlockTypes(getGameLogic().getCurrentDifficulty();", "getGameType().getPlayingFieldBlockTypes(getGameLogic().getCurrentDifficulty());"),
    ("getGameType().getPlayingFieldPieceTypes(getGameLogic().getCurrentDifficulty();", "getGameType().getPlayingFieldPieceTypes(getGameLogic().getCurrentDifficulty());"),
    ("acceptableColors.add(blockType.colors.get(i);", "acceptableColors.add(blockType.colors.get(i));"),
    ("acceptableColors.remove(get(x - 1, y - 1).getColor();", "acceptableColors.remove(get(x - 1, y - 1).getColor());"),
    ("acceptableColors.remove(get(x - 1, y + 1).getColor();", "acceptableColors.remove(get(x - 1, y + 1).getColor());"),
    ("acceptableColors.remove(get(x - 1, y).getColor();", "acceptableColors.remove(get(x - 1, y).getColor());"),
    ("acceptableColors.remove(get(x, y + 1).getColor();", "acceptableColors.remove(get(x, y + 1).getColor());"),
    ("acceptableColors.remove(get(x, y - 1).getColor();", "acceptableColors.remove(get(x, y - 1).getColor());"),
    ("getGameType().getGarbageBlockTypes(getGameLogic().getCurrentDifficulty();", "getGameType().getGarbageBlockTypes(getGameLogic().getCurrentDifficulty());"),
    ("getGameType().getGarbagePieceTypes(getGameLogic().getCurrentDifficulty();", "getGameType().getGarbagePieceTypes(getGameLogic().getCurrentDifficulty());"),
    ("(Easing.easeInOutCircular(shakePlayingFieldTicksDuration/2 + ticksPassed, 0, shakePlayingFieldMaxX, shakePlayingFieldTicksDuration*2);", "(Easing.easeInOutCircular(shakePlayingFieldTicksDuration/2 + ticksPassed, 0, shakePlayingFieldMaxX, shakePlayingFieldTicksDuration*2));"),
    ("(Easing.easeInOutCircular(shakePlayingFieldTicksDuration/2 + ticksPassed, 0, shakePlayingFieldMaxY, shakePlayingFieldTicksDuration*2);", "(Easing.easeInOutCircular(shakePlayingFieldTicksDuration/2 + ticksPassed, 0, shakePlayingFieldMaxY, shakePlayingFieldTicksDuration*2));"),
    ("(Easing.easeInOutCircular(shakePlayingFieldTicksPerShakeXCounter, 0, xOverShakeTime, shakePlayingFieldTicksPerShake);", "(Easing.easeInOutCircular(shakePlayingFieldTicksPerShakeXCounter, 0, xOverShakeTime, shakePlayingFieldTicksPerShake));"),
    ("(Easing.easeInOutCircular(shakePlayingFieldTicksPerShakeYCounter, 0, yOverShakeTime, shakePlayingFieldTicksPerShake * 2);", "(Easing.easeInOutCircular(shakePlayingFieldTicksPerShakeYCounter, 0, yOverShakeTime, shakePlayingFieldTicksPerShake * 2));"),
    ("float fbgX = bgX() + (x*cellW();", "float fbgX = bgX() + (x*cellW());"),
    ("float fbgY = bgY() + (y*cellH();", "float fbgY = bgY() + (y*cellH());"),
    ("((float)(getHeight()*0.6f);", "((float)(getHeight()*0.6f));"),
    ('String.valueOf(b.yGrid) + (" x:") + String.valueOf(x) + (" y:") + String.valueOf(y);', 'String.valueOf(b.yGrid) + (" x:") + String.valueOf(x) + (" y:") + String.valueOf(y));'),
    ('randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomSpecialPieceTypeFromArrayExcludingNormalPiecesOrNull");', 'randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomSpecialPieceTypeFromArrayExcludingNormalPiecesOrNull"));'),
    ('randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomPieceTypeFromArrayExcludingSpecialPieceTypes");', 'randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomPieceTypeFromArrayExcludingSpecialPieceTypes"));'),
    ("getGameType().getNormalPieceTypes(getGameLogic().getCurrentDifficulty();", "getGameType().getNormalPieceTypes(getGameLogic().getCurrentDifficulty());"),
    ("getGameType().getNormalBlockTypes(getGameLogic().getCurrentDifficulty();", "getGameType().getNormalBlockTypes(getGameLogic().getCurrentDifficulty());"),
    ("randomBag.add(tempBag.get(i);", "randomBag.add(tempBag.get(i));"),
    ('arr.get(getGameLogic().getRandomIntLessThan(arr.size(), "getRandomBlockTypeDisregardingSpecialFrequency");', 'arr.get(getGameLogic().getRandomIntLessThan(arr.size(), "getRandomBlockTypeDisregardingSpecialFrequency"));'),
    ('randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomSpecialBlockTypeFromArrayExcludingNormalBlocksOrNull");', 'randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomSpecialBlockTypeFromArrayExcludingNormalBlocksOrNull"));'),
    ('randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomBlockTypeFromArrayExcludingSpecialBlockTypes");', 'randomBag.get(getGameLogic().getRandomIntLessThan(randomBag.size(),"getRandomBlockTypeFromArrayExcludingSpecialBlockTypes"));'),
    ('acceptableColors.get(getGameLogic().getRandomIntLessThan(acceptableColors.size(),"dontPutSameColorDiagonalOrNextToEachOtherReturnNull");', 'acceptableColors.get(getGameLogic().getRandomIntLessThan(acceptableColors.size(),"dontPutSameColorDiagonalOrNextToEachOtherReturnNull"));'),
    ('acceptableColors.get(getGameLogic().getRandomIntLessThan(acceptableColors.size(),"dontPutSameColorNextToEachOtherOrReturnNull");', 'acceptableColors.get(getGameLogic().getRandomIntLessThan(acceptableColors.size(),"dontPutSameColorNextToEachOtherOrReturnNull"));'),
    ('acceptableBlockTypes.get(getGameLogic().getRandomIntLessThan(acceptableBlockTypes.size(), "dontPutSameBlockTypeNextToEachOtherOrReturnNull");', 'acceptableBlockTypes.get(getGameLogic().getRandomIntLessThan(acceptableBlockTypes.size(), "dontPutSameBlockTypeNextToEachOtherOrReturnNull"));')
]

for old, new in replacements:
    text = text.replace(old, new)

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'w', encoding='utf-8') as f:
    f.write(text)
