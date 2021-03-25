define boobsImages = [8506, 8507, 8508, 8509, 8510, 8511, 8512, 8513, 8514, 8515]
define boobsImagesTonque = [8516, 8517]
define assImages = [8518, 8519, 8520, 8521, 8522, 8523, 8524, 8525, 8526, 8527]
define pylonClothDanceImages1 = [9524, 9525, 9526, 9527, 9549, 9550, 9551, 9552]
define pylonClothDanceImages2 = [9528, 9529, 9530, 9531, 9532, 9553, 9554, 9555, 9556]
define pylonClothDanceImages3 = [9533, 9534, 9535, 9557, 9558, 9559, 9560]
define pylonClothDanceImages4 = [9536, 9537, 9538, 9539, 9561, 9562, 9563, 9564]
define pylonClothDanceImages5 = [9540, 9541, 9542, 9543, 9544, 9565, 9566, 9567, 9568]
define pylonClothDanceImages6 = [9545, 9546, 9547, 9548, 9569, 9570, 9571, 9572]
define pylonClothDanceImages7 = [9524, 9525, 9526, 9527, 9573, 9574, 9575, 9576]
define pylonClothDanceImages8 = [9528, 9529, 9530, 9531, 9532, 9577, 9578, 9579, 9580]
#dance1 - 9524, 9525, 9526, 9527
#2 - 9528, 9529, 9530, 9531, 9532
#3 - 9533, 9534, 9535
#4 - 9536, 9537, 9538, 9539
#5 - 9540, 9541, 9542, 9543, 9544
#6 - 9545, 9546, 9547, 9548
#7 (без куртки) - 9549, 9550, 9551, 9552
#8 - 9553, 9554, 9555, 9556
#9 - 9557, 9558, 9559, 9560
#10 - 9561, 9562, 9563, 9564
#11 - 9565, 9566, 9567, 9568
#12 - 9569, 9570, 9571, 9572
#13 - 9573, 9574, 9575, 9576
#14 - 9577, 9578, 9579, 9580
define nakedboobsImages = [8528, 8529]
define nakedboobssquizenipplesImages = [8528, 8529]
define assSpankImages = [9581, 9582]
define nakedboobsshakeImages = [8528, 8529]

default pylonLastCamera = 1

init python:
    def pylon_controller_get_object_path(assetName, suffix1 = ""):
        assetsList = []
        imageFileName = get_image_filename(assetName + suffix1)
        if imageFileName != False:
            assetsList.append([assetName + suffix1, imageFileName])
#        overlayFileName = get_image_filename()
        return assetsList

label pylonController(citizenBehaviorSuffix, monicaBehaviorSuffix, cameraIn = False):
    if cameraIn != False:
        $ camera = cameraIn
    else: #сменяем камеру каждый вызов
        if pylonLastCamera == 1:
            $ camera = 2
        if pylonLastCamera == 2:
            $ camera = 1

    $ pylonLastCamera = camera
    if pylonPreset == 1:
        if camera == 1:
            $ cameraId = 1
        if camera == 2:
            $ cameraId = 2
    if pylonPreset == 2:
        if camera == 1:
            $ cameraId = 2
        if camera == 2:
            $ cameraId = 1

    $ sceneImage = get_image_filename("scene_Hostel_Edge_Camera" + str(cameraId))
    $ monicaAssetName = "Hostel_Edge_Pylon_Monica_" + str(monicaBehaviorSuffix) + "_c" + str(cameraId)
    $ citizenAssetName = "Dial_Citizen_Pylon_" + str(citizenId) + "_" + str(citizenBehaviorSuffix) + "_c" + str(cameraId)

    $ objectsList = []
    if cameraId == 1:
        python:
            objectsList = objectsList + pylon_controller_get_object_path(monicaAssetName, "_overlay") + pylon_controller_get_object_path(citizenAssetName, "_overlay")
            objectsList = objectsList + pylon_controller_get_object_path(monicaAssetName) + pylon_controller_get_object_path(citizenAssetName)

    if cameraId == 2:
        python:
            objectsList = objectsList + pylon_controller_get_object_path(citizenAssetName, "_overlay") + pylon_controller_get_object_path(monicaAssetName, "_overlay")
            objectsList = objectsList + pylon_controller_get_object_path(citizenAssetName) + pylon_controller_get_object_path(monicaAssetName)

    $ renpy.scene()
    show screen pylon_screen(sceneImage, objectsList)
#    $ print "objectsList"
#    $ print objectsList
    return
